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

## 3. Estructura del Repositorio

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

## 4. Estado de Avance por Fases (Cortes)

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
