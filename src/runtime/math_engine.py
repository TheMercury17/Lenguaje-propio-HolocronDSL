# Biblioteca propia de matematicas y estadisticas descriptivas para HolocronDSL
# Implementacion algoritmica pura e independiente (Grupo 5)

import math
from typing import List, Any, Union, Optional, Tuple, Dict


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

    @staticmethod
    def limpiar_pares_numericos(
        valores_x: List[Any],
        valores_y: List[Any]
    ) -> Tuple[List[float], List[float]]:
        """
        Filtra pares ordenados (x_i, y_i) asegurando que ambos elementos sean numericos validos y no nulos.
        Descarta cualquier par incompleto para mantener correspondencia estricta.
        """
        pares_x: List[float] = []
        pares_y: List[float] = []
        min_len = min(len(valores_x), len(valores_y))
        for i in range(min_len):
            vx, vy = valores_x[i], valores_y[i]
            if vx is None or vy is None:
                continue
            try:
                nx = float(vx)
                ny = float(vy)
                if not (math.isnan(nx) or math.isnan(ny) or math.isinf(nx) or math.isinf(ny)):
                    pares_x.append(nx)
                    pares_y.append(ny)
            except (ValueError, TypeError):
                continue
        return pares_x, pares_y

    @staticmethod
    def covarianza(
        valores_x: List[Any],
        valores_y: List[Any],
        muestral: bool = True
    ) -> Optional[float]:
        """
        Calcula la covarianza muestral o poblacional entre dos series numericas:
        Cov(X, Y) = sum((x_i - mean_x) * (y_i - mean_y)) / (n - 1)
        """
        xs, ys = HolocronMath.limpiar_pares_numericos(valores_x, valores_y)
        n = len(xs)
        if n < 2:
            return None
        media_x = sum(xs) / n
        media_y = sum(ys) / n
        suma_productos = sum((x - media_x) * (y - media_y) for x, y in zip(xs, ys))
        denominador = (n - 1) if muestral else n
        return suma_productos / denominador

    @staticmethod
    def correlacion(valores_x: List[Any], valores_y: List[Any]) -> Optional[float]:
        """
        Calcula el coeficiente de correlacion lineal de Pearson (r):
        r = Cov(X, Y) / (s_x * s_y)
        Rango: [-1.0, 1.0]
        """
        xs, ys = HolocronMath.limpiar_pares_numericos(valores_x, valores_y)
        n = len(xs)
        if n < 2:
            return None
        cov = HolocronMath.covarianza(xs, ys, muestral=True)
        desv_x = HolocronMath.desviacion(xs, muestral=True)
        desv_y = HolocronMath.desviacion(ys, muestral=True)
        if cov is None or not desv_x or not desv_y or desv_x == 0 or desv_y == 0:
            return 0.0
        r = cov / (desv_x * desv_y)
        return max(-1.0, min(1.0, r))

    @staticmethod
    def regresion_lineal(
        valores_x: List[Any],
        valores_y: List[Any]
    ) -> dict:
        """
        Calcula el ajuste de regresion lineal simple por el metodo de Minimos Cuadrados Ordinarios (MCO):
        y_hat = m * x + b
        donde:
          m = sum((x - mean_x) * (y - mean_y)) / sum((x - mean_x)^2)
          b = mean_y - m * mean_x
        Retorna diccionario con metricas completas, parametros del modelo y vector de predicciones.
        """
        xs, ys = HolocronMath.limpiar_pares_numericos(valores_x, valores_y)
        n = len(xs)
        if n < 2:
            raise ValueError("Se requieren al menos 2 observaciones numericas validas para calcular la regresion.")

        media_x = sum(xs) / n
        media_y = sum(ys) / n

        ss_xx = sum((x - media_x) ** 2 for x in xs)
        ss_xy = sum((x - media_x) * (y - media_y) for x, y in zip(xs, ys))
        ss_yy = sum((y - media_y) ** 2 for y in ys)

        if ss_xx == 0.0:
            raise ValueError("La variable independiente X presenta varianza cero (todos los valores son identicos).")

        pendiente = ss_xy / ss_xx
        intercepto = media_y - pendiente * media_x

        predicciones = [pendiente * x + intercepto for x in xs]
        residuos = [y - y_hat for y, y_hat in zip(ys, predicciones)]
        ss_res = sum(e ** 2 for e in residuos)

        # Coeficiente de determinacion R^2
        r_cuadrado = 1.0 - (ss_res / ss_yy) if ss_yy > 0 else 0.0
        r_cuadrado = max(0.0, min(1.0, r_cuadrado))

        # Coeficiente de correlacion de Pearson
        correlacion = HolocronMath.correlacion(xs, ys) or 0.0

        # Error estandar de la estimacion
        error_estandar = math.sqrt(ss_res / (n - 2)) if n > 2 else 0.0

        # Signo para formatear la ecuacion
        signo_b = "+" if intercepto >= 0 else "-"
        ecuacion = f"y = {pendiente:.4f} * x {signo_b} {abs(intercepto):.4f}"

        return {
            "n": n,
            "pendiente": round(pendiente, 6),
            "intercepto": round(intercepto, 6),
            "r_cuadrado": round(r_cuadrado, 4),
            "correlacion": round(correlacion, 4),
            "error_estandar": round(error_estandar, 4),
            "ecuacion": ecuacion,
            "predicciones": [round(p, 4) for p in predicciones],
            "media_x": round(media_x, 4),
            "media_y": round(media_y, 4),
            "ss_res": round(ss_res, 4)
        }
