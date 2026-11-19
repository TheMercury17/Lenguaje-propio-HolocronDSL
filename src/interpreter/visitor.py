# Interprete semantico principal para HolocronDSL basado en el patron Visitor
# Ejecuta flujos reproducibles de datos mediante las bibliotecas propias (Grupo 5)

import math
from typing import Any, Dict, List, Optional, Tuple, Union

from src.generated.HolocronDSLVisitor import HolocronDSLVisitor
from src.generated.HolocronDSLParser import HolocronDSLParser

from src.interpreter.symbol_table import SymbolTable, SymbolType
from src.runtime.holocron_table import HolocronTable, HolocronGroupedTable
from src.runtime.io_engine import HolocronIO
from src.runtime.math_engine import HolocronMath
from src.runtime.graphics_engine import HolocronPlotter
from src.runtime.data_structures import (
    HolocronArray,
    HolocronPila,
    HolocronCola,
    NodoArbolDecision,
    crear_lista_dimensionada
)
from src.runtime.ml_engine import (
    KMeansGalactico,
    PerceptronGalactico,
    ArbolDecisionGalactico,
    distancia_euclidiana,
    calcular_impureza_gini,
    calcular_entropia,
    evaluar_exactitud,
    calcular_matriz_confusion
)

from src.errors.semantic_error import (
    HolocronSemanticError,
    VariableNoDefinidaError,
    ColumnaInexistenteError,
    TipoIncompatibleError,
    DivisionPorCeroError,
    MisionNoDefinidaError,
    AridadInvalidaError,
    OperacionInvalidaError,
    IndiceFueraDeRangoError,
    EstructuraVaciaError,
    ErrorModeloML
)


