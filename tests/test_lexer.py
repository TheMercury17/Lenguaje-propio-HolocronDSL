# Pruebas unitarias para el analizador lexico (Lexer) de HolocronDSL
# Valida el reconocimiento de tokens, operadores galacticos, literales y comentarios

import unittest
from antlr4 import InputStream, Token
from src.generated.HolocronDSLLexer import HolocronDSLLexer


class TestHolocronLexer(unittest.TestCase):
    """Verifica el analisis lexico y la tokenizacion correcta."""

    def _obtener_tokens(self, codigo: str):
        """Metodo utilitario para extraer la lista de tipos y textos de tokens."""
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
        codigo = "abrir_holocron archivar_holocron purgar_donde forjar_cristal mision fin_mision"
        tokens, lexer = self._obtener_tokens(codigo)
        textos = [t[1] for t in tokens]
        self.assertIn("abrir_holocron", textos)
        self.assertIn("archivar_holocron", textos)
        self.assertIn("purgar_donde", textos)
        self.assertIn("forjar_cristal", textos)
        self.assertIn("mision", textos)
        self.assertIn("fin_mision", textos)

    def test_operadores_galacticos_y_simbolos(self):
        """Verifica operadores caracteristicos como pipeline '==>' y asignacion '<-'."""
        codigo = "< - <- ==> := == != <= >= < > + - * / % ^"
        tokens, lexer = self._obtener_tokens(codigo)
        textos = [t[1] for t in tokens]
        self.assertIn("<-", textos)
        self.assertIn("==>", textos)
        self.assertIn(":=", textos)
        self.assertIn("==", textos)
        self.assertIn("!=", textos)
        self.assertIn("<=", textos)
        self.assertIn(">=", textos)

    def test_conectores_logicos_de_la_fuerza(self):
        """Verifica los operadores booleanos tematicos."""
        codigo = "y_fuerza o_fuerza no_fuerza"
        tokens, lexer = self._obtener_tokens(codigo)
        nombres = [lexer.symbolicNames[t[0]] for t in tokens]
        self.assertEqual(nombres, ["Y_FUERZA", "O_FUERZA", "NO_FUERZA"])

    def test_literales_booleanos_galacticos(self):
        """Verifica los literales booleanos 'cierto_es' y 'falso_es'."""
        codigo = "cierto_es falso_es"
        tokens, lexer = self._obtener_tokens(codigo)
        for token_type, _ in tokens:
            self.assertEqual(lexer.symbolicNames[token_type], "BOOL")

    def test_literales_numericos_y_cadenas(self):
        """Verifica enteros, decimales y cadenas de caracteres."""
        codigo = '42 3.14159 "Coruscant" "Sector 7"'
        tokens, lexer = self._obtener_tokens(codigo)
        nombres = [lexer.symbolicNames[t[0]] for t in tokens]
        self.assertEqual(nombres, ["NUMERO", "NUMERO", "CADENA", "CADENA"])

    def test_comentarios_linea_y_bloque(self):
        """Verifica que los comentarios sean ignorados sin generar tokens de datos."""
        codigo = """
        -- Este es un comentario de transmision estelar
        cazas <- abrir_holocron "datos.csv"
        /-
          Este es un bloque de comentarios
          sobre la Fuerza y el hiperespacio.
        -/
        """
        tokens, lexer = self._obtener_tokens(codigo)
        textos = [t[1] for t in tokens]
        # Ningun texto de comentario debe aparecer en los tokens utiles
        self.assertNotIn("Este es un comentario", textos)
        self.assertNotIn("Este es un bloque", textos)
        self.assertEqual(textos, ["cazas", "<-", "abrir_holocron", '"datos.csv"'])


if __name__ == "__main__":
    unittest.main()
