# Catalogo de Instrucciones y Palabras Reservadas: HolocronDSL

**Grupo 5:** Andres Sebastian Coral Vallejo, Carol Arenas Cardona  
**Asignatura:** Lenguajes de Programacion y Transduccion (2026-2)  

---

## 1. Operaciones de Ingestion y Persistencia

| Instruccion | Sintaxis | Descripcion Semantica | Ejemplo en HolocronDSL |
| :--- | :--- | :--- | :--- |
| `abrir_holocron` | `abrir_holocron CADENA [delimitado_por CADENA]` | Carga un archivo CSV desde la ruta indicada y genera una referencia tabular. | `cazas <- abrir_holocron "datos/flota.csv"` |
| `archivar_holocron` | `archivar_holocron ID en CADENA [delimitado_por CADENA]` | Escribe en disco el conjunto de datos referenciado en formato CSV. | `archivar_holocron cazas en "salidas/flota.csv"` |

---

## 2. Operadores de Enlace y Flujo

| Operador / Palabra | Sintaxis | Descripcion Semantica | Ejemplo en HolocronDSL |
| :--- | :--- | :--- | :--- |
| `<-` | `ID <- expresion` | Asigna el resultado de una expresion o pipeline a una variable. | `escuadron <- base` |
| `canalizar` | `[canalizar] ID <- expresion` | Modificador opcional de estilo declarativo para asignacion. | `canalizar escuadron <- base` |
| `==>` | `origen ==> operacion` | Operador de pipeline hiperespacial que canaliza la salida anterior como entrada a la siguiente etapa. | `base ==> revelar_sectores [ escudos ]` |
| `:=` | `ID := expresion` | Operador de ligadura interna usado en forja de columnas, agregaciones y propiedades. | `indice := victorias * 10` |

---

## 3. Operaciones de Transformacion y Preparacion

| Instruccion | Sintaxis | Descripcion Semantica | Ejemplo en HolocronDSL |
| :--- | :--- | :--- | :--- |
| `revelar_sectores` | `revelar_sectores [ col1, col2, ... ]` | Proyecta y conserva unicamente las columnas especificadas en la lista. | `revelar_sectores [ modelo, faccion ]` |
| `purgar_donde` | `purgar_donde condicion` | Filtra las filas que cumplan la condicion booleana indicada. | `purgar_donde escudos > 50` |
| `forjar_cristal` | `forjar_cristal ID := expresion` | Computa y agrega una nueva columna calculada al conjunto de datos. | `forjar_cristal total := precio * unidades` |
| `alinear_flota` | `alinear_flota ID [orden_ascendente \| orden_descendente]` | Ordena las filas segun la columna indicada y el criterio de orden. | `alinear_flota victorias orden_descendente` |
| `eliminar_clones` | `eliminar_clones` | Suprime todas las filas duplicadas del conjunto tabular. | `flota ==> eliminar_clones` |
| `sanar_vacios` | `sanar_vacios [descartar \| sustituir_con literal]` | Trata valores faltantes (nulos) descartando filas o reemplazando con un valor. | `sanar_vacios sustituir_con 0` |

---

## 4. Agrupamiento y Funciones de Agregacion

| Instruccion | Sintaxis | Descripcion Semantica | Ejemplo en HolocronDSL |
| :--- | :--- | :--- | :--- |
| `agrupar_sector` | `agrupar_sector [ col1, ... ]` | Segmenta el conjunto de datos por una o varias columnas de agrupamiento. | `agrupar_sector [ faccion ]` |
| `sintetizar_indicadores`| `sintetizar_indicadores [ nom := func(col), ... ]` | Aplica una lista de funciones agregadas sobre los grupos definidos. | `sintetizar_indicadores [ n := recuento() ]` |

### Funciones de Agregacion Estadistica
- `recuento()`: Conteo total de registros en el grupo.
- `acumular(col)`: Sumatoria numerica de los valores de la columna.
- `equilibrio(col)`: Media aritmetica (el equilibrio de la Fuerza en los datos).
- `mediana(col)`: Valor central o percentil 50.
- `cenit(col)`: Valor maximo registrado.
- `nadir(col)`: Valor minimo registrado.
- `desviacion(col)`: Desviacion estandar muestral de la variable.

---

## 5. Proyeccion Holografica (Visualizaciones)

| Clausula | Sintaxis | Descripcion |
| :--- | :--- | :--- |
| `proyectar_holograma` | `proyectar_holograma TIPO desde ID ... fin_holograma` | Delimita un bloque declarativo de generacion grafica. |
| Tipos soportados | `barras`, `lineas`, `dispersion`, `histograma`, `caja` | Formato visual a renderizar. |
| `eje_x := "col"` | Asignacion de la variable para el eje horizontal de la grafica. |
| `eje_y := "col"` | Asignacion de la variable para el eje vertical (opcional en histogramas). |
| `holotitulo := "texto"` | Titulo superior de la proyeccion holografica. |
| `guardar_proyeccion := "ruta.png"` | Ruta del archivo de imagen PNG generado. |

---

## 6. Abstraccion y Control de Flujo

| Instruccion | Sintaxis | Descripcion Semantica |
| :--- | :--- | :--- |
| `mision` | `mision ID con_parametros (p1, p2) ... retornar_orden expr fin_mision` | Define una funcion pura reutilizable que retorna un resultado. |
| `evaluar_fuerza` | `evaluar_fuerza (condicion) senda_luminosa ... senda_oscura ... fin_evaluar` | Estructura de bifurcacion condicional orientada a verificacion de estados. |
| `transmitir_mensaje` | `transmitir_mensaje expr` | Despliega informacion, telemetria o cadenas literales en la consola. |

---

## 7. Operadores y Literales

### Conectores Logicos
- `y_fuerza`: Operador logico AND con evaluacion de cortocircuito.
- `o_fuerza`: Operador logico OR.
- `no_fuerza`: Operador logico unario NOT.

### Operadores Relacionales
- `==`: Igualdad de valor.
- `!=`: Desigualdad de valor.
- `<`, `<=`, `>`, `>=`: Comparaciones de magnitud.

### Operadores Aritmeticos (en orden de precedencia)
1. `^`: Potenciacion (asociatividad por derecha).
2. `*`, `/`, `%`: Multiplicacion, division y modulo.
3. `+`, `-`: Suma y resta.

### Literales
- Booleanos: `cierto_es` (verdadero), `falso_es` (falso).
- Numericos: Enteros (`100`) y decimales con punto flotante (`3.14`).
- Cadenas: Texto delimitado por comillas dobles (`"Sector Galactico"`).
- Comentarios: De linea con `--` y de bloque con `/- ... -/`.
