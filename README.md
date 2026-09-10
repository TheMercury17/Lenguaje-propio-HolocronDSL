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

## 2. Guia Paso a Paso: Desde Cero hasta la Ejecucion

Si nunca has ejecutado un proyecto por consola o no sabes por donde empezar, sigue estos pasos exactos:

### Paso 0: Como abrir la terminal y ubicarse en la carpeta correcta
Para que cualquier comando funcione, tu consola (PowerShell o CMD) debe estar ubicada en la carpeta raiz del proyecto.

**Opcion A (La mas facil en Windows):**
1. Abre el Explorador de Archivos de Windows y entra a la carpeta del proyecto:
   `C:\Users\Sebas\OneDrive\Documents\Sergio Arboleda\Trabajos\Lenguajes de prog\Lenguaje propio`
2. Haz clic en la barra de direcciones superior (donde se ve la ruta de las carpetas).
3. Escribe `powershell` y presiona la tecla `Enter`.
4. Se abrira una ventana azul ya ubicada exactamente en el proyecto.

**Opcion B (Usando el comando `cd` en cualquier terminal):**
Si ya tienes una consola abierta, escribe este comando (con las comillas) y presiona `Enter`:
```powershell
cd "C:\Users\Sebas\OneDrive\Documents\Sergio Arboleda\Trabajos\Lenguajes de prog\Lenguaje propio"
```

Para verificar que estas en el lugar correcto, escribe:
```powershell
dir
```
Debes ver archivos como `README.md`, `run_tests.py`, `Makefile` y carpetas como `src`, `docs` y `examples`.

---

### Paso 1: Que comandos escribir antes de ejecutar las cosas (Preparacion inicial)
Solo debes hacer esto la primera vez que configuras el proyecto:

1. **Verificar que Python este instalado:**
   ```powershell
   python --version
   ```
   *(Debe responder Python 3.11 o superior, por ejemplo Python 3.14)*.

2. **Instalar las dependencias oficiales del proyecto:**
   ```powershell
   pip install -r requirements.txt
   ```
   *(Esto instalara antlr4-python3-runtime, pandas, numpy y matplotlib)*.

3. **Compilar la gramatica ANTLR4 (Generar los analizadores en Python):**
   ```powershell
   python run_tests.py --grammar
   ```
   *(O alternativamente: `antlr4 -Dlanguage=Python3 -visitor -o src/generated grammar/HolocronDSL.g4`)*.

---

### Paso 2: Como ejecutar los ejemplos de HolocronDSL
Los archivos con extension `.holo` (como `examples/01_telemetria_cazas.holo`) contienen codigo escrito en nuestro lenguaje. 

Para ejecutarlos y analizarlos, puedes usar el script rapido `holocron.py` ubicado en la raiz o el script controlador `src/cli.py`:

1. **Validar si un programa esta bien escrito (sin errores sintacticos):**
   ```powershell
   python holocron.py examples/01_telemetria_cazas.holo --check
   ```
   *(O tambien: `python src/cli.py examples/01_telemetria_cazas.holo --check`)*.
   *Respuesta esperada:*
   `Sintaxis verificada con exito: la Fuerza fluye en perfecta armonia.`

2. **Ver como la computadora entiende la estructura de tu codigo (Arbol Sintactico):**
   ```powershell
   python src/cli.py examples/01_telemetria_cazas.holo --tree
   ```
   *Respuesta esperada:* Un diagrama visual que muestra cada sentencia, operacion y token reconocido en el programa.

3. **Ver la notacion jerarquica LISP (parentizada):**
   ```powershell
   python src/cli.py examples/01_telemetria_cazas.holo --lisp
   ```

4. **Probar una linea de codigo directamente en la terminal:**
   ```powershell
   python src/cli.py --codigo "cazas = abrir_holocron \"flota.csv\" |> purgar donde escudos > 50" --tree
   ```

---

### Paso 3: Como ejecutar las pruebas (juntas o por separado)
El proyecto incluye un script gestor (`run_tests.py`) que te permite correr pruebas facilmente:

#### Para ejecutar todas las pruebas a la vez:
```powershell
python run_tests.py
```
*(O si deseas que ademas valide todos los archivos `.holo` de la carpeta examples: `python run_tests.py --all`)*.

#### Para ejecutar las pruebas por separado:
* **Solo el analizador lexico (palabras reservadas, numeros, operadores):**
  ```powershell
  python run_tests.py --lexer
  ```
* **Solo la sintaxis de programas validos (pipelines, agregaciones, hologramas):**
  ```powershell
  python run_tests.py --parser
  ```
* **Solo las pruebas de captura y reporte de errores sintacticos:**
  ```powershell
  python run_tests.py --invalid
  ```
* **Verificar todos los archivos de ejemplo en `examples/`:**
  ```powershell
  python run_tests.py --examples
  ```

---

### Paso 4: (Opcional) Usando el `Makefile`
Si estas en Linux, macOS, WSL o tienes la herramienta `make` instalada:
```bash
make help            # Lista todos los comandos disponibles
make test            # Ejecuta todas las pruebas
make test-lexer      # Solo pruebas lexicas
make test-parser     # Solo pruebas sintacticas validas
make test-invalid    # Solo pruebas de errores
make check-examples  # Valida los 5 ejemplos .holo
make clean           # Limpia archivos de cache
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
