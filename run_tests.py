#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Script utilitario de ejecucion de pruebas y validaciones para HolocronDSL
# Permite ejecutar pruebas completas o por separado en cualquier sistema operativo

import argparse
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

# Re-ejecutar con el interprete de .venv o venv si existe y no esta activado
if "VIRTUAL_ENV" not in os.environ:
    for venv_name in [".venv", "venv"]:
        venv_py = ROOT_DIR / venv_name / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python3")
        if not venv_py.exists() and sys.platform != "win32":
            venv_py = ROOT_DIR / venv_name / "bin/python"
        if venv_py.exists() and sys.executable != str(venv_py):
            try:
                os.execv(str(venv_py), [str(venv_py)] + sys.argv)
            except Exception:
                pass

# Asegurar que los paquetes de .venv se encuentren en sys.path prioritariamente
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


def ejecutar_modulo_pruebas(modulo: str) -> bool:
    """Ejecuta un modulo de pruebas especifico y retorna True si paso exitosamente."""
    print(f"\n" + "=" * 60)
    print(f"Ejecutando: {modulo}")
    print("=" * 60)
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(modulo)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


def ejecutar_todos_los_tests() -> bool:
    """Descubre y ejecuta la totalidad de las pruebas unitarias."""
    print("\n" + "=" * 60)
    print("Ejecutando suite completa de pruebas de HolocronDSL")
    print("=" * 60)
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(ROOT_DIR / "tests"))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


def verificar_ejemplos() -> bool:
    """Valida sintacticamente todos los programas .holo en la carpeta examples/."""
    print("\n" + "=" * 60)
    print("Verificando archivos de ejemplo (.holo) con el CLI")
    print("=" * 60)
    carpeta_ejemplos = ROOT_DIR / "examples"
    archivos = sorted(carpeta_ejemplos.glob("*.holo"))
    if not archivos:
        print("No se encontraron archivos de ejemplo.")
        return False

    todos_validos = True
    for archivo in archivos:
        cmd = [sys.executable, str(ROOT_DIR / "src" / "cli.py"), str(archivo), "--check"]
        resultado = subprocess.run(cmd, capture_output=True, text=True)
        if resultado.returncode == 0:
            print(f"  [OK]  {archivo.name} verificado sin anomalias.")
        else:
            print(f"  [FALLO] {archivo.name}")
            print(resultado.stdout)
            todos_validos = False

    return todos_validos


def compilar_gramatica() -> bool:
    """Invoca ANTLR4 para regenerar los analizadores en src/generated."""
    print("\n" + "=" * 60)
    print("Compilando gramatica ANTLR4 (HolocronDSL.g4)")
    print("=" * 60)
    cmd = ["antlr4", "-Dlanguage=Python3", "-visitor", "-o", "src/generated", "grammar/HolocronDSL.g4"]
    try:
        resultado = subprocess.run(cmd, cwd=str(ROOT_DIR), capture_output=True, text=True)
        if resultado.returncode == 0:
            print("Gramatica compilada exitosamente en src/generated.")
            return True
        else:
            print("Error al compilar la gramatica:")
            print(resultado.stderr)
            return False
    except FileNotFoundError:
        print("Comando 'antlr4' no encontrado en el PATH del sistema.")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Gestor de Pruebas y Tareas para HolocronDSL",
        epilog="Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona"
    )
    parser.add_argument("--lexer", action="store_true", help="Ejecuta unicamente las pruebas del analizador lexico")
    parser.add_argument("--parser", action="store_true", help="Ejecuta unicamente las pruebas sintacticas positivas")
    parser.add_argument("--invalid", action="store_true", help="Ejecuta unicamente las pruebas sintacticas negativas")
    parser.add_argument("--examples", action="store_true", help="Verifica todos los programas de ejemplo en examples/")
    parser.add_argument("--grammar", action="store_true", help="Compila la gramatica ANTLR4")
    parser.add_argument("--all", action="store_true", help="Ejecuta todas las pruebas unitarias y verifica ejemplos")

    args = parser.parse_args()

    # Si no se indica opcion, ejecutar todas las pruebas unitarias
    if not (args.lexer or args.parser or args.invalid or args.examples or args.grammar or args.all):
        exito = ejecutar_todos_los_tests()
        sys.exit(0 if exito else 1)

    exito = True
    if args.grammar:
        exito = compilar_gramatica() and exito
    if args.lexer:
        exito = ejecutar_modulo_pruebas("tests.test_lexer") and exito
    if args.parser:
        exito = ejecutar_modulo_pruebas("tests.test_parser_valid") and exito
    if args.invalid:
        exito = ejecutar_modulo_pruebas("tests.test_parser_invalid") and exito
    if args.examples:
        exito = verificar_ejemplos() and exito
    if args.all:
        exito = ejecutar_todos_los_tests() and verificar_ejemplos() and exito

    sys.exit(0 if exito else 1)


if __name__ == "__main__":
    main()
