# Estructura de datos tabular propia para HolocronDSL (HolocronTable)
# Motor tabular funcional e inmutable desarrollado desde cero (Grupo 5)

from typing import List, Dict, Any, Callable, Optional, Tuple, Union
from src.runtime.math_engine import HolocronMath
from src.runtime.io_engine import HolocronIO
from src.errors.semantic_error import ColumnaInexistenteError


class HolocronTable:
    """
    Representacion en memoria de un conjunto de datos tabular (Holocron).
    Proporciona operaciones funcionales puras para transformacion inmutable.
    """

    def __init__(
        self,
        columnas: List[str],
        filas: List[Dict[str, Any]],
        nombre: str = "holocron_anonimo"
    ):
        self.columnas: List[str] = list(columnas)
        # Copia superficial de filas para garantizar inmutabilidad
        self.filas: List[Dict[str, Any]] = [dict(f) for f in filas]
        self.nombre: str = nombre

    def __len__(self) -> int:
        return len(self.filas)

    def total_filas(self) -> int:
        return len(self.filas)

    def total_columnas(self) -> int:
        return len(self.columnas)

    def validar_columna(
        self,
        nombre_col: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> None:
        """Verifica si una columna existe en la tabla; de lo contrario lanza ColumnaInexistenteError."""
        if nombre_col not in self.columnas:
            raise ColumnaInexistenteError(nombre_col, self.columnas, linea, columna)

    def obtener_columna(
        self,
        nombre_col: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> List[Any]:
        """Extrae la lista de valores asociados a una columna."""
        self.validar_columna(nombre_col, linea, columna)
        return [f.get(nombre_col, None) for f in self.filas]

    def seleccionar(
        self,
        columnas_deseadas: List[str],
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> "HolocronTable":
        """
        Operacion 'revelar' / 'seleccionar':
        Conserva unicamente las columnas indicadas, validando su existencia.
        """
        for col in columnas_deseadas:
            self.validar_columna(col, linea, columna)

        nuevas_filas = []
        for fila in self.filas:
            nueva_fila = {col: fila.get(col, None) for col in columnas_deseadas}
            nuevas_filas.append(nueva_fila)

        return HolocronTable(
            columnas=columnas_deseadas,
            filas=nuevas_filas,
            nombre=f"{self.nombre}_revelado"
        )

    def purgar(
        self,
        predicado_fn: Callable[[Dict[str, Any]], bool]
    ) -> "HolocronTable":
        """
        Operacion 'purgar donde':
        Filtra las filas del holocron evaluando un predicado booleano por fila.
        """
        nuevas_filas = []
        for fila in self.filas:
            try:
                if predicado_fn(fila):
                    nuevas_filas.append(dict(fila))
            except Exception:
                # Si la evaluacion falla (por ejemplo tipo no compatible en fila corrupta), se descarta
                pass

        return HolocronTable(
            columnas=self.columnas,
            filas=nuevas_filas,
            nombre=f"{self.nombre}_purgado"
        )

    def forjar(
        self,
        nueva_columna: str,
        expresion_fn: Callable[[Dict[str, Any]], Any]
    ) -> "HolocronTable":
        """
        Operacion 'forjar col = expr':
        Calcula e inserta una nueva columna en cada fila del holocron.
        """
        nuevas_cols = list(self.columnas)
        if nueva_columna not in nuevas_cols:
            nuevas_cols.append(nueva_columna)

        nuevas_filas = []
        for fila in self.filas:
            copia_fila = dict(fila)
            valor_calculado = expresion_fn(fila)
            copia_fila[nueva_columna] = valor_calculado
            nuevas_filas.append(copia_fila)

        return HolocronTable(
            columnas=nuevas_cols,
            filas=nuevas_filas,
            nombre=f"{self.nombre}_forjado"
        )

    def ordenar(
        self,
        columna: str,
        ascendente: bool = True,
        linea: Optional[int] = None,
        col_pos: Optional[int] = None
    ) -> "HolocronTable":
        """
        Operacion 'ordenar por':
        Ordena las filas segun la columna indicada con manejo robusto de nulos y tipos mixtos.
        """
        self.validar_columna(columna, linea, col_pos)

        def clave_orden(fila):
            v = fila.get(columna, None)
            if v is None:
                # Los nulos se posicionan al final
                return (2, 0, "")
            if isinstance(v, (int, float)):
                return (0, float(v), "")
            return (1, 0, str(v))

        filas_ordenadas = sorted(self.filas, key=clave_orden, reverse=not ascendente)
        return HolocronTable(
            columnas=self.columnas,
            filas=filas_ordenadas,
            nombre=f"{self.nombre}_ordenado"
        )

    def eliminar_clones(self) -> "HolocronTable":
        """
        Operacion 'eliminar_clones':
        Elimina registros duplicados conservando el orden de aparicion original.
        """
        vistos = set()
        filas_unicas = []

        for fila in self.filas:
            # Crear tupla inmutable de los valores en orden de columnas
            tupla_fila = tuple(fila.get(c, None) for c in self.columnas)
            if tupla_fila not in vistos:
                vistos.add(tupla_fila)
                filas_unicas.append(dict(fila))

        return HolocronTable(
            columnas=self.columnas,
            filas=filas_unicas,
            nombre=f"{self.nombre}_sin_clones"
        )

    def sanar_vacios(
        self,
        opcion: str,
        valor_sustituto: Any = None
    ) -> "HolocronTable":
        """
        Operacion 'sanar_vacios':
        - 'descartar': descarta toda fila que contenga al menos un campo nulo.
        - 'con': sustituye los valores nulos por el valor indicado.
        """
        if opcion == "descartar":
            filas_sanas = [
                dict(f) for f in self.filas
                if not any(f.get(c) is None for c in self.columnas)
            ]
        else:
            filas_sanas = []
            for f in self.filas:
                fila_mod = dict(f)
                for c in self.columnas:
                    if fila_mod.get(c) is None:
                        fila_mod[c] = valor_sustituto
                filas_sanas.append(fila_mod)

        return HolocronTable(
            columnas=self.columnas,
            filas=filas_sanas,
            nombre=f"{self.nombre}_sanado"
        )

    def agrupar(
        self,
        columnas_grupo: List[str],
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> "HolocronGroupedTable":
        """
        Operacion 'agrupar por':
        Segmenta el holocron en particiones agrupadas segun las columnas clave.
        """
        for col in columnas_grupo:
            self.validar_columna(col, linea, columna)

        grupos: Dict[Tuple[Any, ...], List[Dict[str, Any]]] = {}
        for fila in self.filas:
            clave = tuple(fila.get(c, None) for c in columnas_grupo)
            if clave not in grupos:
                grupos[clave] = []
            grupos[clave].append(dict(fila))

        return HolocronGroupedTable(
            tabla_origen=self,
            columnas_grupo=columnas_grupo,
            grupos=grupos
        )

    def resumir(
        self,
        agregaciones: List[Tuple[str, str, Optional[str]]],
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> "HolocronTable":
        """
        Operacion 'resumir' sobre la tabla completa (sin agrupamiento previo).
        agregaciones: lista de tuplas (columna_salida, funcion_agregacion, columna_origen_opcional).
        """
        fila_resumen: Dict[str, Any] = {}
        columnas_salida: List[str] = []

        for col_dest, func_nombre, col_orig in agregaciones:
            columnas_salida.append(col_dest)
            valor = self._calcular_agregacion_subconjunto(self.filas, func_nombre, col_orig, linea, columna)
            fila_resumen[col_dest] = valor

        return HolocronTable(
            columnas=columnas_salida,
            filas=[fila_resumen],
            nombre=f"{self.nombre}_resumen"
        )

    def _calcular_agregacion_subconjunto(
        self,
        filas_subconjunto: List[Dict[str, Any]],
        func_nombre: str,
        col_orig: Optional[str],
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> Any:
        """Aplica la funcion estadistica de HolocronMath sobre el conjunto de filas provisto."""
        func = func_nombre.lower()

        if func in ("recuento", "conteo"):
            if col_orig:
                self.validar_columna(col_orig, linea, columna)
                return HolocronMath.conteo([f.get(col_orig) for f in filas_subconjunto])
            return len(filas_subconjunto)

        if not col_orig:
            raise ColumnaInexistenteError(f"(faltante para {func_nombre})", self.columnas, linea, columna)

        self.validar_columna(col_orig, linea, columna)
        valores = [f.get(col_orig) for f in filas_subconjunto]

        if func in ("acumular", "suma"):
            return HolocronMath.suma(valores)
        elif func in ("equilibrio", "promedio", "media"):
            return HolocronMath.redondear(HolocronMath.promedio(valores), 2)
        elif func in ("mediana",):
            return HolocronMath.mediana(valores)
        elif func in ("cenit", "maximo"):
            return HolocronMath.maximo(valores)
        elif func in ("nadir", "minimo"):
            return HolocronMath.minimo(valores)
        elif func in ("desviacion",):
            return HolocronMath.redondear(HolocronMath.desviacion(valores), 2)
        else:
            raise ValueError(f"Funcion de agregacion desconocida: '{func_nombre}'.")

    def archivar(self, ruta: str, delimitador: str = ",") -> str:
        """Persiste la tabla en formato CSV utilizando la biblioteca propia HolocronIO."""
        return HolocronIO.escribir_csv(ruta, self.columnas, self.filas, delimitador)

    def a_cadena_tabular(self, max_filas: int = 15) -> str:
        """Genera una representacion visual en texto (tabla ASCII) para la terminal."""
        if not self.filas:
            return f"[Holocron vacio: {len(self.columnas)} columnas, 0 registros]"

        cols = self.columnas
        filas_mostrar = self.filas[:max_filas]

        # Calcular anchos de columna
        anchos = {}
        for c in cols:
            max_c = len(str(c))
            for f in filas_mostrar:
                val = f.get(c, "")
                if val is None:
                    cad = "nulo"
                elif isinstance(val, bool):
                    cad = "cierto_es" if val else "falso_es"
                else:
                    cad = str(val)
                max_c = max(max_c, len(cad))
            anchos[c] = min(max_c, 30)

        # Construir tabla con caracteres estandar
        linea_borde = "+" + "+".join("-" * (anchos[c] + 2) for c in cols) + "+"
        cabecera = "| " + " | ".join(str(c).ljust(anchos[c]) for c in cols) + " |"

        lineas = [linea_borde, cabecera, linea_borde]
        for f in filas_mostrar:
            partes = []
            for c in cols:
                val = f.get(c, "")
                if val is None:
                    cad = "nulo"
                elif isinstance(val, bool):
                    cad = "cierto_es" if val else "falso_es"
                else:
                    cad = str(val)
                if len(cad) > 30:
                    cad = cad[:27] + "..."
                if isinstance(val, (int, float)) and not isinstance(val, bool):
                    partes.append(cad.rjust(anchos[c]))
                else:
                    partes.append(cad.ljust(anchos[c]))
            lineas.append("| " + " | ".join(partes) + " |")

        lineas.append(linea_borde)
        total = len(self.filas)
        if total > max_filas:
            lineas.append(f"  [... {total - max_filas} registros adicionales omitidos en la transmision ...]")
        lineas.append(f"  (Total de registros galacticos: {total} filas x {len(cols)} columnas)")
        return "\n".join(lineas)

    def __repr__(self) -> str:
        return self.a_cadena_tabular()


class HolocronGroupedTable:
    """
    Representa un conjunto de datos particionado por una o mas columnas de agrupamiento.
    """

    def __init__(
        self,
        tabla_origen: HolocronTable,
        columnas_grupo: List[str],
        grupos: Dict[Tuple[Any, ...], List[Dict[str, Any]]]
    ):
        self.tabla_origen = tabla_origen
        self.columnas_grupo = list(columnas_grupo)
        self.grupos = grupos

    def resumir(
        self,
        agregaciones: List[Tuple[str, str, Optional[str]]],
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> HolocronTable:
        """
        Aplica las funciones de agregacion especificadas sobre cada grupo particionado.
        Retorna una nueva HolocronTable con las columnas de agrupamiento mas los agregados.
        """
        columnas_salida = list(self.columnas_grupo)
        for col_dest, _, _ in agregaciones:
            if col_dest not in columnas_salida:
                columnas_salida.append(col_dest)

        filas_resumen: List[Dict[str, Any]] = []

        # Ordenar las claves de grupo para presentacion deterministica
        claves_ordenadas = sorted(self.grupos.keys(), key=lambda k: tuple(str(x) for x in k))

        for clave in claves_ordenadas:
            filas_grupo = self.grupos[clave]
            fila_res: Dict[str, Any] = {}

            # Poblar las columnas de agrupacion
            for idx_g, col_g in enumerate(self.columnas_grupo):
                fila_res[col_g] = clave[idx_g]

            # Calcular cada metrica de agregacion sobre las filas del grupo
            for col_dest, func_nombre, col_orig in agregaciones:
                valor = self.tabla_origen._calcular_agregacion_subconjunto(
                    filas_grupo, func_nombre, col_orig, linea, columna
                )
                fila_res[col_dest] = valor

            filas_resumen.append(fila_res)

        return HolocronTable(
            columnas=columnas_salida,
            filas=filas_resumen,
            nombre=f"{self.tabla_origen.nombre}_resumen_grupos"
        )
