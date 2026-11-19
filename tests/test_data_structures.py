# =============================================================================
# Pruebas Unitarias: Biblioteca de Estructuras de Datos y Bucles en HolocronDSL
# Autores: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
# =============================================================================

import unittest
from src.runtime.data_structures import (
    HolocronArray,
    HolocronPila,
    HolocronCola,
    NodoArbolDecision,
    crear_lista_dimensionada
)
from src.errors.semantic_error import IndiceFueraDeRangoError, EstructuraVaciaError
from src.compiler.driver import parse_string
from src.interpreter.visitor import HolocronInterpreter


class TestHolocronDataStructures(unittest.TestCase):
    """Verifica el funcionamiento riguroso de arreglos, pilas, colas y arboles."""

    def test_arreglo_operaciones_basicas(self):
        arr = HolocronArray([10, 20, 30])
        self.assertEqual(arr.longitud(), 3)
        self.assertEqual(arr.obtener(0), 10)
        self.assertEqual(arr.obtener(-1), 30)

        arr.asignar(1, 99)
        self.assertEqual(arr.obtener(1), 99)

        arr.agregar(40)
        self.assertEqual(arr.longitud(), 4)
        self.assertEqual(arr.obtener(3), 40)

        removido = arr.remover(0)
        self.assertEqual(removido, 10)
        self.assertEqual(arr.longitud(), 3)

        sub = arr.subarreglo(0, 2)
        self.assertEqual(sub.a_lista_python(), [99, 30])

        invertido = arr.invertir()
        self.assertEqual(invertido.a_lista_python(), [40, 30, 99])

        ordenado = arr.ordenar(ascendente=True)
        self.assertEqual(ordenado.a_lista_python(), [30, 40, 99])

    def test_arreglo_indices_fuera_de_rango(self):
        arr = HolocronArray([1, 2, 3])
        with self.assertRaises(IndiceFueraDeRangoError):
            arr.obtener(5)
        with self.assertRaises(IndiceFueraDeRangoError):
            arr.obtener(-10)
        with self.assertRaises(IndiceFueraDeRangoError):
            arr.asignar(10, 42)

    def test_crear_lista_dimensionada(self):
        lista_10 = crear_lista_dimensionada(10, valor_inicial=0)
        self.assertEqual(lista_10.longitud(), 10)
        self.assertEqual(lista_10.a_lista_python(), [0] * 10)

    def test_pila_lifo_operaciones(self):
        pila = HolocronPila()
        self.assertTrue(pila.esta_vacia())
        self.assertEqual(pila.tamano(), 0)

        pila.apilar("cristal_kyber")
        pila.apilar("sable_luz")
        pila.apilar("holocron_sith")

        self.assertFalse(pila.esta_vacia())
        self.assertEqual(pila.tamano(), 3)
        self.assertEqual(pila.cima(), "holocron_sith")

        extraido = pila.desapilar()
        self.assertEqual(extraido, "holocron_sith")
        self.assertEqual(pila.tamano(), 2)
        self.assertEqual(pila.cima(), "sable_luz")

        pila.vaciar()
        self.assertTrue(pila.esta_vacia())
        with self.assertRaises(EstructuraVaciaError):
            pila.desapilar()
        with self.assertRaises(EstructuraVaciaError):
            pila.cima()

    def test_cola_fifo_operaciones(self):
        cola = HolocronCola()
        self.assertTrue(cola.esta_vacia())

        cola.encolar("caza_xwing")
        cola.encolar("caza_tie")
        cola.encolar("halcon_milenario")

        self.assertEqual(cola.tamano(), 3)
        self.assertEqual(cola.frente(), "caza_xwing")

        atendido = cola.desencolar()
        self.assertEqual(atendido, "caza_xwing")
        self.assertEqual(cola.frente(), "caza_tie")
        self.assertEqual(cola.tamano(), 2)

        cola.vaciar()
        self.assertTrue(cola.esta_vacia())
        with self.assertRaises(EstructuraVaciaError):
            cola.desencolar()
        with self.assertRaises(EstructuraVaciaError):
            cola.frente()

    def test_nodo_arbol_decision_estructura(self):
        hoja_izq = NodoArbolDecision(es_hoja=True, prediccion="Sith", muestras=10, impureza=0.0)
        hoja_der = NodoArbolDecision(es_hoja=True, prediccion="Jedi", muestras=15, impureza=0.1)

        nodo_raiz = NodoArbolDecision(
            es_hoja=False,
            atributo="midiclorianos",
            indice_atributo=0,
            umbral=10000.0,
            rama_izquierda=hoja_izq,
            rama_derecha=hoja_der,
            prediccion="Jedi",
            muestras=25,
            impureza=0.45
        )

        self.assertEqual(nodo_raiz.predecir([8000.0]), "Sith")
        self.assertEqual(nodo_raiz.predecir([15000.0]), "Jedi")
        self.assertIn("midiclorianos <= 10000.0000", str(nodo_raiz))


