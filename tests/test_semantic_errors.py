# Pruebas unitarias de deteccion y reporte de errores semanticos
import unittest
from src.compiler.driver import parse_string
from src.interpreter.visitor import HolocronInterpreter
from src.errors.semantic_error import (
    VariableNoDefinidaError,
    ColumnaInexistenteError,
    TipoIncompatibleError,
    DivisionPorCeroError,
    MisionNoDefinidaError,
    AridadInvalidaError,
    OperacionInvalidaError
)


class TestSemanticErrors(unittest.TestCase):
    """Verifica que el interprete capture y reporte las anomalias semanticas adecuadamente."""

    def _ejecutar(self, codigo: str):
        arbol, err, _ = parse_string(codigo)
        if err.tiene_errores():
            self.fail(f"Error de sintaxis inesperado: {err.obtener_reporte()}")
        interp = HolocronInterpreter()
        return interp.visit(arbol)

    def test_variable_no_definida(self):
        codigo = "mostrar nave_fantasma"
        with self.assertRaises(VariableNoDefinidaError):
            self._ejecutar(codigo)

    def test_columna_inexistente_en_seleccion(self):
        codigo = """
        flota = abrir_holocron "examples/datos/telemetria_flota.csv"
            |> revelar [ columna_falsa ]
        """
        with self.assertRaises(ColumnaInexistenteError):
            self._ejecutar(codigo)

    def test_division_por_cero(self):
        codigo = "resultado = 100 / 0"
        with self.assertRaises(DivisionPorCeroError):
            self._ejecutar(codigo)

    def test_mision_no_definida(self):
        codigo = "res = mision_inexistente(10)"
        with self.assertRaises(MisionNoDefinidaError):
            self._ejecutar(codigo)

    def test_aridad_invalida_en_mision(self):
        codigo = """
        mision calcular(a, b)
            retornar a + b
        fin_mision

        resultado = calcular(10)
        """
        with self.assertRaises(AridadInvalidaError):
            self._ejecutar(codigo)

    def test_operacion_pipeline_sobre_no_tabla(self):
        codigo = "invalido = 42 |> purgar donde escudos > 10"
        with self.assertRaises(OperacionInvalidaError):
            self._ejecutar(codigo)


if __name__ == "__main__":
    unittest.main()
