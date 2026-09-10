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
| **`revelar`** | Salida de consola | Imprime un texto, numero o tabla directamente en la terminal. | `revelar "Mision finalizada con exito"` |
| **`inspeccionar`** | Exploracion | Muestra el esquema de la tabla (columnas y tipos de datos detectados). | `inspeccionar flota` |
| **`purgar donde`** | Transformacion | Filtra filas conservando unicamente aquellas que satisfacen la condicion. | `tabla \|> purgar donde escudos > 80` |
| **`eliminar_clones`** | Limpieza | Remueve registros repetidos o filas duplicadas de la tabla. | `tabla \|> eliminar_clones` |
| **`sanar_vacios con`**| Limpieza | Imputa y rellena celdas vacias o valores faltantes (NaN/null). | `tabla \|> sanar_vacios con 0` |
| **`seleccionar`** | Proyeccion | Conserva exclusivamente las columnas listadas entre corchetes. | `tabla \|> seleccionar [nave, piloto]` |
| **`forjar`** | Calculo | Genera e inserta una columna nueva calculada mediante una expresion. | `tabla \|> forjar blindaje = escudos * 1.2` |
| **`ordenar por`** | Ordenamiento | Reorganiza las filas segun los valores de la columna indicada. | `tabla \|> ordenar por velocidad desc` |
| **`asc` / `desc`** | Sentido de orden | Modificador para orden ascendente (menor a mayor) o descendente. | `ordenar por bajas desc` |
| **`agrupar por`** | Agrupacion | Particiona las filas en grupos segun una o mas columnas categoricas. | `tabla \|> agrupar por [faccion]` |
| **`resumir`** | Agregacion | Calcula metricas agregadas (`promedio`, `suma`, `conteo`, `min`, `max`). | `resumir [media = promedio(potencia)]` |
| **`limitar`** | Paginacion | Restringe la tabla a las primeras N filas indicadas. | `tabla \|> limitar 10` |
| **`holograma`** | Visualizacion | Declara la construccion de una representacion grafica estatica (PNG). | `holograma barras datos x: "f", y: "v", salida: "g.png"` |
| **`barras`** | Tipo de grafico | Grafico de barras para comparar cantidades por categoria. | `holograma barras datos ...` |
| **`dispersion`** | Tipo de grafico | Grafico de dispersion de puntos para correlacion de variables. | `holograma dispersion datos ...` |
| **`lineas`** | Tipo de grafico | Grafico de lineas continuas para analizar tendencias continuas o temporales. | `holograma lineas datos ...` |
| **`histograma`** | Tipo de grafico | Grafico de distribucion de frecuencias numericas por intervalos. | `holograma histograma datos ...` |
| **`si la_fuerza`** | Control condicional | Inicia una bifurcacion logica basada en una condicion booleana. | `si la_fuerza (nivel > 5) entonces` |
| **`entonces`** | Conector condicional | Marca el bloque de codigo a ejecutar si la condicion es verdadera. | `si la_fuerza (condicion) entonces` |
| **`sino`** | Rama alternativa | Marca el bloque de codigo alternativo si la condicion no se cumplio. | `sino ... fin_fuerza` |
| **`fin_fuerza`** | Cierre de bloque | Marca la terminacion formal del bloque condicional. | `fin_fuerza` |
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
├── Makefile                        # Automatizacion de tareas y pruebas
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
│   └── piedra_rosetta.md           # Matriz exhaustiva de equivalencias y traduccion
├── holocron.py                     # Lanzador rapido en la raiz del proyecto
├── src/
│   ├── __init__.py
│   ├── cli.py                      # Punto de entrada por linea de comandos
│   ├── compiler/
│   │   ├── __init__.py
│   │   └── driver.py               # Fachada de tokenizacion, parseo y formato de arbol
│   ├── errors/
│   │   ├── __init__.py
│   │   └── error_listener.py       # Manejador de errores lexicos y sintacticos con linea/columna
│   └── generated/                  # Modulos generados por ANTLR4 (Lexer, Parser, Visitor)
├── examples/
│   ├── datos/
│   │   └── telemetria_flota.csv    # Conjunto de datos de prueba
│   ├── 01_telemetria_cazas.holo    # Flujo basico de carga, seleccion, filtro y archivado
│   ├── 02_censo_galactico.holo     # Agrupamiento por faccion y funciones estadisticas
│   ├── 03_proyeccion_holografica.holo # Bloques declarativos de graficos holograficos
│   ├── 04_mision_avanzada.holo     # Abstraccion con misiones y evaluacion condicional
│   └── 05_proyecto_completo.holo   # Flujo tactico integral paso a paso
└── tests/
    ├── __init__.py
    ├── test_lexer.py               # Pruebas unitarias de tokens y terminales
    ├── test_parser_valid.py        # Pruebas sintacticas positivas y verificacion de ejemplos
    └── test_parser_invalid.py      # Pruebas sintacticas negativas y reporte de errores
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

- **Fase 2: Semantica y Procesamiento de Datos (Proxima entrega):**
  - Implementacion del patron Visitor en Python.
  - Tabla de simbolos y contextos de ejecucion de variables y funciones.
  - Integracion del motor de ejecucion sobre pandas y NumPy.

- **Fase 3: Visualizacion, Integracion y Producto Final:**
  - Motor de visualizacion sobre Matplotlib para proyecciones graficas (PNG).
  - Caso de estudio integral con datos reales y reporte final.
