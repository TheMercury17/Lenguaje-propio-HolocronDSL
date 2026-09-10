# Piedra Rosetta: Tabla Comparativa y de Traduccion de HolocronDSL

**Universidad Sergio Arboleda**  
**Programa de Ciencias de la Computacion e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programacion y Transduccion (2026-2)  
**Equipo de Desarrollo (Grupo 5):**  
- Andres Sebastian Coral Vallejo  
- Carol Arenas Cardona  

---

## 1. Proposito de este Documento

Historicamente, la **Piedra de Rosetta** permitio a los egiptologos descifrar los jeroglificos del Antiguo Egipto al presentar el mismo decreto grabado en tres escrituras distintas: jeroglificos, demotico y griego antiguo.

En la teoria de lenguajes de programacion y transduccion, una **Piedra Rosetta** es un documento academico de referencia comparativa que expone las mismas operaciones de computacion expresadas en los paradigmas dominantes de la industria.

Este documento establece la equivalencia directa entre:
1. **La Operacion Conceptual:** Que transformacion matematica o de datos se desea realizar.
2. **Python con pandas:** El estandar de la industria para manipulacion de datos en entornos generales.
3. **R con dplyr:** El lenguaje funcional pionero en encadenamiento declarativo de pipelines (`%>%` / `|>`).
4. **SQL ANSI:** El estandar universal declarativo para bases de datos relacionales.
5. **HolocronDSL:** Nuestro lenguaje de dominio especifico declarativo inspirado en Star Wars.

---

## 2. Matriz General de Equivalencias

| Concepto / Operacion | Python (pandas) | R (dplyr / readr) | SQL ANSI | HolocronDSL (Star Wars) |
| :--- | :--- | :--- | :--- | :--- |
| **Cargar archivo CSV** | `df = pd.read_csv("datos.csv")` | `df <- read_csv("datos.csv")` | `FROM datos` | `df = abrir_holocron "datos.csv"` |
| **Configurar separador** | `sep=","` | `delim=","` | N/A | `delimitado_por ","` |
| **Asignacion de variable** | `=` | `<-` o `=` | N/A | `=` |
| **Operador de Pipeline** | `.pipe(...)` | `%>%` o `\|>` | Subconsultas encadenadas | `\|>` (o `>>`) |
| **Seleccionar Columnas** | `df[['a', 'b']]` | `select(a, b)` | `SELECT a, b` | `revelar [a, b]` |
| **Filtrar Filas** | `df[df['x'] > 10]` | `filter(x > 10)` | `WHERE x > 10` | `purgar donde x > 10` |
| **Conector Logico Y (AND)** | `&` | `&` | `AND` | `y` (o `y_fuerza`) |
| **Conector Logico O (OR)** | `\|` | `\|` | `OR` | `o` (o `o_fuerza`) |
| **Conector Logico NO (NOT)**| `~` | `!` | `NOT` | `no` (o `no_fuerza`) |
| **Crear / Modificar Columna**| `df['total'] = df['p'] * df['u']` | `mutate(total = p * u)` | `p * u AS total` | `forjar total = p * u` |
| **Ordenar Registros** | `df.sort_values('x', ascending=False)` | `arrange(desc(x))` | `ORDER BY x DESC` | `ordenar por x descendente` |
| **Eliminar Duplicados** | `df.drop_duplicates()` | `distinct()` | `SELECT DISTINCT` | `eliminar_clones` |
| **Tratar Nulos (Rellenar)** | `df.fillna(0)` | `replace_na(list(x = 0))` | `COALESCE(x, 0)` | `sanar_vacios con 0` |
| **Tratar Nulos (Descartar)** | `df.dropna()` | `drop_na()` | `WHERE x IS NOT NULL` | `sanar_vacios descartar` |
| **Agrupar por Categorias** | `df.groupby(['cat'])` | `group_by(cat)` | `GROUP BY cat` | `agrupar por [cat]` |
| **Resumir Indicadores** | `.agg(...)` | `summarise(...)` | Funciones agregadas en `SELECT` | `resumir ...` |
| **Conteo de Registros** | `df.count()` | `n()` | `COUNT(*)` | `recuento()` |
| **Suma Total** | `df['x'].sum()` | `sum(x)` | `SUM(x)` | `acumular(x)` |
| **Media / Promedio** | `df['x'].mean()` | `mean(x)` | `AVG(x)` | `equilibrio(x)` |
| **Mediana Estadistica** | `df['x'].median()` | `median(x)` | `MEDIAN(x)` / `PERCENTILE_CONT(0.5)` | `mediana(x)` |
| **Valor Maximo** | `df['x'].max()` | `max(x)` | `MAX(x)` | `cenit(x)` |
| **Valor Minimo** | `df['x'].min()` | `min(x)` | `MIN(x)` | `nadir(x)` |
| **Desviacion Estandar** | `df['x'].std()` | `sd(x)` | `STDDEV(x)` | `desviacion(x)` |
| **Guardar Resultados CSV** | `df.to_csv("salida.csv")` | `write_csv(df, "salida.csv")` | `INTO OUTFILE "salida.csv"` | `archivar_holocron df en "salida.csv"` |
| **Grafico de Barras** | `df.plot(kind='bar')` | `geom_bar()` | N/A | `holograma barras df` |
| **Grafico de Lineas** | `df.plot(kind='line')` | `geom_line()` | N/A | `holograma lineas df` |
| **Grafico de Dispersion** | `df.plot(kind='scatter')` | `geom_point()` | N/A | `holograma dispersion df` |
| **Histograma** | `df.plot(kind='hist')` | `geom_histogram()` | N/A | `holograma histograma df` |
| **Grafico de Cajas** | `df.plot(kind='box')` | `geom_boxplot()` | N/A | `holograma caja df` |
| **Condicional Logico** | `if condicion: ... else: ...` | `if (cond) { ... } else { ... }` | `CASE WHEN ... THEN ... END` | `evaluar_fuerza ... senda_luminosa ... fin_evaluar` |
| **Definicion de Funciones** | `def mi_funcion(x): ...` | `mi_funcion <- function(x) { ... }` | `CREATE FUNCTION ...` | `mision mi_mision (x) ... retornar y fin_mision` |
| **Impresion en Consola** | `print(...)` | `print(...)` / `cat(...)` | `SELECT 'mensaje'` | `mostrar ...` / `transmitir ...` |
| **Comentarios de Linea** | `# comentario` | `# comentario` | `-- comentario` | `-- comentario` (soporta `#` y `//`) |
| **Comentarios de Bloque** | `""" bloque """` | N/A | `/* bloque */` | `/- bloque -/` (soporta `/* */`) |
| **Literales Booleanos** | `True`, `False` | `TRUE`, `FALSE` | `TRUE`, `FALSE` | `cierto_es`, `falso_es` (o `verdadero`, `falso`) |

