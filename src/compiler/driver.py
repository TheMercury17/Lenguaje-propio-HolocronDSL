# Controlador de analisis lexico y sintactico para HolocronDSL
# Encapsula la interaccion con los analizadores generados por ANTLR4

import sys
from pathlib import Path
from typing import Tuple

from antlr4 import InputStream, CommonTokenStream
from antlr4.tree.Tree import TerminalNodeImpl

from src.generated.HolocronDSLLexer import HolocronDSLLexer
from src.generated.HolocronDSLParser import HolocronDSLParser
from src.errors.error_listener import HolocronErrorListener


def parse_string(codigo: str) -> Tuple[HolocronDSLParser.ProgramaContext, HolocronErrorListener]:
    """
    Analiza una cadena de texto con codigo en HolocronDSL.
    Retorna el arbol sintactico (CST) y el manejador de errores.
    """
    input_stream = InputStream(codigo)
    lexer = HolocronDSLLexer(input_stream)
    
    # Configurar listener personalizado para el lexer
    error_listener = HolocronErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    
    token_stream = CommonTokenStream(lexer)
    parser = HolocronDSLParser(token_stream)
    
    # Configurar listener personalizado para el parser
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    arbol = parser.programa()
    return arbol, error_listener, parser


def parse_file(ruta_archivo: str) -> Tuple[HolocronDSLParser.ProgramaContext, HolocronErrorListener]:
    """
    Lee un archivo con extension .holo y realiza el analisis sintactico.
    """
    path = Path(ruta_archivo)
    if not path.exists():
        raise FileNotFoundError(f"No se encontro el archivo de transmision: {ruta_archivo}")
    
    contenido = path.read_text(encoding="utf-8")
    return parse_string(contenido)


def tree_to_string(tree, parser: HolocronDSLParser) -> str:
    """Devuelve la representacion en formato LISP (parentizado) del arbol."""
    return tree.toStringTree(recog=parser)


def format_ast_tree(node, parser: HolocronDSLParser, indent: str = "", is_last: bool = True) -> str:
    """
    Genera una representacion visual jerarquica y legible del arbol sintactico.
    Muestra la estructura de ramas y hojas de forma clara.
    """
    prefijo = indent + ("\\-- " if is_last else "+-- ")
    nuevo_indent = indent + ("    " if is_last else "|   ")
    
    # Si es nodo terminal (hoja / token concreto)
    if isinstance(node, TerminalNodeImpl):
        texto = node.getText().replace("\n", "\\n").replace("\r", "\\r")
        return f"{prefijo}Token: '{texto}'\n"
    
    # Si es una regla no terminal del parser
    nombre_regla = parser.ruleNames[node.getRuleIndex()]
    lineas = [f"{prefijo}<{nombre_regla}>\n"]
    
    hijos = [node.getChild(i) for i in range(node.getChildCount())]
    for idx, hijo in enumerate(hijos):
        ultimo = (idx == len(hijos) - 1)
        lineas.append(format_ast_tree(hijo, parser, nuevo_indent, ultimo))
        
    return "".join(lineas)
