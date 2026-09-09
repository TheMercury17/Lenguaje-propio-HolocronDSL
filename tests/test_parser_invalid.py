# Pruebas unitarias sintacticas negativas para HolocronDSL
# Valida la deteccion oportuna y el reporte diagnostico de errores sintacticos y lexicos

import unittest
from src.compiler.driver import parse_string


class TestHolocronParserInvalid(unittest.TestCase):
    """Verifica que el Front-end rechace adecuadamente programas con errores sintacticos."""

    def assertSintaxisInvalida(self, codigo: str, fragmento_esperado: str = None):
        """Metodo de asercion auxiliar para verificar que se reporte error."""
        arbol, error_listener, _ = parse_string(codigo)
        self.assertTrue(
            error_listener.tiene_errores(),
            f"Se esperaba que el codigo fuera rechazado por error sintactico, pero fue aceptado:\n{codigo}"
        )
        reporte = error_listener.obtener_reporte()
        self.assertIn("Error Sintactico", reporte)
        if fragmento_esperado:
            self.assertTrue(
                any(fragmento_esperado.lower() in str(err).lower() for err in error_listener.errores),
                f"Se esperaba '{fragmento_esperado}' en los errores reportados:\n{reporte}"
            )
        return error_listener.errores

    def test_falta_operador_asignacion(self):
        """Detecta asignacion invalida donde falta el operador '<-'."""
        codigo = 'flota abrir_holocron "datos.csv"'
        errores = self.assertSintaxisInvalida(codigo)
        self.assertGreaterEqual(len(errores), 1)
        self.assertEqual(errores[0].linea, 1)

    def test_corchetes_no_cerrados_en_seleccion(self):
        """Detecta listas de sectores sin cerrar con corchete ']'."""
        codigo = """
        datos <- base
            ==> revelar_sectores [ sector, potencia, escudos
        """
        self.assertSintaxisInvalida(codigo)

    def test_operacion_pipeline_vacia(self):
        """Detecta una flecha de pipeline sin operacion posterior."""
        codigo = """
        datos <- base
            ==>
        """
        self.assertSintaxisInvalida(codigo)

    def test_holograma_sin_cierre(self):
        """Detecta una proyeccion holografica sin la clausula 'fin_holograma'."""
        codigo = """
        proyectar_holograma barras desde registros
            eje_x := "planeta"
            eje_y := "tropas"
        """
        self.assertSintaxisInvalida(codigo)

    def test_mision_sin_retornar_orden(self):
        """Detecta funciones que omiten la clausula obligatoria 'retornar_orden'."""
        codigo = """
        mision calcular_fuerza con_parametros (datos)
            x <- datos
        fin_mision
        """
        self.assertSintaxisInvalida(codigo)

    def test_condicional_mal_formado(self):
        """Detecta estructuras de evaluacion de fuerza sin parentesis o sin fin_evaluar."""
        codigo = """
        evaluar_fuerza escudos < 10
        senda_luminosa
            transmitir_mensaje "Bajo nivel"
        """
        self.assertSintaxisInvalida(codigo)

    def test_caracter_lexico_invalido(self):
        """Detecta caracteres que no pertenecen al alfabeto del lenguaje."""
        codigo = 'datos <- abrir_holocron "datos.csv" @@@'
        self.assertSintaxisInvalida(codigo)


if __name__ == "__main__":
    unittest.main()
