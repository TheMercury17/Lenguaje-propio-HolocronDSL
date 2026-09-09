# Manejador de errores lexicos y sintacticos para HolocronDSL
# Proporciona mensajes contextuales con ubicacion precisa (linea y columna)

from dataclasses import dataclass
from typing import List, Optional
from antlr4.error.ErrorListener import ErrorListener
from antlr4.Recognizer import Recognizer
from antlr4.Token import Token


@dataclass
class HolocronSyntaxError:
    """Representa una anomalia detectada en la fase lexica o sintactica."""
    linea: int
    columna: int
    mensaje: str
    simbolo: Optional[str] = None

    def __str__(self) -> str:
        simbolo_info = f" en el token '{self.simbolo}'" if self.simbolo else ""
        return f"[Error Sintactico] Linea {self.linea}:{self.columna}{simbolo_info} -> {self.mensaje}"


class HolocronErrorListener(ErrorListener):
    """
    ErrorListener personalizado para ANTLR4.
    Intercepta errores sintacticos y lexicos para generar reportes comprensibles.
    """

    def __init__(self):
        super().__init__()
        self.errores: List[HolocronSyntaxError] = []

    def syntaxError(
        self,
        recognizer: Recognizer,
        offendingSymbol: Optional[Token],
        line: int,
        column: int,
        msg: str,
        e,
    ):
        # Extraer texto del token infractor si esta disponible
        simbolo_texto = offendingSymbol.text if offendingSymbol else None

        # Personalizar y traducir sugerencias comunes de ANTLR
        mensaje_amigable = self._formatear_mensaje(msg, simbolo_texto)

        error = HolocronSyntaxError(
            linea=line,
            columna=column,
            mensaje=mensaje_amigable,
            simbolo=simbolo_texto,
        )
        self.errores.append(error)

    def _formatear_mensaje(self, msg_original: str, simbolo: Optional[str]) -> str:
        """Adapta el mensaje tecnico generado por ANTLR a una explicacion clara."""
        if "no viable alternative at input" in msg_original:
            return f"Construccion no reconocida cerca de '{simbolo}'. Verifique la sintaxis de la instruccion."
        if "mismatched input" in msg_original:
            return f"Elemento inesperado '{simbolo}'. Se esperaba otra palabra reservada, operador o delimitador."
        if "extraneous input" in msg_original:
            return f"Token adicional e innecesario '{simbolo}' detectado en este punto."
        if "missing" in msg_original:
            return f"Falta un elemento requerido en la sentencia: {msg_original}"
        return msg_original

    def tiene_errores(self) -> bool:
        """Indica si se registraron anomalias durante el analisis."""
        return len(self.errores) > 0

    def obtener_reporte(self) -> str:
        """Genera un reporte consolidado en texto de todos los errores."""
        if not self.tiene_errores():
            return "Analisis sintactico completado sin anomalias en los sensores."
        encabezado = f"Se detectaron {len(self.errores)} anomalias sintacticas en el codigo:\n"
        cuerpo = "\n".join(f"  - {err}" for err in self.errores)
        return encabezado + cuerpo
