grammar HolocronDSL;

// =============================================================================
// Gramatica de HolocronDSL (Version Simplificada e Intuitiva)
// Lenguaje de Dominio Especifico para Ciencia de Datos y Visualizacion
// Asignatura: Lenguajes de Programacion y Transduccion - Semestre 2026-2
// Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
// =============================================================================

// -----------------------------------------------------------------------------
// REGLAS DEL PARSER (Sintaxis Simplificada)
// -----------------------------------------------------------------------------

programa
    : sentencia* EOF
    ;

sentencia
    : declaracionMision
    | sentenciaAsignacion
    | sentenciaArchivado
    | sentenciaHolograma
    | sentenciaCondicional
    | sentenciaTransmision
    ;

// -- Definicion de funciones (Misiones) --
declaracionMision
    : MISION ID LPAREN listaParametros? RPAREN
        sentencia*
        RETORNAR expresionPipeline
      FIN_MISION
    ;

listaParametros
    : ID (COMMA ID)*
    ;

// -- Asignacion simple y Pipelines --
sentenciaAsignacion
    : ID OP_ASIG expresionPipeline
    ;

expresionPipeline
    : expresionBase (PIPE operacionPipeline)*
    ;

expresionBase
    : instruccionCarga
    | llamadaMision
    | expresionAritmetica
    ;

instruccionCarga
    : ABRIR_HOLOCRON CADENA (DELIMITADO_POR CADENA)?
    ;

llamadaMision
    : ID LPAREN (expresionPipeline (COMMA expresionPipeline)*)? RPAREN
    ;

// -- Operaciones dentro del pipeline --
operacionPipeline
    : operacionSeleccionar
    | operacionFiltrar
    | operacionForjar
    | operacionOrdenar
    | operacionEliminarClones
    | operacionSanarVacios
    | operacionAgrupar
    | operacionResumir
    ;

operacionSeleccionar
    : REVELAR listaIdentificadoresOpcional
    ;

listaIdentificadoresOpcional
    : LBRACK listaIdentificadores RBRACK
    | listaIdentificadores
    ;

operacionFiltrar
    : PURGAR DONDE? expresionBooleana
    ;

operacionForjar
    : FORJAR ID OP_ASIG expresionAritmetica
    ;

operacionOrdenar
    : ORDENAR POR? ID ordenDireccion?
    ;

ordenDireccion
    : ASCENDENTE
    | DESCENDENTE
    ;

operacionEliminarClones
    : ELIMINAR_CLONES
    ;

operacionSanarVacios
    : SANAR_VACIOS opcionSanado
    ;

opcionSanado
    : DESCARTAR
    | CON literal
    ;

operacionAgrupar
    : AGRUPAR POR? listaIdentificadoresOpcional
    ;

operacionResumir
    : RESUMIR listaAsignacionesAgregacion
    ;

listaAsignacionesAgregacion
    : LBRACK asignacionAgregacion (COMMA asignacionAgregacion)* RBRACK
    | asignacionAgregacion (COMMA asignacionAgregacion)*
    ;

asignacionAgregacion
    : ID OP_ASIG llamadaAgregacion
    ;

llamadaAgregacion
    : FUNC_RECUENTO LPAREN RPAREN
    | FUNC_ACUMULAR LPAREN ID RPAREN
    | FUNC_EQUILIBRIO LPAREN ID RPAREN
    | FUNC_MEDIANA LPAREN ID RPAREN
    | FUNC_CENIT LPAREN ID RPAREN
    | FUNC_NADIR LPAREN ID RPAREN
    | FUNC_DESVIACION LPAREN ID RPAREN
    ;

// -- Persistencia de datos en disco --
sentenciaArchivado
    : ARCHIVAR_HOLOCRON ID EN CADENA (DELIMITADO_POR CADENA)?
    ;

// -- Proyeccion holografica (Graficos) --
sentenciaHolograma
    : HOLOGRAMA tipoGrafica ID
        propiedadHolograma*
      FIN_HOLOGRAMA?
    ;

