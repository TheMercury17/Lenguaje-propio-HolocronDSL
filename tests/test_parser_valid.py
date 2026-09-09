# Pruebas unitarias sintacticas positivas para HolocronDSL
# Verifica que construcciones validas del lenguaje generen un CST sin errores

import unittest
from pathlib import Path
from src.compiler.driver import parse_string, parse_file


class TestHolocronParserValid(unittest.TestCase):
    """Evalua la correcta aceptacion de construcciones gramaticales validas."""

    def assertSintaxisValida(self, codigo: str):
        """Metodo de asercion auxiliar para verificar ausencia de errores."""
        arbol, error_listener, _ = parse_string(codigo)
        self.assertFalse(
            error_listener.tiene_errores(),
            f"Se esperaba sintaxis valida pero se reportaron errores:\n{error_listener.obtener_reporte()}"
        )
        self.assertIsNotNone(arbol)

    def test_carga_y_archivado_simple(self):
        """Verifica carga y guardado basico de holocrones."""
        codigo = """
        datos <- abrir_holocron "datos/galaxias.csv"
        archivar_holocron datos en "salidas/galaxias_copia.csv"
        """
        self.assertSintaxisValida(codigo)

    def test_carga_con_delimitador_personalizado(self):
        """Verifica carga y guardado con especificacion de delimitador."""
        codigo = """
        registro <- abrir_holocron "datos/sensores.tsv" delimitado_por "\t"
        archivar_holocron registro en "salidas/sensores_backup.tsv" delimitado_por "\t"
        """
        self.assertSintaxisValida(codigo)

    def test_pipeline_transformacion_completa(self):
        """Verifica encadenamiento de operaciones en pipeline."""
        codigo = """
        escuadron <- flota
            ==> revelar_sectores [ piloto, rango, naves, escudos ]
            ==> purgar_donde escudos > 80 y_fuerza naves >= 2
            ==> forjar_cristal blindaje_total := escudos * 1.5 + 20
            ==> alinear_flota blindaje_total orden_descendente
            ==> eliminar_clones
            ==> sanar_vacios sustituir_con 0
        """
        self.assertSintaxisValida(codigo)

    def test_agrupamiento_y_todas_las_agregaciones(self):
        """Verifica operaciones de resumen estadistico descriptivo."""
        codigo = """
        resumen <- batallas
            ==> agrupar_sector [ sector, cuadrante ]
            ==> sintetizar_indicadores [
                total_eventos := recuento(),
                bajas_acumuladas := acumular(bajas),
                media_danio := equilibrio(danio),
                mediana_danio := mediana(danio),
                pico_danio := cenit(danio),
                minimo_danio := nadir(danio),
                dispersion_danio := desviacion(danio)
            ]
        """
        self.assertSintaxisValida(codigo)

    def test_proyeccion_holografica_todos_los_tipos(self):
        """Verifica la sintaxis de proyecciones holograficas para todos los graficos soportados."""
        codigo = """
        proyectar_holograma barras desde resumen
            eje_x := "sector"
            eje_y := "total_eventos"
            holotitulo := "Eventos por sector"
            guardar_proyeccion := "salidas/grafica_barras.png"
        fin_holograma

        proyectar_holograma lineas desde telemetria
            eje_x := "tiempo"
            eje_y := "velocidad"
            holotitulo := "Curva de aceleracion"
        fin_holograma

        proyectar_holograma dispersion desde telemetria
            eje_x := "combustible"
            eje_y := "distancia"
        fin_holograma

        proyectar_holograma histograma desde telemetria
            eje_x := "velocidad"
        fin_holograma

        proyectar_holograma caja desde telemetria
            eje_x := "sector"
            eje_y := "danio"
        fin_holograma
        """
        self.assertSintaxisValida(codigo)

    def test_misiones_y_abstraccion(self):
        """Verifica la declaracion y llamada de funciones (misiones)."""
        codigo = """
        mision preparar_flota con_parametros (datos_crudos, umbral)
            resultado <- datos_crudos
                ==> purgar_donde potencia >= umbral
            retornar_orden resultado
        fin_mision

        flota_final <- preparar_flota(flota_base, 75)
        """
        self.assertSintaxisValida(codigo)

    def test_evaluacion_condicional_de_la_fuerza(self):
        """Verifica condicionales galacticos con senda luminosa y oscura."""
        codigo = """
        evaluar_fuerza (nivel_alerta > 3 o_fuerza estado == "critico")
        senda_luminosa
            transmitir_mensaje "Alerta maxima: desplegar escudos."
        senda_oscura
            transmitir_mensaje "Condiciones nominales en el hangar."
        fin_evaluar
        """
        self.assertSintaxisValida(codigo)

    def test_analisis_de_archivos_de_ejemplo(self):
        """Valida que todos los archivos de la carpeta examples/ compilen sin errores."""
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
