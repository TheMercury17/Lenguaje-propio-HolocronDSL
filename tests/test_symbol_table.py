# Pruebas unitarias para la tabla de simbolos y manejo de ambitos
import unittest
from src.interpreter.symbol_table import SymbolTable, SymbolType
from src.errors.semantic_error import VariableNoDefinidaError, MisionNoDefinidaError


class TestSymbolTable(unittest.TestCase):
    """Verifica la correcta definicion, resolucion y aislamiento de ambitos."""

    def setUp(self):
        self.st = SymbolTable()

    def test_definir_y_resolver_global(self):
        self.st.definir("flota_tamanio", 50)
        self.assertTrue(self.st.existe("flota_tamanio"))
        self.assertEqual(self.st.obtener_valor("flota_tamanio"), 50)

    def test_variable_no_definida_lanza_error(self):
        with self.assertRaises(VariableNoDefinidaError):
            self.st.resolver("variable_inexistente")

    def test_ambitos_anidados_y_sombreado(self):
        self.st.definir("nivel_alerta", "verde")

        # Entrar a ambito local
        self.st.entrar_ambito("mision_tactica")
        self.assertEqual(self.st.obtener_valor("nivel_alerta"), "verde")

        # Sombrear variable localmente
        self.st.definir("nivel_alerta", "rojo")
        self.assertEqual(self.st.obtener_valor("nivel_alerta"), "rojo")

        # Salir de ambito
        self.st.salir_ambito()
        self.assertEqual(self.st.obtener_valor("nivel_alerta"), "verde")

    def test_registro_y_resolucion_de_misiones(self):
        self.st.registrar_mision(
            nombre="preparar_caza",
            parametros=["nave", "escudos"],
            sentencias_ctx=[],
            retorno_ctx=None
        )
        mision = self.st.resolver_mision("preparar_caza")
        self.assertEqual(mision.nombre, "preparar_caza")
        self.assertEqual(mision.parametros, ["nave", "escudos"])

        with self.assertRaises(MisionNoDefinidaError):
            self.st.resolver_mision("mision_desconocida")


if __name__ == "__main__":
    unittest.main()
