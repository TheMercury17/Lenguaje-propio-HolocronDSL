# Manual Técnico de Arquitectura e Implementación: HolocronDSL

**Compilador e Intérprete para Lenguaje de Dominio Específico de Ciencia de Datos**  
**Universidad Sergio Arboleda**  
**Programa de Ciencias de la Computación e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programación y Transducción (Semestre 2026-2)  
**Docente:** Joaquín F. Sánchez  
**Equipo de Desarrollo (Grupo 5):**  
- Andrés Sebastián Coral Vallejo  
- Carol Arenas Cardona  

---

## 1. Arquitectura General del Sistema

HolocronDSL está estructurado siguiendo el modelo clásico de transducción y compilación por fases desacopladas, implementando un front-end formal generado con ANTLR4 y un back-end evaluador dinámico basado en el patrón de diseño Visitor en Python 3.

```
                      +---------------------------------------+
                      |         Código Fuente (.holo)         |
                      +---------------------------------------+
                                          |
                                          v
                      +---------------------------------------+
                      |       Analizador Léxico (ANTLR4)      |
                      |          (HolocronDSLLexer)           |
                      +---------------------------------------+
                                          | Flujo de Tokens
                                          v
                      +---------------------------------------+
                      |     Analizador Sintáctico (ANTLR4)    |
                      |          (HolocronDSLParser)          |
                      +---------------------------------------+
                                          | Árbol de Análisis (CST / AST)
                                          v
                      +---------------------------------------+
                      |       Evaluador Semántico Visitor     |
                      |            (HolocronVisitor)          |
                      +---------------------------------------+
                                    |           |
            +-----------------------+           +-----------------------+
            | Control de Ámbitos                | Ejecución de Rutinas
            v                                   v
+-------------------------+         +-----------------------------------+
|    Tabla de Símbolos    |         |    Motores de Ejecución Propios   |
| (SymbolTable / Scope)   |         |-----------------------------------|
+-------------------------+         | • HolocronMath  (Estadística/OLS) |
                                    | • HolocronIO    (CSV / XML .xls)  |
                                    | • HolocronTable (Inmutabilidad)   |
                                    | • HolocronPlotter (Raster PNG)    |
                                    | • DataStructures (Arreglos/Pilas) |
                                    | • MLEngine      (Árbol/K-Means)   |
                                    +-----------------------------------+
                                                        |
                                                        v
                                    +-----------------------------------+
                                    |         Salidas y Efectos         |
                                    |-----------------------------------|
                                    | • Consola / Tablas ASCII          |
                                    | • Archivos CSV y Excel (.xls)     |
                                    | • Gráficos PNG a 300 DPI          |
                                    +-----------------------------------+
```

### 1.1 Estructura Modular del Proyecto
La base del código se organiza estrictamente en paquetes desacoplados:
- `grammar/`: Especificación formal de la gramática léxica y sintáctica (`HolocronDSL.g4`).
- `src/generated/`: Clases generadas automáticamente por ANTLR4 (`Lexer`, `Parser`, `Visitor`, `Listener`).
- `src/compiler/`: Fachada y driver del compilador (`driver.py`), formateador de árboles y control de pipelines.
- `src/interpreter/`: Evaluador semántico (`visitor.py`), gestión de contextos y tabla de símbolos (`symbol_table.py`).
- `src/runtime/`: Motores de ejecución propios (`math_engine.py`, `io_engine.py`, `holocron_table.py`, `graphics_engine.py`, `data_structures.py`, `ml_engine.py`).
- `src/errors/`: Manejo unificado de excepciones sintácticas (`error_listener.py`) y semánticas (`semantic_error.py`).
- `src/cli.py` / `holocron.py`: Punto de entrada unificado de línea de comandos.
- `tests/`: Batería exhaustiva de pruebas unitarias y de integración (93 pruebas automatizadas).

---

## 2. Especificación Formal de la Gramática (ANTLR4)

La gramática se encuentra codificada en `grammar/HolocronDSL.g4`. El lenguaje opera con reglas libres de contexto (CFG) procesables mediante un autómata LL(*).

