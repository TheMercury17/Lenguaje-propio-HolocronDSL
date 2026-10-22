# Pruebas de integracion que ejecutan los 5 ejemplos del repositorio
import os
import unittest
from pathlib import Path
from src.compiler.driver import parse_file
from src.interpreter.visitor import HolocronInterpreter


class TestIntegrationExamples(unittest.TestCase):
    """Valida la ejecucion integral de los 5 programas galacticos y sus artefactos generados."""

    @classmethod
    def setUpClass(cls):
        # Crear directorio de salidas si no existe
        Path("salidas").mkdir(parents=True, exist_ok=True)

    def _ejecutar_archivo(self, ruta_archivo: str):
        arbol, err, _ = parse_file(ruta_archivo)
        self.assertFalse(err.tiene_errores(), f"Errores de sintaxis en {ruta_archivo}: {err.obtener_reporte()}")
        interp = HolocronInterpreter()
        interp.visit(arbol)
        return interp

    def test_ejemplo_01_telemetria_cazas(self):
        interp = self._ejecutar_archivo("examples/01_telemetria_cazas.holo")
        salida_csv = Path("salidas/flota_operativa.csv")
        self.assertTrue(salida_csv.is_file())
        self.assertGreater(salida_csv.stat().st_size, 0)
        self.assertTrue(len(interp.transmisiones) > 0)

    def test_ejemplo_02_censo_galactico(self):
        interp = self._ejecutar_archivo("examples/02_censo_galactico.holo")
        salida_csv = Path("salidas/resumen_facciones.csv")
        self.assertTrue(salida_csv.is_file())
        self.assertGreater(salida_csv.stat().st_size, 0)

    def test_ejemplo_03_proyeccion_holografica(self):
        interp = self._ejecutar_archivo("examples/03_proyeccion_holografica.holo")
        png1 = Path("salidas/victorias_por_faccion.png")
        png2 = Path("salidas/escudos_vs_victorias.png")
        png3 = Path("salidas/distribucion_escudos.png")
        self.assertTrue(png1.is_file())
        self.assertTrue(png2.is_file())
        self.assertTrue(png3.is_file())
        # Verificar que no se creo ningun archivo SVG
        self.assertFalse(Path("salidas/victorias_por_faccion.svg").exists())

    def test_ejemplo_04_mision_avanzada(self):
        interp = self._ejecutar_archivo("examples/04_mision_avanzada.holo")
        salida_csv = Path("salidas/escuadron_aprobado.csv")
        self.assertTrue(salida_csv.is_file())
        self.assertIn("Escuadron validado bajo la senda luminosa.", interp.transmisiones)

    def test_ejemplo_05_proyecto_completo(self):
        interp = self._ejecutar_archivo("examples/05_proyecto_completo.holo")
        salida_csv1 = Path("salidas/escuadron_activo.csv")
        salida_csv2 = Path("salidas/resumen_estrategico.csv")
        salida_png = Path("salidas/naves_operativas.png")
        self.assertTrue(salida_csv1.is_file())
        self.assertTrue(salida_csv2.is_file())
        self.assertTrue(salida_png.is_file())


if __name__ == "__main__":
    unittest.main()
