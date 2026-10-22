# Tabla de simbolos y administracion de ambitos (Scopes) para HolocronDSL
# Implementa el control semantico de identificadores y visibilidad (Grupo 5)

from enum import Enum, auto
from typing import Dict, Any, Optional, List
from src.errors.semantic_error import VariableNoDefinidaError, MisionNoDefinidaError


class SymbolType(Enum):
    TABLE = auto()
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()
    MISSION = auto()
    ANY = auto()


class Symbol:
    """Descriptor individual de un simbolo almacenado en la tabla."""

    def __init__(
        self,
        nombre: str,
        tipo: SymbolType,
        valor: Any,
        linea: Optional[int] = None,
        columna: Optional[int] = None,
        ambito: str = "global"
    ):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna
        self.ambito = ambito

    def __repr__(self) -> str:
        return f"Symbol({self.nombre}: {self.tipo.name} en [{self.ambito}] = {type(self.valor).__name__})"


class MissionDescriptor:
    """Descriptor para encapsular la definicion de una mision (funcion del DSL)."""

    def __init__(
        self,
        nombre: str,
        parametros: List[str],
        sentencias_ctx: List[Any],
        retorno_ctx: Any,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ):
        self.nombre = nombre
        self.parametros = parametros
        self.sentencias_ctx = sentencias_ctx
        self.retorno_ctx = retorno_ctx
        self.linea = linea
        self.columna = columna


class Scope:
    """Representa un contexto de ejecucion o ambito jerarquico."""

    def __init__(self, nombre: str, padre: Optional["Scope"] = None):
        self.nombre = nombre
        self.padre = padre
        self.simbolos: Dict[str, Symbol] = {}

    def definir(self, simbolo: Symbol):
        self.simbolos[simbolo.nombre] = simbolo

    def resolver_local(self, nombre: str) -> Optional[Symbol]:
        return self.simbolos.get(nombre, None)

    def resolver(self, nombre: str) -> Optional[Symbol]:
        if nombre in self.simbolos:
            return self.simbolos[nombre]
        if self.padre:
            return self.padre.resolver(nombre)
        return None

    def variables_visibles(self) -> List[str]:
        vars_set = set(self.simbolos.keys())
        if self.padre:
            vars_set.update(self.padre.variables_visibles())
        return list(vars_set)


class SymbolTable:
    """
    Tabla de simbolos principal con soporte para ambitos anidados (Global y Funciones).
    """

    def __init__(self):
        self.ambito_global = Scope("global")
        self.ambito_actual = self.ambito_global
        self.misiones: Dict[str, MissionDescriptor] = {}

    def entrar_ambito(self, nombre_mision: str):
        """Crea y desciende a un nuevo ambito local."""
        nuevo_scope = Scope(nombre=nombre_mision, padre=self.ambito_actual)
        self.ambito_actual = nuevo_scope

    def salir_ambito(self):
        """Retorna al ambito padre superior."""
        if self.ambito_actual.padre is not None:
            self.ambito_actual = self.ambito_actual.padre

    def inferir_tipo_simbolo(self, valor: Any) -> SymbolType:
        from src.runtime.holocron_table import HolocronTable, HolocronGroupedTable
        if isinstance(valor, (HolocronTable, HolocronGroupedTable)):
            return SymbolType.TABLE
        elif isinstance(valor, bool):
            return SymbolType.BOOLEAN
        elif isinstance(valor, (int, float)):
            return SymbolType.NUMBER
        elif isinstance(valor, str):
            return SymbolType.STRING
        return SymbolType.ANY

    def definir(
        self,
        nombre: str,
        valor: Any,
        tipo: Optional[SymbolType] = None,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> Symbol:
        """Registra o actualiza una variable en el ambito actual."""
        if tipo is None:
            tipo = self.inferir_tipo_simbolo(valor)

        simbolo = Symbol(
            nombre=nombre,
            tipo=tipo,
            valor=valor,
            linea=linea,
            columna=columna,
            ambito=self.ambito_actual.nombre
        )
        self.ambito_actual.definir(simbolo)
        return simbolo

    def resolver(
        self,
        nombre: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> Symbol:
        """
        Busca un simbolo en el ambito actual y sus ancestros.
        Lanza VariableNoDefinidaError si no existe.
        """
        simbolo = self.ambito_actual.resolver(nombre)
        if simbolo is None:
            vars_disponibles = self.ambito_actual.variables_visibles()
            raise VariableNoDefinidaError(nombre, linea, columna, vars_disponibles)
        return simbolo

    def obtener_valor(
        self,
        nombre: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> Any:
        return self.resolver(nombre, linea, columna).valor

    def existe(self, nombre: str) -> bool:
        return self.ambito_actual.resolver(nombre) is not None

    def registrar_mision(
        self,
        nombre: str,
        parametros: List[str],
        sentencias_ctx: List[Any],
        retorno_ctx: Any,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ):
        """Almacena el descriptor de una mision en la tabla global de funciones."""
        mision = MissionDescriptor(
            nombre=nombre,
            parametros=parametros,
            sentencias_ctx=sentencias_ctx,
            retorno_ctx=retorno_ctx,
            linea=linea,
            columna=columna
        )
        self.misiones[nombre] = mision

    def resolver_mision(
        self,
        nombre: str,
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> MissionDescriptor:
        """Recupera el descriptor de una mision; si no existe lanza MisionNoDefinidaError."""
        if nombre not in self.misiones:
            raise MisionNoDefinidaError(nombre, linea, columna)
        return self.misiones[nombre]

    def reiniciar(self):
        """Reinicia la tabla de simbolos al estado inicial limpio."""
        self.ambito_global = Scope("global")
        self.ambito_actual = self.ambito_global
        self.misiones.clear()