### 2.1 Categorías Léxicas y Tokens
1. **Palabras Reservadas de Ingestión y E/S:** `abrir_holocron`, `delimitado_por`, `archivar_holocron`, `en`, `proyectar_holograma`, `guardar_en`, `transmitir`.
2. **Palabras Reservadas de Transformación:** `revelar`, `purgar`, `donde`, `forjar`, `ordenar`, `por`, `ascendente`, `descendente`, `eliminar_clones`, `sanar_vacios`, `con`, `agrupar`, `resumir`, `trazar_regresion`.
3. **Funciones de Agregación y Métricas:** `recuento`, `conteo`, `acumular`, `suma`, `equilibrio`, `promedio`, `mediana`, `cenit`, `maximo`, `nadir`, `minimo`, `desviacion`.
4. **Control de Flujo y Modularización:** `mision`, `fin_mision`, `retornar`, `evaluar_fuerza`, `senda_luminosa`, `senda_oscura`, `fin_evaluar`.
5. **Tipos de Gráficos:** `barras`, `histograma`, `caja`, `lineas`, `dispersion`, `regresion`, `tendencia`.
6. **Operadores y Conectores:**
   - Pipeline: `|>`
   - Asignación: `=`
   - Aritméticos: `+`, `-`, `*`, `/`, `%`, `^`
   - Relacionales: `==`, `!=`, `<`, `<=`, `>`, `>=`
   - Lógicos: `y`, `o`, `no`
7. **Literales y Tipos Primitivos:** Enteros (`NUMERO_ENTERO`), Decimales (`NUMERO_DECIMAL`), Cadenas de caracteres (`CADENA`) y Booleanos (`cierto_es`, `falso_es`, `verdadero`, `falso`).

### 2.2 Precedencia y Asociatividad de Operadores
Para eliminar ambigüedades en expresiones complejas, ANTLR4 aplica precedencia estratificada en la regla `expresion`:
1. Expresiones primarias, llamadas a funciones y literales agrupados en paréntesis.
2. Operador unario de negación (`-` y `no`).
3. Potenciación (`^`), asociativa hacia la derecha.
4. Multiplicación (`*`), división (`/`) y módulo (`%`), asociativos hacia la izquierda.
5. Suma (`+`) y resta (`-`), asociativos hacia la izquierda.
6. Comparaciones relacionales (`==`, `!=`, `<`, `<=`, `>`, `>=`).
7. Conjunción lógica (`y`), asociativa hacia la izquierda.
8. Disyunción lógica (`o`), asociativa hacia la izquierda.

---

## 3. Modelo de Ámbitos y Tabla de Símbolos

El sistema implementa un entorno de ejecución jerárquico mediante las clases `Scope` y `SymbolTable` ubicadas en `src/interpreter/symbol_table.py`.

```
        +-----------------------------------------------+
        |              Ámbito Global (Global)           |
        |  - Variables de entorno y datasets cargados   |
        |  - Registro de funciones/misiones declaradas  |
        +-----------------------------------------------+
                                ^
                                | enlace estático (padre)
        +-----------------------------------------------+
        |         Ámbito Local (Llamada a Misión)       |
        |  - Parámetros formales asociados a argumentos |
        |  - Variables locales calculadas temporalmente |
        +-----------------------------------------------+
```

### 3.1 Características del Modelo de Memoria
- **Ámbitos Anidados con Enlace Estático:** Cada objeto `Scope` posee una referencia opcional a su ámbito contenedor (`padre`). La búsqueda de variables inicia en el ámbito actual y se propaga recursivamente hacia el ámbito global.
- **Sombreado de Variables (Variable Shadowing):** Si una variable local comparte el nombre de una variable global, la definición local prevalece dentro del contexto de la función sin alterar el valor exterior.
- **Inmutabilidad de Referencias Tabulares:** Cada operación sobre un conjunto de datos produce un nuevo objeto `HolocronTable`, preservando el estado original de la variable previa.

---

## 4. Evaluador Semántico (`HolocronVisitor`)

