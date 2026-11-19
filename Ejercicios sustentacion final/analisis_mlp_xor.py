#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Analisis del Perceptron Multicapa (MLP) para el Problema Logico XOR
# Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
# Lenguajes de Programacion y Transduccion (2026-2)
# =============================================================================

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.runtime.ml_engine import PerceptronMulticapaGalactico, evaluar_exactitud, calcular_matriz_confusion

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def analizar_mlp_xor():
    print("=" * 75)
    print("EJERCICIO 3: ANALISIS DEL PERCEPTRON MULTICAPA PARA XOR (ESTIMADOR Y GRAFICAS)")
    print("=" * 75)

    # 1. Definicion del conjunto de datos XOR
    X = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
    y = [0, 1, 1, 0]

    # 2. Instanciacion y entrenamiento del MLP propio
    # Arquitectura: 2 entradas -> 4 neuronas ocultas -> 1 salida
    # Optimizador: Descenso de Gradiente (Gradient Descent) con Retropropagacion (Backpropagation)
    mlp = PerceptronMulticapaGalactico(
        neuronas_ocultas=4,
        tasa_aprendizaje=1.5,
        epocas=3000,
        semilla=123
    )
    mlp.entrenar(X, y)

    # 3. Estimador y metricas
    evaluacion = mlp.evaluar(X, y)
    print("\n1. Resultados de la Estimacion y Evaluacion del Modelo:")
    print(mlp.a_cadena_resumen())
    print("\nTabla de Estimaciones Individuales:")
    print(f"{'Entrada (x1, x2)':<20} | {'Clase Real (y)':<16} | {'P(y=1|x) continua':<20} | {'Prediccion Final':<16}")
    print("-" * 80)
    for xi, yi in zip(X, y):
        prob = mlp.predecir_probabilidad(xi)
        pred = mlp.predecir_uno(xi)
        print(f"({int(xi[0])}, {int(xi[1])}){'':<14} | {yi:<16} | {prob:<20.6f} | {pred:<16}")
    print("-" * 80)
    print(f"Exactitud Global: {evaluacion['exactitud'] * 100:.2f}% | Perdida Final: {evaluacion['perdida_final']:.6f}")

    # 4. Generar Grafica 1: Curva de Convergencia de Perdida (Loss Curve)
    carpeta_salidas = ROOT_DIR / "salidas"
    carpeta_salidas.mkdir(parents=True, exist_ok=True)
    ruta_loss = carpeta_salidas / "convergencia_perdida_xor.png"

    fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    fig.patch.set_facecolor("#0b0f19")
    ax.set_facecolor("#111827")

    historial = mlp.historial_perdida
    ax.plot(range(1, len(historial) + 1), historial, color="#00e5ff", linewidth=2.2, label="Error Cuadratico Medio (MSE)")
    ax.set_title("Curva de Aprendizaje y Convergencia: Descenso de Gradiente (XOR)", color="#f9fafb", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Epoca de Entrenamiento", color="#e5e7eb", fontsize=11)
    ax.set_ylabel("Perdida Acumulada (MSE)", color="#e5e7eb", fontsize=11)
    ax.tick_params(colors="#9ca3af")
    ax.grid(True, linestyle="--", alpha=0.2, color="#9ca3af")
    ax.legend(facecolor="#1f2937", edgecolor="#374151", labelcolor="#f9fafb")

    plt.tight_layout()
    plt.savefig(str(ruta_loss), dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"\n[Grafica 1 Generada] Convergencia de Perdida: {ruta_loss.resolve()}")

    # 5. Generar Grafica 2: Frontera de Decision en 2D (Decision Boundary)
    ruta_boundary = carpeta_salidas / "frontera_decision_xor.png"
    fig, ax = plt.subplots(figsize=(8, 7), dpi=300)
    fig.patch.set_facecolor("#0b0f19")
    ax.set_facecolor("#111827")

    # Malla de evaluacion densa
    pasos = 100
    x_min, x_max = -0.3, 1.3
    y_min, y_max = -0.3, 1.3
    grid_x = [x_min + i * (x_max - x_min) / pasos for i in range(pasos + 1)]
    grid_y = [y_min + i * (y_max - y_min) / pasos for i in range(pasos + 1)]

    Z = []
    for gy in grid_y:
        fila_z = []
        for gx in grid_x:
            fila_z.append(mlp.predecir_probabilidad([gx, gy]))
        Z.append(fila_z)

    # Mapa de calor de contorno de probabilidades
    cont = ax.contourf(grid_x, grid_y, Z, levels=25, cmap="coolwarm", alpha=0.75)
    cbar = plt.colorbar(cont, ax=ax)
    cbar.set_label("Probabilidad P(y=1|x)", color="#e5e7eb")
    cbar.ax.tick_params(colors="#9ca3af")

    # Linea de frontera al umbral 0.5
    ax.contour(grid_x, grid_y, Z, levels=[0.5], colors=["#ffd600"], linewidths=[2.5], linestyles=["--"])

    # Graficar puntos reales de entrenamiento
    for xi, yi in zip(X, y):
        color_pto = "#00e5ff" if yi == 1 else "#ff1744"
        marker_pto = "o" if yi == 1 else "s"
        etiqueta_pto = f"Clase {yi}"
        ax.scatter(xi[0], xi[1], c=color_pto, marker=marker_pto, s=180, edgecolors="#ffffff", linewidths=1.8, zorder=5)
        ax.annotate(f"({int(xi[0])},{int(xi[1])}) -> {yi}", (xi[0], xi[1]),
                    xytext=(xi[0] + 0.04, xi[1] + 0.04), color="#f9fafb", fontsize=11, fontweight="bold")

    ax.set_title("Frontera de Decision No Lineal para XOR (Perceptron Multicapa)", color="#f9fafb", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Entrada x1", color="#e5e7eb", fontsize=11)
    ax.set_ylabel("Entrada x2", color="#e5e7eb", fontsize=11)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.tick_params(colors="#9ca3af")
    ax.grid(True, linestyle=":", alpha=0.3, color="#9ca3af")

    plt.tight_layout()
    plt.savefig(str(ruta_boundary), dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"[Grafica 2 Generada] Frontera de Decision: {ruta_boundary.resolve()}")

    # 6. Respuesta conceptual explicita solicitada por el usuario
    print("\n" + "=" * 75)
    print("RESPUESTA TEORICA FORMAL: ¿QUE ALGORITMO USAMOS Y POR QUE?")
    print("=" * 75)
    print("""
1. ALGORITMO UTILIZADO:
   Usamos RETROPROPAGACION (Backpropagation) basado en DESCENSO DE GRADIENTE
   (Gradient Descent) con funcion de activacion SIGMOIDE LOGISTICA.

2. ¿POR QUE UN PERCEPTRON SIMPLE NO PUEDE RESOLVER XOR?
   En 1969, Marvin Minsky y Seymour Papert demostraron matematicamente que el
   Perceptron simple de una sola capa solo puede generar hiperplanos lineales
   (lineas rectas en 2D). La compuerta XOR es un problema NO LINEALMENTE SEPARABLE:
   los estados (0,1) y (1,0) estan situados diagonalmente opuestos a (0,0) y (1,1),
   por lo que ninguna recta en el plano puede dividirlos sin error.

3. ¿POR QUE EL PERCEPTRON MULTICAPA SI LO RESUELVE?
   Al añadir una capa oculta no lineal con neuronas sigmoides, la red realiza una
   transformacion de coordenadas en un espacio latente donde las cuatro muestras
   se tornan linealmente separables. La neurona de salida combina las salidas
   de la capa oculta trazando la frontera curva amarilla observada en la grafica.

4. MATEMATICA DEL APRENDIZAJE:
   - Funcion de perdida: Error Cuadratico Medio (MSE) L = 0.5 * (y - y_hat)^2
   - Regla de la Cadena: Se calcula la derivada parcial dL/dW para cada peso
     propagando el error hacia atras desde la salida hasta la capa oculta.
   - Descenso de Gradiente: Se actualiza cada peso restando la tasa de
     aprendizaje multiplicada por el gradiente: W = W - eta * (dL/dW).
""")


if __name__ == "__main__":
    analizar_mlp_xor()
