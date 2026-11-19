#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Visualizacion y Analisis Matematico de la Funcion Sigmoide
# Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
# Lenguajes de Programacion y Transduccion (2026-2)
# =============================================================================

import sys
import math
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.compiler.driver import parse_file
from src.interpreter.visitor import HolocronInterpreter
from src.runtime.ml_engine import sigmoide

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def graficar_sigmoide_avanzada():
    print("=" * 70)
    print("EJERCICIO 2: VISUALIZACION Y ANALISIS DE LA FUNCION SIGMOIDE")
    print("=" * 70)

    # 1. Ejecutar el script HolocronDSL oficial
    ruta_holo = Path(__file__).parent / "02_visualizar_sigmoide.holo"
    print(f"1. Ejecutando programa nativo en HolocronDSL: {ruta_holo.name}")
    tree, _, parser = parse_file(str(ruta_holo))
    visitor = HolocronInterpreter()
    visitor.visit(tree)

    # 2. Generar representacion analitica completa con derivada y asintotas
    print("2. Generando proyeccion analitica detallada de la sigmoide y su derivada...")
    xs = [round(-8.0 + i * 0.1, 2) for i in range(161)]
    ys_sig = [sigmoide(x) for x in xs]
    ys_der = [y * (1.0 - y) for y in ys_sig]

    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    fig.patch.set_facecolor("#0b0f19")
    ax.set_facecolor("#111827")

    # Curvas principales
    ax.plot(xs, ys_sig, color="#00e5ff", linewidth=3.0, label=r"Sigmoide: $\sigma(x) = \frac{1}{1 + e^{-x}}$")
    ax.plot(xs, ys_der, color="#e040fb", linewidth=2.2, linestyle="--", label=r"Derivada: $\sigma'(x) = \sigma(x)(1 - \sigma(x))$")

    # Asintotas horizontales y punto de inflexion
    ax.axhline(1.0, color="#ffd600", linestyle=":", alpha=0.7, label=r"Asintota Superior: $y = 1.0$")
    ax.axhline(0.0, color="#9ca3af", linestyle=":", alpha=0.7, label=r"Asintota Inferior: $y = 0.0$")
    ax.axhline(0.5, color="#38bdf8", linestyle="-.", alpha=0.4)
    ax.axvline(0.0, color="#9ca3af", linestyle=":", alpha=0.5)

    # Punto de inflexion central (0, 0.5)
    ax.scatter([0.0], [0.5], color="#ff1744", s=90, zorder=5, label=r"Punto de Inflexion $(0, 0.5)$")
    ax.annotate(r"$(0, 0.5)$" + "\n" + r"$\sigma'(0) = 0.25$", (0.0, 0.5),
                xytext=(0.7, 0.45), color="#f9fafb", fontsize=10,
                arrowprops=dict(arrowstyle="->", color="#00e5ff", lw=1.5))

    ax.set_title("Funcion de Activacion Sigmoide y su Derivada Analitica", color="#f9fafb", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("x (Entrada neta / Potencial de activacion)", color="#e5e7eb", fontsize=12)
    ax.set_ylabel(r"$\sigma(x)$ / $\sigma'(x)$", color="#e5e7eb", fontsize=12)
    ax.set_ylim(-0.05, 1.15)
    ax.set_xlim(-8, 8)
    ax.tick_params(colors="#9ca3af", labelsize=10)
    ax.grid(True, linestyle="--", alpha=0.2, color="#9ca3af")

    ax.legend(loc="upper left", facecolor="#1f2937", edgecolor="#374151", labelcolor="#f9fafb", fontsize=10)

    carpeta_salidas = ROOT_DIR / "salidas"
    carpeta_salidas.mkdir(parents=True, exist_ok=True)
    ruta_salida = carpeta_salidas / "grafica_sigmoide_completa.png"
    plt.tight_layout()
    plt.savefig(str(ruta_salida), dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()

    print(f"  -> Archivo generado: {ruta_salida.resolve()}")
    print("\n3. Propiedades fundamentales de sustentacion:")
    print("  -> Dominio: Todos los reales (-inf, +inf)")
    print("  -> Rango: Intervalo abierto (0.0, 1.0)")
    print("  -> Simetria: sigma(-x) = 1 - sigma(x)")
    print("  -> Maxima pendiente: Ocurre en x = 0 con valor exacto de 0.25")
    print("  -> Rol en Redes Neuronales: Introduce no linealidad y comprime valores")
    print("     a probabilidades continuas, siendo esencial para capas ocultas y de salida.")


if __name__ == "__main__":
    graficar_sigmoide_avanzada()