El evaluador semántico `HolocronVisitor` (`src/interpreter/visitor.py`) hereda de `HolocronDSLVisitor` e implementa la ejecución interpretada recorriendo el árbol AST.

### 4.1 Principales Métodos del Visitor
- `visitPrograma`: Inicializa el ámbito global y evalúa secuencialmente cada sentencia.
- `visitSentenciaAsignacion`: Resuelve la expresión del lado derecho y almacena el resultado tipado en la tabla de símbolos del ámbito activo.
- `visitExpresionPipeline`: Recibe la tabla base y aplica de forma encadenada cada `operacionPipeline` asociada.
- `visitOperacionRevelar`: Valida la existencia de las columnas en la tabla y genera una proyección reducida.
- `visitOperacionPurgar`: Evalúa la expresión condicional para cada fila de la tabla en un contexto temporal de símbolos, conservando aquellas donde la condición resulte verdadera.
- `visitOperacionForjar`: Evalúa una expresión aritmética sobre los valores de la fila y genera una nueva columna calculada.
- `visitOperacionRegresion`: Ejecuta la estimación de regresión lineal OLS sobre las columnas indicadas, adjunta las predicciones y retorna un objeto `HolocronRegressionResult`.
- `visitOperacionKMeans`, `visitOperacionArbol`, `visitOperacionPerceptron`: Despachan modelos de machine learning entrenados desde cero hacia las columnas de la tabla.
- `visitOperacionNormalizar`, `visitOperacionEstandarizar`, `visitOperacionCodificar`: Aplican preprocesamiento y transformaciones matemáticas continuas o categóricas.
- `visitSentenciaAsignacionIndice`: Gestiona la mutación de posiciones en arreglos `arr[i] = val` verificando límites de memoria.
- `visitSentenciaMientras`, `visitSentenciaPara`, `visitSentenciaParaRango`: Controlan la ejecución iterativa de bucles gestionando ámbitos locales y condiciones.
- `visitSentenciaHolograma`: Extrae los metadatos de configuración visual (`titulo`, `eje_x`, `eje_y`, `guardar_en`) e invoca al motor de graficación `HolocronPlotter`.
- `visitSentenciaArchivado`: Recupera el objeto tabular y lo persiste físicamente en disco delegando en `HolocronIO`.

---

## 5. Motores de Ejecución Propios (Runtime)

Para garantizar independencia tecnológica absoluta y evitar dependencias externas como Pandas, NumPy, Scikit-Learn o librerías pesadas, se construyeron seis módulos nativos:

### 5.1 Motor Matemático (`HolocronMath`)
Ubicado en `src/runtime/math_engine.py`, provee algoritmos analíticos puros implementados en Python estándar:
- **Estadística Descriptiva:** Media aritmética (`equilibrio`), mediana para longitudes pares e impares, varianza poblacional y muestral, desviación típica muestral, valores extremos (`cenit` y `nadir`).
- **Covarianza y Correlación de Pearson:**
  $$\text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$
  $$r = \frac{\text{Cov}(X, Y)}{S_x S_y}$$
- **Regresión Lineal Simple por Mínimos Cuadrados Ordinarios (OLS):**
  $$m = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}, \quad b = \bar{y} - m\bar{x}$$
  $$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$
  Calcula además el error estándar de estimación ($S_e$) y el vector de residuos ($e_i = y_i - \hat{y}_i$).

### 5.2 Motor de Entrada/Salida (`HolocronIO`)
Ubicado en `src/runtime/io_engine.py`:
- **Lector de CSV:** Soporta delimitadores configurables (`,`, `;`, `\t`, `|`), maneja cadenas encerradas entre comillas con comillas de escape y realiza inferencia automática de tipos (`int`, `float`, `str`).
- **Serializador XML Spreadsheet 2003 (.xls):** Genera archivos de hojas de cálculo nativas sin requerir paquetes binarios pesados. Escribe la estructura formal XML con declaración de estilos, fuentes y celdas tipadas (`ss:Type="Number"` o `ss:Type="String"`), plenamente compatible con Microsoft Excel y LibreOffice Calc.
- **Resolución Determinística de Rutas:** Garantiza la creación recursiva de directorios contenedores (`path.parent.mkdir(parents=True, exist_ok=True)`) y notifica en terminal la ruta absoluta del archivo generado.

