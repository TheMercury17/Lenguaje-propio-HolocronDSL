# Pruebas unitarias sintacticas negativas para HolocronDSL (Sintaxis Simplificada)

import unittest
from src.compiler.driver import parse_string


class TestHolocronParserInvalid(unittest.TestCase):
    """Verifica que el Front-end rechace adecuadamente programas con errores sintacticos."""

    def assertSintaxisInvalida(self, codigo: str):
        arbol, error_listener, _ = parse_string(codigo)
        self.assertTrue(
            error_listener.tiene_errores(),
            f"Se esperaba que el codigo fuera rechazado por error sintactico, pero fue aceptado:\n{codigo}"
        )
        reporte = error_listener.obtener_reporte()
        self.assertIn("Error Sintactico", reporte)
        return error_listener.errores

    def test_falta_operador_asignacion(self):
        """Detecta asignacion invalida donde falta el '='."""
        codigo = 'flota abrir_holocron "datos.csv"'
        errores = self.assertSintaxisInvalida(codigo)
        self.assertGreaterEqual(len(errores), 1)

    def test_corchetes_no_cerrados_en_seleccion(self):
        """Detecta listas de columnas sin cerrar con corchete ']'."""
        codigo = """
        datos = base
            |> revelar [ sector, potencia, escudos
        """
        self.assertSintaxisInvalida(codigo)

    def test_operacion_pipeline_vacia(self):
        """Detecta un pipeline '|>' sin operacion posterior."""
        codigo = """
        datos = base
            |>
        """
        self.assertSintaxisInvalida(codigo)

    def test_mision_sin_retornar(self):
        """Detecta funciones que omiten la clausula obligatoria 'retornar'."""
        codigo = """
        mision calcular_fuerza (datos)
            x = datos
        fin_mision
        """
        self.assertSintaxisInvalida(codigo)

    def test_condicional_sin_senda_luminosa(self):
        """Detecta estructuras de evaluacion de fuerza sin senda_luminosa."""
        codigo = """
        evaluar_fuerza escudos < 10
            mostrar "Bajo nivel"
        fin_evaluar
        """
        self.assertSintaxisInvalida(codigo)

    def test_caracter_lexico_invalido(self):
        """Detecta caracteres que no pertenecen al alfabeto del lenguaje."""
        codigo = 'datos = abrir_holocron "datos.csv" @@@'
        self.assertSintaxisInvalida(codigo)


if __name__ == "__main__":
    unittest.main()