tipoGrafica
    : TIPO_BARRAS
    | TIPO_LINEAS
    | TIPO_DISPERSION
    | TIPO_HISTOGRAMA
    | TIPO_CAJA
    ;

propiedadHolograma
    : EJE_X CADENA
    | EJE_Y CADENA
    | TITULO CADENA
    | GUARDAR CADENA
    ;

// -- Condicional de la Fuerza --
sentenciaCondicional
    : EVALUAR_FUERZA expresionBooleana
      SENDA_LUMINOSA
        sentencia*
      (SENDA_OSCURA
        sentencia*)?
      FIN_EVALUAR
    ;

// -- Mostrar mensajes o telemetria en consola --
sentenciaTransmision
    : (TRANSMITIR | MOSTRAR) expresionPipeline
    ;

// -- Expresiones booleanas y logicas --
expresionBooleana
    : expresionBooleana (O_LOGICO | O_FUERZA) terminoBooleano     # ExprBoolOr
    | terminoBooleano                                             # ExprBoolTermino
    ;

terminoBooleano
    : terminoBooleano (Y_LOGICO | Y_FUERZA) factorBooleano        # ExprBoolAnd
    | factorBooleano                                              # ExprBoolFactor
    ;

factorBooleano
    : (NO_LOGICO | NO_FUERZA) factorBooleano                      # ExprBoolNot
    | comparacionRelacional                                       # ExprBoolComparacion
    | LPAREN expresionBooleana RPAREN                             # ExprBoolParentesis
    | BOOL                                                        # ExprBoolLiteral
    ;

comparacionRelacional
    : expresionAritmetica operadorRelacional expresionAritmetica
    ;

operadorRelacional
    : OP_IGUAL
    | OP_DIFERENTE
    | OP_MENOR_IGUAL
    | OP_MAYOR_IGUAL
    | OP_MENOR
    | OP_MAYOR
    ;

// -- Expresiones aritmeticas --
expresionAritmetica
    : expresionAritmetica (OP_SUMA | OP_RESTA) terminoAritmetico   # ExprAritSumaResta
    | terminoAritmetico                                             # ExprAritTermino
    ;

terminoAritmetico
    : terminoAritmetico (OP_MULT | OP_DIV | OP_MOD) factorPotencia # ExprAritMultDiv
    | factorPotencia                                               # ExprAritFactor
    ;

factorPotencia
    : atomoAritmetico (OP_POTENCIA factorPotencia)?                 # ExprAritPotencia
    ;

atomoAritmetico
    : NUMERO                                                        # AtomoNumero
    | CADENA                                                        # AtomoCadena
    | BOOL                                                          # AtomoBooleano
    | ID                                                            # AtomoIdentificador
    | LPAREN expresionAritmetica RPAREN                            # AtomoParentesis
    ;

listaIdentificadores
    : ID (COMMA ID)*
    ;

literal
    : NUMERO
    | CADENA
    | BOOL
    ;


// -----------------------------------------------------------------------------
// REGLAS DEL LEXER (Tokens y Terminales Simplificados)
// -----------------------------------------------------------------------------

// -- Palabras reservadas: Modulos y funciones --
MISION                  : 'mision';
RETORNAR                : 'retornar' | 'retornar_orden';
FIN_MISION              : 'fin_mision';

// -- Palabras reservadas: Ingestion y persistencia --
ABRIR_HOLOCRON          : 'abrir_holocron' | 'cargar_holocron';
DELIMITADO_POR          : 'delimitado_por' | 'separador';
ARCHIVAR_HOLOCRON       : 'archivar_holocron' | 'guardar_holocron';
EN                      : 'en';

// -- Palabras reservadas: Transformacion de datos --
REVELAR                 : 'revelar' | 'revelar_sectores' | 'seleccionar';
PURGAR                  : 'purgar' | 'purgar_donde' | 'filtrar';
DONDE                   : 'donde';
FORJAR                  : 'forjar' | 'forjar_cristal' | 'crear';
ORDENAR                 : 'ordenar' | 'alinear_flota';
POR                     : 'por';
ASCENDENTE              : 'ascendente' | 'orden_ascendente';
DESCENDENTE             : 'descendente' | 'orden_descendente';
ELIMINAR_CLONES         : 'eliminar_clones';
SANAR_VACIOS            : 'sanar_vacios';
DESCARTAR               : 'descartar';
CON                     : 'con' | 'sustituir_con';
AGRUPAR                 : 'agrupar' | 'agrupar_sector';
RESUMIR                 : 'resumir' | 'sintetizar' | 'sintetizar_indicadores';

