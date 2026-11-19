# =============================================================================
# Pruebas Unitarias: Biblioteca de Machine Learning y Filtros en HolocronDSL
# Autores: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
# =============================================================================

import unittest
from src.runtime.ml_engine import (
    distancia_euclidiana,
    calcular_impureza_gini,
    calcular_entropia,
    evaluar_exactitud,
    calcular_matriz_confusion,
    KMeansGalactico,
    PerceptronGalactico,
    ArbolDecisionGalactico,
    normalizar_min_max,
    estandarizar_z_score,
    codificar_etiquetas
)
from src.runtime.holocron_table import HolocronTable
from src.compiler.driver import parse_string
from src.interpreter.visitor import HolocronInterpreter


class TestHolocronMLDirect(unittest.TestCase):
    """Verifica directamente las funciones y clases del motor HolocronML."""

    def test_metricas_distancia_y_pureza(self):
        d = distancia_euclidiana([0.0, 0.0], [3.0, 4.0])
        self.assertAlmostEqual(d, 5.0, places=4)

        # Pureza perfecta (una sola clase)
        gini_puro = calcular_impureza_gini(["Jedi", "Jedi", "Jedi"])
        self.assertAlmostEqual(gini_puro, 0.0, places=4)

        # Maxima impureza binaria 50/50
        gini_mixto = calcular_impureza_gini(["Jedi", "Sith"])
        self.assertAlmostEqual(gini_mixto, 0.5, places=4)

        # Entropia de 50/50 es 1.0 bit
        ent_mixta = calcular_entropia(["Jedi", "Sith"])
        self.assertAlmostEqual(ent_mixta, 1.0, places=4)

    def test_evaluacion_exactitud_y_confusion(self):
        y_real = ["Jedi", "Jedi", "Sith", "Sith"]
        y_pred = ["Jedi", "Sith", "Sith", "Sith"]
        acc = evaluar_exactitud(y_real, y_pred)
        self.assertAlmostEqual(acc, 0.75, places=4)

        mat = calcular_matriz_confusion(y_real, y_pred)
        self.assertEqual(mat["matriz"]["Jedi"]["Jedi"], 1)
        self.assertEqual(mat["matriz"]["Jedi"]["Sith"], 1)
        self.assertEqual(mat["matriz"]["Sith"]["Sith"], 2)

    def test_kmeans_galactico(self):
        # Dos grupos claramente separados
        datos = [
            [1.0, 1.0], [1.2, 0.9], [0.8, 1.1],
            [10.0, 10.0], [10.5, 9.8], [9.7, 10.2]
        ]
        kmeans = KMeansGalactico(k=2, max_iteraciones=20)
        kmeans.entrenar(datos)

        self.assertEqual(len(kmeans.centroides), 2)
        preds = kmeans.predecir(datos)
        # Los tres primeros deben compartir cluster y los tres ultimos otro cluster
        self.assertEqual(preds[0], preds[1])
        self.assertEqual(preds[1], preds[2])
        self.assertEqual(preds[3], preds[4])
        self.assertEqual(preds[4], preds[5])
        self.assertNotEqual(preds[0], preds[3])
        self.assertIn("Inercia", kmeans.a_cadena_resumen())

    def test_perceptron_galactico(self):
        # Clasificador lineal binario (AND logico)
        X = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        y = [0, 0, 0, 1]
        p = PerceptronGalactico(tasa_aprendizaje=0.1, epocas=30)
        p.entrenar(X, y)

        preds = p.predecir(X)
        self.assertEqual(preds, y)
        self.assertAlmostEqual(p.exactitud_entrenamiento, 1.0, places=4)
        self.assertIn("Vector de Pesos", p.a_cadena_resumen())

    def test_arbol_decision_galactico(self):
        # Datos de naves: [escudos, velocidad] -> estado
        X = [
            [20.0, 500.0],
            [30.0, 450.0],
            [80.0, 800.0],
            [90.0, 850.0]
        ]
        y = ["Vulnerable", "Vulnerable", "Blindada", "Blindada"]
        arbol = ArbolDecisionGalactico(profundidad_maxima=3)
        arbol.entrenar(X, y, nombres_caracteristicas=["escudos", "velocidad"])

        preds = arbol.predecir(X)
        self.assertEqual(preds, y)
        self.assertAlmostEqual(arbol.exactitud_entrenamiento, 1.0, places=4)

        # Inferencia de muestra no vista
        nueva_nave = [85.0, 820.0]
        self.assertEqual(arbol.predecir_uno(nueva_nave), "Blindada")
        self.assertIn("escudos", arbol.a_cadena_resumen())

    def test_filtros_y_normalizacion(self):
        vals = [10.0, 20.0, 30.0, 40.0, 50.0]
        minmax = normalizar_min_max(vals)
        self.assertAlmostEqual(minmax[0], 0.0, places=4)
        self.assertAlmostEqual(minmax[-1], 1.0, places=4)

        zscore = estandarizar_z_score(vals)
        self.assertAlmostEqual(sum(zscore) / len(zscore), 0.0, places=4)

        categorias = ["Corellia", "Kuat", "Corellia", "Mandalore"]
        cods, mapeo = codificar_etiquetas(categorias)
        self.assertEqual(len(cods), 4)
        self.assertEqual(cods[0], cods[2])
        self.assertEqual(len(mapeo), 3)