### 5.3 Motor de Tablas Inmutables (`HolocronTable` y `HolocronRegressionResult`)
Ubicado en `src/runtime/holocron_table.py`:
- Los datos se modelan internamente como una lista inmutable de diccionarios `List[Dict[str, Any]]`.
- Cada operación (`purgar`, `revelar`, `forjar`, `ordenar`, `sanar_vacios`) retorna una nueva instancia de `HolocronTable`, garantizando transparencia referencial.
- `HolocronRegressionResult` especializa a la tabla almacenando los parámetros del modelo ($m$, $b$, $R^2$, $r$) y sobrecargando los métodos de visualización tabular para imprimir resúmenes estadísticos completos en la consola.
- Integración nativa de métodos ML en la tabla: `agrupar_kmeans()`, `clasificar_arbol()`, `clasificar_perceptron()`, `normalizar_minmax()`, `estandarizar_zscore()`, `codificar_etiquetas()`.

### 5.4 Motor de Proyección Visual (`HolocronPlotter`)
Ubicado en `src/runtime/graphics_engine.py`:
- Configura el backend no interactivo `matplotlib.use('Agg')`, permitiendo generar mapas de bits directamente en memoria sin requerir entorno de ventanas ni servidores X11 en Linux.
- **Restricción Estricta:** No utiliza formato vectorial SVG. Genera exclusivamente archivos matriciales raster PNG a una densidad fija de **300 DPI**.
- **Tema Visual Galáctico:** Aplica fondos oscuros tácticos (`#0b0f19`), tipografías blancas nítidas, rejillas alfa sutiles y realces cromáticos de alto contraste en cian `#00e5ff`, magenta `#e040fb` y ámbar `#ffd600`.
- Soporta cinco modos gráficos: `barras`, `histograma`, `caja`, `lineas` y `regresion` (diagrama de dispersión con línea de tendencia OLS y leyenda estadística embebida).

### 5.5 Motor de Estructuras de Datos Nativas (`src/runtime/data_structures.py`)
Implementa las estructuras de datos fundamentales para la gestión algorítmica de colecciones:
- `HolocronArray`: Arreglo dinámico indexable con verificación estricta de límites, operaciones de rebanado (`subarreglo`), inserción en cualquier índice, remoción, inversión y ordenamiento nativo sin dependencias.
- `crear_lista_dimensionada(tamano, valor)`: Función de factoría para instanciar arreglos de longitud fija inicializados con valores por defecto.
- `HolocronPila`: Estructura lineal LIFO con operaciones protegidas `apilar`, `desapilar`, `cima` y `esta_vacia`.
- `HolocronCola`: Estructura lineal FIFO con operaciones protegidas `encolar`, `desencolar`, `frente` y `esta_vacia`.
- `NodoArbolDecision`: Estructura jerárquica binaria que almacena umbrales, columnas de partición, impureza de Gini, conteo de muestras y referencias a subárboles izquierdo y derecho.

### 5.6 Motor Propio de Aprendizaje de Máquina (`src/runtime/ml_engine.py`)
Implementa algoritmos analíticos puros de machine learning sin paquetes externos:
- `ArbolDecisionGalactico`: Clasificador supervisado CART que optimiza de forma recursiva la reducción de impureza de Gini para variables continuas y categóricas.
- `PerceptronGalactico`: Clasificador lineal supervisado con regla estocástica de corrección de pesos y sesgo de Frank Rosenblatt.
- `KMeansGalactico`: Algoritmo de agrupamiento no supervisado con inicialización k-means++ determinística, cálculo de distancias euclidianas multivariadas y convergencia iterativa de centroides.
- `Metricas`: `evaluar_exactitud()`, `calcular_matriz_confusion()`, `distancia_euclidiana()`, `calcular_impureza_gini()`, `calcular_entropia()`.
- `Preprocesamiento`: `normalizar_min_max()`, `estandarizar_z_score()`, `codificar_etiquetas()`.

