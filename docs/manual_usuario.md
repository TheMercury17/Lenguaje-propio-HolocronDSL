# Manual de Usuario: HolocronDSL

**Lenguaje de Dominio Específico para Ciencia de Datos y Visualización**  
**Universidad Sergio Arboleda**  
**Programa de Ciencias de la Computación e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programación y Transducción (Semestre 2026-2)  
**Docente:** Joaquín F. Sánchez  
**Equipo de Desarrollo (Grupo 5):**  
- Andrés Sebastián Coral Vallejo  
- Carol Arenas Cardona  

---

## 1. Introducción y Propósito

HolocronDSL es un Lenguaje de Dominio Específico (DSL) declarativo y funcional diseñado para construir flujos reproducibles de ingestión, depuración, transformación, modelado estadístico y proyección visual de conjuntos de datos.

A diferencia de los lenguajes de propósito general, HolocronDSL adopta una sintaxis expresiva basada en el encadenamiento funcional mediante el operador pipeline (`|>`), garantizando la inmutabilidad de los datos intermedios y permitiendo que tanto analistas como desarrolladores expresen transformaciones complejas en pocas líneas de código legible.

---

## 2. Requisitos del Sistema e Instalación

El lenguaje se encuentra construido sobre Python 3 y ANTLR4, y está diseñado para operar de manera nativa en entornos Linux (especialmente distribuciones basadas en Debian como Kali Linux y Ubuntu) y sistemas Microsoft Windows.

### 2.1 Requisitos Previos
- **Python:** Versión 3.10 o superior (compatible y verificado en Python 3.11, 3.12 y 3.13).
- **Manejador de paquetes:** `pip`.
- **Entorno de ejecución:** Terminal de comandos (Bash, Zsh o PowerShell).
- **Herramientas opcionales:** `make` para automatización de tareas y `libreoffice` para visualización inmediata de reportes `.xls` generados.

### 2.2 Instalación en Linux / Kali Linux

Para preparar el entorno de ejecución en una distribución Linux (como Kali Linux en VirtualBox):

1. **Clonar o descomprimir el repositorio:**
   ```bash
   git clone https://github.com/TheMercury17/Lenguaje-propio-HolocronDSL.git
   cd Lenguaje-propio-HolocronDSL
   ```

