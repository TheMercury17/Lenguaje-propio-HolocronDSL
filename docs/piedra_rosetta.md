# Piedra Rosetta: Tabla de Traduccion y Equivalencias de HolocronDSL

**Universidad Sergio Arboleda**  
**Programa de Ciencias de la Computacion e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programacion y Transduccion (2026-2)  
**Equipo de Desarrollo (Grupo 5):**  
- Andres Sebastian Coral Vallejo  
- Carol Arenas Cardona  

---

## 1. Proposito de este Documento

Historicamente, la **Piedra de Rosetta** permitio a los egiptologos descifrar los jeroglificos del Antiguo Egipto al presentar el mismo decreto grabado en tres escrituras distintas: jeroglificos, demotico y griego antiguo.

En la teoria de lenguajes de programacion y compiladores, una **Piedra Rosetta** es un documento de referencia comparativa que expone las mismas operaciones de computacion expresadas en multiples lenguajes y paradigmas.

Este documento establece la equivalencia directa entre:
1. **La Operacion Conceptual:** Que transformacion matematica o de datos se desea realizar.
2. **Python + pandas:** El estandar de facto en la industria de la ciencia de datos.
3. **SQL / R (dplyr):** El paradigma relacional y funcional clasico.
4. **El Lenguaje de Referencia ("Lenguaje Momo/Grasa"):** Implementacion del repositorio de referencia estudiantil.
5. **HolocronDSL:** Nuestro lenguaje formal, declarativo e inspirado en Star Wars.

Esta matriz demuestra que **HolocronDSL no solo tiene un equivalente absoluto para cada caracteristica existente en el lenguaje de referencia**, sino que **incorpora capacidades avanzadas adicionales exigidas en la especificacion del curso** (como eliminacion de duplicados, saneamiento de nulos y abstraccion de funciones mediante misiones), conservando una originalidad absoluta de diseño y sintaxis.

---

## 2. Matriz General de Equivalencias

