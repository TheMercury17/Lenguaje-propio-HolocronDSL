# Pruebas unitarias para la biblioteca propia HolocronIO
import unittest
import tempfile
from pathlib import Path
from src.runtime.io_engine import HolocronIO
from src.errors.semantic_error import ArchivoNoEncontradoError


class TestHolocronIO(unittest.TestCase):
    """Verifica el analisis de formato CSV, inferencia de tipos y serializacion."""

    def test_inferencia_tipos_atomicos(self):
        self.assertEqual(HolocronIO.inferir_tipo("42"), 42)
        self.assertEqual(HolocronIO.inferir_tipo("-15"), -15)
        self.assertEqual(HolocronIO.inferir_tipo("3.1415"), 3.1415)
        self.assertEqual(HolocronIO.inferir_tipo("cierto_es"), True)
        self.assertEqual(HolocronIO.inferir_tipo("falso_es"), False)
        self.assertEqual(HolocronIO.inferir_tipo("verdadero"), True)
        self.assertEqual(HolocronIO.inferir_tipo("falso"), False)
        self.assertIsNone(HolocronIO.inferir_tipo("nulo"))
        self.assertIsNone(HolocronIO.inferir_tipo("NaN"))
        self.assertIsNone(HolocronIO.inferir_tipo(""))
        self.assertEqual(HolocronIO.inferir_tipo("TIE Fighter"), "TIE Fighter")
        self.assertEqual(HolocronIO.inferir_tipo('"X-Wing"'), "X-Wing")

    def test_separar_linea_csv_compleja(self):
        linea = 'ISD-01,"Imperial Star Destroyer, Class I",Imperio,5000'
        campos = HolocronIO.separar_linea_csv(linea, delimitador=",")
        self.assertEqual(campos, ["ISD-01", "Imperial Star Destroyer, Class I", "Imperio", "5000"])

    def test_lectura_y_escritura_ciclo_completo(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            ruta_csv = Path(tmp_dir) / "prueba_flota.csv"
            cols = ["id", "modelo", "potencia", "activo"]
            filas = [
                {"id": "A1", "modelo": "Interceptor", "potencia": 150, "activo": True},
                {"id": "A2", "modelo": "Bombardero", "potencia": 200, "activo": False},
                {"id": "A3", "modelo": "Caza Estelar", "potencia": None, "activo": True}
            ]

            HolocronIO.escribir_csv(str(ruta_csv), cols, filas, delimitador=",")
            self.assertTrue(ruta_csv.is_file())

            cols_leidas, filas_leidas = HolocronIO.leer_csv(str(ruta_csv), delimitador=",")
            self.assertEqual(cols_leidas, cols)
            self.assertEqual(len(filas_leidas), 3)
            self.assertEqual(filas_leidas[0]["id"], "A1")
            self.assertEqual(filas_leidas[0]["potencia"], 150)
            self.assertEqual(filas_leidas[0]["activo"], True)
            self.assertIsNone(filas_leidas[2]["potencia"])

    def test_archivo_inexistente(self):
        with self.assertRaises(ArchivoNoEncontradoError):
            HolocronIO.leer_csv("ruta_fantasma_no_existe.csv")


if __name__ == "__main__":
    unittest.main()
