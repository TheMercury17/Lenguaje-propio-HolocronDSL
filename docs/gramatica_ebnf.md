# Especificacion Formal de la Gramatica en EBNF: HolocronDSL

**Universidad Sergio Arboleda**  
**Lenguajes de Programacion y Transduccion (2026-2)**  
**Grupo 5:** Andres Sebastian Coral Vallejo, Carol Arenas Cardona  

La siguiente especificacion utiliza la notacion estandar EBNF (Extended Backus-Naur Form):
- `{ A }` denota cero o mas repeticiones de `A`.
- `[ A ]` denota cero o una aparicion opcional de `A`.
- `( A | B )` denota seleccion alternativa.
- Los simbolos terminales se encierran entre comillas simples `'...'` o se especifican en mayusculas.

---

## 1. Reglas Sintacticas (No Terminales)

```ebnf
Programa
    = { Sentencia } EOF ;

Sentencia
    = DeclaracionMision
    | SentenciaAsignacion
    | SentenciaArchivado
    | SentenciaHolograma
    | SentenciaCondicional
    | SentenciaTransmision ;

DeclaracionMision
    = 'mision' ID 'con_parametros' '(' [ ListaParametros ] ')'
      { Sentencia }
      'retornar_orden' ExpresionPipeline
      'fin_mision' ;

ListaParametros
    = ID { ',' ID } ;

SentenciaAsignacion
    = [ 'canalizar' ] ID '<-' ExpresionPipeline ;

ExpresionPipeline
    = ExpresionBase { '==>' OperacionPipeline } ;

ExpresionBase
    = InstruccionCarga
    | LlamadaMision
    | ExpresionAritmetica ;

InstruccionCarga
    = 'abrir_holocron' CADENA [ 'delimitado_por' CADENA ] ;

LlamadaMision
    = ID '(' [ ExpresionPipeline { ',' ExpresionPipeline } ] ')' ;

OperacionPipeline
    = OperacionSeleccionar
    | OperacionFiltrar
    | OperacionForjar
    | OperacionAlinear
    | OperacionEliminarClones
    | OperacionSanarVacios
    | OperacionAgrupar
    | OperacionSintetizar ;

OperacionSeleccionar
    = 'revelar_sectores' '[' ListaIdentificadores ']' ;

OperacionFiltrar
    = 'purgar_donde' ExpresionBooleana ;

OperacionForjar
    = 'forjar_cristal' ID ':=' ExpresionAritmetica ;

OperacionAlinear
    = 'alinear_flota' ID [ 'orden_ascendente' | 'orden_descendente' ] ;

OperacionEliminarClones
    = 'eliminar_clones' ;

OperacionSanarVacios
    = 'sanar_vacios' ( 'descartar' | 'sustituir_con' Literal ) ;

OperacionAgrupar
    = 'agrupar_sector' '[' ListaIdentificadores ']' ;

OperacionSintetizar
    = 'sintetizar_indicadores' '[' AsignacionAgregacion { ',' AsignacionAgregacion } ']' ;

AsignacionAgregacion
    = ID ':=' LlamadaAgregacion ;

LlamadaAgregacion
    = 'recuento' '(' ')'
    | 'acumular' '(' ID ')'
    | 'equilibrio' '(' ID ')'
    | 'mediana' '(' ID ')'
    | 'cenit' '(' ID ')'
    | 'nadir' '(' ID ')'
    | 'desviacion' '(' ID ')' ;

SentenciaArchivado
    = 'archivar_holocron' ID 'en' CADENA [ 'delimitado_por' CADENA ] ;

SentenciaHolograma
    = 'proyectar_holograma' TipoGrafica 'desde' ID
      { PropiedadHolograma }
      'fin_holograma' ;

TipoGrafica
    = 'barras' | 'lineas' | 'dispersion' | 'histograma' | 'caja' ;

PropiedadHolograma
    = ( 'eje_x' | 'eje_y' | 'holotitulo' | 'guardar_proyeccion' ) ':=' CADENA ;

SentenciaCondicional
    = 'evaluar_fuerza' '(' ExpresionBooleana ')'
      'senda_luminosa'
          { Sentencia }
      [ 'senda_oscura'
          { Sentencia } ]
      'fin_evaluar' ;

SentenciaTransmision
    = 'transmitir_mensaje' ExpresionPipeline ;

ExpresionBooleana
    = TerminoBooleano { 'o_fuerza' TerminoBooleano } ;

TerminoBooleano
    = FactorBooleano { 'y_fuerza' FactorBooleano } ;

FactorBooleano
    = 'no_fuerza' FactorBooleano
    | ComparacionRelacional
    | '(' ExpresionBooleana ')'
    | BOOL ;

ComparacionRelacional
    = ExpresionAritmetica OperadorRelacional ExpresionAritmetica ;

OperadorRelacional
    = '==' | '!=' | '<=' | '>=' | '<' | '>' ;

ExpresionAritmetica
    = TerminoAritmetico { ( '+' | '-' ) TerminoAritmetico } ;

TerminoAritmetico
    = FactorPotencia { ( '*' | '/' | '%' ) FactorPotencia } ;

FactorPotencia
    = AtomoAritmetico [ '^' FactorPotencia ] ;

AtomoAritmetico
    = NUMERO
    | CADENA
    | BOOL
    | ID
    | '(' ExpresionAritmetica ')' ;

ListaIdentificadores
    = ID { ',' ID } ;

Literal
    = NUMERO | CADENA | BOOL ;
```

---

## 2. Reglas Lexicas (Terminales)

```ebnf
BOOL              = 'cierto_es' | 'falso_es' ;
NUMERO            = DIGITO { DIGITO } [ '.' DIGITO { DIGITO } ] ;
CADENA            = '"' { CARACTER_CADENA } '"' ;
ID                = ( LETRA | '_' ) { LETRA | DIGITO | '_' } ;

DIGITO            = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;
LETRA             = 'a'..'z' | 'A'..'Z' ;
COMENTARIO_LINEA  = '--' { CARACTER_SIN_SALTO } ( '\r' | '\n' ) ;
COMENTARIO_BLOQUE = '/-' { CUALQUIER_CARACTER } '-/' ;
ESPACIOS          = { ' ' | '\t' | '\r' | '\n' } ;
```
