# HolocronDSL: Lenguaje de Dominio Especifico para Ciencia de Datos y Visualizacion

**Universidad Sergio Arboleda**  
**Programa de Ciencias de la Computacion e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programacion y Transduccion  
**Periodo Academico:** Semestre 2026-2  
**Docente:** Joaquin F. Sanchez  

### Equipo de Desarrollo (Grupo 5)
- **Andres Sebastian Coral Vallejo**
- **Carol Arenas Cardona**

---

## 1. Descripcion General

HolocronDSL es un lenguaje de dominio especifico (DSL) declarativo y funcional diseñado para describir flujos reproducibles de ingestion, depuracion, transformacion, agregacion y visualizacion grafica de datos.

El lenguaje adopta una identidad conceptual y estetica basada en el universo de **Star Wars**:
- Las fuentes de datos son tratadas como **holocrones**.
- El flujo de transformacion se modela mediante un conector de pipeline hiperespacial limpio (`|>`).
- Las variables se vinculan con el operador estandar de asignacion (`=`).
- La depuracion de registros utiliza primitivas declarativas como `purgar donde`, `eliminar_clones` y `sanar_vacios con`.
- La generacion de nuevas variables se realiza mediante la clausula `forjar variable = expresion`.
- Las visualizaciones graficas se declaran mediante bloques de **hologramas** (`holograma tipo datos`).
- El lenguaje cuenta con abstraccion funcional (`mision`) y bifurcaciones condicionales (`evaluar_fuerza` con `senda_luminosa` y `senda_oscura`).

Esta arquitectura garantiza una originalidad absoluta frente a otros lenguajes convencionales (evitando patrones directos de C++, Java o Python) y proporciona una separacion estricta entre la sintaxis formal (definida en ANTLR4) y la ejecucion semantica en Python.

---

## 2. Guia de Instalacion y Ejecucion Multiplataforma (Linux, Kali Linux y Windows)

Para desplegar y ejecutar HolocronDSL en cualquier sistema operativo (especialmente en distribuciones Linux como Kali Linux en VirtualBox, Debian, Ubuntu, o en entornos Windows), se deben seguir las siguientes instrucciones secuenciales:

### Paso 0: Obtencion del proyecto y ubicacion de trabajo

#### En entornos Linux (Kali Linux, Debian, Ubuntu):
1. Abrir la terminal del sistema (`bash` o `zsh`).
2. En caso de clonar mediante Git:
   ```bash
   git clone https://github.com/TheMercury17/Lenguaje-propio-HolocronDSL.git
   cd Lenguaje-propio-HolocronDSL
   ```
3. En caso de contar con la carpeta ya descargada, navegar hasta ella:
   ```bash
   cd ruta/hacia/Lenguaje-propio-HolocronDSL
   ```
4. Comprobar la presencia de los archivos del repositorio con:
   ```bash
   ls -la
   ```
   Se observaran archivos como `Makefile`, `run_tests.py`, `requirements.txt` y los directorios `grammar`, `src`, `docs` y `examples`.

#### En entornos Windows:
1. Abrir PowerShell o CMD y posicionarse en la carpeta donde reside el proyecto:
   ```powershell
   cd ruta\hacia\Lenguaje-propio-HolocronDSL
   ```
2. Para comprobar la correcta ubicacion, ejecutar:
   ```powershell
   dir
   ```

---

### Paso 1: Instalacion de dependencias y preparacion del entorno

#### En Kali Linux y distribuciones basadas en Debian:
En versiones recientes de Kali Linux, el gestor de paquetes del sistema restringe la instalacion global de paquetes de Python mediante `pip` (politica PEP 668 de entorno administrado externamente). Por tal razon, se debe preparar un entorno virtual aislado:

