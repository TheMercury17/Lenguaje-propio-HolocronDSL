# =============================================================================
# Biblioteca Propia de Machine Learning y Analisis Predictivo: HolocronDSL
# Implementacion desde cero de K-Means, Perceptron, Arbol de Decision y Filtros
# Autores: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
# =============================================================================

import math
from typing import Any, Dict, List, Optional, Tuple, Union
from src.errors.semantic_error import ErrorModeloML
from src.runtime.data_structures import NodoArbolDecision, HolocronArray


# -----------------------------------------------------------------------------
# Funciones Matematicas y Metricas de Evaluacion
# -----------------------------------------------------------------------------

def distancia_euclidiana(punto_a: List[float], punto_b: List[float]) -> float:
    """Calcula la distancia euclidiana entre dos vectores de igual dimension."""
    if len(punto_a) != len(punto_b):
        raise ErrorModeloML(
            modelo="DistanciaEuclidiana",
            detalle=f"Dimensiones incompatibles: {len(punto_a)} frente a {len(punto_b)}"
        )
    suma_cuadrados = sum((float(a) - float(b)) ** 2 for a, b in zip(punto_a, punto_b))
    return math.sqrt(suma_cuadrados)


def calcular_impureza_gini(etiquetas: List[Any]) -> float:
    """
    Calcula el indice de impureza de Gini para una coleccion de etiquetas de clase.
    Gini = 1 - sum(p_i^2)
    """
    n = len(etiquetas)
    if n == 0:
        return 0.0

    conteos: Dict[Any, int] = {}
    for etiq in etiquetas:
        conteos[etiq] = conteos.get(etiq, 0) + 1

    suma_prob_cuadradas = sum((conteo / n) ** 2 for conteo in conteos.values())
    return 1.0 - suma_prob_cuadradas


def calcular_entropia(etiquetas: List[Any]) -> float:
    """Calcula la entropia de Shannon de un conjunto de etiquetas."""
    n = len(etiquetas)
    if n == 0:
        return 0.0

    conteos: Dict[Any, int] = {}
    for etiq in etiquetas:
        conteos[etiq] = conteos.get(etiq, 0) + 1

    entropia = 0.0
    for conteo in conteos.values():
        p = conteo / n
        if p > 0:
            entropia -= p * math.log2(p)
    return entropia


def evaluar_exactitud(y_real: List[Any], y_pred: List[Any]) -> float:
    """Calcula la proporcion de aciertos (accuracy) entre predicciones y valores reales."""
    if len(y_real) != len(y_pred) or len(y_real) == 0:
        return 0.0
    aciertos = sum(1 for yr, yp in zip(y_real, y_pred) if yr == yp)
    return aciertos / len(y_real)


def calcular_matriz_confusion(y_real: List[Any], y_pred: List[Any]) -> Dict[str, Any]:
    """Genera la matriz de confusion para dos listas de etiquetas emparejadas."""
    clases = sorted(list(set(y_real) | set(y_pred)))
    matriz: Dict[Any, Dict[Any, int]] = {c1: {c2: 0 for c2 in clases} for c1 in clases}

    for yr, yp in zip(y_real, y_pred):
        matriz[yr][yp] += 1

    return {
        "clases": clases,
        "matriz": matriz,
        "exactitud": evaluar_exactitud(y_real, y_pred)
    }


# -----------------------------------------------------------------------------
# Algoritmo 1: Agrupamiento no Supervisado K-Means (KMeansGalactico)
# -----------------------------------------------------------------------------