---

## 6. Subsistema de Manejo y Diagnóstico de Errores

El compilador clasifica y reporta los errores en tres niveles con información contextual precisa:

1. **Errores Léxicos y Sintácticos:**
   Implementados mediante `HolocronErrorListener` (`src/errors/error_listener.py`), el cual intercepta llamadas de ANTLR4 e imprime en terminal:
   - Número de línea y columna del token infractor.
   - Texto del token esperado frente al encontrado.
   - Sugerencia correctiva en lenguaje natural.
2. **Errores Semánticos:**
   Definidos en `src/errors/semantic_error.py`:
   - `VariableNoDefinidaError`: Identificador no registrado en la tabla de símbolos.
   - `ColumnaNoExisteError`: Acceso a una columna ausente en el esquema tabular activo.
   - `TipoIncompatibleError`: Operación aritmética o relacional sobre tipos discordantes.
   - `DivisionPorCeroError`: Intento de dividir por cero en una expresión calculada.
   - `IndiceFueraDeRangoError`: Acceso a un índice fuera de los límites del arreglo.
   - `EstructuraVaciaError`: Operación de extracción sobre una pila o cola vacía.
   - `ErrorModeloML`: Inconsistencia en parámetros, dimensiones o datos de entrenamiento de modelos ML.
   - `HolocronIOError`: Falla de acceso, apertura o escritura de archivos en disco.

---

## 7. Metodología de Pruebas y Validación Automatizada

El aseguramiento de calidad del compilador se sustenta en una batería de pruebas automatizadas mediante el framework `unittest` de Python, ejecutables a través del script `run_tests.py` o el comando `make test`.

### 7.1 Matriz de Cobertura de Pruebas (93 Pruebas en Total)

| Suite de Pruebas | Archivo | Cantidad | Alcance de Verificación |
| :--- | :--- | :---: | :--- |
| **Lexer** | `tests/test_lexer.py` | 6 | Reconocimiento de palabras reservadas, operadores, comentarios y literales. |
| **Parser Válido** | `tests/test_parser_valid.py` | 8 | Construcciones sintácticas correctas, pipelines y proyecciones. |
| **Parser Inválido** | `tests/test_parser_invalid.py` | 6 | Detección y reporte de errores sintácticos intencionales. |
| **Motor Matemático** | `tests/test_math_engine.py` | 7 | Promedio, mediana, varianza, extremos, división por cero y valores nulos. |
| **Motor de E/S** | `tests/test_io_engine.py` | 5 | Inferencia de tipos, parseo CSV, persistencia XML Excel (.xls) y rutas. |
| **Motor Tabular** | `tests/test_holocron_table.py` | 8 | Inmutabilidad, filtrado, ordenamiento, agrupación y agregaciones. |
| **Tabla de Símbolos** | `tests/test_symbol_table.py` | 4 | Ámbitos jerárquicos, resolución de símbolos y sombreado. |
| **Ejecución Semántica** | `tests/test_semantic_execution.py` | 18 | Asignaciones, expresiones compuestas, funciones y condicionales. |
| **Regresión y Visualización** | `tests/test_regression.py` | 7 | Estimación OLS, correlación, ajuste tabular y proyecciones PNG. |
| **Estructuras de Datos** | `tests/test_data_structures.py` | 12 | Arreglos, listas de tamaño fijo, pilas LIFO, colas FIFO, bucles (mientras, para, recorrer) y nodos de árbol. |
| **Machine Learning** | `tests/test_machine_learning.py` | 12 | K-Means, Perceptrón, Árbol CART, Gini, Entropía, métricas, normalización y pipelines DSL. |
| **Pruebas de Integración** | `tests/test_integration_examples.py` | 6 | Ejecución de los programas de ejemplo completos `.holo`. |

Todas las pruebas se ejecutan de manera determinística en aproximadamente 2 segundos sin generar efectos colaterales persistentes en el entorno de desarrollo.
