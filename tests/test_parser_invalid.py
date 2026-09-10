# Pruebas unitarias sintacticas negativas para HolocronDSL (Sintaxis Simplificada)

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

for venv_name in [".venv", "venv"]:
    vdir = ROOT_DIR / venv_name
    if vdir.is_dir():
        for sp in vdir.glob("lib/python*/site-packages"):
            if sp.is_dir() and str(sp) not in sys.path:
                sys.path.insert(0, str(sp))
        sp_win = vdir / "Lib" / "site-packages"
        if sp_win.is_dir() and str(sp_win) not in sys.path:
            sys.path.insert(0, str(sp_win))

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

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