class KMeansGalactico:
    """
    Agrupamiento no supervisado K-Means implementado puramente desde cero.
    Particiona un conjunto de observaciones multidimensionales en K grupos.
    """

    def __init__(self, k: int = 3, max_iteraciones: int = 100, tolerancia: float = 1e-4):
        if k < 1:
            raise ErrorModeloML(modelo="KMeans", detalle="El numero de clusters k debe ser mayor o igual a 1")
        self.k = int(k)
        self.max_iteraciones = int(max_iteraciones)
        self.tolerancia = float(tolerancia)
        self.centroides: List[List[float]] = []
        self.inercia: float = 0.0
        self.iteraciones_ejecutadas: int = 0

    def _inicializar_centroides(self, X: List[List[float]]) -> List[List[float]]:
        """Inicializacion de centroides distribuida deterministicamente sobre los datos."""
        n = len(X)
        if n < self.k:
            raise ErrorModeloML(
                modelo="KMeans",
                detalle=f"Numero de muestras ({n}) menor que el numero de clusters ({self.k})"
            )
        paso = max(1, n // self.k)
        centroides = [list(X[min(i * paso, n - 1)]) for i in range(self.k)]
        return centroides

    def entrenar(self, X: List[List[float]]) -> 'KMeansGalactico':
        """Ajusta los centroides a traves de iteraciones de minimizacion de distancias."""
        if not X:
            raise ErrorModeloML(modelo="KMeans", detalle="El conjunto de datos de entrenamiento esta vacio")

        self.centroides = self._inicializar_centroides(X)
        dim = len(X[0])

        for iter_idx in range(self.max_iteraciones):
            self.iteraciones_ejecutadas = iter_idx + 1
            # 1. Asignar cada punto al centroide mas cercano
            clusters: List[List[List[float]]] = [[] for _ in range(self.k)]
            for punto in X:
                dists = [distancia_euclidiana(punto, c) for c in self.centroides]
                cluster_asignado = dists.index(min(dists))
                clusters[cluster_asignado].append(punto)

            # 2. Recalcular posicion de cada centroide
            nuevos_centroides: List[List[float]] = []
            cambio_maximo = 0.0

            for i in range(self.k):
                if clusters[i]:
                    nuevo_c = [
                        sum(p[d] for p in clusters[i]) / len(clusters[i])
                        for d in range(dim)
                    ]
                else:
                    nuevo_c = list(self.centroides[i])

                desplazamiento = distancia_euclidiana(self.centroides[i], nuevo_c)
                if desplazamiento > cambio_maximo:
                    cambio_maximo = desplazamiento
                nuevos_centroides.append(nuevo_c)

            self.centroides = nuevos_centroides
            if cambio_maximo < self.tolerancia:
                break

        # 3. Calcular la inercia final (suma de distancias cuadradas a centroides)
        self.inercia = 0.0
        for punto in X:
            dists_sq = [distancia_euclidiana(punto, c) ** 2 for c in self.centroides]
            self.inercia += min(dists_sq)

        return self

    def predecir_uno(self, punto: List[float]) -> int:
        """Determina el cluster mas cercano para una muestra individual."""
        if not self.centroides:
            raise ErrorModeloML(modelo="KMeans", detalle="El modelo no ha sido entrenado")
        dists = [distancia_euclidiana(punto, c) for c in self.centroides]
        return dists.index(min(dists))

    def predecir(self, X: List[List[float]]) -> List[int]:
        """Asigna etiquetas de cluster a una coleccion de muestras."""
        return [self.predecir_uno(p) for p in X]

    def a_cadena_resumen(self) -> str:
        """Genera un reporte textual descriptivo del modelo K-Means ajustado."""
        lineas = [
            f"[K-Means Galactico] Modelo entrenado con {self.k} clusters:",
            f"  -> Iteraciones: {self.iteraciones_ejecutadas}",
            f"  -> Inercia (WSS): {self.inercia:.4f}",
            "  -> Centroides finales:"
        ]
        for idx, c in enumerate(self.centroides):
            coords = ", ".join(f"{val:.3f}" for val in c)
            lineas.append(f"     Cluster {idx}: ({coords})")
        return "\n".join(lineas)


# -----------------------------------------------------------------------------
# Algoritmo 2: Perceptron Lineal Supervisado (PerceptronGalactico)
# -----------------------------------------------------------------------------

class PerceptronGalactico:
    """
    Perceptron lineal binario implementado desde cero para clasificacion supervisada.
    Utiliza la regla de aprendizaje de Rosenblatt para ajustar pesos y sesgo.
    """

    def __init__(self, tasa_aprendizaje: float = 0.05, epocas: int = 50):
        self.tasa_aprendizaje = float(tasa_aprendizaje)
        self.epocas = int(epocas)
        self.pesos: List[float] = []
        self.sesgo: float = 0.0
        self.clases_originales: List[Any] = []
        self.exactitud_entrenamiento: float = 0.0

    def entrenar(self, X: List[List[float]], y: List[Any]) -> 'PerceptronGalactico':
        """
        Entrena el perceptron sobre las caracteristicas X y las etiquetas y.
        Mapea las etiquetas a 0 y 1 internamente si son arbitrarias.
        """
        if len(X) != len(y) or len(X) == 0:
            raise ErrorModeloML(
                modelo="Perceptron",
                detalle=f"Numero de muestras ({len(X)}) difiere del numero de etiquetas ({len(y)})"
            )

        # Identificar y registrar las dos clases binarias
        clases_unicas = sorted(list(set(y)))
        if len(clases_unicas) > 2:
            raise ErrorModeloML(
                modelo="Perceptron",
                detalle=f"El perceptron clasico solo admite 2 clases binarias, pero se encontraron {len(clases_unicas)}: {clases_unicas}"
            )
        elif len(clases_unicas) == 1:
            clases_unicas.append("otra_clase")

        self.clases_originales = clases_unicas
        # Mapear a 0 y 1
        y_bin = [1 if val == self.clases_originales[1] else 0 for val in y]

        dim = len(X[0])
        self.pesos = [0.0 for _ in range(dim)]
        self.sesgo = 0.0

        for _ in range(self.epocas):
            for xi, yi in zip(X, y_bin):
                # Activacion lineal: z = w * x + b
                z = sum(w * x for w, x in zip(self.pesos, xi)) + self.sesgo
                pred = 1 if z >= 0.0 else 0
                error = yi - pred
                if error != 0:
                    delta = self.tasa_aprendizaje * error
                    for d in range(dim):
                        self.pesos[d] += delta * float(xi[d])
                    self.sesgo += delta

        # Evaluar la exactitud final sobre el conjunto de entrenamiento
        preds_entrenamiento = self.predecir(X)
        self.exactitud_entrenamiento = evaluar_exactitud(y, preds_entrenamiento)
        return self

    def predecir_uno(self, x: List[float]) -> Any:
        """Clasifica un vector de caracteristicas individual."""
        if not self.pesos:
            raise ErrorModeloML(modelo="Perceptron", detalle="El perceptron no ha sido entrenado")
        z = sum(w * float(val) for w, val in zip(self.pesos, x)) + self.sesgo
        etiqueta_bin = 1 if z >= 0.0 else 0
        return self.clases_originales[etiqueta_bin]

    def predecir(self, X: List[List[float]]) -> List[Any]:
        """Clasifica una coleccion de muestras."""
        return [self.predecir_uno(x) for x in X]

    def a_cadena_resumen(self) -> str:
        """Genera un reporte descriptivo de los parametros aprendidos."""
        pesos_str = ", ".join(f"{w:.4f}" for w in self.pesos)
        lineas = [
            "[Perceptron Galactico] Modelo Lineal Entrenado:",
            f"  -> Clases: {self.clases_originales[0]} (0) vs {self.clases_originales[1]} (1)",
            f"  -> Vector de Pesos (w): [{pesos_str}]",
            f"  -> Sesgo (b): {self.sesgo:.4f}",
            f"  -> Epocas ejecutadas: {self.epocas} (Tasa: {self.tasa_aprendizaje})",
            f"  -> Exactitud en entrenamiento: {self.exactitud_entrenamiento * 100:.2f}%"
        ]
        return "\n".join(lineas)


# -----------------------------------------------------------------------------
# Algoritmo 3: Arbol de Decision Supervisado (ArbolDecisionGalactico)
# -----------------------------------------------------------------------------

class ArbolDecisionGalactico:
    """
    Arbol de Decision binario supervisado tipo CART implementado desde cero.
    Selecciona recursivamente divisiones que minimizan la impureza de Gini.
    """

    def __init__(self, profundidad_maxima: int = 4, min_muestras_division: int = 2):
        self.profundidad_maxima = int(profundidad_maxima)
        self.min_muestras_division = int(min_muestras_division)
        self.raiz: Optional[NodoArbolDecision] = None
        self.nombres_caracteristicas: List[str] = []
        self.exactitud_entrenamiento: float = 0.0

    def _clase_mayoritaria(self, y: List[Any]) -> Any:
        """Determina la clase modal mas frecuente en una lista."""
        if not y:
            return None
        conteos: Dict[Any, int] = {}
        for val in y:
            conteos[val] = conteos.get(val, 0) + 1
        return max(conteos.keys(), key=lambda k: conteos[k])

    def _mejor_division(
        self, X: List[List[float]], y: List[Any]
    ) -> Tuple[Optional[int], Optional[float], float]:
        """
        Encuentra el mejor atributo y umbral numerico que maximice la reduccion de Gini.
        Retorna (indice_atributo, mejor_umbral, mejor_ganancia_gini).
        """
        n = len(y)
        if n < self.min_muestras_division:
            return None, None, 0.0

        impureza_actual = calcular_impureza_gini(y)
        mejor_ganancia = 0.0
        mejor_attr: Optional[int] = None
        mejor_umbral: Optional[float] = None
        num_attrs = len(X[0])

        for attr in range(num_attrs):
            # Obtener valores ordenados unicos para generar puntos de corte
            valores = sorted(list(set(float(X[i][attr]) for i in range(n))))
            if len(valores) <= 1:
                continue

            for idx in range(len(valores) - 1):
                umbral = (valores[idx] + valores[idx + 1]) / 2.0

                # Particionar
                y_izq = [y[i] for i in range(n) if float(X[i][attr]) <= umbral]
                y_der = [y[i] for i in range(n) if float(X[i][attr]) > umbral]

                if not y_izq or not y_der:
                    continue

                # Calcular impureza ponderada
                peso_izq = len(y_izq) / n
                peso_der = len(y_der) / n
                gini_dividido = peso_izq * calcular_impureza_gini(y_izq) + peso_der * calcular_impureza_gini(y_der)
                ganancia = impureza_actual - gini_dividido

                if ganancia > mejor_ganancia:
                    mejor_ganancia = ganancia
                    mejor_attr = attr
                    mejor_umbral = umbral

        return mejor_attr, mejor_umbral, mejor_ganancia

    def _construir_nodo(
        self, X: List[List[float]], y: List[Any], profundidad: int = 0
    ) -> NodoArbolDecision:
        """Construye recursivamente los nodos y hojas del arbol de decision."""
        n = len(y)
        impureza = calcular_impureza_gini(y)
        clase_pred = self._clase_mayoritaria(y)

        # Criterios de parada: pureza, profundidad maxima o muestras insuficientes
        if (
            impureza == 0.0
            or profundidad >= self.profundidad_maxima
            or n < self.min_muestras_division
        ):
            return NodoArbolDecision(
                es_hoja=True,
                prediccion=clase_pred,
                muestras=n,
                impureza=impureza
            )

        attr, umbral, ganancia = self._mejor_division(X, y)
        if attr is None or ganancia <= 0.0:
            return NodoArbolDecision(
                es_hoja=True,
                prediccion=clase_pred,
                muestras=n,
                impureza=impureza
            )

        # Particionar datos
        nombre_attr = self.nombres_caracteristicas[attr] if attr < len(self.nombres_caracteristicas) else f"attr_{attr}"
        X_izq = [X[i] for i in range(n) if float(X[i][attr]) <= umbral]
        y_izq = [y[i] for i in range(n) if float(X[i][attr]) <= umbral]
        X_der = [X[i] for i in range(n) if float(X[i][attr]) > umbral]
        y_der = [y[i] for i in range(n) if float(X[i][attr]) > umbral]

        rama_izq = self._construir_nodo(X_izq, y_izq, profundidad + 1)
        rama_der = self._construir_nodo(X_der, y_der, profundidad + 1)

        return NodoArbolDecision(
            es_hoja=False,
            atributo=nombre_attr,
            indice_atributo=attr,
            umbral=umbral,
            rama_izquierda=rama_izq,
            rama_derecha=rama_der,
            prediccion=clase_pred,
            muestras=n,
            impureza=impureza
        )

    def entrenar(
        self,
        X: List[List[float]],
        y: List[Any],
        nombres_caracteristicas: Optional[List[str]] = None
    ) -> 'ArbolDecisionGalactico':
        """Entrena el arbol de decision sobre la matriz X y etiquetas y."""
        if len(X) != len(y) or len(X) == 0:
            raise ErrorModeloML(
                modelo="ArbolDecision",
                detalle=f"Numero de muestras ({len(X)}) difiere del numero de etiquetas ({len(y)})"
            )

        dim = len(X[0])
        if nombres_caracteristicas and len(nombres_caracteristicas) == dim:
            self.nombres_caracteristicas = list(nombres_caracteristicas)
        else:
            self.nombres_caracteristicas = [f"col_{i}" for i in range(dim)]

        self.raiz = self._construir_nodo(X, y, profundidad=0)
        preds = self.predecir(X)
        self.exactitud_entrenamiento = evaluar_exactitud(y, preds)
        return self

    def predecir_uno(self, x: List[float]) -> Any:
        """Clasifica una muestra individual recorriendo la estructura de nodos."""
        if self.raiz is None:
            raise ErrorModeloML(modelo="ArbolDecision", detalle="El arbol no ha sido entrenado")
        return self.raiz.predecir(x)

    def predecir(self, X: List[List[float]]) -> List[Any]:
        """Clasifica una coleccion de muestras."""
        return [self.predecir_uno(x) for x in X]

    def a_cadena_resumen(self) -> str:
        """Retorna la visualizacion estructural completa del arbol."""
        if self.raiz is None:
            return "[Arbol de Decision] Arbol no inicializado."
        cabecera = [
            f"[Arbol de Decision Galactico] Estructura Jerarquica (Profundidad Max = {self.profundidad_maxima}):",
            f"  -> Exactitud en entrenamiento: {self.exactitud_entrenamiento * 100:.2f}%",
            "------------------------------------------------------------------"
        ]
        return "\n".join(cabecera) + "\n" + str(self.raiz)


# -----------------------------------------------------------------------------
# Filtros y Normalizacion de Datos (Preprocesamiento)
# -----------------------------------------------------------------------------

def normalizar_min_max(valores: List[float]) -> List[float]:
    """Escala una serie numerica al intervalo continuo [0.0, 1.0]."""
    validos = [float(v) for v in valores if v is not None]
    if not validos:
        return [0.0 for _ in valores]
    v_min = min(validos)
    v_max = max(validos)
    rango = v_max - v_min
    if rango == 0.0:
        return [0.0 for _ in valores]
    return [
        (float(v) - v_min) / rango if v is not None else 0.0
        for v in valores
    ]


def estandarizar_z_score(valores: List[float]) -> List[float]:
    """Estandariza una serie numerica para tener media 0 y varianza 1."""
    validos = [float(v) for v in valores if v is not None]
    if not validos:
        return [0.0 for _ in valores]
    media = sum(validos) / len(validos)
    varianza = sum((v - media) ** 2 for v in validos) / len(validos)
    desviacion = math.sqrt(varianza)
    if desviacion == 0.0:
        return [0.0 for _ in valores]
    return [
        (float(v) - media) / desviacion if v is not None else 0.0
        for v in valores
    ]


def codificar_etiquetas(valores: List[Any]) -> Tuple[List[int], Dict[Any, int]]:
    """Codifica etiquetas categoricas arbitrarias a numeros enteros consecutivos [0, k-1]."""
    mapeo: Dict[Any, int] = {}
    codificados: List[int] = []
    contador = 0
    for val in valores:
        if val not in mapeo:
            mapeo[val] = contador
            contador += 1
        codificados.append(mapeo[val])
    return codificados, mapeo