// -- Funciones de agregacion estadistica --
FUNC_RECUENTO           : 'recuento' | 'conteo';
FUNC_ACUMULAR           : 'acumular' | 'suma';
FUNC_EQUILIBRIO         : 'equilibrio' | 'promedio' | 'media';
FUNC_MEDIANA            : 'mediana';
FUNC_CENIT              : 'cenit' | 'maximo';
FUNC_NADIR              : 'nadir' | 'minimo';
FUNC_DESVIACION         : 'desviacion';

// -- Palabras reservadas: Visualizaciones --
HOLOGRAMA               : 'holograma' | 'proyectar_holograma' | 'graficar';
FIN_HOLOGRAMA           : 'fin_holograma';
TIPO_BARRAS             : 'barras';
TIPO_LINEAS             : 'lineas';
TIPO_DISPERSION         : 'dispersion';
TIPO_HISTOGRAMA         : 'histograma';
TIPO_CAJA               : 'caja' | 'cajas';
EJE_X                   : 'eje_x';
EJE_Y                   : 'eje_y';
TITULO                  : 'titulo' | 'holotitulo';
GUARDAR                 : 'guardar' | 'guardar_proyeccion';

// -- Control de flujo y transmision --
EVALUAR_FUERZA          : 'evaluar_fuerza' | 'si' | 'si_fuerza';
SENDA_LUMINOSA          : 'senda_luminosa' | 'entonces';
SENDA_OSCURA            : 'senda_oscura' | 'sino';
FIN_EVALUAR             : 'fin_evaluar' | 'fin_si';
TRANSMITIR              : 'transmitir' | 'transmitir_mensaje';
MOSTRAR                 : 'mostrar';

// -- Conectores logicos simples y galacticos --
Y_LOGICO                : 'y';
Y_FUERZA                : 'y_fuerza';
O_LOGICO                : 'o';
O_FUERZA                : 'o_fuerza';
NO_LOGICO               : 'no';
NO_FUERZA               : 'no_fuerza';

// -- Conector de pipeline intuitivo: '|>' o '>>' --
PIPE                    : '|>' | '>>';

// -- Operador de asignacion estandar --
OP_ASIG                 : '=';

// -- Operadores relacionales --
OP_IGUAL                : '==';
OP_DIFERENTE            : '!=';
OP_MENOR_IGUAL          : '<=';
OP_MAYOR_IGUAL          : '>=';
OP_MENOR                : '<';
OP_MAYOR                : '>';

// -- Operadores aritmeticos --
OP_SUMA                 : '+';
OP_RESTA                : '-';
OP_MULT                 : '*';
OP_DIV                  : '/';
OP_MOD                  : '%';
OP_POTENCIA             : '^';

// -- Delimitadores --
LPAREN                  : '(';
RPAREN                  : ')';
LBRACK                  : '[';
RBRACK                  : ']';
COMMA                   : ',';

// -- Literales booleanos --
BOOL                    : 'cierto_es' | 'falso_es' | 'verdadero' | 'falso';

// -- Literales numericos --
NUMERO                  : [0-9]+ ('.' [0-9]+)?;

// -- Literales de cadena (comillas dobles y simples) --
CADENA                  : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'';

// -- Identificadores --
ID                      : [a-zA-Z_][a-zA-Z0-9_]*;

// -- Comentarios (linea con --, # o //; bloque con /- -/ o /* */) --
COMENTARIO_LINEA        : ('--' | '#' | '//') ~[\r\n]* -> skip;
COMENTARIO_BLOQUE       : ('/-' .*? '-/' | '/*' .*? '*/') -> skip;

// -- Espacios en blanco --
WS                      : [ \t\r\n]+ -> skip;