1. **Instalacion de paquetes base del sistema operativo (en caso de no tenerlos instalados):**
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv make default-jre
   ```
   *(Nota: `default-jre` se requiere en caso de que se desee recompilar la gramatica ANTLR4 desde cero).*

2. **Creacion y activacion del entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   *(Al activarse el entorno, la consola antepondra el prefijo `(venv)`).*

3. **Instalacion de las dependencias oficiales del proyecto:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Esto instalara `antlr4-python3-runtime`, `pandas`, `numpy` y `matplotlib`).*

4. **Verificacion de los analizadores de ANTLR4 generados:**
   ```bash
   python3 run_tests.py --grammar
   ```

#### En Windows:
1. **Creacion y activacion del entorno virtual:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. **Instalacion de dependencias:**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Verificacion de los analizadores de ANTLR4:**
   ```powershell
   python run_tests.py --grammar
   ```

---

### Paso 2: Ejecucion y analisis de programas HolocronDSL (.holo)

Los programas escritos en HolocronDSL poseen la extension `.holo` y se ubican en el directorio `examples/`. Para su analisis sintactico e inspeccion de arboles, se dispone del lanzador `holocron.py` o de la interfaz `src/cli.py`:

1. **Verificar la validez sintactica de un script (modo verificacion):**
   - En Linux / Kali Linux:
     ```bash
     python3 holocron.py examples/01_telemetria_cazas.holo --check
     ```
   - En Windows:
     ```powershell
     python holocron.py examples/01_telemetria_cazas.holo --check
     ```
   *Salida esperada:*
   `Sintaxis verificada con exito: la Fuerza fluye en perfecta armonia.`

2. **Visualizar el Arbol Sintactico Concreto (CST) en formato jerarquico:**
   - En Linux / Kali Linux:
     ```bash
     python3 src/cli.py examples/01_telemetria_cazas.holo --tree
     ```
   - En Windows:
     ```powershell
     python src/cli.py examples/01_telemetria_cazas.holo --tree
     ```
   *Salida esperada:* Representacion visual en consola con la descomposicion de cada regla sintactica y token reconocido.

3. **Visualizar el arbol en notacion parentizada tipo LISP:**
   ```bash
   python3 src/cli.py examples/01_telemetria_cazas.holo --lisp
   ```

4. **Analizar una linea o expresion directamente desde la terminal:**
   ```bash
   python3 src/cli.py --codigo "cazas = abrir_holocron \"flota.csv\" |> purgar donde escudos > 50" --tree
   ```

---

### Paso 3: Ejecucion de la suite de pruebas unitarias

El script `run_tests.py` coordina las pruebas automatizadas de forma multiplataforma:

#### Ejecucion de la totalidad de las pruebas unitarias:
- En Linux / Kali Linux:
  ```bash
  python3 run_tests.py
  ```
- En Windows:
  ```powershell
  python run_tests.py
  ```
*(Para evaluar ademas la validez de los 5 programas de ejemplo de la carpeta `examples/`, se añade el parametro `--all`: `python3 run_tests.py --all`).*

#### Ejecucion modular de pruebas por componente:
* **Pruebas del analizador lexico (tokens, palabras reservadas y literales):**
  ```bash
  python3 run_tests.py --lexer
  ```
* **Pruebas del analizador sintactico (construcciones y pipelines validos):**
  ```bash
  python3 run_tests.py --parser
  ```
* **Pruebas de deteccion de errores sintacticos y recuperacion:**
  ```bash
  python3 run_tests.py --invalid
  ```
* **Validacion sintactica de todos los ejemplos en `examples/`:**
  ```bash
  python3 run_tests.py --examples
  ```

---

### Paso 4: Automatizacion con Makefile (Recomendado en Linux / Kali Linux)

En entornos Unix y distribuciones como Kali Linux, se recomienda el empleo de la herramienta `make` para agilizar las tareas de desarrollo:

```bash
make help            # Lista todos los comandos disponibles en el proyecto
make install         # Instala las dependencias declaradas en requirements.txt
make test            # Ejecuta la totalidad de las pruebas unitarias
make test-lexer      # Ejecuta exclusivamente las pruebas lexicas
make test-parser     # Ejecuta exclusivamente las pruebas sintacticas positivas
make test-invalid    # Ejecuta pruebas sintacticas de deteccion de errores
make check-examples  # Valida sintacticamente los 5 programas galacticos en examples/
make clean           # Remueve archivos residuales de cache (__pycache__)
```

---

## 3. Anatomia del Codigo y Diccionario de Palabras Reservadas

Para garantizar que cualquier persona comprenda de inmediato el codigo de HolocronDSL, cada elemento de un script `.holo` pertenece a una de **5 categorias bien delimitadas**:

### 3.1. Las 5 Categorias de Elementos
1. **Palabras Reservadas:** Ordenes e instrucciones fijas predefinidas en el compilador (`abrir_holocron`, `purgar donde`, `forjar`, `holograma`, etc.). No pueden usarse como variables.
2. **Nombres de Variables:** Identificadores libres creados por el usuario para guardar tablas o resultados en memoria (`telemetria`, `escuadron_activo`). Se escriben sin comillas.
3. **Nombres de Columnas:** Encabezados que vienen definidos en el archivo CSV (`modelo`, `faccion`, `escudos`, `velocidad`).
4. **Operadores y Conectores:** Simbolos que transforman o canalizan informacion: asignacion (`=`), tuberia hiperespacial (`|>`), aritmetica (`+`, `-`, `*`, `/`) y comparacion (`>`, `<`, `==`).
5. **Literales:** Valores constantes directos: textos entre comillas (`"datos.csv"`), numeros (`100`, `3.14`) o booleanos (`cierto_es`, `falso_es`).

### 3.2. Diccionario Exhaustivo de Palabras Reservadas

A continuacion se presenta la totalidad del lexico reservado de HolocronDSL, clasificado por categoria con su significado en lenguaje cotidiano y ejemplo ilustrativo:

| Palabra Reservada | Categoria | Significado en Lenguaje Cotidiano | Ejemplo de Uso |
| :--- | :--- | :--- | :--- |
| **`abrir_holocron`** | Entrada de datos | Lee un archivo CSV y lo carga como tabla en memoria. | `datos = abrir_holocron "flota.csv"` |
| **`archivar`** | Salida de datos | Exporta y guarda una tabla procesada en un archivo CSV en disco. | `archivar mi_tabla en "salida.csv"` |
| **`en`** | Conector | Especifica la ruta destino para la sentencia `archivar`. | `archivar datos en "reporte.csv"` |
| **`transmitir`** | Salida de consola | Imprime un texto, numero, tabla o modelo de regresion con formato en la terminal. | `transmitir "Mision completada"` |
| **`trazar_regresion`** | Modelado estadistico | Ajusta una regresion lineal simple OLS sobre dos variables numericas y genera predicciones. | `tabla \|> trazar_regresion [eje_x = "distancia", eje_y = "latencia", destino = "pred"]` |
| **`inspeccionar`** | Exploracion | Muestra el esquema de la tabla (columnas y tipos de datos detectados). | `inspeccionar flota` |
| **`purgar donde`** | Transformacion | Filtra filas conservando unicamente aquellas que satisfacen la condicion. | `tabla \|> purgar donde escudos > 80` |
| **`eliminar_clones`** | Limpieza | Remueve registros repetidos o filas duplicadas de la tabla. | `tabla \|> eliminar_clones` |
| **`sanar_vacios con`**| Limpieza | Imputa y rellena celdas vacias o valores faltantes (NaN/null). | `tabla \|> sanar_vacios con 0` |
| **`revelar`** | Proyeccion | Conserva exclusivamente las columnas listadas entre corchetes. | `tabla \|> revelar [nave, piloto]` |
| **`forjar`** | Calculo | Genera e inserta una columna nueva calculada mediante una expresion. | `tabla \|> forjar blindaje = escudos * 1.2` |
| **`ordenar por`** | Ordenamiento | Reorganiza las filas segun los valores de la columna indicada. | `tabla \|> ordenar por velocidad desc` |
| **`ascendente` / `descendente`** | Sentido de orden | Modificador para orden ascendente (menor a mayor) o descendente. | `ordenar por bajas descendente` |
| **`agrupar por`** | Agrupacion | Particiona las filas en grupos segun una o mas columnas categoricas. | `tabla \|> agrupar por [faccion]` |
| **`resumir`** | Agregacion | Aplica funciones de resumen (`equilibrio`, `acumular`, `recuento`, `cenit`, `nadir`, `desviacion`). | `resumir media = equilibrio(potencia)` |
| **`recuento` / `conteo`** | Agregacion | Cuenta el numero de filas de cada grupo particionado. | `n_naves = recuento()` |
| **`equilibrio` / `promedio`** | Agregacion | Calcula la media aritmetica de la columna numerica especificada. | `media = equilibrio(escudos)` |
| **`acumular` / `suma`** | Agregacion | Calcula la sumatoria acumulada de la columna numerica. | `total = acumular(combustible)` |
| **`cenit` / `maximo`** | Agregacion | Obtiene el valor maximo registrado en la columna. | `techo = cenit(velocidad)` |
| **`nadir` / `minimo`** | Agregacion | Obtiene el valor minimo registrado en la columna. | `piso = nadir(latencia)` |
| **`proyectar_holograma`** | Visualizacion | Declara la construccion de una representacion grafica PNG de 300 DPI sin SVG. | `proyectar_holograma barras datos [eje_x = "f", eje_y = "v", guardar_en = "g.png"]` |
| **`barras`** | Tipo de grafico | Grafico de barras para comparar cantidades por categoria. | `proyectar_holograma barras datos [...]` |
| **`histograma`** | Tipo de grafico | Grafico de distribucion de frecuencias numericas por intervalos. | `proyectar_holograma histograma datos [...]` |
| **`caja`** | Tipo de grafico | Diagrama de caja y bigotes (boxplot) para dispersion y cuartiles. | `proyectar_holograma caja datos [...]` |
| **`lineas`** | Tipo de grafico | Grafico de lineas continuas para tendencias o series ordenadas. | `proyectar_holograma lineas datos [...]` |
| **`regresion` / `tendencia`** | Tipo de grafico | Dispersion con linea de regresion lineal OLS, ecuacion y R^2. | `proyectar_holograma regresion datos [...]` |
| **`evaluar_fuerza`** | Control condicional | Inicia una bifurcacion logica basada en una condicion booleana. | `evaluar_fuerza (nivel > 5)` |
| **`senda_luminosa`** | Rama afirmativa | Bloque a ejecutar en caso de que la condicion evaluada sea verdadera. | `senda_luminosa: ...` |
| **`senda_oscura`** | Rama alternativa | Bloque alternativo a ejecutar en caso de que la condicion sea falsa. | `senda_oscura: ...` |
| **`fin_evaluar`** | Cierre condicional | Marca la conclusion formal del bloque condicional evaluado. | `fin_evaluar` |
| **`mision`** | Subrutina / Funcion | Define una rutina parametrizada y reutilizable con nombre propio. | `mision calcular_danio(base, factor)` |
| **`retornar`** | Retorno de valor | Devuelve un resultado computado hacia el llamador de la mision. | `retornar base * factor` |
| **`fin_mision`** | Cierre de funcion | Marca la conclusion de la declaracion de una mision. | `fin_mision` |
| **`cierto_es` / `verdadero`** | Booleano | Valor booleano positivo (true). | `activo = cierto_es` |
| **`falso_es` / `falso`** | Booleano | Valor booleano negativo (false). | `bloqueado = falso_es` |
| **`nulo`** | Valor ausente | Representa la ausencia de valor o dato faltante (null / None). | `valor = nulo` |
| **`y` / `y_fuerza`** | Operador logico | Conjuncion logica (ambas expresiones deben ser ciertas). | `escudos > 50 y blindaje > 20` |
| **`o` / `o_fuerza`** | Operador logico | Disyuncion logica (al menos una de las expresiones debe ser cierta). | `faccion == "A" o faccion == "B"` |
| **`no` / `no_fuerza`**| Operador logico | Negacion logica que invierte el valor de verdad de una expresion. | `no (activo == cierto_es)` |

---

## 4. Estructura del Repositorio

```text
Lenguaje propio/
├── Makefile                        # Automatizacion de tareas, pruebas y ejecucion
├── run_tests.py                    # Gestor multiplataforma de pruebas unitarias
├── .gitignore                      # Exclusion de archivos temporales y caches
├── README.md                       # Documentacion principal del proyecto
├── requirements.txt                # Dependencias oficiales de Python
├── grammar/
│   └── HolocronDSL.g4              # Especificacion lexica y sintactica en ANTLR4
├── docs/
│   ├── alcance.md                  # Documento de alcance y delimitacion formal
│   ├── catalogo_instrucciones.md   # Catalogo de palabras reservadas y semantica
│   ├── gramatica_ebnf.md           # Gramatica formal en notacion EBNF
│   ├── manual_programacion.md      # Manual tutorial intuitivo para principiantes
│   ├── manual_usuario.md           # Manual de usuario final para ejecucion y CLI
│   ├── manual_tecnico.md           # Manual tecnico de arquitectura, runtime y AST
│   ├── caso_estudio.md             # Informe formal del caso de estudio (8 puntos)
│   ├── guia_de_estudio.md          # Guia de estudio y banco de preguntas para sustentacion
│   ├── piedra_rosetta.md           # Matriz exhaustiva de equivalencias y traduccion
│   └── reglas_semanticas.md        # Especificacion formal de reglas semanticas y motores
├── holocron.py                     # Lanzador e interprete rapido en la raiz
├── src/
│   ├── __init__.py
│   ├── cli.py                      # Punto de entrada por linea de comandos e interprete
│   ├── compiler/
│   │   ├── __init__.py
│   │   └── driver.py               # Fachada de tokenizacion, parseo y formato de arbol
│   ├── errors/
│   │   ├── __init__.py
│   │   ├── error_listener.py       # Errores lexicos y sintacticos con linea/columna
│   │   └── semantic_error.py       # Jerarquia de errores semanticos y diagnostico
│   ├── generated/                  # Modulos generados por ANTLR4 (Lexer, Parser, Visitor)
│   ├── interpreter/                # Motor de ejecucion semantica
│   │   ├── __init__.py
│   │   ├── symbol_table.py         # Tabla de simbolos y gestion de ambitos (scopes)
│   │   └── visitor.py              # Interprete evaluador basado en patron Visitor
│   └── runtime/                    # Bibliotecas propias del lenguaje
│       ├── __init__.py
│       ├── holocron_table.py       # Estructura tabular inmutable y metodos ML
│       ├── io_engine.py            # Motor propio de I/O CSV y XML Spreadsheet 2003 (.xls)
│       ├── math_engine.py          # Biblioteca matematica, estadistica y regresion OLS
│       ├── graphics_engine.py      # Motor de renderizado PNG a 300 DPI sin SVG (HolocronPlotter)
│       ├── data_structures.py      # Arreglos, listas dimensionadas, pilas, colas y arboles
│       └── ml_engine.py            # Motor nativo de Machine Learning (Arbol CART, KMeans, Perceptron)
├── examples/
│   ├── datos/
│   │   ├── telemetria_flota.csv    # Conjunto de datos de prueba (fase 1 y 2)
│   │   └── telemetria_redes_galacticas.csv # Datos de telemetria del caso de estudio (fase 3)
│   ├── 01_telemetria_cazas.holo    # Flujo basico de carga, seleccion, filtro y archivado
│   ├── 02_censo_galactico.holo     # Agrupamiento por faccion y funciones estadisticas
│   ├── 03_proyeccion_holografica.holo # Bloques declarativos de graficos holograficos PNG
│   ├── 04_mision_avanzada.holo     # Abstraccion con misiones y evaluacion condicional
│   ├── 05_proyecto_completo.holo   # Flujo tactico integral paso a paso
│   ├── 06_caso_estudio_final.holo  # Caso de estudio: telemetria, regresion lineal y 5 graficos
│   └── 07_estructuras_y_machine_learning.holo # Listas de 10 pos, pilas, colas, bucles y ML
├── salidas/                        # Artefactos reales generados por el interprete
│   ├── flota_operativa.csv
│   ├── resumen_facciones.csv
│   ├── caso_estudio_resumen_sectores.csv
│   ├── caso_estudio_predicciones.xls
│   ├── caso_estudio_01_barras_sectores.png
│   ├── caso_estudio_02_histograma_latencia.png
│   ├── caso_estudio_03_caja_ancho_banda.png
│   ├── caso_estudio_04_lineas_degradacion.png
│   ├── caso_estudio_05_regresion_latencia.png
│   └── ...
└── tests/
    ├── __init__.py
    ├── test_lexer.py               # Pruebas unitarias de tokens y terminales
    ├── test_parser_valid.py        # Pruebas sintacticas positivas
    ├── test_parser_invalid.py      # Pruebas sintacticas negativas
    ├── test_math_engine.py         # Pruebas de algoritmos de HolocronMath
    ├── test_io_engine.py           # Pruebas de parser/serializador de HolocronIO
    ├── test_holocron_table.py      # Pruebas de operaciones tabulares inmutables
    ├── test_symbol_table.py        # Pruebas de ambitos y tabla de simbolos
    ├── test_semantic_errors.py     # Pruebas de deteccion de anomalias semanticas
    ├── test_semantic_execution.py  # Pruebas de ejecucion de sentencias y pipelines
    ├── test_regression.py          # Pruebas de regresion lineal OLS y graficacion
    ├── test_data_structures.py     # Pruebas de arreglos, pilas, colas y bucles
    ├── test_machine_learning.py    # Pruebas de Arbol CART, KMeans, Perceptron y metricas
    └── test_integration_examples.py# Pruebas integrales de los programas galacticos
