# Pruebas unitarias y de integracion para la funcionalidad de Regresion Lineal y Correlacion
# Fase 3: Modelado Estadistico y Proyeccion de Tendencias (Grupo 5)

import unittest
import tempfile
from pathlib import Path

from src.runtime.math_engine import HolocronMath
from src.runtime.holocron_table import HolocronTable, HolocronRegressionResult
from src.runtime.graphics_engine import HolocronPlotter
from src.compiler.driver import parse_string
from src.interpreter.visitor import HolocronInterpreter
from src.errors.semantic_error import HolocronSemanticError


class TestRegression(unittest.TestCase):
    """Verifica el analisis matematico, la transformacion tabular y la proyeccion visual de regresiones."""

    def test_covarianza_y_correlacion_matematica(self):
        # Datos perfectamente correlacionados linealmente: y = 2x + 1
        x = [1, 2, 3, 4, 5]
        y = [3, 5, 7, 9, 11]

        cov = HolocronMath.covarianza(x, y)
        self.assertIsNotNone(cov)
        self.assertAlmostEqual(cov, 5.0, places=4)

        r = HolocronMath.correlacion(x, y)
        self.assertIsNotNone(r)
        self.assertAlmostEqual(r, 1.0, places=4)

        # Correlacion inversa: y = -3x + 10
        y_inv = [7, 4, 1, -2, -5]
        r_inv = HolocronMath.correlacion(x, y_inv)
        self.assertAlmostEqual(r_inv, -1.0, places=4)

    def test_regresion_lineal_calculo_mco(self):
        # Puntos con variabilidad real
        x = [10, 20, 30, 40, 50]
        y = [25, 45, 62, 84, 105]

        modelo = HolocronMath.regresion_lineal(x, y)
        self.assertEqual(modelo["n"], 5)
        # Pendiente m cercana a 2.0
        self.assertAlmostEqual(modelo["pendiente"], 2.0, delta=0.1)
        # Intercepto b cercano a 4.0
        self.assertAlmostEqual(modelo["intercepto"], 4.0, delta=2.0)
        # R^2 debe ser muy alto (> 0.99)
        self.assertGreater(modelo["r_cuadrado"], 0.99)
        self.assertIn("y =", modelo["ecuacion"])
        self.assertEqual(len(modelo["predicciones"]), 5)

    def test_regresion_lineal_casos_limite(self):
        # Menos de 2 puntos debe lanzar error
        with self.assertRaises(ValueError):
            HolocronMath.regresion_lineal([1], [10])

        # Varianza cero en X (todos los X iguales) debe lanzar error
        with self.assertRaises(ValueError):
            HolocronMath.regresion_lineal([5, 5, 5], [10, 20, 30])

    def test_trazar_regresion_en_tabla(self):
        columnas = ["id", "distancia", "tiempo"]
        filas = [
            {"id": "A1", "distancia": 100, "tiempo": 20},
            {"id": "A2", "distancia": 200, "tiempo": 38},
            {"id": "A3", "distancia": 300, "tiempo": 61},
            {"id": "A4", "distancia": 400, "tiempo": 79},
            {"id": "A5", "distancia": 500, "tiempo": 102}
        ]
        tabla = HolocronTable(columnas, filas, "viajes")
        resultado = tabla.trazar_regresion(
            col_x="distancia",
            col_y="tiempo",
            col_destino="tiempo_estimado"
        )

        self.assertIsInstance(resultado, HolocronRegressionResult)
        self.assertIn("tiempo_estimado", resultado.columnas)
        self.assertEqual(len(resultado), 5)
        self.assertGreater(resultado.modelo["r_cuadrado"], 0.99)
        # Comprobar cuadro resumen en texto
        resumen_txt = resultado.a_cadena_resumen_modelo()
        self.assertIn("MODELO DE REGRESION LINEAL", resumen_txt)
        self.assertIn("Ecuacion de la Recta", resumen_txt)

    def test_ejecucion_dsl_pipeline_regresion(self):
        codigo = """
        datos = abrir_holocron "examples/datos/telemetria_flota.csv"
        flota_modelo = datos
            |> revelar [ identificador, escudos, victorias ]
            |> trazar_regresion [ eje_x = escudos, eje_y = victorias, destino = victorias_esperadas ]
        """
        arbol, err, _ = parse_string(codigo)
        self.assertFalse(err.tiene_errores())
        interp = HolocronInterpreter()
        interp.visit(arbol)

        res = interp.symbol_table.obtener_valor("flota_modelo")
        self.assertIsInstance(res, HolocronRegressionResult)
        self.assertIn("victorias_esperadas", res.columnas)
        self.assertTrue(len(res.modelo["predicciones"]) > 0)

    def test_ejecucion_dsl_sentencia_regresion_directa(self):
        codigo = """
        flota = abrir_holocron "examples/datos/telemetria_flota.csv"
        trazar_regresion flota [ eje_x = escudos, eje_y = victorias ]
        """
        arbol, err, _ = parse_string(codigo)
        self.assertFalse(err.tiene_errores())
        interp = HolocronInterpreter()
        interp.visit(arbol)

        flota_mod = interp.symbol_table.obtener_valor("flota")
        self.assertIsInstance(flota_mod, HolocronRegressionResult)
        self.assertIn("pred_victorias", flota_mod.columnas)

    def test_proyeccion_holograma_regresion(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            ruta_png = Path(tmp_dir) / "regresion_test.png"
            codigo = f"""
            datos = abrir_holocron "examples/datos/telemetria_flota.csv"
            proyectar_holograma regresion datos [
                eje_x = "escudos",
                eje_y = "victorias",
                titulo = "Regresion de Escudos vs Victorias",
                guardar = "{ruta_png.as_posix()}"
            ]
            """
            arbol, err, _ = parse_string(codigo)
            self.assertFalse(err.tiene_errores())
            interp = HolocronInterpreter()
            interp.visit(arbol)

            self.assertTrue(ruta_png.is_file())
            self.assertGreater(ruta_png.stat().st_size, 1000)


if __name__ == "__main__":
    unittest.main()
