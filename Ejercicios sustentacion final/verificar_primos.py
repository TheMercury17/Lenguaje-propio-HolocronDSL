"""
=============================================================================
EJERCICIO 5: Verificacion y Comparacion de Filtro Funcional de Primos
Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
Lenguajes de Programacion y Transduccion - Universidad Sergio Arboleda
=============================================================================
"""

import time
import os
import sys

# Anadir la ruta raiz del proyecto para importar modulos del compilador
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.compiler.driver import parse_file
from src.interpreter.visitor import HolocronInterpreter


def es_primo_python(n: int) -> bool:
    """Implementacion nativa en Python del algoritmo de primalidad O(sqrt(n))."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def ejecutar_verificacion():
    print("=" * 70)
    print("VERIFICACION DE FILTRADO FUNCIONAL DE NUMEROS PRIMOS (1 AL 100)")
    print("=" * 70)

    # 1. Calculo en Python con filter() funcional
    inicio_py = time.perf_counter()
    numeros_py = list(range(1, 101))
    primos_py = list(filter(es_primo_python, numeros_py))
    tiempo_py = (time.perf_counter() - inicio_py) * 1000

    print(f"Python nativo:")
    print(f"  - Total numeros analizados: {len(numeros_py)}")
    print(f"  - Total primos identificados: {len(primos_py)}")
    print(f"  - Lista de primos: {primos_py}")
    print(f"  - Tiempo de ejecucion: {tiempo_py:.4f} ms\n")

    # 2. Ejecucion del programa en HolocronDSL
    ruta_holo = os.path.join(os.path.dirname(__file__), "05_filtro_primos_1_100.holo")
    print(f"Ejecutando programa HolocronDSL: {os.path.basename(ruta_holo)}")

    inicio_holo = time.perf_counter()
    arbol, error_listener, parser = parse_file(ruta_holo)
    if error_listener.tiene_errores():
        print("Errores sintacticos detectados:")
        for err in error_listener.errores:
            print(f"  - {err}")
        return False

    interprete = HolocronInterpreter()
    interprete.visit(arbol)
    tiempo_holo = (time.perf_counter() - inicio_holo) * 1000

    # Obtener variables de la tabla de simbolos
    simbolo_filtrados = interprete.symbol_table.resolver("primos_filtrados")
    primos_holo = (
        simbolo_filtrados.valor.a_lista_python()
        if hasattr(simbolo_filtrados.valor, "a_lista_python")
        else simbolo_filtrados.valor
    )

    print(f"\nResultados obtenidos desde HolocronDSL:")
    print(f"  - Total primos identificados: {len(primos_holo)}")
    print(f"  - Lista de primos: {primos_holo}")
    print(f"  - Tiempo total (parseo + interpretacion AST): {tiempo_holo:.4f} ms")

    # 3. Validacion formal
    coinciden = primos_py == primos_holo
    assert coinciden, "Discrepancia detectada entre Python y HolocronDSL"
    assert len(primos_holo) == 25, f"Se esperaban 25 primos, se obtuvieron {len(primos_holo)}"

    print("\n" + "=" * 70)
    print("VALIDACION MATEMATICA Y COMPUTACIONAL: EXITOSA (100% COINCIDENCIA)")
    print(f"Exactamente 25 numeros primos identificados entre 1 y 100.")
    print("=" * 70)
    return True


if __name__ == "__main__":
    ejecutar_verificacion()