```

---

## 5. Estado de Avance por Fases (Cortes)

- **Fase 1: Especificacion y Front-end del Lenguaje (Completada):**
  - Delimitacion del dominio, documento de alcance y catalogo de instrucciones.
  - Gramatica formal en EBNF y gramatica unificada ANTLR4 (`HolocronDSL.g4`).
  - Generador de Lexer y Parser en Python con ANTLR 4.13.2.
  - Manejador de errores de sintaxis personalizado con reporte preciso de linea y columna.
  - Interfaz CLI funcional para inspeccion del arbol sintactico.
  - Manual de programacion para principiantes en `docs/manual_programacion.md`.
  - Makefile y gestor de pruebas `run_tests.py` para ejecucion general o individual.
  - 5 ejemplos galacticos documentados y suite de pruebas unitarias al 100% de aprobacion.

- **Fase 2: Semantica y Procesamiento de Datos con Motores Propios (Completada):**
  - Implementacion del patron Visitor en Python (`HolocronVisitor`).
  - Tabla de simbolos con gestion de ambitos locales y globales (`SymbolTable` y `Scope`).
  - Biblioteca propia de matematicas y estadistica descriptiva pura (`HolocronMath`).
  - Biblioteca propia de lectura, inferencia de tipos y serializacion CSV (`HolocronIO`).
  - Soporte de exportacion a hojas de calculo nativas Excel (.xls) mediante XML Spreadsheet 2003.
  - Estructura de datos tabular inmutable (`HolocronTable` y `HolocronGroupedTable`).
  - Motor grafico de proyeccion holografica exportando exclusivamente a **PNG** a 300 DPI (`HolocronPlotter`), sin utilizar formato SVG.
  - Captura y diagnostico de errores semanticos (variables inexistentes, columnas no encontradas, division por cero, tipos incompatibles, aridad de misiones).
  - Pruebas unitarias y de integracion ampliadas.

- **Fase 3: Visualizacion Avanzada, Estructuras Nativas, Machine Learning y Producto Final (100% Completada):**
  - Incorporacion de modelado de **Regresion Lineal Simple por Minimos Cuadrados Ordinarios (OLS)** con instruccion nativa `trazar_regresion` en pipeline.
  - Calculo analitico de pendiente $m$, intercepto $b$, coeficiente de determinacion $R^2$, correlacion de Pearson $r$, residuos y error estandar.
  - Subclase especializada `HolocronRegressionResult` que preserva la inmutabilidad tabular y permite encadenamientos posteriores.
  - Soporte completo para 5 tipos de graficos PNG a 300 DPI: `barras`, `histograma`, `caja`, `lineas` y `regresion` (dispersion con recta ajustada y leyenda con $R^2$).
  - **Estructuras de datos nativas desde cero (`src/runtime/data_structures.py`):** Arreglos dinámicos (`HolocronArray`), listas dimensionadas de tamaño fijo (ej. `crear_lista(10, 0)`), indexación y asignación por índice `arr[i] = val`, Pilas LIFO (`HolocronPila`), Colas FIFO (`HolocronCola`), Nodos jerárquicos de Árbol de Decisión (`NodoArbolDecision`) y bucles (`mientras`, `para`, `recorrer`).
  - **Motor propio de Machine Learning (`src/runtime/ml_engine.py`):** Algoritmos de clasificación por Árbol de Decisión CART (Gini), Perceptrón lineal de Rosenblatt, Agrupamiento K-Means no supervisado (K-Means++ euclidiano), métricas de exactitud y matriz de confusión, normalizaciones Min-Max y Z-Score, e integración fluida en pipelines de Holocron.
  - Caso de estudio integral en telecomunicaciones galacticas (`examples/06_caso_estudio_final.holo`) con 30 nodos y 10 atributos.
  - Demostración integral de estructuras y ML en `examples/07_estructuras_y_machine_learning.holo`.
  - Generacion automatica de reportes consolidados en CSV, Excel nativo (.xls) y 5 graficos PNG en `salidas/`.
  - Documentacion final exhaustiva: **Manual de Usuario** (`docs/manual_usuario.md`), **Manual Tecnico** (`docs/manual_tecnico.md`), **Informe de Caso de Estudio** (`docs/caso_estudio.md`) y **Guia de Estudio con Banco de Preguntas Orales** (`docs/guia_de_estudio.md`).
  - Suite de pruebas de regresion e integracion ampliada a **93 pruebas automatizadas con 100% de aprobacion** en aproximadamente 2 segundos.
