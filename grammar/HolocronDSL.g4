grammar HolocronDSL;

// =============================================================================
// Gramatica de HolocronDSL
// Lenguaje de Dominio Especifico para Ciencia de Datos y Visualizacion
// Asignatura: Lenguajes de Programacion y Transduccion - Semestre 2026-2
// Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
// =============================================================================

// -----------------------------------------------------------------------------
// REGLAS DEL PARSER (Sintaxis del Lenguaje)
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

// -- Definicion de funciones y abstraccion --
declaracionMision
    : MISION ID CON_PARAMETROS LPAREN listaParametros? RPAREN
        sentencia*
        RETORNAR_ORDEN expresionPipeline
      FIN_MISION
    ;

listaParametros
    : ID (COMMA ID)*
    ;

// -- Asignacion y encadenamiento (Pipelines) --
sentenciaAsignacion
    : CANALIZAR? ID ASIGNAR expresionPipeline
    ;

expresionPipeline
    : expresionBase (FLECHA_PIPELINE operacionPipeline)*
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

// -- Operaciones dentro del flujo de transformacion --
operacionPipeline
    : operacionSeleccionar
    | operacionFiltrar
    | operacionForjar
    | operacionAlinear
    | operacionEliminarClones
    | operacionSanarVacios
    | operacionAgrupar
    | operacionSintetizar
    ;

operacionSeleccionar
    : REVELAR_SECTORES LBRACK listaIdentificadores RBRACK
    ;

operacionFiltrar
    : PURGAR_DONDE expresionBooleana
    ;

operacionForjar
    : FORJAR_CRISTAL ID OP_FORJAR expresionAritmetica
    ;

operacionAlinear
    : ALINEAR_FLOTA ID ordenDireccion?
    ;

ordenDireccion
    : ORDEN_ASCENDENTE
    | ORDEN_DESCENDENTE
    ;

operacionEliminarClones
    : ELIMINAR_CLONES
    ;

operacionSanarVacios
    : SANAR_VACIOS opcionSanado
    ;

opcionSanado
    : DESCARTAR
    | SUSTITUIR_CON literal
    ;

operacionAgrupar
    : AGRUPAR_SECTOR LBRACK listaIdentificadores RBRACK
    ;

operacionSintetizar
    : SINTETIZAR_INDICADORES LBRACK listaAsignacionesAgregacion RBRACK
    ;

listaAsignacionesAgregacion
    : asignacionAgregacion (COMMA asignacionAgregacion)*
    ;

asignacionAgregacion
    : ID OP_FORJAR llamadaAgregacion
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

// -- Persistencia de datos --
sentenciaArchivado
    : ARCHIVAR_HOLOCRON ID EN CADENA (DELIMITADO_POR CADENA)?
    ;

// -- Proyeccion holografica (Visualizaciones) --
sentenciaHolograma
    : PROYECTAR_HOLOGRAMA tipoGrafica DESDE ID
        propiedadHolograma*
      FIN_HOLOGRAMA
    ;

tipoGrafica
    : TIPO_BARRAS
    | TIPO_LINEAS
    | TIPO_DISPERSION
    | TIPO_HISTOGRAMA
    | TIPO_CAJA
    ;

propiedadHolograma
    : EJE_X OP_FORJAR CADENA
    | EJE_Y OP_FORJAR CADENA
    | HOLOTITULO OP_FORJAR CADENA
    | GUARDAR_PROYECCION OP_FORJAR CADENA
    ;

// -- Condicional galactico --
sentenciaCondicional
    : EVALUAR_FUERZA LPAREN expresionBooleana RPAREN
      SENDA_LUMINOSA
        sentencia*
      (SENDA_OSCURA
        sentencia*)?
      FIN_EVALUAR
    ;

// -- Transmision de mensajes por consola --
sentenciaTransmision
    : TRANSMITIR_MENSAJE expresionPipeline
    ;

// -- Expresiones booleanas y logicas --
expresionBooleana
    : expresionBooleana O_FUERZA terminoBooleano     # ExprBoolOr
    | terminoBooleano                                 # ExprBoolTermino
    ;

terminoBooleano
    : terminoBooleano Y_FUERZA factorBooleano        # ExprBoolAnd
    | factorBooleano                                  # ExprBoolFactor
    ;

