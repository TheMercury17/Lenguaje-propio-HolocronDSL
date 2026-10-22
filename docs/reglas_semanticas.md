# Especificacion Semantica y Motores Propios de HolocronDSL

**Universidad Sergio Arboleda**  
**Programa de Ciencias de la Computacion e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programacion y Transduccion  
**Periodo Academico:** Semestre 2026-2  
**Docente:** Joaquin F. Sanchez  

### Equipo de Desarrollo (Grupo 5)
- **Andres Sebastian Coral Vallejo**
- **Carol Arenas Cardona**

---

## 1. Alcance de la Fase 2 (Segundo Corte)

El segundo corte del proyecto tiene como objetivo la implementacion semantica formal y la ejecucion reproducible de flujos de datos mediante el patron **Visitor**, la **tabla de simbolos** y el desarrollo de **bibliotecas propias e independientes** para matematicas, lectura/escritura de archivos y manipulacion tabular inmutable, produciendo salidas verificables en CSV e imagenes PNG (sin el uso de formato SVG).

---

## 2. Bibliotecas Propias del Lenguaje

Para garantizar originalidad absoluta y evitar dependencias de caja negra, HolocronDSL opera sobre una suite de bibliotecas disenadas internamente en el subpaquete `src/runtime/`:

### 2.1. Motor de I/O de Archivos (`HolocronIO`)
Ubicacion: `src/runtime/io_engine.py`

- **Lectura de Archivos Tabulares (`leer_csv`):**
  - Implementa un analizador sintactico caracter a caracter con soporte para delimitadores configurables (`,`, `;`, `\t`, `|`).
  - Reconoce y respeta campos entrecomillados con comas internas o saltos de linea.
  - Inferencia automatica de tipos atomicos:
    - Literales galacticos booleanos: `cierto_es` / `verdadero` -> `True`, `falso_es` / `falso` -> `False`.
    - Literales nulos: `nulo`, `null`, `nan`, vacios -> `None`.
    - Numericos enteros (`int`) y de punto flotante (`float`).
    - Cadenas de texto limpias (`str`).
- **Escritura y Persistencia (`escribir_csv`):**
  - Serializa tablas a disco formateando valores nulos, booleanos galacticos y aplicando entrecomillado inteligente cuando el campo contiene el delimitador.
  - Asegura la creacion automatica de directorios destino (`salidas/`).

### 2.2. Motor Matematico y Estadistico (`HolocronMath`)
Ubicacion: `src/runtime/math_engine.py`

- Algoritmos estadisticos descriptivos propios:
  - **`suma` (`acumular`):** Sumatoria de valores numericos ignorando observaciones nulas.
  - **`promedio` (`equilibrio` / `media`):** Media aritmetica $\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$.
  - **`mediana`:** Punto medio de la distribucion ordenada; interpola la media de los dos valores centrales si $n$ es par.
  - **`maximo` (`cenit`):** Determinacion del valor maximo.
  - **`minimo` (`nadir`):** Determinacion del valor minimo.
  - **`conteo` (`recuento`):** Cardinalidad de registros validos no nulos.
  - **`varianza` y `desviacion`:** Varianza y desviacion estandar muestral ($s = \sqrt{\frac{1}{n-1}\sum (x_i - \bar{x})^2}$) y poblacional.
  - Operaciones aritmeticas seguras con deteccion de division y modulo entre cero.

### 2.3. Estructura de Datos Tabular (`HolocronTable` y `HolocronGroupedTable`)
Ubicacion: `src/runtime/holocron_table.py`

- **Inmutabilidad y Enfoque Funcional:**
  Cada operacion del pipeline hiperespacial (`|>`) no muta el conjunto de datos de origen, sino que proyecta y retorna una nueva instancia de `HolocronTable`.
- **Operaciones Nativas:**
  - `seleccionar(columnas)`: Filtra y preserva unicamente los atributos solicitados, validando previamente su existencia en el esquema.
  - `purgar(predicado)`: Aplica una funcion booleana de filtrado sobre cada fila.
  - `forjar(nueva_columna, expresion)`: Computa y agrega una nueva dimension derivada.
  - `ordenar(columna, ascendente)`: Ordenamiento robusto de registros con manejo de nulos y tipos heterogeneos.
  - `eliminar_clones()`: Deduplicacion deterministica preservando el orden original.
  - `sanar_vacios(opcion, valor_sustituto)`: Eliminacion de filas incompletas (`descartar`) o imputacion de valores (`con <valor>`).
  - `agrupar(columnas)`: Particiona la tabla en grupos categoricos indexados por tuplas clave.
  - `resumir(agregaciones)`: Reduce grupos a metricas escalares mediante `HolocronMath`.

### 2.4. Motor Grafico Holografico (`HolocronPlotter`)
Ubicacion: `src/runtime/graphics_engine.py`

- **Cumplimiento Estricto de Restricciones:**
  - **No utiliza formato SVG bajo ninguna circunstancia.**
  - Genera exclusivamente archivos de imagen rasterizados en formato **PNG** de alta definicion (300 DPI).
- **Estetica Galactica de Alto Contraste:**
  - Fondo espacial oscuro (`#090D16`), rejilla tactica sutil (`#1E293B`) y paleta de rayos laser (Cian `#00F0FF`, Ambar `#FFE81F`, Plasma Rojo `#FF2A55`, Esmeralda `#10B981`).
