# Pruebas unitarias para la biblioteca propia HolocronMath
import unittest
from src.runtime.math_engine import HolocronMath


class TestHolocronMath(unittest.TestCase):
    """Verifica la precision de los algoritmos matematicos y estadisticos propios."""

    def test_suma_y_promedio(self):
        datos = [10, 20, 30, 40]
        self.assertEqual(HolocronMath.suma(datos), 100)
        self.assertEqual(HolocronMath.promedio(datos), 25.0)

    def test_valores_nulos_e_ignorados(self):
        datos = [10, None, 20, "invalido", 30]
        self.assertEqual(HolocronMath.suma(datos), 60)
        self.assertEqual(HolocronMath.promedio(datos), 20.0)
        self.assertEqual(HolocronMath.conteo(datos), 4)

    def test_mediana_impar_y_par(self):
        self.assertEqual(HolocronMath.mediana([5, 1, 9]), 5)
        self.assertEqual(HolocronMath.mediana([1, 2, 3, 4]), 2.5)

    def test_cenit_y_nadir(self):
        datos = [15, 3, 89, 42, -5]
        self.assertEqual(HolocronMath.maximo(datos), 89)
        self.assertEqual(HolocronMath.minimo(datos), -5)

    def test_varianza_y_desviacion(self):
        datos = [10, 12, 23, 23, 16, 23, 21, 16]
        # Media = 18
        # Varianza muestral aproximada = 27.42857
        var = HolocronMath.varianza(datos, muestral=True)
        self.assertAlmostEqual(var, 27.42857, places=4)
        desv = HolocronMath.desviacion(datos, muestral=True)
        self.assertAlmostEqual(desv, 5.2372, places=3)

    def test_potencia_y_modulo(self):
        self.assertEqual(HolocronMath.potencia(2, 3), 8)
        self.assertEqual(HolocronMath.modulo(10, 3), 1)

    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            HolocronMath.division_segura(10, 0)
        with self.assertRaises(ZeroDivisionError):
            HolocronMath.modulo(10, 0)


if __name__ == "__main__":
    unittest.main()