| Concepto / Operacion | Python (pandas) | SQL / R (dplyr) | Lenguaje de Referencia (Momo) | HolocronDSL (Star Wars) |
| :--- | :--- | :--- | :--- | :--- |
| **Cargar archivo CSV** | `df = pd.read_csv("datos.csv")` | `read_csv("datos.csv")` | `pasa_el_pack "datos.csv" XD` | `df = abrir_holocron "datos.csv"` |
| **Configurar separador** | `sep=","` | `sep=","` | `separador ","` | `delimitado_por ","` |
| **Operador de Asignacion** | `=` | `<-` / `=` | `=` | `=` |
| **Operador de Pipeline** | Encadenamiento con puntos `.pipe()` | `%>%` o `\|>` | `\|:v>` o `\|>` | `\|>` (o `>>`) |
| **Terminador de Sentencia** | Salto de linea | Salto de linea / `;` | `XD` obligatorio | Salto de linea limpio (sin terminador artificial) |
| **Seleccionar Columnas** | `df[['a', 'b']]` | `SELECT a, b` / `select(a, b)` | `escojo_a [a, b]` / `escojo_a_los_papus` | `revelar [a, b]` |
| **Filtrar Filas** | `df[df['x'] > 10]` | `WHERE x > 10` / `filter(x > 10)` | `but_te_enteras_que x > 10` | `purgar donde x > 10` |
| **Conector Logico Y (AND)** | `&` | `AND` | Operador relacional encadenado | `y` (o `y_fuerza`) |
| **Conector Logico O (OR)** | `\|` | `OR` | Operador relacional encadenado | `o` (o `o_fuerza`) |
| **Conector Logico NO (NOT)**| `~` | `NOT` | No implementado de forma aislada | `no` (o `no_fuerza`) |
| **Crear / Modificar Columna**| `df['total'] = df['p'] * df['u']` | `total = p * u` / `mutate(total = p * u)`| `el_futuro_es_hoy_oiste_viejo total = p * u` | `forjar total = p * u` |
| **Ordenar Registros** | `df.sort_values('x', ascending=False)` | `ORDER BY x DESC` / `arrange(desc(x))` | `ordenar_a_los_papus x de_arriba_a_abajo` | `ordenar por x descendente` |
| **Eliminar Duplicados** | `df.drop_duplicates()` | `SELECT DISTINCT` / `distinct()` | *No implementado* | `eliminar_clones` |
| **Tratar Nulos (Rellenar)** | `df.fillna(0)` | `COALESCE(col, 0)` / `replace_na(0)` | *No implementado* | `sanar_vacios con 0` |
| **Tratar Nulos (Descartar)** | `df.dropna()` | `WHERE col IS NOT NULL` / `drop_na()`| *No implementado* | `sanar_vacios descartar` |
| **Agrupar por Categorias** | `df.groupby(['cat'])` | `GROUP BY cat` / `group_by(cat)` | `juntar_a_la_grasa_por [cat]` | `agrupar por [cat]` |
| **Resumir Indicadores** | `.agg(...)` | Funciones agregadas en `SELECT` | `sacar_cuentas ...` | `resumir ...` |
| **Conteo de Registros** | `df.count()` | `COUNT(*)` / `n()` | `contar_papus()` / `conteo()` | `recuento()` |
| **Suma Total** | `df['x'].sum()` | `SUM(x)` | `suma(x)` / `sumar_papus(x)` | `acumular(x)` |
| **Media / Promedio** | `df['x'].mean()` | `AVG(x)` / `mean(x)` | `promedio(x)` / `media(x)` | `equilibrio(x)` |
| **Mediana Estadistica** | `df['x'].median()` | `MEDIAN(x)` / `median(x)` | `mediana(x)` | `mediana(x)` |
| **Valor Maximo** | `df['x'].max()` | `MAX(x)` | `el_mas_pro(x)` / `maximo(x)` | `cenit(x)` |
| **Valor Minimo** | `df['x'].min()` | `MIN(x)` | `el_mas_manco(x)` / `minimo(x)` | `nadir(x)` |
| **Desviacion Estandar** | `df['x'].std()` | `STDDEV(x)` / `sd(x)` | `desviacion_pro(x)` | `desviacion(x)` |
| **Guardar Resultados CSV** | `df.to_csv("salida.csv")` | `INTO OUTFILE "salida.csv"` | `subir_al_grupo id en "salida.csv" XD` | `archivar_holocron id en "salida.csv"` |
| **Grafico de Barras** | `df.plot(kind='bar')` | `geom_bar()` | `graficar_momos_en_barras id ... XD` | `holograma barras id ...` |
| **Grafico de Lineas** | `df.plot(kind='line')` | `geom_line()` | `graficar_momos_en_lineas id ... XD` | `holograma lineas id ...` |
| **Grafico de Dispersion** | `df.plot(kind='scatter')` | `geom_point()` | `graficar_momos_en_dispersion id ... XD` | `holograma dispersion id ...` |
| **Histograma** | `df.plot(kind='hist')` | `geom_histogram()` | `graficar_momos_en_histograma id ... XD` | `holograma histograma id ...` |
| **Grafico de Cajas** | `df.plot(kind='box')` | `geom_boxplot()` | `graficar_momos_en_cajas id ... XD` | `holograma caja id ...` |
| **Condicional Logico** | `if condicion: ... else: ...` | `CASE WHEN ... THEN ... ELSE ... END` | `si_el_papu ... entonces ... fin_del_momo XD` | `evaluar_fuerza ... senda_luminosa ... fin_evaluar` |
| **Definicion de Funciones** | `def mi_funcion(x): ...` | `FUNCTION mi_funcion(x) ...` | *No implementado* | `mision mi_mision (x) ... retornar y fin_mision` |
| **Impresion en Consola** | `print(...)` | `PRINT` / `cat(...)` | `when_haces ... XD` | `mostrar ...` / `transmitir ...` |
| **Comentarios de Linea** | `# comentario` | `-- comentario` | `# comentario` / `// comentario` | `-- comentario` (soporta `#` y `//`) |
| **Comentarios de Bloque** | `""" bloque """` | `/* bloque */` | *No implementado* | `/- bloque -/` (soporta `/* */`) |
| **Literales Booleanos** | `True`, `False` | `TRUE`, `FALSE` | `1`, `0` | `cierto_es`, `falso_es` (o `verdadero`, `falso`) |

