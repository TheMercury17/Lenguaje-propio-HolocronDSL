# Pruebas unitarias de ejecucion semantica correcta
import unittest
from src.compiler.driver import parse_string
from src.interpreter.visitor import HolocronInterpreter
from src.runtime.holocron_table import HolocronTable


class TestSemanticExecution(unittest.TestCase):
    """Verifica la ejecucion completa y correcta de construcciones del lenguaje."""

    def _interpretar(self, codigo: str) -> HolocronInterpreter:
        arbol, err, _ = parse_string(codigo)
        if err.tiene_errores():
            self.fail(f"Error sintactico inesperado: {err.obtener_reporte()}")
        interp = HolocronInterpreter()
        interp.visit(arbol)
        return interp

    def test_asignacion_aritmetica_y_logica(self):
        codigo = """
        x = 10 + 5 * 2
        z = (20 - 4) / 4
        flag = cierto_es
        """
        interp = self._interpretar(codigo)
        self.assertEqual(interp.symbol_table.obtener_valor("x"), 20)
        self.assertEqual(interp.symbol_table.obtener_valor("z"), 4)
        self.assertEqual(interp.symbol_table.obtener_valor("flag"), True)

    def test_mision_con_retorno_de_calculo(self):
        codigo = """
        mision potencia_de_fuego(base, multiplicador)
            total = base * multiplicador + 10
            retornar total
        fin_mision

        fuerza_caza = potencia_de_fuego(50, 2)
        """
        interp = self._interpretar(codigo)
        self.assertEqual(interp.symbol_table.obtener_valor("fuerza_caza"), 110)

    def test_evaluacion_condicional_senda_luminosa(self):
        codigo = """
        estado = "inicial"
        evaluar_fuerza 10 > 5
        senda_luminosa
            estado = "luminoso"
        senda_oscura
            estado = "oscuro"
        fin_evaluar
        """
        interp = self._interpretar(codigo)
        self.assertEqual(interp.symbol_table.obtener_valor("estado"), "luminoso")

    def test_evaluacion_condicional_senda_oscura(self):
        codigo = """
        estado = "inicial"
        evaluar_fuerza 2 > 100
        senda_luminosa
            estado = "luminoso"
        senda_oscura
            estado = "oscuro"
        fin_evaluar
        """
        interp = self._interpretar(codigo)
        self.assertEqual(interp.symbol_table.obtener_valor("estado"), "oscuro")

    def test_pipeline_completo_sobre_archivo(self):
        codigo = """
        datos = abrir_holocron "examples/datos/telemetria_flota.csv"
        cazas_imperiales = datos
            |> revelar [ identificador, faccion, escudos, victorias ]
            |> purgar donde faccion == "Imperio"
            |> forjar rango = victorias * 2
            |> ordenar por rango descendente
        """
        interp = self._interpretar(codigo)
        tabla = interp.symbol_table.obtener_valor("cazas_imperiales")
        self.assertIsInstance(tabla, HolocronTable)
        self.assertTrue(len(tabla) > 0)
        self.assertIn("rango", tabla.columnas)
        # Todos deben ser de faccion Imperio
        facciones = [f["faccion"] for f in tabla.filas]
        self.assertTrue(all(fac == "Imperio" for fac in facciones))


if __name__ == "__main__":
    unittest.main()
