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
- El flujo de transformacion se modela mediante un operador de pipeline hiperespacial (`==>`).
- Las variables se vinculan con el operador de canalizacion (`<-`).
- La depuracion de registros utiliza primitivas declarativas como `purgar_donde`, `eliminar_clones` y `sanar_vacios`.
- La generacion de nuevas variables se realiza mediante la clausula `forjar_cristal`.
- Las visualizaciones graficas se declaran como **proyecciones holograficas** (`proyectar_holograma`).
- El lenguaje cuenta con abstraccion funcional (`mision`) y bifurcaciones condicionales (`evaluar_fuerza` con `senda_luminosa` y `senda_oscura`).

Esta arquitectura garantiza una originalidad absoluta frente a otros lenguajes convencionales (evitando patrones directos de C++, Java o Python) y proporciona una separacion estricta entre la sintaxis formal (definida en ANTLR4) y la ejecucion semantica en Python.

---

## 2. Estructura del Repositorio

```text
Lenguaje propio/
├── .gitignore                      # Exclusion de archivos temporales y caches
├── README.md                       # Documentacion principal del proyecto
├── requirements.txt                # Dependencias oficiales de Python
├── grammar/
│   └── HolocronDSL.g4              # Especificacion lexica y sintactica en ANTLR4
├── docs/
│   ├── alcance.md                  # Documento de alcance y delimitacion formal
│   ├── catalogo_instrucciones.md   # Catalogo de palabras reservadas y semantica
│   └── gramatica_ebnf.md           # Gramatica formal en notacion EBNF
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
│   └── 04_mision_avanzada.holo     # Abstraccion con misiones y evaluacion condicional
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

---

## 4. Guia de Ejecucion del Front-end

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
python src/cli.py --codigo "cazas <- abrir_holocron \"flota.csv\" ==> purgar_donde escudos > 50" --tree
```

---

## 5. Ejecucion de la Suite de Pruebas

El proyecto cuenta con 21 pruebas automatizadas que cubren el analisis lexico, las estructuras sintacticas validas y la captura diagnostica de errores.

Para ejecutar la suite completa:
```bash
python -m unittest discover -s tests
```

Para ejecutar modulos individuales de prueba:
```bash
python -m unittest tests/test_lexer.py
python -m unittest tests/test_parser_valid.py
python -m unittest tests/test_parser_invalid.py
```

---

## 6. Estado de Avance por Fases (Cortes)

- **Fase 1: Especificacion y Front-end del Lenguaje (Completada):**
  - Delimitacion del dominio, documento de alcance y catalogo de instrucciones.
  - Gramatica formal en EBNF y gramatica unificada ANTLR4 (`HolocronDSL.g4`).
  - Generador de Lexer y Parser en Python con ANTLR 4.13.2.
  - Manejador de errores de sintaxis personalizado con reporte preciso de linea y columna.
  - Interfaz CLI funcional para inspeccion del arbol sintactico.
  - Ejemplos galacticos documentados y suite de pruebas unitarias al 100% de aprobacion.

- **Fase 2: Semantica y Procesamiento de Datos (Proxima entrega):**
  - Implementacion del patron Visitor en Python.
  - Tabla de simbolos y contextos de ejecucion de variables y funciones.
  - Integracion del motor de ejecucion sobre pandas y NumPy.

- **Fase 3: Visualizacion, Integracion y Producto Final:**
  - Motor de visualizacion sobre Matplotlib para proyecciones graficas (PNG).
  - Caso de estudio integral con datos reales y reporte final.
