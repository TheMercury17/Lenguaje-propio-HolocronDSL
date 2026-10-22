# Pruebas unitarias para la estructura de datos HolocronTable
import unittest
from src.runtime.holocron_table import HolocronTable
from src.errors.semantic_error import ColumnaInexistenteError


class TestHolocronTable(unittest.TestCase):
    """Verifica las operaciones funcionales sobre conjuntos de datos tabulares."""

    def setUp(self):
        self.columnas = ["id", "faccion", "escudos", "victorias"]
        self.filas = [
            {"id": "T1", "faccion": "Imperio", "escudos": 0, "victorias": 3},
            {"id": "T2", "faccion": "Imperio", "escudos": 40, "victorias": 7},
            {"id": "X1", "faccion": "Alianza", "escudos": 100, "victorias": 12},
            {"id": "X2", "faccion": "Alianza", "escudos": 110, "victorias": 15},
            {"id": "M1", "faccion": "Independiente", "escudos": 200, "victorias": 45}
        ]
        self.tabla = HolocronTable(self.columnas, self.filas, "flota_test")

    def test_revelar_columnas_validas(self):
        sub = self.tabla.seleccionar(["id", "escudos"])
        self.assertEqual(sub.columnas, ["id", "escudos"])
        self.assertEqual(len(sub), 5)
        self.assertNotIn("faccion", sub.filas[0])

    def test_revelar_columna_inexistente_lanza_error(self):
        with self.assertRaises(ColumnaInexistenteError):
            self.tabla.seleccionar(["id", "columna_inexistente"])

    def test_purgar_filas(self):
        filtrada = self.tabla.purgar(lambda f: f["escudos"] > 50 and f["victorias"] >= 10)
        self.assertEqual(len(filtrada), 3)
        ids = [f["id"] for f in filtrada.filas]
        self.assertEqual(ids, ["X1", "X2", "M1"])

    def test_forjar_nueva_columna(self):
        forjada = self.tabla.forjar("poder", lambda f: f["escudos"] + f["victorias"] * 10)
        self.assertIn("poder", forjada.columnas)
        self.assertEqual(forjada.filas[0]["poder"], 30)   # 0 + 30
        self.assertEqual(forjada.filas[2]["poder"], 220)  # 100 + 120

    def test_ordenar_ascendente_y_descendente(self):
        asc = self.tabla.ordenar("victorias", ascendente=True)
        self.assertEqual(asc.filas[0]["id"], "T1")
        self.assertEqual(asc.filas[-1]["id"], "M1")

        desc = self.tabla.ordenar("victorias", ascendente=False)
        self.assertEqual(desc.filas[0]["id"], "M1")
        self.assertEqual(desc.filas[-1]["id"], "T1")

    def test_eliminar_clones(self):
        filas_con_duplicados = list(self.filas) + [dict(self.filas[0])]
        tabla_dup = HolocronTable(self.columnas, filas_con_duplicados)
        self.assertEqual(len(tabla_dup), 6)
        limpia = tabla_dup.eliminar_clones()
        self.assertEqual(len(limpia), 5)

    def test_sanar_vacios(self):
        filas_con_nulos = [
            {"id": "A1", "escudos": None, "victorias": 5},
            {"id": "A2", "escudos": 50, "victorias": None},
            {"id": "A3", "escudos": 80, "victorias": 10}
        ]
        t = HolocronTable(["id", "escudos", "victorias"], filas_con_nulos)

        # Descartar
        descartadas = t.sanar_vacios("descartar")
        self.assertEqual(len(descartadas), 1)
        self.assertEqual(descartadas.filas[0]["id"], "A3")

        # Sustituir con 0
        rellenas = t.sanar_vacios("con", valor_sustituto=0)
        self.assertEqual(len(rellenas), 3)
        self.assertEqual(rellenas.filas[0]["escudos"], 0)
        self.assertEqual(rellenas.filas[1]["victorias"], 0)

    def test_agrupar_y_resumir(self):
        agrupada = self.tabla.agrupar(["faccion"])
        resumen = agrupada.resumir([
            ("total_naves", "recuento", None),
            ("promedio_escudos", "equilibrio", "escudos"),
            ("max_victorias", "cenit", "victorias")
        ])
        self.assertEqual(len(resumen), 3)  # Alianza, Imperio, Independiente
        # Buscar Alianza
        fila_alianza = next(f for f in resumen.filas if f["faccion"] == "Alianza")
        self.assertEqual(fila_alianza["total_naves"], 2)
        self.assertEqual(fila_alianza["promedio_escudos"], 105.0)
        self.assertEqual(fila_alianza["max_victorias"], 15)


if __name__ == "__main__":
    unittest.main()