factorBooleano
    : NO_FUERZA factorBooleano                        # ExprBoolNot
    | comparacionRelacional                           # ExprBoolComparacion
    | LPAREN expresionBooleana RPAREN                 # ExprBoolParentesis
    | BOOL                                            # ExprBoolLiteral
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
// REGLAS DEL LEXER (Tokens y Terminales)
// -----------------------------------------------------------------------------

// -- Palabras reservadas: Flujo y funciones --
MISION                  : 'mision';
CON_PARAMETROS          : 'con_parametros';
RETORNAR_ORDEN          : 'retornar_orden';
FIN_MISION              : 'fin_mision';

// -- Palabras reservadas: Ingestion y persistencia --
ABRIR_HOLOCRON          : 'abrir_holocron';
DELIMITADO_POR          : 'delimitado_por';
ARCHIVAR_HOLOCRON       : 'archivar_holocron';
EN                      : 'en';
CANALIZAR               : 'canalizar';

// -- Palabras reservadas: Transformacion de datos --
REVELAR_SECTORES        : 'revelar_sectores';
PURGAR_DONDE            : 'purgar_donde';
FORJAR_CRISTAL          : 'forjar_cristal';
ALINEAR_FLOTA           : 'alinear_flota';
ORDEN_ASCENDENTE        : 'orden_ascendente';
ORDEN_DESCENDENTE       : 'orden_descendente';
ELIMINAR_CLONES         : 'eliminar_clones';
SANAR_VACIOS            : 'sanar_vacios';
DESCARTAR               : 'descartar';
SUSTITUIR_CON           : 'sustituir_con';
AGRUPAR_SECTOR          : 'agrupar_sector';
SINTETIZAR_INDICADORES  : 'sintetizar_indicadores';

// -- Funciones de agregacion descriptiva --
FUNC_RECUENTO           : 'recuento';
FUNC_ACUMULAR           : 'acumular';
FUNC_EQUILIBRIO         : 'equilibrio';
FUNC_MEDIANA            : 'mediana';
FUNC_CENIT              : 'cenit';
FUNC_NADIR              : 'nadir';
FUNC_DESVIACION        : 'desviacion';

// -- Palabras reservadas: Proyeccion holografica --
PROYECTAR_HOLOGRAMA     : 'proyectar_holograma';
DESDE                   : 'desde';
FIN_HOLOGRAMA           : 'fin_holograma';
TIPO_BARRAS             : 'barras';
TIPO_LINEAS             : 'lineas';
TIPO_DISPERSION         : 'dispersion';
TIPO_HISTOGRAMA         : 'histograma';
TIPO_CAJA               : 'caja';
EJE_X                   : 'eje_x';
EJE_Y                   : 'eje_y';
HOLOTITULO              : 'holotitulo';
GUARDAR_PROYECCION      : 'guardar_proyeccion';

// -- Palabras reservadas: Control y transmision --
EVALUAR_FUERZA          : 'evaluar_fuerza';
SENDA_LUMINOSA          : 'senda_luminosa';
SENDA_OSCURA            : 'senda_oscura';
FIN_EVALUAR             : 'fin_evaluar';
TRANSMITIR_MENSAJE      : 'transmitir_mensaje';

// -- Conectores logicos de la Fuerza --
Y_FUERZA                : 'y_fuerza';
O_FUERZA                : 'o_fuerza';
NO_FUERZA               : 'no_fuerza';

// -- Operador de pipeline --
FLECHA_PIPELINE         : '==>';

// -- Operadores de asignacion --
ASIGNAR                 : '<-';
OP_FORJAR               : ':=';

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

// -- Delimitadores y signos de puntuacion --
LPAREN                  : '(';
RPAREN                  : ')';
LBRACK                  : '[';
RBRACK                  : ']';
COMMA                   : ',';

// -- Literales booleanos --
BOOL                    : 'cierto_es' | 'falso_es';

// -- Literales numericos: decimales y enteros --
NUMERO                  : [0-9]+ ('.' [0-9]+)?;

// -- Literales de texto (cadenas entre comillas dobles) --
CADENA                  : '"' (~["\r\n])* '"';

// -- Identificadores galacticos --
ID                      : [a-zA-Z_][a-zA-Z0-9_]*;

// -- Comentarios galacticos --
// Comentario de una sola linea con doble guion
COMENTARIO_LINEA        : '--' ~[\r\n]* -> skip;

// Comentario de bloque
COMENTARIO_BLOQUE       : '/-' .*? '-/' -> skip;

// -- Espacios en blanco ignorados --
WS                      : [ \t\r\n]+ -> skip;
