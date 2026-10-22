# Biblioteca propia de matematicas y estadisticas descriptivas para HolocronDSL
# Implementacion algoritmica pura e independiente (Grupo 5)

import math
from typing import List, Any, Union, Optional


class HolocronMath:
    """
    Biblioteca de computo matematico y estadistico para la ciencia de datos galactica.
    Implementa algoritmos estadisticos descriptivos desde cero sin dependencias opacas.
    """

    @staticmethod
    def limpiar_numericos(valores: List[Any]) -> List[Union[int, float]]:
        """Extrae unicamente los valores numericos validos, descartando nulos y cadenas no convertibles."""
        resultado = []
        for v in valores:
            if v is None:
                continue
            if isinstance(v, (int, float)) and not (isinstance(v, float) and math.isnan(v)):
                resultado.append(v)
            elif isinstance(v, str):
                try:
                    num = float(v.strip())
                    resultado.append(int(num) if num.is_integer() else num)
                except ValueError:
                    continue
        return resultado

    @staticmethod
    def suma(valores: List[Any]) -> Union[int, float]:
        """Calcula la sumatoria acumulada de los valores numericos."""
        nums = HolocronMath.limpiar_numericos(valores)
        if not nums:
            return 0
        total = 0
        for x in nums:
            total += x
        return total

    @staticmethod
    def promedio(valores: List[Any]) -> Optional[float]:
        """Calcula el equilibrio o media aritmetica."""
        nums = HolocronMath.limpiar_numericos(valores)
        if not nums:
            return None
        return HolocronMath.suma(nums) / len(nums)

    @staticmethod
    def mediana(valores: List[Any]) -> Optional[Union[int, float]]:
        """Calcula la mediana dividiendo la distribucion ordenada en dos mitades iguales."""
        nums = sorted(HolocronMath.limpiar_numericos(valores))
        n = len(nums)
        if n == 0:
            return None
        mitad = n // 2
        if n % 2 != 0:
            return nums[mitad]
        else:
            return (nums[mitad - 1] + nums[mitad]) / 2.0

    @staticmethod
    def maximo(valores: List[Any]) -> Optional[Union[int, float]]:
        """Determina el cenit o valor maximo de una coleccion."""
        nums = HolocronMath.limpiar_numericos(valores)
        if not nums:
            return None
        m = nums[0]
        for x in nums[1:]:
            if x > m:
                m = x
        return m

    @staticmethod
    def minimo(valores: List[Any]) -> Optional[Union[int, float]]:
        """Determina el nadir o valor minimo de una coleccion."""
        nums = HolocronMath.limpiar_numericos(valores)
        if not nums:
            return None
        m = nums[0]
        for x in nums[1:]:
            if x < m:
                m = x
        return m

    @staticmethod
    def conteo(valores: List[Any]) -> int:
        """Determina el recuento de observaciones validas (no nulas)."""
        return sum(1 for v in valores if v is not None)

    @staticmethod
    def varianza(valores: List[Any], muestral: bool = True) -> Optional[float]:
        """Calcula la varianza muestral o poblacional."""
        nums = HolocronMath.limpiar_numericos(valores)
        n = len(nums)
        if n <= 1:
            return 0.0 if n == 1 else None
        media = HolocronMath.promedio(nums)
        suma_cuadrados = sum((x - media) ** 2 for x in nums)
        denominador = (n - 1) if muestral else n
        return suma_cuadrados / denominador

    @staticmethod
    def desviacion(valores: List[Any], muestral: bool = True) -> Optional[float]:
        """Calcula la desviacion estandar como raiz cuadrada de la varianza."""
        var = HolocronMath.varianza(valores, muestral)
        if var is None:
            return None
        return math.sqrt(var)

    @staticmethod
    def potencia(base: Union[int, float], exponente: Union[int, float]) -> Union[int, float]:
        """Calcula la potencia base ^ exponente."""
        return base ** exponente

    @staticmethod
    def modulo(dividendo: Union[int, float], divisor: Union[int, float]) -> Union[int, float]:
        """Calcula el residuo o modulo de una division."""
        if divisor == 0:
            raise ZeroDivisionError("Modulo por cero no permitido.")
        return dividendo % divisor

    @staticmethod
    def division_segura(dividendo: Union[int, float], divisor: Union[int, float]) -> float:
        """Realiza la division aritmetica verificando division por cero."""
        if divisor == 0:
            raise ZeroDivisionError("Division por cero no permitida.")
        return dividendo / divisor

    @staticmethod
    def redondear(valor: Optional[float], decimales: int = 2) -> Optional[float]:
        """Redondea un valor numerico al numero de decimales especificado."""
        if valor is None:
            return None
        return round(float(valor), decimales)
