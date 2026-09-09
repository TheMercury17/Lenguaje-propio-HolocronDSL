# Interfaz de linea de comandos (CLI) para HolocronDSL
# Permite analizar sintacticamente archivos .holo y visualizar el arbol de derivacion

import argparse
import sys
from pathlib import Path

# Ajustar PYTHONPATH para ejecucion directa del script
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.compiler.driver import parse_file, parse_string, format_ast_tree, tree_to_string


def main():
    parser = argparse.ArgumentParser(
        description="HolocronDSL - Front-end y Analizador Sintactico para Ciencia de Datos Galactica",
        epilog="Proyecto de curso: Lenguajes de Programacion y Transduccion (Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona)"
    )
    parser.add_argument("archivo", nargs="?", help="Ruta al archivo con extension .holo a analizar")
    parser.add_argument("--tree", action="store_true", help="Imprime el arbol sintactico en formato jerarquico legible")
    parser.add_argument("--lisp", action="store_true", help="Imprime el arbol sintactico en formato parentizado LISP")
    parser.add_argument("--check", action="store_true", help="Valida unicamente la correctitud sintactica del codigo")
    parser.add_argument("--codigo", type=str, help="Cadena de codigo en linea para analisis rapido")
    parser.add_argument("--version", action="version", version="HolocronDSL v1.0.0 (Corte 1 - Front-end)")

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

        print(f"Iniciando escaneo de la transmision: {origen}...")

        if error_listener.tiene_errores():
            print("\n" + "=" * 60)
            print("ALERTAS EN EL SISTEMA: Se encontraron anomalias sintacticas:")
            print("=" * 60)
            print(error_listener.obtener_reporte())
            sys.exit(2)

        print("\nSintaxis verificada con exito: la Fuerza fluye en perfecta armonia.")
        
        if args.tree:
            print("\nEstructura jerarquica del Arbol Sintactico (CST):")
            print("=" * 60)
            print(format_ast_tree(arbol, parser_obj))

        if args.lisp:
            print("\nRepresentacion parentizada (LISP):")
            print("=" * 60)
            print(tree_to_string(arbol, parser_obj))

    except FileNotFoundError as e:
        print(f"Error de acceso: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Falla imprevista durante el analisis: {e}", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
