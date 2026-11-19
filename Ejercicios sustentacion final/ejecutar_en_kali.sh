#!/usr/bin/env bash
# =============================================================================
# SCRIPT DE EJECUCION PARA MAQUINA VIRTUAL KALI LINUX
# Proyecto HolocronDSL - Sustentacion Final (Fase 3)
# Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
# =============================================================================

set -e

# Asegurar ejecucion desde la raiz del repositorio
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

echo "============================================================================"
echo "  HOLOCRONDDSL - EJECUTOR DE SUSTENTACION FINAL EN KALI LINUX"
echo "  Directorio de trabajo: ${REPO_ROOT}"
echo "============================================================================"

# Deteccion del ejecutable de Python
if [ -n "${VIRTUAL_ENV}" ]; then
    PYTHON_CMD="python3"
    echo "[Entorno] Utilizando entorno virtual activo: ${VIRTUAL_ENV}"
elif [ -f ".venv/bin/python" ]; then
    PYTHON_CMD=".venv/bin/python"
    echo "[Entorno] Utilizando interprete de .venv local: ${PYTHON_CMD}"
else
    PYTHON_CMD="python3"
    echo "[Entorno] Utilizando interprete del sistema: $(which python3)"
fi

echo ""
echo "Seleccione una opcion para ejecutar:"
echo "  1) Ejecutar los 5 ejercicios completos secuencialmente"
echo "  2) Ejercicio 1: Factorial (5 al 100) y Benchmark frente a Python"
echo "  3) Ejercicio 2: Proyeccion y Analisis de la Funcion Sigmoide"
echo "  4) Ejercicio 3: Perceptron Multicapa para XOR (Backprop y Descenso Gradiente)"
echo "  5) Ejercicio 4: Analisis Exploratorio de Datos (EDA) sobre censo_ingresos.xlsx"
echo "  6) Ejercicio 5: Filtro Funcional de Numeros Primos del 1 al 100"
echo "  7) Ejecutar Suite Completa de Pruebas Unitarias (93 pruebas)"
echo "  8) Abrir visor de graficas generadas en Kali Linux (Ristretto / xdg-open)"
echo "  9) Salir"
echo "============================================================================"

OPCION="${1:-}"

if [ -z "${OPCION}" ]; then
    read -p "Ingrese su opcion [1-9]: " OPCION
fi

case "${OPCION}" in
    1)
        echo ""
        echo ">>> [1/5] Ejecutando Ejercicio 1: Factorial y Benchmark..."
        "${PYTHON_CMD}" holocron.py "Ejercicios sustentacion final/01_factorial_rendimiento.holo"
        "${PYTHON_CMD}" "Ejercicios sustentacion final/benchmark_factorial.py"

        echo ""
        echo ">>> [2/5] Ejecutando Ejercicio 2: Funcion Sigmoide..."
        "${PYTHON_CMD}" holocron.py "Ejercicios sustentacion final/02_visualizar_sigmoide.holo"
        "${PYTHON_CMD}" "Ejercicios sustentacion final/generar_sigmoide.py"

        echo ""
        echo ">>> [3/5] Ejecutando Ejercicio 3: Perceptron Multicapa XOR..."
        "${PYTHON_CMD}" holocron.py "Ejercicios sustentacion final/03_perceptron_multicapa_xor.holo"
        "${PYTHON_CMD}" "Ejercicios sustentacion final/analisis_mlp_xor.py"

        echo ""
        echo ">>> [4/5] Ejecutando Ejercicio 4: Analisis Exploratorio .xlsx..."
        "${PYTHON_CMD}" holocron.py "Ejercicios sustentacion final/04_analisis_exploratorio_xlsx.holo"
        "${PYTHON_CMD}" "Ejercicios sustentacion final/analisis_eda_xlsx.py"

        echo ""
        echo ">>> [5/5] Ejecutando Ejercicio 5: Filtro Funcional de Primos..."
        "${PYTHON_CMD}" holocron.py "Ejercicios sustentacion final/05_filtro_primos_1_100.holo"
        "${PYTHON_CMD}" "Ejercicios sustentacion final/verificar_primos.py"

        echo ""
        echo "============================================================================"
        echo "LOS 5 EJERCICIOS FUERON EJECUTADOS CON EXITO."
        echo "Todas las salidas graficas (PNG) y reportes (CSV y XLS) se encuentran en:"
        echo "  - Ejercicios sustentacion final/salidas/"
        echo "  - salidas/"
        echo "============================================================================"
        ;;

    2)
        echo ""
        echo ">>> Ejecutando Ejercicio 1: Factorial 5-100..."
        "${PYTHON_CMD}" holocron.py "Ejercicios sustentacion final/01_factorial_rendimiento.holo"
        "${PYTHON_CMD}" "Ejercicios sustentacion final/benchmark_factorial.py"
        ;;

    3)
        echo ""
        echo ">>> Ejecutando Ejercicio 2: Funcion Sigmoide..."
        "${PYTHON_CMD}" holocron.py "Ejercicios sustentacion final/02_visualizar_sigmoide.holo"
        "${PYTHON_CMD}" "Ejercicios sustentacion final/generar_sigmoide.py"
        ;;

    4)
        echo ""
        echo ">>> Ejecutando Ejercicio 3: Perceptron Multicapa XOR..."
        "${PYTHON_CMD}" holocron.py "Ejercicios sustentacion final/03_perceptron_multicapa_xor.holo"
        "${PYTHON_CMD}" "Ejercicios sustentacion final/analisis_mlp_xor.py"
        ;;

    5)
        echo ""
        echo ">>> Ejecutando Ejercicio 4: Analisis Exploratorio .xlsx..."
        "${PYTHON_CMD}" holocron.py "Ejercicios sustentacion final/04_analisis_exploratorio_xlsx.holo"
        "${PYTHON_CMD}" "Ejercicios sustentacion final/analisis_eda_xlsx.py"
        ;;

    6)
        echo ""
        echo ">>> Ejecutando Ejercicio 5: Filtro Funcional de Primos..."
        "${PYTHON_CMD}" holocron.py "Ejercicios sustentacion final/05_filtro_primos_1_100.holo"
        "${PYTHON_CMD}" "Ejercicios sustentacion final/verificar_primos.py"
        ;;

    7)
        echo ""
        echo ">>> Ejecutando suite completa de pruebas unitarias e integrales..."
        "${PYTHON_CMD}" run_tests.py --all
        ;;

    8)
        echo ""
        echo ">>> Abriendo directorio de salidas visuales..."
        if command -v xdg-open &>/dev/null; then
            xdg-open "Ejercicios sustentacion final/salidas" &
        elif command -v ristretto &>/dev/null; then
            ristretto "Ejercicios sustentacion final/salidas/frontera_decision_xor.png" &
        else
            echo "Visor no detectado. Puede explorar los archivos PNG en 'Ejercicios sustentacion final/salidas/'."
        fi
        ;;

    9)
        echo "Operacion cancelada."
        exit 0
        ;;

    *)
        echo "Opcion no valida: ${OPCION}"
        exit 1
        ;;
esac