---

## 3. Comparativa Practica: Un Mismo Flujo en los 3 Paradigmas

Para observar con total claridad la diferencia de elegancia, legibilidad y diseño, observemos la solucion al mismo problema de analisis en los tres lenguajes:

### Problema:
> Cargar un archivo de ventas, seleccionar columnas relevantes, filtrar registros con precio positivo, calcular el total vendido, agrupar por ciudad, calcular el promedio de ventas y exportar a un CSV.

---

### Solucion 1: Python con pandas (Codigo Imperativo Tradicional)
```python
import pandas as pd

ventas = pd.read_csv("datos/ventas.csv")
ventas_limpias = ventas[['fecha', 'ciudad', 'unidades', 'precio']]
ventas_limpias = ventas_limpias[ventas_limpias['precio'] > 0]
ventas_limpias['total'] = ventas_limpias['unidades'] * ventas_limpias['precio']

resumen = ventas_limpias.groupby('ciudad').agg(
    promedio_total=('total', 'mean'),
    max_total=('total', 'max')
).reset_index()

resumen.to_csv("salidas/resumen_ciudades.csv", index=False)
print("Analisis finalizado")
```

---

### Solucion 2: Lenguaje de Referencia (Tematica Memes / Papus)
```text
ventas = pasa_el_pack "datos/ventas.csv" XD
ventas_limpias = ventas
    |:v> escojo_a [fecha, ciudad, unidades, precio]
    |:v> but_te_enteras_que precio > 0
    |:v> el_futuro_es_hoy_oiste_viejo total = unidades * precio XD

resumen = ventas_limpias
    |:v> juntar_a_la_grasa_por [ciudad]
    |:v> sacar_cuentas
        promedio_total = promedio(total),
        max_total = el_mas_pro(total) XD

subir_al_grupo resumen en "salidas/resumen_ciudades.csv" XD
when_haces "Analisis finalizado" XD
```

---

### Solucion 3: HolocronDSL (Tematica Galactica Star Wars, Limpio e Intuitivo)
```holocron
ventas = abrir_holocron "datos/ventas.csv"

ventas_limpias = ventas
    |> revelar [ fecha, ciudad, unidades, precio ]
    |> purgar donde precio > 0
    |> forjar total = unidades * precio

resumen = ventas_limpias
    |> agrupar por [ ciudad ]
    |> resumir
        promedio_total = equilibrio(total),
        max_total = cenit(total)

archivar_holocron resumen en "salidas/resumen_ciudades.csv"
mostrar "Analisis finalizado"
```

---

## 4. Evaluacion de Diferenciacion y Cumplimiento

1. **Cero Plagio / Cero Similitud Lexica:**
   - Ninguna palabra reservada de HolocronDSL coincide con el lenguaje de referencia.
   - Se eliminaron los terminadores artificiales molestos como `XD`.
   - Se descartaron operadores comicos como `|:v>` en favor del conector funcional estándar de hiperespacio `|>`.

2. **Mayor Poder Expresivo:**
   - HolocronDSL incorpora primitivas de limpieza de datos indispensables para la ciencia de datos real que no existen en el lenguaje de referencia:
     - `eliminar_clones` para deduplicacion de registros.
     - `sanar_vacios con ...` y `sanar_vacios descartar` para tratamiento de valores nulos (NaN / NULL).
     - Abstraccion completa con paso de argumentos y retorno de tablas mediante `mision`.

3. **Adherencia Exacta al Documento del Curso (`Proyecto_LP.pdf`):**
   - La sintaxis de HolocronDSL respeta al 100% la estructura conceptual propuesta por el docente Joaquin F. Sanchez, ofreciendo una experiencia declarativa, elegante y reproducible.
