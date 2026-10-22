# Modulo de errores semanticos para HolocronDSL
# Gestiona errores en tiempo de interpretacion con reporte de linea y columna

from typing import Optional, List


class HolocronSemanticError(Exception):
    """Excepcion base para errores semanticos detectados durante la interpretacion."""

    def __init__(
        self,
        mensaje: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None,
        sugerencia: Optional[str] = None
    ):
        self.mensaje = mensaje
        self.linea = linea
        self.columna = columna
        self.sugerencia = sugerencia
        super().__init__(self.formatear())

    def formatear(self) -> str:
        posicion = ""
        if self.linea is not None and self.columna is not None:
            posicion = f"[Linea {self.linea}, Columna {self.columna}] "
        elif self.linea is not None:
            posicion = f"[Linea {self.linea}] "

        resultado = f"Error Semantico: {posicion}{self.mensaje}"
        if self.sugerencia:
            resultado += f"\n  Sugerencia: {self.sugerencia}"
        return resultado


class VariableNoDefinidaError(HolocronSemanticError):
    """Se lanza cuando se intenta acceder a una variable que no existe en el ambito actual."""

    def __init__(
        self,
        nombre_var: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None,
        variables_disponibles: Optional[List[str]] = None
    ):
        mensaje = f"El identificador '{nombre_var}' no ha sido registrado en la memoria del holocron."
        sugerencia = None
        if variables_disponibles:
            sugerencia = f"Las variables registradas actualmente son: {', '.join(sorted(variables_disponibles))}."
        super().__init__(mensaje, linea, columna, sugerencia)


class ColumnaInexistenteError(HolocronSemanticError):
    """Se lanza cuando una operacion hace referencia a una columna ausente en el holocron."""

    def __init__(
        self,
        nombre_col: str,
        columnas_disponibles: Optional[List[str]] = None,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ):
        mensaje = f"La columna '{nombre_col}' no existe en la estructura del holocron procesado."
        sugerencia = None
        if columnas_disponibles:
            sugerencia = f"Las columnas disponibles son: [{', '.join(repr(c) for c in columnas_disponibles)}]."
        super().__init__(mensaje, linea, columna, sugerencia)


class TipoIncompatibleError(HolocronSemanticError):
    """Se lanza ante operaciones entre tipos que no son compatibles."""

    def __init__(
        self,
        operacion: str,
        tipo_izq: str,
        tipo_der: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ):
        mensaje = f"Operacion '{operacion}' no valida entre tipos incompatibles: '{tipo_izq}' y '{tipo_der}'."
        sugerencia = "Verifique que ambos operandos sean numericos para operaciones aritmeticas o compatibles para comparaciones."
        super().__init__(mensaje, linea, columna, sugerencia)


class DivisionPorCeroError(HolocronSemanticError):
    """Se lanza ante intentos de division o modulo entre cero."""

    def __init__(
        self,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ):
        mensaje = "Perturbacion matematica: intento de division o modulo entre cero."
        sugerencia = "Verifique los valores del denominador o purgue filas con ceros antes de forjar la columna."
        super().__init__(mensaje, linea, columna, sugerencia)


class MisionNoDefinidaError(HolocronSemanticError):
    """Se lanza cuando se invoca una mision que no ha sido declarada."""

    def __init__(
        self,
        nombre_mision: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ):
        mensaje = f"La mision tactica '{nombre_mision}' no ha sido asignada ni declarada en la flota."
        sugerencia = "Asegurese de declarar la mision con 'mision nombre(...) ... fin_mision' antes de invocarla."
        super().__init__(mensaje, linea, columna, sugerencia)


class AridadInvalidaError(HolocronSemanticError):
    """Se lanza cuando la cantidad de argumentos no coincide con los parametros de la mision."""

    def __init__(
        self,
        nombre_mision: str,
        esperados: int,
        recibidos: int,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ):
        mensaje = f"La mision '{nombre_mision}' requiere {esperados} parametro(s), pero se suministraron {recibidos}."
        sugerencia = "Revise la definicion de la mision para pasar el numero exacto de parametros."
        super().__init__(mensaje, linea, columna, sugerencia)


class ArchivoNoEncontradoError(HolocronSemanticError):
    """Se lanza cuando la ruta de un holocron CSV a abrir no existe o no es accesible."""

    def __init__(
        self,
        ruta: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ):
        mensaje = f"No se pudo acceder al holocron fisico en la ruta: '{ruta}'."
        sugerencia = "Verifique la existencia del archivo en el disco y su ruta relativa o absoluta."
        super().__init__(mensaje, linea, columna, sugerencia)


class OperacionInvalidaError(HolocronSemanticError):
    """Se lanza cuando se intenta una operacion de transformacion sobre un tipo que no es una tabla."""

    def __init__(
        self,
        operacion: str,
        tipo_recibido: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ):
        mensaje = f"La operacion de pipeline '{operacion}' solo puede aplicarse sobre tablas (holocrones), no sobre '{tipo_recibido}'."
        sugerencia = "Asegurese de que la base del pipeline sea un holocron cargado o transformado."
        super().__init__(mensaje, linea, columna, sugerencia)
