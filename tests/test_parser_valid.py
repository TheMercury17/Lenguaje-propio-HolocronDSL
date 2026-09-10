# Pruebas unitarias sintacticas positivas para HolocronDSL (Sintaxis Simplificada)

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
from src.compiler.driver import parse_string, parse_file


class TestHolocronParserValid(unittest.TestCase):
    """Evalua la correcta aceptacion de construcciones gramaticales validas."""

    def assertSintaxisValida(self, codigo: str):
        arbol, error_listener, _ = parse_string(codigo)
        self.assertFalse(
            error_listener.tiene_errores(),
            f"Se esperaba sintaxis valida pero se reportaron errores:\n{error_listener.obtener_reporte()}"
        )
        self.assertIsNotNone(arbol)

    def test_carga_y_archivado_simple(self):
        """Verifica carga y guardado basico con sintaxis simple '='."""
        codigo = """
        datos = abrir_holocron "datos/galaxias.csv"
        archivar_holocron datos en "salidas/galaxias_copia.csv"
        """
        self.assertSintaxisValida(codigo)

    def test_carga_con_delimitador(self):
        """Verifica especificacion de delimitador."""
        codigo = """
        registro = abrir_holocron "datos/sensores.tsv" delimitado_por "\t"
        archivar_holocron registro en "salidas/sensores_backup.tsv" delimitado_por "\t"
        """
        self.assertSintaxisValida(codigo)

    def test_pipeline_transformacion_intuitivo(self):
        """Verifica encadenamiento limpio con '|>' y '='."""
        codigo = """
        escuadron = flota
            |> revelar [ piloto, rango, naves, escudos ]
            |> purgar donde escudos > 80 y naves >= 2
            |> forjar blindaje_total = escudos * 1.5 + 20
            |> ordenar por blindaje_total descendente
            |> eliminar_clones
            |> sanar_vacios con 0
        """
        self.assertSintaxisValida(codigo)

    def test_agrupamiento_y_resumen(self):
        """Verifica agrupamiento y resumen estadistico intuitivo."""
        codigo = """
        resumen = batallas
            |> agrupar por [ sector, cuadrante ]
            |> resumir
                total_eventos = recuento(),
                bajas_acumuladas = acumular(bajas),
                media_danio = equilibrio(danio),
                mediana_danio = mediana(danio),
                pico_danio = cenit(danio),
                minimo_danio = nadir(danio),
                dispersion_danio = desviacion(danio)
        """
        self.assertSintaxisValida(codigo)

    def test_holograma_todos_los_tipos(self):
        """Verifica bloques declarativos de hologramas limpios."""
        codigo = """
        holograma barras resumen
            eje_x "sector"
            eje_y "total_eventos"
            titulo "Eventos por sector"
            guardar "salidas/grafica_barras.png"

        holograma lineas telemetria
            eje_x "tiempo"
            eje_y "velocidad"
            titulo "Curva de aceleracion"

        holograma dispersion telemetria
            eje_x "combustible"
            eje_y "distancia"

        holograma histograma telemetria
            eje_x "velocidad"

        holograma caja telemetria
            eje_x "sector"
            eje_y "danio"
        """
        self.assertSintaxisValida(codigo)

    def test_misiones_y_abstraccion(self):
        """Verifica funciones y retorno de datos."""
        codigo = """
        mision preparar_flota (datos_crudos, umbral)
            resultado = datos_crudos
                |> purgar donde potencia >= umbral
            retornar resultado
        fin_mision

        flota_final = preparar_flota(flota_base, 75)
        """
        self.assertSintaxisValida(codigo)

    def test_evaluacion_condicional_de_la_fuerza(self):
        """Verifica condicionales simples y legibles."""
        codigo = """
        evaluar_fuerza nivel_alerta > 3 o estado == "critico"
        senda_luminosa
            mostrar "Alerta maxima: desplegar escudos."
        senda_oscura
            mostrar "Condiciones nominales en el hangar."
        fin_evaluar
        """
        self.assertSintaxisValida(codigo)

    def test_analisis_de_archivos_de_ejemplo(self):
        """Valida que todos los ejemplos en examples/ compilen sin errores."""
        carpeta_ejemplos = Path(__file__).resolve().parent.parent / "examples"
        archivos_holo = list(carpeta_ejemplos.glob("*.holo"))
        self.assertGreater(len(archivos_holo), 0, "No se encontraron archivos .holo en examples/")

        for archivo in archivos_holo:
            with self.subTest(archivo=archivo.name):
                arbol, error_listener, _ = parse_file(str(archivo))
                self.assertFalse(
                    error_listener.tiene_errores(),
                    f"El archivo de ejemplo {archivo.name} presento errores sintacticos:\n{error_listener.obtener_reporte()}"
                )
                self.assertIsNotNone(arbol)


if __name__ == "__main__":
    unittest.main()