---

## 3. Comparativa Practica: Un Mismo Flujo en los 3 Estandares y HolocronDSL

Para observar con claridad la diferencia de expresividad y diseño, analicemos el mismo flujo de datos resuelto en los tres estandares consolidados y en **HolocronDSL**:

### Problema de Negocio:
> Cargar un conjunto de datos de telemetria de naves, seleccionar atributos clave, purgar aquellas con escudos inactivos (cero o menor), calcular el indice de poder de fuego, agrupar por faccion, calcular el promedio de escudos y el maximo poder de fuego, y exportar la tabla resumen a un archivo CSV.

---

### Solucion 1: Python con pandas (Paradigma Orientado a Objetos e Indexacion)
```python
import pandas as pd

# Ingestion
flota = pd.read_csv("datos/telemetria.csv")

# Preparacion y transformacion
flota_limpia = flota[['modelo', 'faccion', 'escudos', 'victorias']]
flota_limpia = flota_limpia[flota_limpia['escudos'] > 0]
flota_limpia['poder_fuego'] = flota_limpia['victorias'] * 15 + flota_limpia['escudos'] / 2

# Agrupamiento y agregacion
resumen = flota_limpia.groupby('faccion').agg(
    promedio_defensa=('escudos', 'mean'),
    max_ataque=('poder_fuego', 'max')
).reset_index()

# Exportacion
resumen.to_csv("salidas/resumen_facciones.csv", index=False)
print("Analisis de flota finalizado")
```

---

### Solucion 2: R con dplyr (Paradigma Funcional con Pipes)
```r
library(dplyr)
library(readr)

# Ingestion y pipeline funcional
flota <- read_csv("datos/telemetria.csv")

resumen <- flota %>%
  select(modelo, faccion, escudos, victorias) %>%
  filter(escudos > 0) %>%
  mutate(poder_fuego = victorias * 15 + escudos / 2) %>%
  group_by(faccion) %>%
  summarise(
    promedio_defensa = mean(escudos),
    max_ataque = max(poder_fuego)
  )

# Exportacion
write_csv(resumen, "salidas/resumen_facciones.csv")
cat("Analisis de flota finalizado\n")
```

---

### Solucion 3: SQL ANSI (Paradigma Relacional Declarativo)
```sql
-- Creacion de tabla intermedia con transformaciones y agregacion agrupada
WITH flota_filtrada AS (
    SELECT 
        modelo, 
        faccion, 
        escudos, 
        victorias,
        (victorias * 15 + escudos / 2.0) AS poder_fuego
    FROM telemetria
    WHERE escudos > 0
)
SELECT 
    faccion,
    AVG(escudos) AS promedio_defensa,
    MAX(poder_fuego) AS max_ataque
FROM flota_filtrada
GROUP BY faccion;
```

---

### Solucion 4: HolocronDSL (Lenguaje de Dominio Especifico Galactico)
```holocron
-- Ingestion del holocron de datos
flota = abrir_holocron "datos/telemetria.csv"

-- Pipeline fluido de preparacion y calculo
flota_activa = flota
    |> revelar [ modelo, faccion, escudos, victorias ]
    |> purgar donde escudos > 0
    |> forjar poder_fuego = victorias * 15 + escudos / 2

-- Agrupamiento por sector y sintesis de indicadores descriptivos
resumen = flota_activa
    |> agrupar por [ faccion ]
    |> resumir
        promedio_defensa = equilibrio(escudos),
        max_ataque = cenit(poder_fuego)

-- Persistencia en disco y notificacion
archivar_holocron resumen en "salidas/resumen_facciones.csv"
mostrar "Analisis de flota finalizado"
```

---

## 4. Ventajas de Diseño de HolocronDSL

1. **Simplicidad Declarativa:**
   A diferencia de Python con pandas, no requiere gestionar indices (`.reset_index()`), ni sintaxis redundante de indexacion booleana (`df[df['col'] > 0]`).
2. **Encadenamiento Natural:**
   Adopta la elegancia del conector de pipeline funcional (`|>`), evitando el anidamiento complejo de subconsultas como en SQL.
3. **Vocabulario Tematico Coherente:**
   Las operaciones reflejan de manera intuitiva el dominio:
   - `abrir_holocron` / `archivar_holocron` para lectura y escritura.
   - `purgar donde` para filtrado.
   - `forjar` para calculo de columnas.
   - `equilibrio` (media), `cenit` (maximo) y `nadir` (minimo) como funciones estadisticas elegantes y naturales.
   - `holograma` para proyecciones visuales de datos.