class TestHolocronTableML(unittest.TestCase):
    """Verifica la integracion de algoritmos de ML sobre tablas HolocronTable."""

    def setUp(self):
        self.filas = [
            {"id": "N-1", "escudos": 150, "velocidad": 1200, "faccion": "Imperio", "clase": "Elite"},
            {"id": "N-2", "escudos": 140, "velocidad": 1150, "faccion": "Imperio", "clase": "Elite"},
            {"id": "N-3", "escudos": 60, "velocidad": 700, "faccion": "Rebelde", "clase": "Estandar"},
            {"id": "N-4", "escudos": 50, "velocidad": 680, "faccion": "Rebelde", "clase": "Estandar"}
        ]
        self.tabla = HolocronTable(
            columnas=["id", "escudos", "velocidad", "faccion", "clase"],
            filas=self.filas,
            nombre="flota_test"
        )

    def test_agrupar_kmeans_en_tabla(self):
        tabla_k = self.tabla.agrupar_kmeans(columnas=["escudos", "velocidad"], k=2, col_destino="grupo_km")
        self.assertIn("grupo_km", tabla_k.columnas)
        self.assertEqual(len(tabla_k.filas), 4)
        # N-1 y N-2 deben tener el mismo cluster
        c1 = tabla_k.filas[0]["grupo_km"]
        c2 = tabla_k.filas[1]["grupo_km"]
        c3 = tabla_k.filas[2]["grupo_km"]
        self.assertEqual(c1, c2)
        self.assertNotEqual(c1, c3)

    def test_clasificar_arbol_en_tabla(self):
        tabla_arb = self.tabla.clasificar_arbol(
            col_objetivo="clase",
            columnas_caracteristicas=["escudos", "velocidad"],
            col_destino="pred_clase"
        )
        self.assertIn("pred_clase", tabla_arb.columnas)
        for f in tabla_arb.filas:
            self.assertEqual(f["clase"], f["pred_clase"])

    def test_clasificar_perceptron_en_tabla(self):
        tabla_per = self.tabla.clasificar_perceptron(
            col_objetivo="clase",
            columnas_caracteristicas=["escudos", "velocidad"],
            col_destino="pred_p",
            epocas=40
        )
        self.assertIn("pred_p", tabla_per.columnas)
        for f in tabla_per.filas:
            self.assertEqual(f["clase"], f["pred_p"])

    def test_normalizar_y_codificar_en_tabla(self):
        tabla_norm = self.tabla.normalizar_minmax(columnas=["escudos", "velocidad"])
        val_escudos = [f["escudos"] for f in tabla_norm.filas]
        self.assertEqual(min(val_escudos), 0.0)
        self.assertEqual(max(val_escudos), 1.0)

        tabla_cod = self.tabla.codificar_etiquetas(columnas=["faccion"])
        self.assertIsInstance(tabla_cod.filas[0]["faccion"], int)


class TestHolocronDSLMLPipelines(unittest.TestCase):
    """Verifica la ejecucion de Machine Learning dentro de scripts DSL."""

    def test_dsl_ml_pipeline_completo(self):
        codigo = """
        datos = abrir_holocron "examples/datos/telemetria_flota.csv"
        
        datos_ml = datos
            |> agrupar_kmeans [ k = 2, columnas = [escudos, victorias], destino = "sector_cluster" ]
            |> clasificar_arbol [ objetivo = "faccion", columnas = [escudos, victorias], destino = "faccion_arbol" ]
            |> normalizar_minmax [ columnas = [escudos, victorias] ]
        
        filas_procesadas = longitud(datos_ml)
        """
        tree, _, _ = parse_string(codigo)
        interp = HolocronInterpreter()
        interp.visit(tree)

        res = interp.symbol_table.obtener_valor("datos_ml")
        self.assertIn("sector_cluster", res.columnas)
        self.assertIn("faccion_arbol", res.columnas)
        self.assertEqual(interp.symbol_table.obtener_valor("filas_procesadas"), len(res.filas))

    def test_dsl_funciones_ml_incorporadas(self):
        codigo = """
        y_real = [1, 1, 0, 0]
        y_pred = [1, 1, 1, 0]
        exactitud_obtenida = evaluar_exactitud(y_real, y_pred)
        dist = distancia([0, 0], [6, 8])
        """
        tree, _, _ = parse_string(codigo)
        interp = HolocronInterpreter()
        interp.visit(tree)

        self.assertAlmostEqual(interp.symbol_table.obtener_valor("exactitud_obtenida"), 0.75, places=4)
        self.assertAlmostEqual(interp.symbol_table.obtener_valor("dist"), 10.0, places=4)


if __name__ == "__main__":
    unittest.main()
