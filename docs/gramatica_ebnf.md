# Especificacion Formal de la Gramatica en EBNF: HolocronDSL

**Universidad Sergio Arboleda**  
**Lenguajes de Programacion y Transduccion (2026-2)**  
**Grupo 5:** Andres Sebastian Coral Vallejo, Carol Arenas Cardona  

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
    = 'mision' ID '(' [ ListaParametros ] ')'
      { Sentencia }
      'retornar' ExpresionPipeline
      'fin_mision' ;

ListaParametros
    = ID { ',' ID } ;

SentenciaAsignacion
    = ID '=' ExpresionPipeline ;

ExpresionPipeline
    = ExpresionBase { '|>' OperacionPipeline } ;

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
    | OperacionOrdenar
    | OperacionEliminarClones
    | OperacionSanarVacios
    | OperacionAgrupar
    | OperacionResumir ;

OperacionSeleccionar
    = 'revelar' ( '[' ListaIdentificadores ']' | ListaIdentificadores ) ;

OperacionFiltrar
    = 'purgar' [ 'donde' ] ExpresionBooleana ;

OperacionForjar
    = 'forjar' ID '=' ExpresionAritmetica ;

OperacionOrdenar
    = 'ordenar' [ 'por' ] ID [ 'ascendente' | 'descendente' ] ;

OperacionEliminarClones
    = 'eliminar_clones' ;

OperacionSanarVacios
    = 'sanar_vacios' ( 'descartar' | 'con' Literal ) ;

OperacionAgrupar
    = 'agrupar' [ 'por' ] ( '[' ListaIdentificadores ']' | ListaIdentificadores ) ;

OperacionResumir
    = 'resumir' ( '[' AsignacionAgregacion { ',' AsignacionAgregacion } ']'
                | AsignacionAgregacion { ',' AsignacionAgregacion } ) ;

AsignacionAgregacion
    = ID '=' LlamadaAgregacion ;

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
    = 'holograma' TipoGrafica ID
      { PropiedadHolograma }
      [ 'fin_holograma' ] ;

TipoGrafica
    = 'barras' | 'lineas' | 'dispersion' | 'histograma' | 'caja' ;

PropiedadHolograma
    = ( 'eje_x' | 'eje_y' | 'titulo' | 'guardar' ) CADENA ;

SentenciaCondicional
    = 'evaluar_fuerza' ExpresionBooleana
      'senda_luminosa'
          { Sentencia }
      [ 'senda_oscura'
          { Sentencia } ]
      'fin_evaluar' ;

SentenciaTransmision
    = ( 'mostrar' | 'transmitir' ) ExpresionPipeline ;

ExpresionBooleana
    = TerminoBooleano { ( 'o' | 'o_fuerza' ) TerminoBooleano } ;

TerminoBooleano
    = FactorBooleano { ( 'y' | 'y_fuerza' ) FactorBooleano } ;

FactorBooleano
    = ( 'no' | 'no_fuerza' ) FactorBooleano
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
    = NUMERO | CADENA | BOOL | ID | '(' ExpresionAritmetica ')' ;

ListaIdentificadores
    = ID { ',' ID } ;

Literal
    = NUMERO | CADENA | BOOL ;
```
