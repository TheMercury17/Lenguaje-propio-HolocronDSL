# =============================================================================
# Biblioteca Propia de Estructuras de Datos Nativas: HolocronDSL
# Implementacion desde cero de Arreglos, Pilas, Colas y Nodos de Arbol
# Autores: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
# =============================================================================

from typing import Any, List, Optional, Iterator, Union
from src.errors.semantic_error import IndiceFueraDeRangoError, EstructuraVaciaError


class HolocronArray:
    """
    Estructura de Arreglo / Lista Dinamica nativa para HolocronDSL.
    Proporciona operaciones de indexacion segura, insercion, remocion,
    rebanado y transformacion inmutable o mutable controlada.
    """

    def __init__(self, elementos: Optional[List[Any]] = None):
        if elementos is None:
            self._datos: List[Any] = []
        elif isinstance(elementos, HolocronArray):
            self._datos = list(elementos._datos)
        elif isinstance(elementos, (list, tuple)):
            self._datos = list(elementos)
        else:
            self._datos = [elementos]

    def longitud(self) -> int:
        """Retorna la cardinalidad o numero de elementos en el arreglo."""
        return len(self._datos)

    def obtener(self, indice: int) -> Any:
        """
        Recupera el elemento en la posicion especificada.
        Soporta indexacion positiva [0, n-1] y negativa [-n, -1].
        """
        n = len(self._datos)
        if indice < 0:
            indice_ajustado = n + indice
        else:
            indice_ajustado = indice

        if indice_ajustado < 0 or indice_ajustado >= n:
            raise IndiceFueraDeRangoError(indice=indice, longitud=n)

        return self._datos[indice_ajustado]

    def asignar(self, indice: int, valor: Any) -> None:
        """Asigna un valor en la posicion especificada."""
        n = len(self._datos)
        if indice < 0:
            indice_ajustado = n + indice
        else:
            indice_ajustado = indice

        if indice_ajustado < 0 or indice_ajustado >= n:
            raise IndiceFueraDeRangoError(indice=indice, longitud=n)

        self._datos[indice_ajustado] = valor

    def agregar(self, elemento: Any) -> 'HolocronArray':
        """Añade un nuevo elemento al final del arreglo."""
        self._datos.append(elemento)
        return self

    def insertar(self, indice: int, elemento: Any) -> 'HolocronArray':
        """Inserta un elemento en la posicion indicada."""
        n = len(self._datos)
        if indice < 0 or indice > n:
            raise IndiceFueraDeRangoError(indice=indice, longitud=n)
        self._datos.insert(indice, elemento)
        return self

    def remover(self, indice: int) -> Any:
        """Remueve y retorna el elemento en la posicion indicada."""
        n = len(self._datos)
        if indice < 0 or indice >= n:
            raise IndiceFueraDeRangoError(indice=indice, longitud=n)
        return self._datos.pop(indice)

    def subarreglo(self, inicio: int, fin: int) -> 'HolocronArray':
        """Extrae un subarreglo en el rango [inicio, fin)."""
        return HolocronArray(self._datos[inicio:fin])

    def invertir(self) -> 'HolocronArray':
        """Retorna un nuevo arreglo con los elementos en orden inverso."""
        return HolocronArray(list(reversed(self._datos)))

    def ordenar(self, ascendente: bool = True) -> 'HolocronArray':
        """Retorna un nuevo arreglo ordenado."""
        try:
            return HolocronArray(sorted(self._datos, reverse=not ascendente))
        except TypeError:
            return HolocronArray(sorted(self._datos, key=lambda x: str(x), reverse=not ascendente))

    def esta_vacio(self) -> bool:
        """Indica si el arreglo carece de elementos."""
        return len(self._datos) == 0

    def a_lista_python(self) -> List[Any]:
        """Convierte la estructura a una lista estandar de Python."""
        return list(self._datos)

    def __len__(self) -> int:
        return len(self._datos)

    def __getitem__(self, item: Union[int, slice]) -> Any:
        if isinstance(item, slice):
            return HolocronArray(self._datos[item])
        return self.obtener(int(item))

    def __setitem__(self, key: int, value: Any) -> None:
        self.asignar(int(key), value)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._datos)

    def __str__(self) -> str:
        elementos_str = ", ".join(repr(x) if isinstance(x, str) else str(x) for x in self._datos)
        return f"[{elementos_str}]"

    def __repr__(self) -> str:
        return f"HolocronArray({self._datos})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, HolocronArray):
            return self._datos == other._datos
        if isinstance(other, list):
            return self._datos == other
        return False


def crear_lista_dimensionada(tamano: int, valor_inicial: Any = 0) -> HolocronArray:
    """Crea un arreglo con un numero fijo de posiciones inicializadas."""
    if tamano < 0:
        raise ValueError("El tamaño de un arreglo no puede ser negativo.")
    return HolocronArray([valor_inicial for _ in range(tamano)])


