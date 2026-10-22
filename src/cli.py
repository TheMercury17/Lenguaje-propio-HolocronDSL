#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Interfaz de linea de comandos (CLI) para HolocronDSL
# Permite analizar sintacticamente y ejecutar programas .holo

import argparse
import os
import sys
from pathlib import Path

# Ajustar PYTHONPATH y cargar .venv si existe
ROOT_DIR = Path(__file__).resolve().parent.parent

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

from src.compiler.driver import parse_file, parse_string, format_ast_tree, tree_to_string
from src.interpreter.visitor import HolocronInterpreter
from src.errors.semantic_error import HolocronSemanticError


def main():
    parser = argparse.ArgumentParser(
        description="HolocronDSL - Interprete y Procesador de Ciencia de Datos Galactica",
        epilog="Proyecto de curso: Lenguajes de Programacion y Transduccion (Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona)"
    )
    parser.add_argument("archivo", nargs="?", help="Ruta al archivo con extension .holo a ejecutar")
    parser.add_argument("--check", action="store_true", help="Valida unicamente la correctitud sintactica sin ejecutar")
    parser.add_argument("--tree", action="store_true", help="Imprime el arbol sintactico en formato jerarquico legible")
    parser.add_argument("--lisp", action="store_true", help="Imprime el arbol sintactico en formato parentizado LISP")
    parser.add_argument("--codigo", type=str, help="Cadena de codigo en linea para analisis y ejecucion rapida")
    parser.add_argument("--verbose", "-v", action="store_true", help="Imprime informacion detallada durante la ejecucion")
    parser.add_argument("--version", action="version", version="HolocronDSL v2.0.0 (Corte 2 - Semantica y Ejecucion)")

    args = parser.parse_args()

    if not args.archivo and not args.codigo:
        parser.print_help()
        sys.exit(1)

    try:
        if args.codigo:
            arbol, error_listener, parser_obj = parse_string(args.codigo)
            origen = "transmision en linea"
        else:
            arbol, error_listener, parser_obj = parse_file(args.archivo)
            origen = args.archivo

        if args.check:
            print(f"Iniciando escaneo de la transmision: {origen}...")

        if error_listener.tiene_errores():
            print("\n" + "=" * 60)
            print("ALERTAS EN EL SISTEMA: Se encontraron anomalias sintacticas:")
            print("=" * 60)
            print(error_listener.obtener_reporte())
            sys.exit(2)

        if args.check:
            print("\nSintaxis verificada con exito: la Fuerza fluye en perfecta armonia.")
            sys.exit(0)

        if args.tree:
            print("\nEstructura jerarquica del Arbol Sintactico (CST):")
            print("=" * 60)
            print(format_ast_tree(arbol, parser_obj))

        if args.lisp:
            print("\nRepresentacion parentizada (LISP):")
            print("=" * 60)
            print(tree_to_string(arbol, parser_obj))

        # Si no se solicito arbol exclusivamente o check, procedemos a la ejecucion semantica
        if not args.tree and not args.lisp:
            interprete = HolocronInterpreter(verbose=args.verbose)
            interprete.visit(arbol)

    except HolocronSemanticError as se:
        print("\n" + "=" * 60, file=sys.stderr)
        print("PERTURBACION EN LA FUERZA: Error semantico detectado:", file=sys.stderr)
        print("=" * 60, file=sys.stderr)
        print(se.formatear(), file=sys.stderr)
        sys.exit(4)
    except FileNotFoundError as e:
        print(f"Error de acceso a datos: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Falla imprevista durante el procesamiento: {e}", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