class HolocronInterpreter(HolocronDSLVisitor):
    """
    Intérprete evaluador de HolocronDSL.
    Recorre el árbol de análisis sintáctico (CST/AST) ejecutando las instrucciones
    semánticas y gestionando la tabla de símbolos y bibliotecas propias.
    """

    def __init__(self, verbose: bool = False):
        super().__init__()
        self.symbol_table = SymbolTable()
        self.fila_contexto_actual: Optional[Dict[str, Any]] = None
        self.transmisiones: List[str] = []
        self.archivos_generados: List[str] = []
        self.verbose: bool = verbose

    # -------------------------------------------------------------------------
    # PROGRAMA Y SENTENCIAS
    # -------------------------------------------------------------------------

    def visitPrograma(self, ctx: HolocronDSLParser.ProgramaContext):
        resultado = None
        for sentencia_ctx in ctx.sentencia():
            resultado = self.visit(sentencia_ctx)
        return resultado

    def visitSentencia(self, ctx: HolocronDSLParser.SentenciaContext):
        return self.visitChildren(ctx)

    def visitDeclaracionMision(self, ctx: HolocronDSLParser.DeclaracionMisionContext):
        nombre_mision = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column

        parametros = []
        if ctx.listaParametros():
            parametros = [id_token.getText() for id_token in ctx.listaParametros().ID()]

        sentencias = list(ctx.sentencia())
        retorno = ctx.expresionPipeline()

        self.symbol_table.registrar_mision(
            nombre=nombre_mision,
            parametros=parametros,
            sentencias_ctx=sentencias,
            retorno_ctx=retorno,
            linea=linea,
            columna=columna
        )
        return None

    def visitSentenciaAsignacion(self, ctx: HolocronDSLParser.SentenciaAsignacionContext):
        nombre_var = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column

        valor = self.visit(ctx.expresionPipeline())
        self.symbol_table.definir(nombre_var, valor, linea=linea, columna=columna)
        return valor

    def visitSentenciaAsignacionIndice(self, ctx: HolocronDSLParser.SentenciaAsignacionIndiceContext):
        nombre_var = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column
        contenedor = self.symbol_table.obtener_valor(nombre_var, linea=linea, columna=columna)
        indice = int(self.visit(ctx.expresionAritmetica()))
        valor = self.visit(ctx.expresionPipeline())
        if isinstance(contenedor, HolocronArray):
            contenedor.asignar(indice, valor)
        elif isinstance(contenedor, list):
            if indice < -len(contenedor) or indice >= len(contenedor):
                raise IndiceFueraDeRangoError(indice, len(contenedor), linea, columna)
            contenedor[indice] = valor
        else:
            raise TipoIncompatibleError("asignacion_indice", type(contenedor).__name__, "int", linea, columna)
        return valor

    def visitSentenciaLlamada(self, ctx: HolocronDSLParser.SentenciaLlamadaContext):
        nombre = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column
        argumentos = [self.visit(arg) for arg in ctx.expresionPipeline()]
        return self._ejecutar_llamada(nombre, argumentos, linea, columna)

    # -------------------------------------------------------------------------
    # PIPELINE Y OPERACIONES
    # -------------------------------------------------------------------------

    def visitExpresionPipeline(self, ctx: HolocronDSLParser.ExpresionPipelineContext):
        # Evaluar la base del pipeline
        valor = self.visit(ctx.expresionBase())

        # Encadenar cada operacion pipeline secuencialmente
        for op_ctx in ctx.operacionPipeline():
            if not isinstance(valor, (HolocronTable, HolocronGroupedTable)):
                raise OperacionInvalidaError(
                    operacion=op_ctx.start.text,
                    tipo_recibido=type(valor).__name__,
                    linea=op_ctx.start.line,
                    columna=op_ctx.start.column
                )
            valor = self._ejecutar_operacion_pipeline(op_ctx, valor)

        return valor

    def _ejecutar_operacion_pipeline(
        self,
        op_ctx: HolocronDSLParser.OperacionPipelineContext,
        tabla_entrada: Union[HolocronTable, HolocronGroupedTable]
    ) -> Union[HolocronTable, HolocronGroupedTable]:
        linea = op_ctx.start.line
        columna = op_ctx.start.column

        # 1. Seleccionar / Revelar
        if op_ctx.operacionSeleccionar():
            sel_ctx = op_ctx.operacionSeleccionar()
            cols = self._extraer_identificadores(sel_ctx.listaIdentificadoresOpcional())
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.seleccionar(cols, linea=linea, columna=columna)

        # 2. Purgar / Filtrar
        elif op_ctx.operacionFiltrar():
            filt_ctx = op_ctx.operacionFiltrar()
            expr_bool = filt_ctx.expresionBooleana()
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen

            def predicado(fila: Dict[str, Any]) -> bool:
                prev_ctx = self.fila_contexto_actual
                self.fila_contexto_actual = fila
                try:
                    return bool(self.visit(expr_bool))
                finally:
                    self.fila_contexto_actual = prev_ctx

            return tabla_entrada.purgar(predicado)

        # 3. Forjar / Crear columna calculada
        elif op_ctx.operacionForjar():
            forj_ctx = op_ctx.operacionForjar()
            nombre_col = forj_ctx.ID().getText()
            expr_arit = forj_ctx.expresionAritmetica()
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen

            def evaluador_col(fila: Dict[str, Any]) -> Any:
                prev_ctx = self.fila_contexto_actual
                self.fila_contexto_actual = fila
                try:
                    return self.visit(expr_arit)
                finally:
                    self.fila_contexto_actual = prev_ctx

            return tabla_entrada.forjar(nombre_col, evaluador_col)

        # 4. Ordenar
        elif op_ctx.operacionOrdenar():
            ord_ctx = op_ctx.operacionOrdenar()
            nombre_col = ord_ctx.ID().getText()
            ascendente = True
            if ord_ctx.ordenDireccion():
                if ord_ctx.ordenDireccion().DESCENDENTE():
                    ascendente = False
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.ordenar(nombre_col, ascendente, linea=linea, col_pos=columna)

        # 5. Eliminar clones
        elif op_ctx.operacionEliminarClones():
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.eliminar_clones()

        # 6. Sanar vacios
        elif op_ctx.operacionSanarVacios():
            san_ctx = op_ctx.operacionSanarVacios()
            opc_ctx = san_ctx.opcionSanado()
            if opc_ctx.DESCARTAR():
                opcion = "descartar"
                valor_sustituto = None
            else:
                opcion = "con"
                valor_sustituto = self._obtener_valor_literal(opc_ctx.literal())

            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.sanar_vacios(opcion, valor_sustituto)

        # 7. Agrupar
        elif op_ctx.operacionAgrupar():
            agrup_ctx = op_ctx.operacionAgrupar()
            cols = self._extraer_identificadores(agrup_ctx.listaIdentificadoresOpcional())
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.agrupar(cols, linea=linea, columna=columna)

        # 8. Resumir
        elif op_ctx.operacionResumir():
            res_ctx = op_ctx.operacionResumir()
            lista_asignaciones = res_ctx.listaAsignacionesAgregacion().asignacionAgregacion()
            agregaciones: List[Tuple[str, str, Optional[str]]] = []

            for asig_ctx in lista_asignaciones:
                col_dest = asig_ctx.ID().getText()
                llamada_ctx = asig_ctx.llamadaAgregacion()

                if llamada_ctx.FUNC_RECUENTO():
                    func_nombre = "recuento"
                    col_orig = None
                elif llamada_ctx.FUNC_ACUMULAR():
                    func_nombre = "acumular"
                    col_orig = llamada_ctx.ID().getText()
                elif llamada_ctx.FUNC_EQUILIBRIO():
                    func_nombre = "equilibrio"
                    col_orig = llamada_ctx.ID().getText()
                elif llamada_ctx.FUNC_MEDIANA():
                    func_nombre = "mediana"
                    col_orig = llamada_ctx.ID().getText()
                elif llamada_ctx.FUNC_CENIT():
                    func_nombre = "cenit"
                    col_orig = llamada_ctx.ID().getText()
                elif llamada_ctx.FUNC_NADIR():
                    func_nombre = "nadir"
                    col_orig = llamada_ctx.ID().getText()
                elif llamada_ctx.FUNC_DESVIACION():
                    func_nombre = "desviacion"
                    col_orig = llamada_ctx.ID().getText()
                else:
                    func_nombre = llamada_ctx.start.text
                    col_orig = llamada_ctx.ID().getText() if llamada_ctx.ID() else None

                agregaciones.append((col_dest, func_nombre, col_orig))

            return tabla_entrada.resumir(agregaciones, linea=linea, columna=columna)

        # 9. Trazar Regresion / Sintonizar Trayectoria
        elif op_ctx.operacionRegresion():
            reg_ctx = op_ctx.operacionRegresion()
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen

            col_x, col_y, col_destino = self._extraer_parametros_regresion(
                reg_ctx.parametroRegresion(), linea, columna
            )
            return tabla_entrada.trazar_regresion(
                col_x=col_x,
                col_y=col_y,
                col_destino=col_destino,
                linea=linea,
                columna=columna
            )

        # 10. Agrupar K-Means
        elif op_ctx.operacionKMeans():
            k_ctx = op_ctx.operacionKMeans()
            params = self._extraer_parametros_ml(k_ctx.parametroML()) if k_ctx.parametroML() else {}
            k = int(params.get("k", params.get("clusters", 3)))
            cols = params.get("columnas", params.get("cols", []))
            destino = params.get("destino", "cluster")
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.agrupar_kmeans(columnas=cols, k=k, col_destino=destino, linea=linea, columna=columna)

        # 11. Clasificar con Arbol de Decision
        elif op_ctx.operacionClasificarArbol():
            arb_ctx = op_ctx.operacionClasificarArbol()
            params = self._extraer_parametros_ml(arb_ctx.parametroML()) if arb_ctx.parametroML() else {}
            objetivo = params.get("objetivo", params.get("clase", params.get("y", None)))
            if not objetivo:
                raise ErrorModeloML("ArbolDecision", "Se debe especificar el parametro 'objetivo' en clasificar_arbol", linea, columna)
            cols = params.get("columnas", params.get("caracteristicas", None))
            prof = int(params.get("profundidad", 4))
            destino = params.get("destino", f"pred_{objetivo}")
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.clasificar_arbol(col_objetivo=str(objetivo), columnas_caracteristicas=cols, profundidad=prof, col_destino=str(destino), linea=linea, columna=columna)

        # 12. Clasificar con Perceptron
        elif op_ctx.operacionClasificarPerceptron():
            per_ctx = op_ctx.operacionClasificarPerceptron()
            params = self._extraer_parametros_ml(per_ctx.parametroML()) if per_ctx.parametroML() else {}
            objetivo = params.get("objetivo", params.get("clase", params.get("y", None)))
            if not objetivo:
                raise ErrorModeloML("Perceptron", "Se debe especificar el parametro 'objetivo' en clasificar_perceptron", linea, columna)
            cols = params.get("columnas", params.get("caracteristicas", None))
            epocas = int(params.get("epocas", 50))
            tasa = float(params.get("tasa", 0.05))
            destino = params.get("destino", f"pred_{objetivo}")
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.clasificar_perceptron(col_objetivo=str(objetivo), columnas_caracteristicas=cols, epocas=epocas, tasa=tasa, col_destino=str(destino), linea=linea, columna=columna)

        # 13. Normalizar Min-Max
        elif op_ctx.operacionNormalizarMinMax():
            nm_ctx = op_ctx.operacionNormalizarMinMax()
            params = self._extraer_parametros_ml(nm_ctx.parametroML()) if nm_ctx.parametroML() else {}
            cols = params.get("columnas", [c for c in tabla_entrada.columnas if any(isinstance(f.get(c), (int, float)) for f in tabla_entrada.filas)])
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.normalizar_minmax(columnas=cols, linea=linea, columna=columna)

        # 14. Estandarizar Z-Score
        elif op_ctx.operacionEstandarizarZScore():
            zs_ctx = op_ctx.operacionEstandarizarZScore()
            params = self._extraer_parametros_ml(zs_ctx.parametroML()) if zs_ctx.parametroML() else {}
            cols = params.get("columnas", [c for c in tabla_entrada.columnas if any(isinstance(f.get(c), (int, float)) for f in tabla_entrada.filas)])
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.estandarizar_zscore(columnas=cols, linea=linea, columna=columna)

        # 15. Codificar Etiquetas
        elif op_ctx.operacionCodificarEtiquetas():
            ce_ctx = op_ctx.operacionCodificarEtiquetas()
            params = self._extraer_parametros_ml(ce_ctx.parametroML()) if ce_ctx.parametroML() else {}
            cols = params.get("columnas", [c for c in tabla_entrada.columnas if any(isinstance(f.get(c), str) for f in tabla_entrada.filas)])
            if isinstance(tabla_entrada, HolocronGroupedTable):
                tabla_entrada = tabla_entrada.tabla_origen
            return tabla_entrada.codificar_etiquetas(columnas=cols, linea=linea, columna=columna)

        raise OperacionInvalidaError(op_ctx.getText(), type(tabla_entrada).__name__, linea, columna)

    def _extraer_parametros_ml(self, lista_params) -> Dict[str, Any]:
        """Extrae un diccionario de parametros a partir de una lista de parametroML."""
        resultado = {}
        for p in lista_params:
            texto = p.getText()
            if "=" in texto:
                partes = texto.split("=", 1)
                clave = partes[0].strip().lower()
                val_raw = partes[1].strip()
                if val_raw.startswith("[") and val_raw.endswith("]"):
                    cols = [c.strip().strip('"\'') for c in val_raw[1:-1].split(",") if c.strip()]
                    resultado[clave] = cols
                else:
                    val_limpio = val_raw.strip('"\'')
                    try:
                        if "." in val_limpio:
                            resultado[clave] = float(val_limpio)
                        else:
                            resultado[clave] = int(val_limpio)
                    except ValueError:
                        resultado[clave] = val_limpio
            else:
                resultado[texto.lower()] = True
        return resultado

    def _extraer_parametros_regresion(
        self,
        lista_params,
        linea: int,
        columna: int
    ) -> Tuple[str, str, Optional[str]]:
        """
        Extrae col_x, col_y y opcionalmente col_destino de la lista de nodos parametroRegresion.
        Admite tanto formato clave-valor (eje_x = col, x = col, destino = col) como formato posicional.
        """
        col_x = None
        col_y = None
        col_destino = None
        posicionales: List[str] = []

        for p_ctx in lista_params:
            if p_ctx.OP_ASIG():
                clave = p_ctx.start.text.lower()
                tokens_id = p_ctx.ID()
                val = tokens_id[-1].getText() if tokens_id else p_ctx.getText().split("=")[-1].strip()

                if clave in ("eje_x", "x", "var_x", "independiente", "x_var"):
                    col_x = val
                elif clave in ("eje_y", "y", "var_y", "dependiente", "y_var", "respuesta"):
                    col_y = val
                elif clave in ("destino", "guardar_prediccion", "guardar_en", "como", "prediccion"):
                    col_destino = val
                else:
                    posicionales.append(val)
            else:
                if p_ctx.ID():
                    txt_id = p_ctx.ID().getText() if not isinstance(p_ctx.ID(), list) else p_ctx.ID()[0].getText()
                    posicionales.append(txt_id)

        idx_pos = 0
        if not col_x and idx_pos < len(posicionales):
            col_x = posicionales[idx_pos]
            idx_pos += 1
        if not col_y and idx_pos < len(posicionales):
            col_y = posicionales[idx_pos]
            idx_pos += 1
        if not col_destino and idx_pos < len(posicionales):
            col_destino = posicionales[idx_pos]
            idx_pos += 1

        if not col_x or not col_y:
            raise HolocronSemanticError(
                "La operacion de regresion requiere especificar tanto la variable X como la variable Y "
                "(por ejemplo: trazar_regresion [ eje_x = escudos, eje_y = victorias ]).",
                linea, columna
            )

        return col_x, col_y, col_destino

    def _extraer_identificadores(self, ctx_opcional: HolocronDSLParser.ListaIdentificadoresOpcionalContext) -> List[str]:
        if ctx_opcional.listaIdentificadores():
            return [id_node.getText() for id_node in ctx_opcional.listaIdentificadores().ID()]
        return []

    # -------------------------------------------------------------------------
    # EXPRESION BASE Y CARGA DE DATOS
    # -------------------------------------------------------------------------

    def visitExpresionBase(self, ctx: HolocronDSLParser.ExpresionBaseContext):
        if ctx.instruccionCarga():
            return self.visit(ctx.instruccionCarga())
        elif ctx.llamadaMision():
            return self.visit(ctx.llamadaMision())
        elif ctx.expresionAritmetica():
            return self.visit(ctx.expresionAritmetica())
        return self.visitChildren(ctx)

    def visitInstruccionCarga(self, ctx: HolocronDSLParser.InstruccionCargaContext):
        ruta_cruda = ctx.CADENA(0).getText()
        ruta = self._limpiar_cadena(ruta_cruda)
        delimitador = ","

        if ctx.DELIMITADO_POR():
            delimitador = self._limpiar_cadena(ctx.CADENA(1).getText())

        linea = ctx.start.line
        columna = ctx.start.column

        columnas, registros = HolocronIO.leer_csv(
            ruta=ruta,
            delimitador=delimitador,
            linea_origen=linea,
            columna_origen=columna
        )
        return HolocronTable(columnas=columnas, filas=registros, nombre=ruta)

    def visitLlamadaMision(self, ctx: HolocronDSLParser.LlamadaMisionContext):
        nombre_mision = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column

        argumentos = []
        for expr_arg in ctx.expresionPipeline():
            argumentos.append(self.visit(expr_arg))

        return self._ejecutar_llamada(nombre_mision, argumentos, linea, columna)

    # -------------------------------------------------------------------------
    # ARCHIVADO Y HOLOGRAMAS (VISUALIZACION)
    # -------------------------------------------------------------------------

    def visitSentenciaArchivado(self, ctx: HolocronDSLParser.SentenciaArchivadoContext):
        nombre_var = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column

        valor = self.symbol_table.obtener_valor(nombre_var, linea=linea, columna=columna)
        if not isinstance(valor, HolocronTable):
            if isinstance(valor, HolocronGroupedTable):
                valor = valor.tabla_origen
            else:
                raise OperacionInvalidaError("archivar_holocron", type(valor).__name__, linea, columna)

        ruta = self._limpiar_cadena(ctx.CADENA(0).getText())
        delimitador = ","
        if ctx.DELIMITADO_POR():
            delimitador = self._limpiar_cadena(ctx.CADENA(1).getText())

        ruta_absoluta = valor.archivar(ruta, delimitador)
        self.archivos_generados.append(ruta_absoluta)
        formato = "Excel (.xls)" if ruta_absoluta.lower().endswith((".xls", ".xml")) else "CSV"
        print(f"[Holocron Guardado] Holocron '{nombre_var}' exportado con exito:")
        print(f"  -> Formato: {formato}")
        print(f"  -> Registros: {len(valor.filas)} filas | {len(valor.columnas)} columnas")
        print(f"  -> Ubicacion absoluta: {ruta_absoluta}")
        return ruta_absoluta

    def visitSentenciaHolograma(self, ctx: HolocronDSLParser.SentenciaHologramaContext):
        tipo_grafica = ctx.tipoGrafica().getText()
        nombre_var = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column

        valor = self.symbol_table.obtener_valor(nombre_var, linea=linea, columna=columna)
        if not isinstance(valor, HolocronTable):
            if isinstance(valor, HolocronGroupedTable):
                valor = valor.tabla_origen
            else:
                raise OperacionInvalidaError("holograma", type(valor).__name__, linea, columna)

        propiedades: Dict[str, str] = {}
        for prop_ctx in ctx.propiedadHolograma():
            cadena_val = self._limpiar_cadena(prop_ctx.CADENA().getText())
            if prop_ctx.EJE_X():
                propiedades["eje_x"] = cadena_val
            elif prop_ctx.EJE_Y():
                propiedades["eje_y"] = cadena_val
            elif prop_ctx.TITULO():
                propiedades["titulo"] = cadena_val
            elif prop_ctx.GUARDAR():
                propiedades["guardar"] = cadena_val

        ruta_png = HolocronPlotter.proyectar_holograma(
            tipo=tipo_grafica,
            tabla=valor,
            propiedades=propiedades,
            linea=linea,
            columna=columna
        )
        self.archivos_generados.append(ruta_png)
        print(f"[Holograma Proyectado] Grafico PNG ({tipo_grafica}) generado con exito:")
        print(f"  -> Titulo: {propiedades.get('titulo', 'Sin titulo')}")
        print(f"  -> Ubicacion absoluta: {ruta_png}")
        return ruta_png

    def visitSentenciaRegresion(self, ctx: HolocronDSLParser.SentenciaRegresionContext):
        nombre_var = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column

        valor = self.symbol_table.obtener_valor(nombre_var, linea=linea, columna=columna)
        if not isinstance(valor, HolocronTable):
            if isinstance(valor, HolocronGroupedTable):
                valor = valor.tabla_origen
            else:
                raise OperacionInvalidaError("trazar_regresion", type(valor).__name__, linea, columna)

        col_x, col_y, col_destino = self._extraer_parametros_regresion(
            ctx.parametroRegresion(), linea, columna
        )
        resultado = valor.trazar_regresion(
            col_x=col_x,
            col_y=col_y,
            col_destino=col_destino,
            linea=linea,
            columna=columna
        )
        self.symbol_table.definir(nombre_var, resultado, linea=linea, columna=columna)
        m = resultado.modelo
        print(f"[Holocron Regresion] Modelo ajustado para '{nombre_var}':")
        print(f"  -> Ecuacion: {m['ecuacion']}")
        print(f"  -> R^2: {m['r_cuadrado']} | Pearson r: {m['correlacion']}")
        return resultado

    # -------------------------------------------------------------------------
    # CONTROL DE FLUJO Y TRANSMISION
    # -------------------------------------------------------------------------

    def visitSentenciaCondicional(self, ctx: HolocronDSLParser.SentenciaCondicionalContext):
        condicion = self.visit(ctx.expresionBooleana())

        # Contar cuantas sentencias pertenecen a la senda luminosa vs senda oscura
        # En la gramatica: SENDA_LUMINOSA sentencia* (SENDA_OSCURA sentencia*)? FIN_EVALUAR
        sentencias = ctx.sentencia()
        if not ctx.SENDA_OSCURA():
            if bool(condicion):
                for s in sentencias:
                    self.visit(s)
        else:
            indice_oscura = -1
            token_oscura = ctx.SENDA_OSCURA().getSymbol()
            for idx, s in enumerate(sentencias):
                if s.start.tokenIndex > token_oscura.tokenIndex:
                    indice_oscura = idx
                    break

            if indice_oscura == -1:
                sentencias_luminosas = sentencias
                sentencias_oscuras = []
            else:
                sentencias_luminosas = sentencias[:indice_oscura]
                sentencias_oscuras = sentencias[indice_oscura:]

            if bool(condicion):
                for s in sentencias_luminosas:
                    self.visit(s)
            else:
                for s in sentencias_oscuras:
                    self.visit(s)

        return None

    def visitSentenciaMientras(self, ctx: HolocronDSLParser.SentenciaMientrasContext):
        expr_bool = ctx.expresionBooleana()
        resultado = None
        iteraciones = 0
        MAX_ITER = 100000
        while bool(self.visit(expr_bool)):
            iteraciones += 1
            if iteraciones > MAX_ITER:
                raise HolocronSemanticError(
                    "Bucle interrumpido: se supero el limite de seguridad de 100000 iteraciones en el bucle 'mientras'.",
                    ctx.start.line, ctx.start.column
                )
            for sent_ctx in ctx.sentencia():
                resultado = self.visit(sent_ctx)
        return resultado

    def visitSentenciaPara(self, ctx: HolocronDSLParser.SentenciaParaContext):
        nombre_var = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column
        coleccion = self.visit(ctx.expresionPipeline())

        if isinstance(coleccion, HolocronArray):
            elementos = coleccion.a_lista_python()
        elif isinstance(coleccion, (list, tuple)):
            elementos = list(coleccion)
        elif isinstance(coleccion, (HolocronPila, HolocronCola)):
            elementos = coleccion.a_arreglo().a_lista_python()
        elif isinstance(coleccion, HolocronTable):
            elementos = coleccion.filas
        elif isinstance(coleccion, str):
            elementos = list(coleccion)
        else:
            raise TipoIncompatibleError("recorrer", type(coleccion).__name__, "coleccion", linea, columna)

        resultado = None
        for elem in elementos:
            self.symbol_table.definir(nombre_var, elem, linea=linea, columna=columna)
            for sent_ctx in ctx.sentencia():
                resultado = self.visit(sent_ctx)
        return resultado

    def visitSentenciaParaRango(self, ctx: HolocronDSLParser.SentenciaParaRangoContext):
        nombre_var = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column
        inicio = int(self.visit(ctx.expresionAritmetica(0)))
        fin = int(self.visit(ctx.expresionAritmetica(1)))
        paso = 1
        if ctx.PASO():
            paso = int(self.visit(ctx.expresionAritmetica(2)))

        resultado = None
        rango = range(inicio, fin + 1, paso) if paso > 0 else range(inicio, fin - 1, paso)
        for val in rango:
            self.symbol_table.definir(nombre_var, val, linea=linea, columna=columna)
            for sent_ctx in ctx.sentencia():
                resultado = self.visit(sent_ctx)
        return resultado

    def visitSentenciaTransmision(self, ctx: HolocronDSLParser.SentenciaTransmisionContext):
        valor = self.visit(ctx.expresionPipeline())
        if isinstance(valor, HolocronTable):
            mensaje = valor.a_cadena_tabular()
        elif isinstance(valor, bool):
            mensaje = "cierto_es" if valor else "falso_es"
        elif valor is None:
            mensaje = "nulo"
        else:
            mensaje = str(valor)

        print(mensaje)
        self.transmisiones.append(mensaje)
        return mensaje

    # -------------------------------------------------------------------------
    # EXPRESIONES BOOLEANAS Y LOGICAS
    # -------------------------------------------------------------------------

    def visitExprBoolOr(self, ctx: HolocronDSLParser.ExprBoolOrContext):
        izq = bool(self.visit(ctx.expresionBooleana()))
        if izq:
            return True
        der = bool(self.visit(ctx.terminoBooleano()))
        return izq or der

    def visitExprBoolTermino(self, ctx: HolocronDSLParser.ExprBoolTerminoContext):
        return self.visit(ctx.terminoBooleano())

    def visitExprBoolAnd(self, ctx: HolocronDSLParser.ExprBoolAndContext):
        izq = bool(self.visit(ctx.terminoBooleano()))
        if not izq:
            return False
        der = bool(self.visit(ctx.factorBooleano()))
        return izq and der

    def visitExprBoolFactor(self, ctx: HolocronDSLParser.ExprBoolFactorContext):
        return self.visit(ctx.factorBooleano())

    def visitExprBoolNot(self, ctx: HolocronDSLParser.ExprBoolNotContext):
        val = bool(self.visit(ctx.factorBooleano()))
        return not val

    def visitExprBoolParentesis(self, ctx: HolocronDSLParser.ExprBoolParentesisContext):
        return self.visit(ctx.expresionBooleana())

    def visitExprBoolLiteral(self, ctx: HolocronDSLParser.ExprBoolLiteralContext):
        txt = ctx.BOOL().getText().lower()
        return txt in ("cierto_es", "verdadero", "true")

    def visitExprBoolComparacion(self, ctx: HolocronDSLParser.ExprBoolComparacionContext):
        return self.visit(ctx.comparacionRelacional())

    def visitComparacionRelacional(self, ctx: HolocronDSLParser.ComparacionRelacionalContext):
        val_izq = self.visit(ctx.expresionAritmetica(0))
        val_der = self.visit(ctx.expresionAritmetica(1))
        op = ctx.operadorRelacional().getText()
        linea = ctx.start.line
        columna = ctx.start.column

        # Manejo de comparaciones con nulos
        if val_izq is None or val_der is None:
            if op == "==":
                return val_izq is val_der
            elif op == "!=":
                return val_izq is not val_der
            return False

        try:
            if op == "==":
                return val_izq == val_der
            elif op == "!=":
                return val_izq != val_der
            elif op == "<":
                return val_izq < val_der
            elif op == "<=":
                return val_izq <= val_der
            elif op == ">":
                return val_izq > val_der
            elif op == ">=":
                return val_izq >= val_der
        except TypeError:
            raise TipoIncompatibleError(op, type(val_izq).__name__, type(val_der).__name__, linea, columna)

        return False

    # -------------------------------------------------------------------------
    # EXPRESIONES ARITMETICAS
    # -------------------------------------------------------------------------

    def visitExprAritSumaResta(self, ctx: HolocronDSLParser.ExprAritSumaRestaContext):
        izq = self.visit(ctx.expresionAritmetica())
        der = self.visit(ctx.terminoAritmetico())
        op = ctx.OP_SUMA().getText() if ctx.OP_SUMA() else ctx.OP_RESTA().getText()
        linea = ctx.start.line
        columna = ctx.start.column

        if izq is None or der is None:
            return None

        if op == "+":
            if isinstance(izq, str) or isinstance(der, str):
                return str(izq) + str(der)
            self._validar_ambos_numericos(op, izq, der, linea, columna)
            res = izq + der
            return int(res) if isinstance(res, float) and res.is_integer() else res
        else:
            self._validar_ambos_numericos(op, izq, der, linea, columna)
            res = izq - der
            return int(res) if isinstance(res, float) and res.is_integer() else res

    def visitExprAritTermino(self, ctx: HolocronDSLParser.ExprAritTerminoContext):
        return self.visit(ctx.terminoAritmetico())

    def visitExprAritMultDiv(self, ctx: HolocronDSLParser.ExprAritMultDivContext):
        izq = self.visit(ctx.terminoAritmetico())
        der = self.visit(ctx.factorPotencia())
        linea = ctx.start.line
        columna = ctx.start.column

        if ctx.OP_MULT():
            op = "*"
        elif ctx.OP_DIV():
            op = "/"
        else:
            op = "%"

        if izq is None or der is None:
            return None

        self._validar_ambos_numericos(op, izq, der, linea, columna)

        if op == "*":
            res = izq * der
            return int(res) if isinstance(res, float) and res.is_integer() else res
        elif op == "/":
            if der == 0:
                raise DivisionPorCeroError(linea, columna)
            res = izq / der
            return int(res) if res.is_integer() else res
        elif op == "%":
            if der == 0:
                raise DivisionPorCeroError(linea, columna)
            res = izq % der
            return int(res) if isinstance(res, float) and res.is_integer() else res

    def visitExprAritFactor(self, ctx: HolocronDSLParser.ExprAritFactorContext):
        return self.visit(ctx.factorPotencia())

    def visitExprAritPotencia(self, ctx: HolocronDSLParser.ExprAritPotenciaContext):
        base = self.visit(ctx.atomoAritmetico())
        if ctx.OP_POTENCIA():
            exponente = self.visit(ctx.factorPotencia())
            linea = ctx.start.line
            columna = ctx.start.column
            if base is None or exponente is None:
                return None
            self._validar_ambos_numericos("^", base, exponente, linea, columna)
            res = base ** exponente
            return int(res) if isinstance(res, float) and res.is_integer() else res
        return base

    # -------------------------------------------------------------------------
    # ATOMOS Y LITERALES
    # -------------------------------------------------------------------------

    def visitAtomoArreglo(self, ctx: HolocronDSLParser.AtomoArregloContext):
        elementos = [self.visit(expr) for expr in ctx.expresionPipeline()]
        return HolocronArray(elementos)

    def visitAtomoIndexacion(self, ctx: HolocronDSLParser.AtomoIndexacionContext):
        nombre_var = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column
        contenedor = self.symbol_table.obtener_valor(nombre_var, linea=linea, columna=columna)
        indice = int(self.visit(ctx.expresionAritmetica()))
        if isinstance(contenedor, (HolocronArray, list, tuple)):
            if isinstance(contenedor, HolocronArray):
                return contenedor.obtener(indice)
            else:
                if indice < -len(contenedor) or indice >= len(contenedor):
                    raise IndiceFueraDeRangoError(indice, len(contenedor), linea, columna)
                return contenedor[indice]
        elif isinstance(contenedor, str):
            if indice < -len(contenedor) or indice >= len(contenedor):
                raise IndiceFueraDeRangoError(indice, len(contenedor), linea, columna)
            return contenedor[indice]
        else:
            raise TipoIncompatibleError("indexacion", type(contenedor).__name__, "int", linea, columna)

    def visitAtomoLlamada(self, ctx: HolocronDSLParser.AtomoLlamadaContext):
        nombre = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column
        argumentos = [self.visit(arg) for arg in ctx.expresionPipeline()]
        return self._ejecutar_llamada(nombre, argumentos, linea, columna)

    def visitAtomoNumero(self, ctx: HolocronDSLParser.AtomoNumeroContext):
        texto = ctx.NUMERO().getText()
        if "." in texto:
            return float(texto)
        return int(texto)

    def visitAtomoCadena(self, ctx: HolocronDSLParser.AtomoCadenaContext):
        return self._limpiar_cadena(ctx.CADENA().getText())

    def visitAtomoBooleano(self, ctx: HolocronDSLParser.AtomoBooleanoContext):
        txt = ctx.BOOL().getText().lower()
        return txt in ("cierto_es", "verdadero", "true")

    def visitAtomoIdentificador(self, ctx: HolocronDSLParser.AtomoIdentificadorContext):
        nombre = ctx.ID().getText()
        linea = ctx.start.line
        columna = ctx.start.column

        # 1. Si estamos evaluando dentro de una fila de tabla, la columna tiene prioridad
        if self.fila_contexto_actual is not None:
            if nombre in self.fila_contexto_actual:
                return self.fila_contexto_actual[nombre]

        # 2. Si no es columna de la fila actual, buscar en la tabla de simbolos
        if self.symbol_table.existe(nombre):
            return self.symbol_table.obtener_valor(nombre, linea=linea, columna=columna)

        # 3. Si estabamos en fila y no existia ni como columna ni como variable
        if self.fila_contexto_actual is not None:
            raise ColumnaInexistenteError(nombre, list(self.fila_contexto_actual.keys()), linea, columna)

        # 4. Error de variable no definida
        raise VariableNoDefinidaError(nombre, linea, columna, self.symbol_table.ambito_actual.variables_visibles())

    def visitAtomoParentesis(self, ctx: HolocronDSLParser.AtomoParentesisContext):
        return self.visit(ctx.expresionAritmetica())

    # -------------------------------------------------------------------------
    # METODOS DE APOYO
    # -------------------------------------------------------------------------

    def _obtener_valor_literal(self, ctx: HolocronDSLParser.LiteralContext) -> Any:
        if ctx.NUMERO():
            txt = ctx.NUMERO().getText()
            return float(txt) if "." in txt else int(txt)
        elif ctx.CADENA():
            return self._limpiar_cadena(ctx.CADENA().getText())
        elif ctx.BOOL():
            return ctx.BOOL().getText().lower() in ("cierto_es", "verdadero", "true")
        return None

    def _limpiar_cadena(self, texto_crudo: str) -> str:
        """Remueve comillas simples o dobles de los extremos de un literal de cadena."""
        if (texto_crudo.startswith('"') and texto_crudo.endswith('"')) or \
           (texto_crudo.startswith("'") and texto_crudo.endswith("'")):
            return texto_crudo[1:-1]
        return texto_crudo

    def _validar_ambos_numericos(self, op: str, val_izq: Any, val_der: Any, linea: int, columna: int):
        if isinstance(val_izq, bool) or isinstance(val_der, bool) or \
           not isinstance(val_izq, (int, float)) or not isinstance(val_der, (int, float)):
            raise TipoIncompatibleError(op, type(val_izq).__name__, type(val_der).__name__, linea, columna)

    def _ejecutar_llamada(self, nombre: str, argumentos: List[Any], linea: int, columna: int) -> Any:
        nombre_lower = nombre.lower()

        # 1. Funciones de Estructuras de Datos
        if nombre_lower in ("crear_pila", "nueva_pila"):
            init = argumentos[0] if argumentos else None
            return HolocronPila(init)

        elif nombre_lower in ("apilar", "push"):
            if len(argumentos) < 2:
                raise AridadInvalidaError(nombre, 2, len(argumentos), linea, columna)
            pila = argumentos[0]
            if not isinstance(pila, HolocronPila):
                raise TipoIncompatibleError("apilar", type(pila).__name__, "HolocronPila", linea, columna)
            return pila.apilar(argumentos[1])

        elif nombre_lower in ("desapilar", "pop"):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            pila = argumentos[0]
            if not isinstance(pila, HolocronPila):
                raise TipoIncompatibleError("desapilar", type(pila).__name__, "HolocronPila", linea, columna)
            return pila.desapilar()

        elif nombre_lower in ("cima", "tope", "peek"):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            pila = argumentos[0]
            if not isinstance(pila, HolocronPila):
                raise TipoIncompatibleError("cima", type(pila).__name__, "HolocronPila", linea, columna)
            return pila.cima()

        elif nombre_lower in ("crear_cola", "nueva_cola"):
            init = argumentos[0] if argumentos else None
            return HolocronCola(init)

        elif nombre_lower in ("encolar", "queue"):
            if len(argumentos) < 2:
                raise AridadInvalidaError(nombre, 2, len(argumentos), linea, columna)
            cola = argumentos[0]
            if not isinstance(cola, HolocronCola):
                raise TipoIncompatibleError("encolar", type(cola).__name__, "HolocronCola", linea, columna)
            return cola.encolar(argumentos[1])

        elif nombre_lower in ("desencolar", "dequeue"):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            cola = argumentos[0]
            if not isinstance(cola, HolocronCola):
                raise TipoIncompatibleError("desencolar", type(cola).__name__, "HolocronCola", linea, columna)
            return cola.desencolar()

        elif nombre_lower in ("frente", "front"):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            cola = argumentos[0]
            if not isinstance(cola, HolocronCola):
                raise TipoIncompatibleError("frente", type(cola).__name__, "HolocronCola", linea, columna)
            return cola.frente()

        elif nombre_lower in ("esta_vacia", "es_vacia"):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            est = argumentos[0]
            if hasattr(est, "esta_vacia"):
                return est.esta_vacia()
            elif hasattr(est, "esta_vacio"):
                return est.esta_vacio()
            elif isinstance(est, (list, tuple, str, dict)):
                return len(est) == 0
            return False

        elif nombre_lower in ("longitud", "tamano", "len", "conteo_elementos"):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            obj = argumentos[0]
            if isinstance(obj, HolocronTable):
                return len(obj.filas)
            if hasattr(obj, "longitud"):
                return obj.longitud()
            if hasattr(obj, "tamano"):
                return obj.tamano()
            if isinstance(obj, (list, tuple, str, dict)):
                return len(obj)
            return 1

        elif nombre_lower in ("crear_lista", "crear_arreglo", "nuevo_arreglo"):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            tam = int(argumentos[0])
            val_defecto = argumentos[1] if len(argumentos) > 1 else 0
            return crear_lista_dimensionada(tam, val_defecto)

        elif nombre_lower in ("agregar", "append"):
            if len(argumentos) < 2:
                raise AridadInvalidaError(nombre, 2, len(argumentos), linea, columna)
            arr = argumentos[0]
            if isinstance(arr, HolocronArray):
                return arr.agregar(argumentos[1])
            elif isinstance(arr, list):
                arr.append(argumentos[1])
                return arr
            raise TipoIncompatibleError("agregar", type(arr).__name__, "HolocronArray", linea, columna)

        elif nombre_lower in ("insertar",):
            if len(argumentos) < 3:
                raise AridadInvalidaError(nombre, 3, len(argumentos), linea, columna)
            arr = argumentos[0]
            idx = int(argumentos[1])
            if isinstance(arr, HolocronArray):
                return arr.insertar(idx, argumentos[2])
            elif isinstance(arr, list):
                arr.insert(idx, argumentos[2])
                return arr
            raise TipoIncompatibleError("insertar", type(arr).__name__, "HolocronArray", linea, columna)

        elif nombre_lower in ("remover", "eliminar_indice"):
            if len(argumentos) < 2:
                raise AridadInvalidaError(nombre, 2, len(argumentos), linea, columna)
            arr = argumentos[0]
            idx = int(argumentos[1])
            if isinstance(arr, HolocronArray):
                return arr.remover(idx)
            elif isinstance(arr, list):
                return arr.pop(idx)
            raise TipoIncompatibleError("remover", type(arr).__name__, "HolocronArray", linea, columna)

        elif nombre_lower in ("obtener",):
            if len(argumentos) < 2:
                raise AridadInvalidaError(nombre, 2, len(argumentos), linea, columna)
            arr = argumentos[0]
            idx = int(argumentos[1])
            if isinstance(arr, HolocronArray):
                return arr.obtener(idx)
            elif isinstance(arr, (list, tuple)):
                return arr[idx]
            raise TipoIncompatibleError("obtener", type(arr).__name__, "HolocronArray", linea, columna)

        elif nombre_lower in ("subarreglo", "rebanada"):
            if len(argumentos) < 3:
                raise AridadInvalidaError(nombre, 3, len(argumentos), linea, columna)
            arr = argumentos[0]
            ini = int(argumentos[1])
            fin = int(argumentos[2])
            if isinstance(arr, HolocronArray):
                return arr.subarreglo(ini, fin)
            elif isinstance(arr, list):
                return arr[ini:fin]
            raise TipoIncompatibleError("subarreglo", type(arr).__name__, "HolocronArray", linea, columna)

        elif nombre_lower in ("invertir",):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            arr = argumentos[0]
            if isinstance(arr, HolocronArray):
                return arr.invertir()
            elif isinstance(arr, list):
                return list(reversed(arr))
            raise TipoIncompatibleError("invertir", type(arr).__name__, "HolocronArray", linea, columna)

        elif nombre_lower in ("ordenar_lista",):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            arr = argumentos[0]
            asc = argumentos[1] if len(argumentos) > 1 else True
            if isinstance(arr, HolocronArray):
                return arr.ordenar(asc)
            elif isinstance(arr, list):
                return sorted(arr, reverse=not asc)
            raise TipoIncompatibleError("ordenar_lista", type(arr).__name__, "HolocronArray", linea, columna)

        # 2. Funciones de Machine Learning
        elif nombre_lower in ("crear_arbol", "nuevo_arbol"):
            prof = int(argumentos[0]) if argumentos else 4
            return ArbolDecisionGalactico(profundidad_maxima=prof)

        elif nombre_lower in ("crear_perceptron", "nuevo_perceptron"):
            tasa = float(argumentos[0]) if argumentos else 0.05
            epocas = int(argumentos[1]) if len(argumentos) > 1 else 50
            return PerceptronGalactico(tasa_aprendizaje=tasa, epocas=epocas)

        elif nombre_lower in ("crear_kmeans", "nuevo_kmeans"):
            k = int(argumentos[0]) if argumentos else 3
            return KMeansGalactico(k=k)

        elif nombre_lower in ("evaluar_exactitud", "exactitud", "accuracy"):
            if len(argumentos) < 2:
                raise AridadInvalidaError(nombre, 2, len(argumentos), linea, columna)
            y_real = list(argumentos[0]) if hasattr(argumentos[0], "__iter__") else [argumentos[0]]
            y_pred = list(argumentos[1]) if hasattr(argumentos[1], "__iter__") else [argumentos[1]]
            return evaluar_exactitud(y_real, y_pred)

        elif nombre_lower in ("matriz_confusion",):
            if len(argumentos) < 2:
                raise AridadInvalidaError(nombre, 2, len(argumentos), linea, columna)
            y_real = list(argumentos[0]) if hasattr(argumentos[0], "__iter__") else [argumentos[0]]
            y_pred = list(argumentos[1]) if hasattr(argumentos[1], "__iter__") else [argumentos[1]]
            res = calcular_matriz_confusion(y_real, y_pred)
            return str(res["matriz"])

        elif nombre_lower in ("distancia_euclidiana", "distancia"):
            if len(argumentos) < 2:
                raise AridadInvalidaError(nombre, 2, len(argumentos), linea, columna)
            return distancia_euclidiana(list(argumentos[0]), list(argumentos[1]))

        elif nombre_lower in ("impureza_gini", "gini"):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            return calcular_impureza_gini(list(argumentos[0]))

        elif nombre_lower in ("entropia",):
            if len(argumentos) < 1:
                raise AridadInvalidaError(nombre, 1, len(argumentos), linea, columna)
            return calcular_entropia(list(argumentos[0]))

        # 3. Mision de usuario
        mision = self.symbol_table.resolver_mision(nombre, linea=linea, columna=columna)
        if len(argumentos) != len(mision.parametros):
            raise AridadInvalidaError(
                nombre_mision=nombre,
                esperados=len(mision.parametros),
                recibidos=len(argumentos),
                linea=linea,
                columna=columna
            )

        self.symbol_table.entrar_ambito(nombre)
        try:
            for nombre_param, valor_arg in zip(mision.parametros, argumentos):
                self.symbol_table.definir(nombre_param, valor_arg, linea=linea, columna=columna)
            for sent_ctx in mision.sentencias_ctx:
                self.visit(sent_ctx)
            return self.visit(mision.retorno_ctx)
        finally:
            self.symbol_table.salir_ambito()
