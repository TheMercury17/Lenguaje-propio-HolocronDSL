#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Benchmarking de Rendimiento: Factorial en HolocronDSL vs Python Nativo
# Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
# Lenguajes de Programacion y Transduccion (2026-2)
# =============================================================================

import sys
import time
from pathlib import Path

# Configurar rutas para importar componentes del compilador
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.compiler.driver import parse_string
from src.interpreter.visitor import HolocronInterpreter as HolocronVisitor
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def factorial_python(n: int) -> int:
    """Implementacion equivalente en Python iterativo puro."""
    acum = 1
    for i in range(1, n + 1):
        acum *= i
    return acum


CODIGO_HOLOCRON_UN_VALOR = """
mision factorial(numero)
    acumulado = 1
    para factor desde 1 hasta numero
        acumulado = acumulado * factor
    fin_para
    retornar acumulado
fin_mision

resultado = factorial({n})
"""


def ejecutar_factorial_holocron(n: int) -> int:
    codigo = CODIGO_HOLOCRON_UN_VALOR.format(n=n)
    tree, _, parser = parse_string(codigo)
    visitor = HolocronVisitor()
    visitor.visit(tree)
    simbolo = visitor.symbol_table.resolver("resultado")
    return simbolo.valor if hasattr(simbolo, "valor") else simbolo


def ejecutar_benchmark():
    print("=" * 70)
    print("BENCHMARK COMPARATIVO DE RENDIMIENTO: FACTORIAL (5 AL 100)")
    print("HolocronDSL (Interprete AST Visitor) vs Python 3 (Bytecode CPython)")
    print("=" * 70)

    valores_n = list(range(5, 101, 5))
    tiempos_python = []
    tiempos_holocron = []

    # Validacion de correccion
    print("\n1. Verificacion de consistencia de calculo:")
    for n in [5, 10, 25, 50, 100]:
        res_py = factorial_python(n)
        res_holo = ejecutar_factorial_holocron(n)
        coincide = (res_py == res_holo)
        estado = "COINCIDE" if coincide else "DISCREPANCIA"
        print(f"  -> n = {n:3d}: Py={str(res_py)[:15]}... | Holo={str(res_holo)[:15]}... [{estado}]")

    print("\n2. Ejecutando mediciones temporales (promedio de 10 ejecuciones por n)...")
    repeticiones = 10

    for n in valores_n:
        # Python puro
        t0 = time.perf_counter()
        for _ in range(repeticiones):
            _ = factorial_python(n)
        t1 = time.perf_counter()
        t_py_ms = ((t1 - t0) / repeticiones) * 1000.0
        tiempos_python.append(t_py_ms)

        # HolocronDSL
        t0 = time.perf_counter()
        for _ in range(repeticiones):
            _ = ejecutar_factorial_holocron(n)
        t1 = time.perf_counter()
        t_holo_ms = ((t1 - t0) / repeticiones) * 1000.0
        tiempos_holocron.append(t_holo_ms)

    # Imprimir tabla comparativa
    print("\n" + "=" * 70)
    print(f"{'n':>5} | {'Python (ms)':>15} | {'HolocronDSL (ms)':>18} | {'Factor Overhead':>15}")
    print("-" * 70)
    for i, n in enumerate(valores_n):
        t_py = tiempos_python[i]
        t_holo = tiempos_holocron[i]
        ratio = t_holo / t_py if t_py > 0 else 0.0
        print(f"{n:5d} | {t_py:15.6f} | {t_holo:18.6f} | {ratio:14.1f}x")
    print("=" * 70)

    # Generar grafica comparativa de rendimiento
    carpeta_salidas = ROOT_DIR / "salidas"
    carpeta_salidas.mkdir(parents=True, exist_ok=True)
    ruta_grafica = carpeta_salidas / "comparativa_rendimiento_factorial.png"

    fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300)
    fig.patch.set_facecolor("#0b0f19")
    ax1.set_facecolor("#111827")

    color_holo = "#00e5ff"
    color_py = "#e040fb"

    ax1.set_xlabel("Valor de n", color="#e5e7eb", fontsize=12, labelpad=10)
    ax1.set_ylabel("Tiempo HolocronDSL (ms)", color=color_holo, fontsize=12)
    linea1 = ax1.plot(valores_n, tiempos_holocron, color=color_holo, marker="o", linewidth=2.5, label="HolocronDSL (ms)")
    ax1.tick_params(axis="y", labelcolor=color_holo, colors="#9ca3af")
    ax1.tick_params(axis="x", colors="#9ca3af")
    ax1.grid(True, linestyle="--", alpha=0.2, color="#9ca3af")

    ax2 = ax1.twinx()
    ax2.set_ylabel("Tiempo Python Nativo (ms)", color=color_py, fontsize=12)
    linea2 = ax2.plot(valores_n, tiempos_python, color=color_py, marker="s", linestyle="--", linewidth=2.0, label="Python 3 (ms)")
    ax2.tick_params(axis="y", labelcolor=color_py, colors="#9ca3af")

    plt.title("Analisis de Rendimiento: Factorial en HolocronDSL vs Python", color="#f9fafb", fontsize=14, fontweight="bold", pad=15)

    lineas = linea1 + linea2
    etiquetas = [l.get_label() for l in lineas]
    ax1.legend(lineas, etiquetas, loc="upper left", facecolor="#1f2937", edgecolor="#374151", labelcolor="#f9fafb")

    plt.tight_layout()
    plt.savefig(str(ruta_grafica), dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()

    print(f"\n[Grafica Generada] Ubicacion: {ruta_grafica.resolve()}")
    print("\n3. Analisis teorico de sustentacion:")
    print("  -> Complejidad Algoritmica: Ambos algoritmos son O(n) en tiempo.")
    print("  -> Origen del Overhead: HolocronDSL ejecuta un interprete dinamico")
    print("     en memoria sobre el arbol de analisis sintactico (AST) mediante el patron")
    print("     Visitor, evaluando llamadas, creando ambitos en la Tabla de Simbolos y")
    print("     despachando dinamicamente cada nodo de la gramatica. Por su parte,")
    print("     Python compila a bytecode de CPython optimizado a nivel de maquina.")
    print("  -> Precision Aritmetica: Ambos manejan enteros de precision arbitraria")
    print("     sin desbordamiento (BigInt), calculando exactamente 100! (158 digitos).")


if __name__ == "__main__":
    ejecutar_benchmark()