class HolocronPila:
    """
    Estructura de Pila (Stack, LIFO: Last-In, First-Out) nativa para HolocronDSL.
    Implementada puramente sobre listas internas sin librerias externas.
    """

    def __init__(self, elementos_iniciales: Optional[List[Any]] = None):
        self._elementos: List[Any] = []
        if elementos_iniciales:
            for elem in elementos_iniciales:
                self.apilar(elem)

    def apilar(self, elemento: Any) -> Any:
        """Inserta un nuevo elemento en la cima de la pila."""
        self._elementos.append(elemento)
        return elemento

    def desapilar(self) -> Any:
        """Remueve y extrae el elemento superior de la pila."""
        if not self._elementos:
            raise EstructuraVaciaError(nombre_estructura="Pila", operacion="desapilar")
        return self._elementos.pop()

    def cima(self) -> Any:
        """Inspecciona el elemento superior de la pila sin removerlo."""
        if not self._elementos:
            raise EstructuraVaciaError(nombre_estructura="Pila", operacion="cima")
        return self._elementos[-1]

    def esta_vacia(self) -> bool:
        """Indica si la pila se encuentra desprovista de elementos."""
        return len(self._elementos) == 0

    def tamano(self) -> int:
        """Retorna el numero actual de elementos apilados."""
        return len(self._elementos)

    def vaciar(self) -> None:
        """Descarta la totalidad de los elementos apilados."""
        self._elementos.clear()

    def a_arreglo(self) -> HolocronArray:
        """Convierte la pila en un HolocronArray ordenado desde la base hasta la cima."""
        return HolocronArray(list(self._elementos))

    def __len__(self) -> int:
        return len(self._elementos)

    def __str__(self) -> str:
        if not self._elementos:
            return "<Pila Holocron: [Vacia]>"
        rep = " -> ".join(str(x) for x in reversed(self._elementos))
        return f"<Pila Holocron (Cima -> Base): [{rep}]>"

    def __repr__(self) -> str:
        return f"HolocronPila({self._elementos})"


class HolocronCola:
    """
    Estructura de Cola (Queue, FIFO: First-In, First-Out) nativa para HolocronDSL.
    Implementada puramente sobre listas internas sin librerias externas.
    """

    def __init__(self, elementos_iniciales: Optional[List[Any]] = None):
        self._elementos: List[Any] = []
        if elementos_iniciales:
            for elem in elementos_iniciales:
                self.encolar(elem)

    def encolar(self, elemento: Any) -> Any:
        """Inserta un elemento al final de la cola."""
        self._elementos.append(elemento)
        return elemento

    def desencolar(self) -> Any:
        """Extrae el primer elemento en el frente de la cola."""
        if not self._elementos:
            raise EstructuraVaciaError(nombre_estructura="Cola", operacion="desencolar")
        return self._elementos.pop(0)

    def frente(self) -> Any:
        """Inspecciona el elemento en el frente de la cola sin removerlo."""
        if not self._elementos:
            raise EstructuraVaciaError(nombre_estructura="Cola", operacion="frente")
        return self._elementos[0]

    def esta_vacia(self) -> bool:
        """Indica si la cola no contiene elementos."""
        return len(self._elementos) == 0

    def tamano(self) -> int:
        """Retorna el numero actual de elementos encolados."""
        return len(self._elementos)

    def vaciar(self) -> None:
        """Descarta la totalidad de los elementos encolados."""
        self._elementos.clear()

    def a_arreglo(self) -> HolocronArray:
        """Convierte la cola en un HolocronArray ordenado desde el frente al final."""
        return HolocronArray(list(self._elementos))

    def __len__(self) -> int:
        return len(self._elementos)

    def __str__(self) -> str:
        if not self._elementos:
            return "<Cola Holocron: [Vacia]>"
        rep = " -> ".join(str(x) for x in self._elementos)
        return f"<Cola Holocron (Frente -> Final): [{rep}]>"

    def __repr__(self) -> str:
        return f"HolocronCola({self._elementos})"


class NodoArbolDecision:
    """
    Nodo de un Arbol de Decision binario implementado desde cero.
    Puede representar una division condicional (nodo interno) o una clasificacion final (hoja).
    """

    def __init__(
        self,
        es_hoja: bool = False,
        atributo: Optional[str] = None,
        indice_atributo: Optional[int] = None,
        umbral: Optional[float] = None,
        rama_izquierda: Optional['NodoArbolDecision'] = None,
        rama_derecha: Optional['NodoArbolDecision'] = None,
        prediccion: Optional[Any] = None,
        muestras: int = 0,
        impureza: float = 0.0
    ):
        self.es_hoja = es_hoja
        self.atributo = atributo
        self.indice_atributo = indice_atributo
        self.umbral = umbral
        self.rama_izquierda = rama_izquierda
        self.rama_derecha = rama_derecha
        self.prediccion = prediccion
        self.muestras = muestras
        self.impureza = impureza

    def predecir(self, muestra: Union[List[float], dict]) -> Any:
        """Recorre el arbol recursivamente para predecir la clase de la muestra."""
        if self.es_hoja:
            return self.prediccion

        if isinstance(muestra, dict):
            val = muestra.get(self.atributo)
        else:
            val = muestra[self.indice_atributo]

        if val is None:
            return self.prediccion

        if float(val) <= float(self.umbral):
            if self.rama_izquierda:
                return self.rama_izquierda.predecir(muestra)
            return self.prediccion
        else:
            if self.rama_derecha:
                return self.rama_derecha.predecir(muestra)
            return self.prediccion

    def a_cadena_jerarquica(self, nivel: int = 0, prefijo: str = "") -> str:
        """Genera una representacion visual jerarquica en texto ASCII del arbol."""
        indent = "    " * nivel
        if self.es_hoja:
            return f"{indent}{prefijo}-> Hoja: Prediccion = {self.prediccion} (Muestras = {self.muestras}, Impureza = {self.impureza:.4f})\n"

        condicion = f"[{self.atributo} <= {self.umbral:.4f}]"
        linea = f"{indent}{prefijo}Decision: {condicion} (Muestras = {self.muestras}, Gini = {self.impureza:.4f})\n"
        if self.rama_izquierda:
            linea += self.rama_izquierda.a_cadena_jerarquica(nivel + 1, "[SI] ")
        if self.rama_derecha:
            linea += self.rama_derecha.a_cadena_jerarquica(nivel + 1, "[NO] ")
        return linea

    def __str__(self) -> str:
        return self.a_cadena_jerarquica()
