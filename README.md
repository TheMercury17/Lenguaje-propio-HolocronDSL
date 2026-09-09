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

## 2. Estructura del Repositorio

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
│   └── manual_programacion.md      # Manual tutorial intuitivo para principiantes
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

## 3. Requisitos y Configuracion del Entorno

### Requisitos Previos
- Python 3.11 o superior (probado en Python 3.14).
- `antlr4-tools` y `antlr4-python3-runtime` (version 4.13.2).
- Bibliotecas para analisis de datos: `pandas`, `numpy` y `matplotlib`.

### Instalacion de Dependencias
```bash
pip install -r requirements.txt
```

### Compilacion de la Gramatica (Generacion de Codigo)
Para regenerar los analizadores lexicos y sintacticos a partir del archivo `.g4`, ejecute:
```bash
antlr4 -Dlanguage=Python3 -visitor -o src/generated grammar/HolocronDSL.g4
```
*(Tambien disponible con `make grammar` o `python run_tests.py --grammar`).*

---

## 4. Automatizacion de Pruebas (Makefile y Gestor Multiplataforma)

El proyecto ofrece tres formas equivalentes y comodas para ejecutar las pruebas, adaptandose a cualquier sistema operativo:

### Opcion A: Usando el `Makefile` (Recomendado para entornos Linux, macOS o WSL)
```bash
make help            # Despliega la lista de comandos disponibles
make test            # Ejecuta la suite completa de pruebas unitarias
make test-lexer      # Ejecuta solo las pruebas del analizador lexico
make test-parser     # Ejecuta solo las pruebas sintacticas validas
make test-invalid    # Ejecuta solo las pruebas sintacticas negativas
make check-examples  # Valida todos los ejemplos .holo de examples/
make clean           # Limpia los caches de Python
```

### Opcion B: Usando el Gestor Python `run_tests.py` (Recomendado para Windows)
No requiere tener `make` instalado en el sistema:
```bash
python run_tests.py              # Ejecuta toda la suite de pruebas unitarias
python run_tests.py --all        # Ejecuta pruebas y valida todos los ejemplos
python run_tests.py --lexer      # Ejecuta solo pruebas lexicas
python run_tests.py --parser     # Ejecuta solo pruebas sintacticas validas
python run_tests.py --invalid    # Ejecuta solo pruebas sintacticas de error
python run_tests.py --examples   # Valida sintaxis de los archivos de ejemplo
python run_tests.py --grammar    # Recompila la gramatica con ANTLR4
```

### Opcion C: Ejecucion Manual por Separado con Python puro
Si prefieres ejecutar cada prueba directamente con el modulo `unittest` de Python:
```bash
# Ejecutar suite completa
python -m unittest discover -s tests

# Ejecutar pruebas por separado
python -m unittest tests/test_lexer.py
python -m unittest tests/test_parser_valid.py
python -m unittest tests/test_parser_invalid.py
```

---

## 5. Guia de Ejecucion del Front-end

El sistema incluye una herramienta de linea de comandos (`src/cli.py`) que permite escanear archivos `.holo`, validar su sintaxis y generar representaciones visuales del arbol de analisis (CST).

### Validacion Rapida de Sintaxis
```bash
python src/cli.py examples/01_telemetria_cazas.holo --check
```

### Visualizacion Jerarquica del Arbol Sintactico
```bash
python src/cli.py examples/01_telemetria_cazas.holo --tree
```

### Visualizacion en Notacion Parentizada (LISP)
```bash
python src/cli.py examples/01_telemetria_cazas.holo --lisp
```

### Analisis de Codigo en Linea
```bash
python src/cli.py --codigo "cazas = abrir_holocron \"flota.csv\" |> purgar donde escudos > 50" --tree
```

---

## 6. Estado de Avance por Fases (Cortes)

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
