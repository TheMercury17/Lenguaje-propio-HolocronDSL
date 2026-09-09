# Pruebas unitarias para el analizador lexico (Lexer) de HolocronDSL (Sintaxis Simplificada)

import unittest
from antlr4 import InputStream, Token
from src.generated.HolocronDSLLexer import HolocronDSLLexer


class TestHolocronLexer(unittest.TestCase):
    """Verifica el analisis lexico y la tokenizacion correcta."""

    def _obtener_tokens(self, codigo: str):
        stream = InputStream(codigo)
        lexer = HolocronDSLLexer(stream)
        tokens = []
        token = lexer.nextToken()
        while token.type != Token.EOF:
            tokens.append((token.type, token.text))
            token = lexer.nextToken()
        return tokens, lexer

    def test_palabras_reservadas_nucleo(self):
        """Verifica palabras reservadas de ingestion, transformacion y control."""
        codigo = "abrir_holocron archivar_holocron purgar forjar ordenar mision fin_mision"
        tokens, lexer = self._obtener_tokens(codigo)
        textos = [t[1] for t in tokens]
        self.assertIn("abrir_holocron", textos)
        self.assertIn("archivar_holocron", textos)
        self.assertIn("purgar", textos)
        self.assertIn("forjar", textos)
        self.assertIn("ordenar", textos)
        self.assertIn("mision", textos)
        self.assertIn("fin_mision", textos)

    def test_operadores_y_pipeline(self):
        """Verifica el operador pipe '|>' y el operador de asignacion '='."""
        codigo = "= |> >> == != <= >= < > + - * / % ^"
        tokens, lexer = self._obtener_tokens(codigo)
        textos = [t[1] for t in tokens]
        self.assertIn("=", textos)
        self.assertIn("|>", textos)
        self.assertIn(">>", textos)
        self.assertIn("==", textos)
        self.assertIn("!=", textos)
        self.assertIn("<=", textos)
        self.assertIn(">=", textos)

    def test_conectores_logicos(self):
        """Verifica los operadores booleanos 'y', 'o', 'no'."""
        codigo = "y o no y_fuerza o_fuerza no_fuerza"
        tokens, lexer = self._obtener_tokens(codigo)
        textos = [t[1] for t in tokens]
        self.assertIn("y", textos)
        self.assertIn("o", textos)
        self.assertIn("no", textos)

    def test_literales_booleanos(self):
        """Verifica los literales booleanos 'cierto_es', 'falso_es', 'verdadero', 'falso'."""
        codigo = "cierto_es falso_es verdadero falso"
        tokens, lexer = self._obtener_tokens(codigo)
        for token_type, _ in tokens:
            self.assertEqual(lexer.symbolicNames[token_type], "BOOL")

    def test_literales_numericos_y_cadenas(self):
        """Verifica enteros, decimales y cadenas de texto."""
        codigo = '42 3.14159 "Coruscant" "Sector 7"'
        tokens, lexer = self._obtener_tokens(codigo)
        nombres = [lexer.symbolicNames[t[0]] for t in tokens]
        self.assertEqual(nombres, ["NUMERO", "NUMERO", "CADENA", "CADENA"])

    def test_comentarios_linea_y_bloque(self):
        """Verifica que los comentarios sean ignorados sin generar tokens de datos."""
        codigo = """
        -- Comentario de una linea
        cazas = abrir_holocron "datos.csv"
        /-
          Comentario de bloque sobre la flota
        -/
        """
        tokens, lexer = self._obtener_tokens(codigo)
        textos = [t[1] for t in tokens]
        self.assertNotIn("Comentario de una linea", textos)
        self.assertNotIn("Comentario de bloque", textos)
        self.assertEqual(textos, ["cazas", "=", "abrir_holocron", '"datos.csv"'])


if __name__ == "__main__":
    unittest.main()