class TestHolocronDSLLoopsAndArrays(unittest.TestCase):
    """Verifica la ejecucion en DSL de arreglos, bucles y funciones de estructuras."""

    def test_dsl_arreglo_literal_e_indexacion(self):
        codigo = """
        flota = [100, 200, 300, 400]
        primero = flota[0]
        ultimo = flota[3]
        flota[1] = 999
        segundo_modificado = flota[1]
        """
        tree, _, _ = parse_string(codigo)
        interp = HolocronInterpreter()
        interp.visit(tree)

        self.assertEqual(interp.symbol_table.obtener_valor("primero"), 100)
        self.assertEqual(interp.symbol_table.obtener_valor("ultimo"), 400)
        self.assertEqual(interp.symbol_table.obtener_valor("segundo_modificado"), 999)

    def test_dsl_crear_lista_dimensionada_y_manipulacion(self):
        codigo = """
        lista_diez = crear_lista(10, 5)
        longitud_detectada = longitud(lista_diez)
        agregar(lista_diez, 50)
        longitud_tras_agregar = longitud(lista_diez)
        """
        tree, _, _ = parse_string(codigo)
        interp = HolocronInterpreter()
        interp.visit(tree)

        self.assertEqual(interp.symbol_table.obtener_valor("longitud_detectada"), 10)
        self.assertEqual(interp.symbol_table.obtener_valor("longitud_tras_agregar"), 11)

    def test_dsl_bucle_mientras(self):
        codigo = """
        contador = 0
        acumulador = 0
        mientras (contador < 5)
            acumulador = acumulador + contador
            contador = contador + 1
        fin_mientras
        """
        tree, _, _ = parse_string(codigo)
        interp = HolocronInterpreter()
        interp.visit(tree)

        self.assertEqual(interp.symbol_table.obtener_valor("contador"), 5)
        self.assertEqual(interp.symbol_table.obtener_valor("acumulador"), 0 + 1 + 2 + 3 + 4)

    def test_dsl_bucle_para_rango(self):
        codigo = """
        total_acumulado = 0
        para i desde 1 hasta 4
            total_acumulado = total_acumulado + i
        fin_para
        """
        tree, _, _ = parse_string(codigo)
        interp = HolocronInterpreter()
        interp.visit(tree)

        self.assertEqual(interp.symbol_table.obtener_valor("total_acumulado"), 1 + 2 + 3 + 4)

    def test_dsl_bucle_recorrer_coleccion(self):
        codigo = """
        elementos = [10, 20, 30]
        total = 0
        recorrer item en elementos
            total = total + item
        fin_recorrer
        """
        tree, _, _ = parse_string(codigo)
        interp = HolocronInterpreter()
        interp.visit(tree)

        self.assertEqual(interp.symbol_table.obtener_valor("total"), 60)

    def test_dsl_pila_y_cola_operaciones(self):
        codigo = """
        mi_pila = crear_pila()
        apilar(mi_pila, 10)
        apilar(mi_pila, 20)
        elemento_cima = cima(mi_pila)
        desapilado = desapilar(mi_pila)

        mi_cola = crear_cola()
        encolar(mi_cola, 100)
        encolar(mi_cola, 200)
        elemento_frente = frente(mi_cola)
        desencolado = desencolar(mi_cola)
        """
        tree, _, _ = parse_string(codigo)
        interp = HolocronInterpreter()
        interp.visit(tree)

        self.assertEqual(interp.symbol_table.obtener_valor("elemento_cima"), 20)
        self.assertEqual(interp.symbol_table.obtener_valor("desapilado"), 20)
        self.assertEqual(interp.symbol_table.obtener_valor("elemento_frente"), 100)
        self.assertEqual(interp.symbol_table.obtener_valor("desencolado"), 100)


if __name__ == "__main__":
    unittest.main()