2. **Crear y activar un entorno virtual de Python (Recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias del proyecto:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   *Nota:* En caso de disponer de la herramienta `make`, se puede ejecutar directamente:
   ```bash
   make install
   ```

4. **Verificar la instalación ejecutando la suite de pruebas automatizadas:**
   ```bash
   make test
   # o alternativamente:
   python3 run_tests.py --all
   ```
   El sistema confirmará la ejecución exitosa de las 69 pruebas unitarias e integrales.

### 2.3 Instalación en Windows

1. Abrir una consola de PowerShell o Command Prompt en la carpeta del proyecto.
2. Crear y activar el entorno virtual:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Instalar las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
4. Comprobar el funcionamiento:
   ```powershell
   python run_tests.py --all
   ```

---

## 3. Modos de Ejecución desde la Línea de Comandos (CLI)

El proyecto ofrece dos puntos de entrada equivalentes: el comando directo `python3 holocron.py` o el módulo del compilador `python3 -m src.cli`.

### 3.1 Sintaxis General
```bash
python3 holocron.py <archivo.holo> [opciones]
```

### 3.2 Opciones y Modos Disponibles

| Opción / Flag | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| *(Por defecto)* | Ejecuta e interpreta completamente el programa, realizando transformaciones, cálculos y generando archivos. | `python3 holocron.py examples/01_telemetria_cazas.holo` |
| `--check` | Realiza únicamente la verificación léxica y sintáctica sin ejecutar transformaciones en disco. Ideal para validación rápida. | `python3 holocron.py programa.holo --check` |
| `--tree` | Muestra el árbol de análisis sintáctico (CST/AST) en formato jerárquico indentado legible. | `python3 holocron.py programa.holo --tree` |
| `--lisp` | Imprime la representación del árbol sintáctico en notación LISP / S-Expression. | `python3 holocron.py programa.holo --lisp` |
| `--verbose` | Muestra mensajes detallados de depuración durante las fases de análisis y evaluación. | `python3 holocron.py programa.holo --verbose` |
| `--tokens` | Imprime la secuencia completa de tokens reconocidos por el analizador léxico. | `python3 holocron.py programa.holo --tokens` |

### 3.3 Automatización con Makefile

En sistemas Linux con la utilidad `make` instalada, se dispone de los siguientes objetivos directos:

- `make help`: Despliega el catálogo de instrucciones y comandos disponibles.
- `make test`: Ejecuta la totalidad de pruebas automatizadas (69 pruebas).
- `make check-examples`: Valida sintácticamente todos los programas de ejemplo `.holo`.
- `make run-examples`: Ejecuta todos los programas de ejemplo produciendo sus salidas en `salidas/`.
- `make clean`: Elimina archivos temporales, cachés de Python y registros generados.

---

## 4. Referencia Completa del Lenguaje

### 4.1 Comentarios
Los comentarios permiten documentar el código y son omitidos por el compilador:
- **Comentario de una línea:** Se inicia con dos guiones consecutivos (`--`).
  ```holocron
  -- Este es un comentario explicativo
  ```
- **Comentario de bloque:** Delimitado por `/*` y `*/`.
  ```holocron
  /*
     Comentario que abarca
     multiples lineas de texto.
  */
  ```

### 4.2 Ingestión de Datos (`abrir_holocron`)
Permite cargar un conjunto de datos tabulares desde un archivo CSV.
```holocron
flota = abrir_holocron "datos/naves.csv"
telemetria = abrir_holocron "datos/sensores.csv" delimitado_por ";"
```

### 4.3 Operador de Pipeline (`|>`)
Permite encadenar transformaciones de datos de forma fluida e inmutable. Cada etapa recibe la tabla resultante de la etapa anterior y entrega una nueva tabla con la modificación aplicada.

### 4.4 Operaciones de Transformación en Pipeline

#### A. Selección de Columnas (`revelar`)
Aísla las variables o columnas que se desean conservar en el conjunto de datos.
```holocron
naves_reducidas = flota |> revelar [modelo, escudos, velocidad]
```

#### B. Filtrado Condicional (`purgar donde`)
Filtra registros que satisfacen una expresión lógica y relacional.
```holocron
naves_combate = flota |> purgar donde escudos > 100 y estado == "Operativo"
```

#### C. Creación de Variables Calculadas (`forjar`)
Añade una nueva columna calculada a partir de expresiones aritméticas entre columnas existentes o constantes numéricas.
```holocron
flota_potenciada = flota |> forjar poder_fuego = (armas * 1.5) + escudos
```

#### D. Ordenamiento de Filas (`ordenar por`)
Reordena las filas según los valores de una columna en orden ascendente o descendente.
```holocron
flota_ordenada = flota |> ordenar por velocidad descendente
```

#### E. Eliminación de Duplicados (`eliminar_clones`)
Elimina filas duplicadas idénticas para asegurar la unicidad de las observaciones.
```holocron
flota_unica = flota |> eliminar_clones
```

#### F. Saneamiento de Valores Nulos (`sanar_vacios con`)
Reemplaza celdas vacías o nulas por un valor predeterminado especificado.
```holocron
flota_limpia = flota |> sanar_vacios con 0
```

#### G. Agrupamiento y Resumen Estadístico (`agrupar por` / `resumir`)
Segmenta el conjunto por una o varias columnas y aplica funciones de agregación para obtener un resumen estadístico tabular.
```holocron
resumen_sector = flota
    |> agrupar por [sector]
    |> resumir total_naves = recuento(),
               escudo_promedio = equilibrio(escudos),
               escudo_maximo = cenit(escudos),
               escudo_minimo = nadir(escudos),
               potencia_total = acumular(poder_fuego)
```

**Funciones de agregación disponibles:**
- `recuento()` o `conteo()`: Cuenta el número de filas del grupo.
- `acumular(col)` o `suma(col)`: Sumatoria de los valores de la columna.
- `equilibrio(col)` o `promedio(col)`: Media aritmética.
- `mediana(col)`: Mediana estadística.
- `cenit(col)` o `maximo(col)`: Valor máximo.
- `nadir(col)` o `minimo(col)`: Valor mínimo.
- `desviacion(col)`: Desviación estándar muestral.

---

## 5. Modelado Estadístico: Regresión Lineal Simple (`trazar_regresion`)

HolocronDSL cuenta con un motor nativo para estimar modelos de regresión lineal simple por el método de Mínimos Cuadrados Ordinarios (OLS), sin requerir librerías externas de aprendizaje automático.

### 5.1 Sintaxis en Pipeline
```holocron
modelo = tabla_datos
    |> trazar_regresion [
        eje_x = "nombre_columna_x",
        eje_y = "nombre_columna_y",
        destino = "nombre_columna_prediccion"
    ]
```

### 5.2 Parámetros
- `eje_x`: Nombre de la columna que actúa como variable independiente o predictora.
- `eje_y`: Nombre de la columna que actúa como variable dependiente o respuesta.
- `destino` *(Opcional)*: Nombre de la columna donde se almacenarán los valores ajustados predichos ($\hat{y}$). Si se omite, se asigna por defecto `prediccion`.

### 5.3 Información Calculada por el Modelo
Al ejecutar `trazar_regresion`, el lenguaje calcula internamente:
- **Pendiente ($m$):** Razón de cambio marginal.
- **Intercepto ($b$):** Valor esperado de $y$ cuando $x = 0$.
- **Coeficiente de determinación ($R^2$):** Proporción de la varianza explicada ($0 \le R^2 \le 1$).
- **Coeficiente de correlación de Pearson ($r$):** Intensidad y sentido de la relación lineal ($-1 \le r \le 1$).
- **Residuos:** Diferencia puntual entre el valor real y el estimado ($y_i - \hat{y}_i$).

Al transmitir el modelo con `transmitir modelo`, el lenguaje imprime en consola un resumen formateado del ajuste y la tabla extendida con las predicciones.

---

## 6. Proyección de Visualizaciones Holográficas (`proyectar_holograma`)

El motor de gráficos de HolocronDSL genera imágenes matriciales en formato PNG de alta resolución (300 DPI) utilizando una paleta temática oscura táctica. Por diseño estricto y para garantizar compatibilidad multiplataforma, **no se utiliza formato vectorial SVG**.

### 6.1 Tipos de Gráficos Disponibles

| Tipo | Descripción | Parámetros Requeridos |
| :--- | :--- | :--- |
| `barras` | Compara valores numéricos a través de categorías discretas. | `eje_x` (categoría), `eje_y` (métrica). |
| `histograma` | Analiza la distribución de frecuencias de una variable numérica continua. | `eje_x` (métrica numérica). |
| `caja` | Diagrama de caja y bigotes (boxplot) que expone cuartiles, mediana y dispersión. | `eje_y` (métrica numérica). |
| `lineas` | Representa la evolución o tendencia de una serie de observaciones ordenadas. | `eje_x` (índice o categoría), `eje_y` (métrica). |
| `regresion` o `tendencia` | Diagrama de dispersión de puntos empíricos con la recta de regresión lineal ajustada superpuesta. | `eje_x` (variable independiente), `eje_y` (variable dependiente). |

### 6.2 Propiedades Configurables en el Bloque
- `titulo`: Texto del encabezado de la gráfica.
- `eje_x`: Columna asignada al eje horizontal.
- `eje_y`: Columna asignada al eje vertical.
- `etiqueta_x`: *(Opcional)* Título personalizado para el eje horizontal.
- `etiqueta_y`: *(Opcional)* Título personalizado para el eje vertical.
- `paleta`: *(Opcional)* Esquema cromático (`galactica`, `defecto`).
- `guardar_en`: Ruta relativa o absoluta del archivo PNG a generar.

### 6.3 Ejemplo de Proyección
```holocron
proyectar_holograma barras resumen_sectores [
    titulo = "Latencia Media por Sector",
    eje_x = "sector",
    eje_y = "latencia_media",
    guardar_en = "salidas/grafico_barras.png"
]

proyectar_holograma regresion datos_red [
    titulo = "Modelo de Regresion: Distancia vs Latencia",
    eje_x = "distancia_parsecs",
    eje_y = "latencia_ms",
    guardar_en = "salidas/grafico_regresion.png"
]
```

---

## 7. Exportación y Persistencia de Resultados

### 7.1 Exportación a CSV
Permite almacenar cualquier conjunto de datos en un archivo de texto delimitado por comas:
```holocron
archivar_holocron tabla_resultados en "salidas/reporte.csv"
```

### 7.2 Exportación a Excel Nativo (.xls)
HolocronDSL cuenta con un motor de serialización nativo para generar hojas de cálculo compatibles con Microsoft Excel y LibreOffice Calc utilizando el estándar **XML Spreadsheet 2003**, sin necesidad de bibliotecas externas pesadas:
```holocron
archivar_holocron tabla_resultados en "salidas/reporte.xls"
```
El sistema detecta automáticamente la extensión `.xls` y escribe un libro de cálculo con celdas tipadas numéricas y de texto, garantizando la creación de directorios destino si no existen previamente.

---

## 8. Funciones Modulares (`mision`) y Estructuras de Control (`evaluar_fuerza`)

### 8.1 Definición de Misiones (Funciones)
Las misiones encapsulan lógica de cálculo o transformación reutilizable:
```holocron
mision calcular_eficiencia(velocidad, consumo)
    evaluar_fuerza (consumo > 0)
        senda_luminosa:
            retornar velocidad / consumo
        senda_oscura:
            retornar 0
    fin_evaluar
fin_mision

rendimiento = calcular_eficiencia(1200, 40)
```

### 8.2 Transmisión de Mensajes (`transmitir`)
Permite imprimir en consola cadenas literales, números, variables o tablas con formato ASCII tabulado:
```holocron
transmitir "Analisis finalizado exitosamente."
transmitir tabla_resultados
```

---

## 9. Diagnóstico y Resolución de Errores

HolocronDSL ofrece mensajes de error descriptivos con indicación precisa de la línea y la columna donde ocurrió la anomalía:

### 9.1 Errores Léxicos y Sintácticos
- **Causa común:** Carácter no reconocido, corchete o paréntesis sin cerrar, palabra reservada mal escrita o falta del operador de asignación (`=`).
- **Mensaje típico en consola:**
  ```text
  [Error Sintactico] Linea 14, Columna 8: Se encontro 'agrupar' pero se esperaba un identificador o sentencia valida.
  ```
- **Solución:** Verificar que las instrucciones estén precedidas por el operador pipeline `|>` cuando correspondan a transformaciones encadenadas.

### 9.2 Errores Semánticos
- **Variable no definida (`VariableNoDefinidaError`):** Se intenta utilizar una variable antes de ser asignada.
- **Columna no existente (`ColumnaNoExisteError`):** Se hace referencia a un nombre de columna que no pertenece a la tabla actual. Verificar mayúsculas y minúsculas (el lenguaje es sensible a la capitalización).
- **Tipos incompatibles (`TipoIncompatibleError`):** Se intenta realizar una operación aritmética o relacional entre tipos no compatibles (por ejemplo, comparar un número con una cadena de texto).
- **División por cero (`DivisionPorCeroError`):** Una expresión calculada genera una división entre cero. Se recomienda utilizar condicionales o reemplazar valores con `sanar_vacios`.
