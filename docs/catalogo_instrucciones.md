# Catalogo de Instrucciones y Palabras Reservadas: HolocronDSL

**Universidad Sergio Arboleda**  
**Grupo 5:** Andres Sebastian Coral Vallejo, Carol Arenas Cardona  
**Asignatura:** Lenguajes de Programacion y Transduccion (2026-2)  

---

## 1. Operaciones de Ingestion y Persistencia

| Instruccion | Sintaxis | Descripcion Semantica | Ejemplo en HolocronDSL |
| :--- | :--- | :--- | :--- |
| `abrir_holocron` | `abrir_holocron CADENA [delimitado_por CADENA]` | Carga un archivo CSV desde la ruta indicada. | `cazas = abrir_holocron "datos/flota.csv"` |
| `archivar_holocron` | `archivar_holocron ID en CADENA [delimitado_por CADENA]` | Escribe en disco el conjunto de datos en formato CSV. | `archivar_holocron cazas en "salidas/flota.csv"` |

---

## 2. Enlace y Flujo

| Operador / Palabra | Sintaxis | Descripcion Semantica | Ejemplo en HolocronDSL |
| :--- | :--- | :--- | :--- |
| `=` | `ID = expresion` | Asignacion directa estándar y limpia. | `escuadron = base` |
| `\|>` | `origen \|> operacion` | Operador de pipeline hiperespacial para encadenar operaciones. | `base \|> revelar [ escudos ]` |

---

## 3. Operaciones de Transformacion y Preparacion

| Instruccion | Sintaxis | Descripcion Semantica | Ejemplo en HolocronDSL |
| :--- | :--- | :--- | :--- |
| `revelar` | `revelar [ col1, col2, ... ]` | Proyecta y conserva unicamente las columnas especificadas. | `revelar [ modelo, faccion ]` |
| `purgar donde` | `purgar donde condicion` | Filtra las filas que cumplan la condicion logico-relacional. | `purgar donde escudos > 50` |
| `forjar` | `forjar ID = expresion` | Computa y agrega una nueva columna calculada con signo `=`. | `forjar total = precio * unidades` |
| `ordenar por` | `ordenar por ID [ascendente \| descendente]` | Ordena las filas segun la columna indicada. | `ordenar por victorias descendente` |
| `eliminar_clones` | `eliminar_clones` | Suprime filas duplicadas del conjunto tabular. | `flota \|> eliminar_clones` |
| `sanar_vacios` | `sanar_vacios [descartar \| con literal]` | Trata valores faltantes (nulos) descartando o rellenando. | `sanar_vacios con 0` |

---

## 4. Agrupamiento y Funciones de Agregacion

| Instruccion | Sintaxis | Descripcion Semantica | Ejemplo en HolocronDSL |
| :--- | :--- | :--- | :--- |
| `agrupar por` | `agrupar por [ col1, ... ]` | Segmenta el conjunto de datos por una o varias columnas. | `agrupar por [ faccion ]` |
| `resumir` | `resumir col = func(arg), ...` | Aplica funciones agregadas sobre los grupos definidos. | `resumir n = recuento()` |

### Funciones Estadisticas Soportadas:
- `recuento()` o `conteo()`: Conteo de registros.
- `acumular(col)` o `suma(col)`: Sumatoria de la columna.
- `equilibrio(col)` o `promedio(col)`: Media aritmetica (el equilibrio de la Fuerza en los datos).
- `mediana(col)`: Valor central o percentil 50.
- `cenit(col)` o `maximo(col)`: Valor maximo.
- `nadir(col)` o `minimo(col)`: Valor minimo.
- `desviacion(col)`: Desviacion estandar muestral.

---

## 5. Proyeccion Holografica (Visualizaciones)

| Clausula | Sintaxis | Descripcion |
| :--- | :--- | :--- |
| `holograma` | `holograma TIPO ID ...` | Delimita un bloque declarativo de generacion grafica. |
| Tipos soportados | `barras`, `lineas`, `dispersion`, `histograma`, `caja` | Formato visual a renderizar. |
| `eje_x "col"` | Asignacion de la variable para el eje horizontal. |
| `eje_y "col"` | Asignacion de la variable para el eje vertical. |
| `titulo "texto"` | Titulo superior de la proyeccion holografica. |
| `guardar "ruta.png"` | Ruta del archivo de imagen PNG generado. |

---

## 6. Abstraccion y Control de Flujo

| Instruccion | Sintaxis | Descripcion Semantica |
| :--- | :--- | :--- |
| `mision` | `mision ID (p1, p2) ... retornar expr fin_mision` | Define una funcion reutilizable que retorna un resultado. |
| `evaluar_fuerza` | `evaluar_fuerza condicion senda_luminosa ... senda_oscura ... fin_evaluar` | Bifurcacion condicional limpia. |
| `mostrar` / `transmitir` | `mostrar expr` | Despliega mensajes o resultados en la consola. |

---

## 7. Operadores y Literales

- Conectores logicos: `y`, `o`, `no` (o sus alias `y_fuerza`, `o_fuerza`, `no_fuerza`).
- Relacionales: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Aritmeticos: `^`, `*`, `/`, `%`, `+`, `-`.
- Literales: `cierto_es` / `verdadero`, `falso_es` / `falso`, enteros, decimales y cadenas.