- **Tipos de Graficas Soportadas:**
  - `barras`: Comparacion categorica entre grupos.
  - `lineas`: Tendencias continuas o temporales con marcadores.
  - `dispersion`: Correlacion bidimensional de puntos.
  - `histograma`: Distribucion de frecuencias por intervalos.
  - `caja`: Diagrama de dispersion, cuartiles y atipicos.

---

## 3. Tabla de Simbolos y Gestion de Ambitos (Scopes)

Ubicacion: `src/interpreter/symbol_table.py`

### 3.1. Tipos de Simbolos
El sistema clasifica las entidades registradas en:
- `TABLE`: Instancia de `HolocronTable` o `HolocronGroupedTable`.
- `NUMBER`: Entero o decimal (`int` / `float`).
- `STRING`: Cadena de texto (`str`).
- `BOOLEAN`: Valor booleano (`True` / `False`).
- `MISSION`: Descriptor de subrutina con parametros formales y sentencias.

### 3.2. Jerarquia de Ambitos
- **Ambito Global (`global`):** Almacena variables de nivel superior (datasets cargados, transformados y constantes).
- **Ambitos Locales (`mision <nombre>`):** Al invocar una mision con `ID(args...)`, se crea un ambito hijo que enlaza los argumentos con los parametros formales. Al finalizar la mision, se destruye el ambito local y se retorna el resultado al llamador.
- **Sombreado de Variables (Shadowing):** Un parametro o variable local puede coexistir con una variable global del mismo nombre sin alterar el valor exterior.

---

## 4. Reglas Semanticas y Verificacion en Tiempo de Ejecucion

| Codigo de Regla | Descripcion de la Regla Semantica | Accion ante Incumplimiento |
| :--- | :--- | :--- |
| **SEM-01** | Toda variable referenciada debe haber sido asignada previamente en el ambito actual o en sus ancestros. | Lanza `VariableNoDefinidaError` indicando variables registradas. |
| **SEM-02** | Toda columna utilizada en `revelar`, `purgar`, `forjar`, `ordenar`, `agrupar`, `resumir` o `holograma` debe existir en el holocron activo. | Lanza `ColumnaInexistenteError` listando las columnas disponibles. |
| **SEM-03** | Los operandos de expresiones aritmeticas (`+`, `-`, `*`, `/`, `%`, `^`) deben ser de tipo numerico (`int` o `float`), con excepcion de la concatenacion de cadenas en `+`. | Lanza `TipoIncompatibleError`. |
| **SEM-04** | El divisor en operaciones de division (`/`) o modulo (`%`) no puede ser numericamente igual a cero. | Lanza `DivisionPorCeroError`. |
| **SEM-05** | La invocacion de una mision debe corresponder a un nombre registrado previamente en la tabla de misiones. | Lanza `MisionNoDefinidaError`. |
| **SEM-06** | El numero de argumentos suministrados en una llamada a mision debe coincidir exactamente con la cantidad de parametros formales. | Lanza `AridadInvalidaError`. |
| **SEM-07** | Las operaciones de pipeline (`|>`) solo pueden encadenarse sobre objetos de tipo holocron (`HolocronTable`). | Lanza `OperacionInvalidaError`. |
| **SEM-08** | Toda ruta indicada en `abrir_holocron` debe corresponder a un archivo existente y legible en disco. | Lanza `ArchivoNoEncontradoError`. |
| **SEM-09** | Las sentencias `holograma` deben especificar extension `.png` (el uso de `.svg` esta expresamente prohibido). | Lanza `HolocronSemanticError`. |

---

## 5. Arquitectura del Interprete Visitor

Ubicacion: `src/interpreter/visitor.py`

El interprete `HolocronInterpreter` hereda de `HolocronDSLVisitor`:
```text
                  +-----------------------------------+
                  |         Programa Fuente           |
                  +-----------------------------------+
                                    |
                                    v
                  +-----------------------------------+
                  |     ANTLR4 Lexer & Parser         |
                  +-----------------------------------+
                                    |
                                    v
                  +-----------------------------------+
                  |    Arbol Sintactico Concreto      |
                  +-----------------------------------+
                                    |
                                    v
                  +-----------------------------------+
                  |    HolocronInterpreter (Visitor)  |
                  +-----------------------------------+
                     /           |          \          \
                    v            v           v          v
            SymbolTable    HolocronTable   HolocronMath  HolocronPlotter
            (Ambitos)       (Datasets)      (Calculos)    (PNG / No SVG)
```

1. **`visitPrograma`:** Recorre secuencialmente las sentencias del script.
2. **`visitDeclaracionMision`:** Registra el descriptor de la funcion en la tabla de simbolos sin ejecutar su cuerpo prematuramente.
3. **`visitSentenciaAsignacion`:** Resuelve la expresion o pipeline derecho y almacena el resultado bajo el identificador izquierdo.
4. **`visitExpresionPipeline`:** Toma la base (`expresionBase`) y canaliza el dataset secuencialmente a traves de cada `operacionPipeline`.
5. **`visitSentenciaCondicional`:** Evalua la condicion booleana; si es verdadera despacha el bloque `senda_luminosa`, en caso contrario ejecuta `senda_oscura`.
6. **`visitSentenciaArchivado`:** Invoca `HolocronTable.archivar()` delegando en `HolocronIO`.
7. **`visitSentenciaHolograma`:** Extrae las propiedades (`eje_x`, `eje_y`, `titulo`, `guardar`) y llama a `HolocronPlotter.proyectar_holograma()`.
8. **`visitSentenciaTransmision`:** Imprime tablas o escalares formateados en consola y los preserva en el buffer de transmisiones.
