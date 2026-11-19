# Guía Integral de Estudio y Sustentación: HolocronDSL

**Asignatura:** Lenguajes de Programación y Transducción (Periodo 2026-2)  
**Institución:** Universidad Sergio Arboleda  
**Docente:** Joaquín F. Sánchez  
**Equipo de Desarrollo (Grupo 5):**  
- Andrés Sebastián Coral Vallejo  
- Carol Arenas Cardona  

---

## 1. Visión General del Proyecto y Filosofía Arquitectónica

### 1.1 ¿Qué es HolocronDSL?
HolocronDSL es un lenguaje de dominio específico (DSL) declarativo, fuertemente tipado en su capa semántica y de paradigma funcional para la ciencia de datos. Su propósito fundamental es modelar flujos de trabajo reproducibles de extracción, depuración, transformación, agregación estadística y visualización de datos tabulares.

### 1.2 Identidad Temática Galáctica
El lenguaje utiliza una metáfora inspirada en la saga de Star Wars para dar coherencia y legibilidad a sus construcciones:
* **Holocrones (`abrir_holocron`):** Representan conjuntos de datos tabulares inmutables (equivalentes a DataFrames).
* **Pipeline Hiperespacial (`|>`):** Operador de encadenamiento que transfiere el flujo de datos de una etapa a la siguiente sin mutar el estado anterior.
* **Misiones (`mision ... fin_mision`):** Subrutinas o funciones parametrizadas reutilizables con ámbito léxico propio.
* **Control de Fuerza (`evaluar_fuerza`, `senda_luminosa`, `senda_oscura`):** Estructuras condicionales de bifurcación (`if / else`).
* **Hologramas (`proyectar_holograma`):** Visualizaciones gráficas proyectadas en imágenes estáticas de alta resolución (formato PNG exclusivamente).
* **Transmisiones (`transmitir`):** Instrucciones de emisión de resultados y tablas hacia la terminal estándar.

### 1.3 Alcance de las Entregas Académicas
* **Entrega 1 (Fase Léxica y Sintáctica):** Reconocimiento de tokens, gramática formal libre de contexto (EBNF) en ANTLR4, generación del árbol de análisis sintáctico (CST/AST) y reporte de errores sintácticos con detección precisa de línea y columna.
* **Entrega 2 (Fase Semántica, Intérprete y Bibliotecas Propias):** Verificación de tipos, tabla de símbolos con ámbitos anidados, evaluador mediante el patrón Visitor, suite de 4 bibliotecas propias (`HolocronIO`, `HolocronMath`, `HolocronTable`, `HolocronPlotter`) desarrolladas sin librerías externas prohibidas (sin pandas, sin numpy, sin openpyxl, sin xlwt, sin SVG) y ejecución completa a disco (CSV, Excel `.xls` y PNG).
* **Entrega 3 (Fase de Optimización o Generación de Código):** Optimizaciones intermedias o transducción a lenguaje objetivo final.

---

## 2. Entrega 1: Fase Léxica y Sintáctica (Actualizada)

### 2.1 El Analizador Léxico (Lexer)
El archivo `src/grammar/HolocronDSL.g4` define las reglas léxicas mediante expresiones regulares. Su trabajo es convertir el flujo continuo de caracteres del código fuente en una secuencia lineal de unidades mínimas de significado denominadas **Tokens**.

#### Canales y Descarte de Caracteres
* **Espacios y Saltos de Línea:** Las reglas `WS` envían los espacios, tabulaciones y saltos de línea al canal oculto de ANTLR (`-> skip`), lo que significa que el lenguaje es insensible a la indentación o espaciado arbitrario (a diferencia de Python).
* **Comentarios:**
  * De línea única: `// comentario -> skip`
  * De bloque multilínea: `/* comentario */ -> skip`

#### Categorías Principales de Tokens (Con Uso, Contexto y Ejemplos Explícitos)

##### 1. Palabras Reservadas de Ingestión y Entrada/Salida
* **`abrir_holocron`** *(Carga un archivo CSV desde disco a la memoria como un conjunto de datos tabular inmutable)*.  
  Se utiliza como la expresión base al inicio de un pipeline o asignado a una variable.
  ```holocron
  mi_tabla = abrir_holocron "datos/flota.csv"
  ```
  *Explicación del ejemplo:*  
  - La variable receptora se llama `mi_tabla` y almacenará los datos cargados en memoria.  
  - `"datos/flota.csv"` es la ruta del archivo que se va a leer.

* **`delimitado_por`** *(Especifica el caracter que separa los campos en el archivo de texto, por defecto es la coma `,`)*.  
  Se utiliza como modificador opcional inmediatamente después de la ruta del archivo.
  ```holocron
  mi_tabla_separada = abrir_holocron "datos/censo.csv" delimitado_por ";"
  ```
  *Explicación del ejemplo:*  
  - La variable se llama `mi_tabla_separada`.  
  - `delimitado_por ";"` le indica al lector que las columnas están separadas por punto y coma en vez de coma.

* **`archivar_holocron`** *(Exporta y persiste una tabla en disco en formato CSV o en hoja de cálculo de Excel `.xls`)*.  
  Se utiliza como una sentencia de exportación al final de los análisis.
  ```holocron
  archivar_holocron mi_tabla_final en "salidas/reporte_flota.xls"
  ```
  *Explicación del ejemplo:*  
  - `archivar_holocron`: Palabra clave de guardado.  
  - `mi_tabla_final`: Nombre de la variable que contiene la tabla con los datos a exportar.  
  - `en`: Conector sintáctico obligatorio.  
  - `"salidas/reporte_flota.xls"`: Ruta de destino. Al terminar en `.xls`, el sistema genera automáticamente una hoja de cálculo nativa de Excel compatible con LibreOffice Calc.

* **`en`** *(Conector sintáctico obligatorio que introduce la ruta de archivo para `archivar_holocron`)*.

* **`proyectar_holograma`** *(Genera un gráfico visual y lo guarda en disco en formato de imagen PNG a 300 DPI)*.  
  Se utiliza como una sentencia para crear visualizaciones (`barras`, `lineas`, `dispersion`, `histograma`, `caja`).
  ```holocron
  proyectar_holograma barras mi_tabla_grafica [
      eje_x = "faccion",
      eje_y = "victorias",
      titulo = "Total de Victorias por Faccion",
      guardar = "salidas/grafica_barras.png"
  ]
  ```
  *Explicación del ejemplo:*  
  - `barras`: Es el tipo de gráfico elegido.  
  - `mi_tabla_grafica`: Es la variable que contiene los datos a graficar.  
  - `eje_x = "faccion"`: Columna categórica para el eje horizontal.  
  - `eje_y = "victorias"`: Columna numérica para las alturas.  
  - `guardar`: Ruta de destino obligatoriamente en formato `.png` (el lenguaje rechaza `.svg`).

* **`transmitir`** *(Emite e imprime en la consola o terminal el contenido tabular, numérico o textual)*.  
  Se utiliza para mostrar resultados al usuario en pantalla.
  ```holocron
  transmitir "Mostrando registros aprobados:"
  transmitir mi_tabla_filtrada
  ```
  *Explicación del ejemplo:*  
  - La primera línea imprime el mensaje literal en la terminal.  
  - La segunda línea imprime la tabla `mi_tabla_filtrada` formateada visualmente con columnas y cuadrículas en texto plano ASCII.

---

##### 2. Palabras Reservadas de Transformación (Operaciones del Pipeline)
* **`revelar`** *(Selecciona únicamente las columnas indicadas y descarta las que no estén en la lista)*.  
  Se usa después del operador `|>` con una lista de nombres de columnas entre corchetes `[ ... ]`.
  ```holocron
  mi_tabla_reducida = mi_tabla |> revelar [ columna_id, columna_escudos, columna_victorias ]
  ```
  *Explicación del ejemplo:*  
  - La variable original es `mi_tabla`.  
  - La nueva variable resultante es `mi_tabla_reducida`.  
  - `columna_id`, `columna_escudos` y `columna_victorias` son los nombres exactos de las columnas que se conservarán; cualquier otra columna de la tabla original queda descartada.

* **`purgar`** *(Filtra horizontalmente las filas de la tabla según una condición lógica booleana)*.  
  Se usa después del operador `|>` acompañado obligatoriamente de la palabra `donde`.
  ```holocron
  mi_tabla_filtrada = mi_tabla |> purgar donde columna_escudos > 100 y columna_victorias >= 5
  ```
  *Explicación del ejemplo:*  
  - La nueva variable es `mi_tabla_filtrada`.  
  - Solo se mantendrán las filas donde el valor de `columna_escudos` sea estrictamente mayor a 100 y `columna_victorias` sea mayor o igual a 5.

* **`donde`** *(Conector gramatical obligatorio que enlaza la instrucción `purgar` con la condición lógica a evaluar)*.

* **`forjar`** *(Crea una nueva columna calculada a partir de fórmulas aritméticas sobre columnas existentes)*.  
  Se usa después del operador `|>` con la sintaxis: `forjar nombre_nueva_columna = expresion`.
  ```holocron
  mi_tabla_calculada = mi_tabla |> forjar columna_poder = columna_escudos + columna_victorias * 10
  ```
  *Explicación del ejemplo:*  
  - La nueva variable resultante se llama `mi_tabla_calculada`.  
  - `columna_poder` es el nombre de la nueva columna creada.  
  - El valor de `columna_poder` se calcula fila por fila multiplicando `columna_victorias` por 10 y sumándole `columna_escudos`.

* **`ordenar`** *(Ordena las filas de la tabla según el valor de una columna elegida)*.  
  Se usa después del operador `|>` acompañado obligatoriamente del conector `por`.
  ```holocron
  mi_tabla_ordenada = mi_tabla |> ordenar por columna_victorias descendente
  ```
  *Explicación del ejemplo:*  
  - La variable resultante se llama `mi_tabla_ordenada`.  
  - `columna_victorias` es la columna utilizada como criterio de ordenación.  
  - `descendente` indica que las filas con más victorias aparecerán primero (de mayor a menor). Si se omite, el orden es ascendente por defecto.

* **`por`** *(Conector gramatical obligatorio utilizado en `ordenar por` y en `agrupar por`)*.

* **`ascendente`** *(Modificador opcional en `ordenar por` para ordenar de menor a mayor o alfabéticamente de la A a la Z)*.

* **`descendente`** *(Modificador en `ordenar por` para ordenar de mayor a menor o alfabéticamente de la Z a la A)*.

* **`eliminar_clones`** *(Busca y elimina todas las filas duplicadas que tengan exactamente los mismos valores en todas sus columnas)*.  
  Se usa después del operador `|>`.
  ```holocron
  mi_tabla_sin_duplicados = mi_tabla |> eliminar_clones
  ```
  *Explicación del ejemplo:*  
  - `mi_tabla_sin_duplicados` contendrá únicamente registros únicos.

* **`sanar_vacios`** *(Detecta celdas vacías o nulas (`None`/`nulo`) y las procesa según la estrategia elegida)*.  
  Se usa después del operador `|>` con una de dos opciones: `descartar` o `con <valor>`.
  ```holocron
  // Opcion 1: Descartar filas incompletas
  mi_tabla_limpia = mi_tabla |> sanar_vacios descartar

  // Opcion 2: Rellenar celdas vacias con un valor por defecto
  mi_tabla_rellena = mi_tabla |> sanar_vacios con 0
  ```
  *Explicación del ejemplo:*  
  - Con `descartar`, cualquier fila con al menos un campo nulo es borrada.  
  - Con `con 0`, las celdas nulas se reemplazan por el número `0`.

* **`descartar`** *(Opción de `sanar_vacios` para borrar las filas que tengan celdas vacías)*.

* **`con`** *(Opción de `sanar_vacios` para sustituir los valores vacíos por el valor que se escriba a continuación)*.

* **`agrupar`** *(Segmenta la tabla en subgrupos de filas que compartan los mismos valores en las columnas especificadas)*.  
  Se usa después del operador `|>` con la sintaxis: `agrupar por [ columna_clave ]`.
  ```holocron
  mis_grupos = mi_tabla |> agrupar por [ columna_faccion ]
  ```
  *Explicación del ejemplo:*  
  - La variable `mis_grupos` almacena la tabla segmentada (`HolocronGroupedTable`), lista para aplicar funciones estadísticas sobre cada facción.

* **`resumir`** *(Calcula métricas estadísticas agregadas sobre los grupos creados o sobre la tabla entera)*.  
  Se usa después del operador `|>` recibiendo una lista de asignaciones de funciones de agregación.
  ```holocron
  mi_resumen = mi_tabla
      |> agrupar por [ columna_faccion ]
      |> resumir [
          columna_total_naves = recuento(),
          columna_media_escudos = equilibrio(columna_escudos),
          columna_max_victorias = cenit(columna_victorias)
      ]
  ```
  *Explicación del ejemplo:*  
  - La variable resultante se llama `mi_resumen`.  
  - Cada facción tendrá una fila en la nueva tabla.  
  - `columna_total_naves` contendrá cuántas naves tiene esa facción (`recuento()`).  
  - `columna_media_escudos` contendrá el promedio de escudos (`equilibrio(...)`).  
  - `columna_max_victorias` contendrá el valor máximo de victorias registrado (`cenit(...)`).

---

##### 3. Funciones de Agregación (Usadas exclusivamente dentro de `resumir`)
* **`recuento()`** / **`conteo()`** *(Cuenta cuántas filas pertenecen a cada grupo. No requiere obligatoriamente una columna)*.  
  ```holocron
  columna_cantidad_naves = recuento()
  ```
  *Explicación:* Crea la nueva columna `columna_cantidad_naves` con el número total de registros de cada grupo.

* **`acumular(columna)`** / **`suma(columna)`** *(Calcula la sumatoria total de los valores numéricos de una columna en cada grupo)*.  
  ```holocron
  columna_total_victorias = acumular(victorias)
  ```
  *Explicación:* Suma todos los valores de la columna `victorias` del grupo y los guarda en la nueva columna `columna_total_victorias`.

* **`equilibrio(columna)`** / **`promedio(columna)`** *(Calcula el promedio o media aritmética de los valores de una columna)*.  
  ```holocron
  columna_escudos_medios = equilibrio(escudos)
  ```
  *Explicación:* Suma los valores de `escudos` del grupo y los divide entre el número de filas válidas, redondeando a dos decimales.

* **`mediana(columna)`** *(Calcula el valor central que divide la muestra ordenada en dos partes iguales)*.  
  ```holocron
  columna_escudos_mediana = mediana(escudos)
  ```
  *Explicación:* Ordena los escudos del grupo y selecciona el elemento central exacto (o el promedio de los dos centrales si la cantidad es par).

* **`cenit(columna)`** / **`maximo(columna)`** *(Encuentra el valor numérico más alto o tope superior de la columna en cada grupo)*.  
  ```holocron
  columna_record_victorias = cenit(victorias)
  ```
  *Explicación:* Asigna en `columna_record_victorias` el valor máximo encontrado en la columna `victorias`.

* **`nadir(columna)`** / **`minimo(columna)`** *(Encuentra el valor numérico más bajo o piso inferior de la columna en cada grupo)*.  
  ```holocron
  columna_menor_blindaje = nadir(escudos)
  ```
  *Explicación:* Asigna en `columna_menor_blindaje` el valor más bajo encontrado en la columna `escudos`.

* **`desviacion(columna)`** *(Calcula la desviación estándar de la columna para medir qué tan dispersos están los datos)*.  
  ```holocron
  columna_dispersion = desviacion(escudos)
  ```
  *Explicación:* Mide la variabilidad de la columna `escudos` respecto a su promedio. Si todos los escudos son iguales, el resultado es 0.

---

##### 4. Estructuras de Control y Funciones
* **`mision`**, **`fin_mision`**, **`retornar`** *(Declaran y delimitan una función reutilizable con parámetros y ámbito léxico local propio)*.  
  ```holocron
  mision mi_calculo(parametro_base, parametro_extra)
      variable_local = parametro_base * 2
      resultado_final = variable_local + parametro_extra
      retornar resultado_final
  fin_mision

  mi_variable_global = mi_calculo(50, 10)
  ```
  *Explicación del ejemplo:*  
  - `mi_calculo`: Nombre de la función (misión).  
  - `parametro_base` y `parametro_extra`: Entradas de la función.  
  - `variable_local`: Solo existe dentro de la misión (ámbito local).  
  - `retornar resultado_final`: Devuelve el valor `(50 * 2) + 10 = 110`.  
  - `mi_variable_global`: Variable en el ámbito global que recibe el número `110`.

* **`evaluar_fuerza`**, **`senda_luminosa`**, **`senda_oscura`**, **`fin_evaluar`** *(Estructura condicional equivalente al `if / else` para bifurcar la ejecución según una condición lógica)*.  
  ```holocron
  mi_variable_estado = "desconocido"

  evaluar_fuerza mi_variable_puntaje >= 70
  senda_luminosa
      mi_variable_estado = "Aprobado"
      transmitir "El postulante ha superado la prueba."
  senda_oscura
      mi_variable_estado = "Reprobado"
      transmitir "El postulante debe repetir la prueba."
  fin_evaluar
  ```
  *Explicación del ejemplo:*  
  - Si `mi_variable_puntaje` es mayor o igual a 70, el intérprete entra a la `senda_luminosa` y asigna `"Aprobado"`.  
  - Si es menor a 70, el intérprete entra a la `senda_oscura` y asigna `"Reprobado"`.  
  - `fin_evaluar` cierra el bloque condicional.

---

##### 5. Operadores y Conectores
* **`|>` (Pipeline Hiperespacial):** *(Pasa el resultado de la expresión izquierda como entrada directa a la operación derecha)*.  
  Ejemplo: `mi_tabla |> purgar donde columna_edad >= 18`
* **`=` (Asignación):** *(Asigna un valor evaluado a la variable que se encuentra a la izquierda)*.  
  Ejemplo: `mi_numero = 100`
* **Aritméticos:**
  - `+` *(Suma matemática o concatenación de textos si hay cadenas involucradas)*:  
    `resultado_suma = 15 + 5` (da 20) | `saludo = "Hola " + "Galaxia"` (da "Hola Galaxia")
  - `-` *(Resta matemática)*: `resultado_resta = 20 - 8` (da 12)
  - `*` *(Multiplicación matemática)*: `resultado_multiplicacion = 6 * 7` (da 42)
  - `/` *(División matemática protegida contra división por cero)*: `resultado_division = 50 / 2` (da 25.0)
  - `%` *(Módulo o residuo de la división entera)*: `resultado_modulo = 10 % 3` (da 1)
  - `^` *(Potenciación o exponente)*: `resultado_potencia = 2 ^ 3` (da 8)
* **Relacionales (Comparación):**
  - `==` *(Igual que)*: `columna_tipo == "Caza"`
  - `!=` *(Diferente de)*: `columna_faccion != "Pirata"`
  - `<` *(Menor estricto que)*: `columna_escudos < 50`
  - `<=` *(Menor o igual que)*: `columna_tripulantes <= 2`
  - `>` *(Mayor estricto que)*: `columna_victorias > 10`
  - `>=` *(Mayor o igual que)*: `columna_velocidad >= 800`
* **Lógicos (Conectores booleanos):**
  - `y` *(AND lógico: se cumple solo si ambas condiciones son ciertas)*:  
    `columna_escudos > 50 y columna_victorias > 2`
  - `o` *(OR lógico: se cumple si al menos una de las dos condiciones es cierta)*:  
    `columna_faccion == "Imperio" o columna_faccion == "Rebelion"`
  - `no` *(NOT lógico: invierte el valor de verdad de la condición)*:  
    `no (columna_escudos == 0)`

---

##### 6. Literales y Tipos de Datos Atómicos
* **`cierto_es`** / **`verdadero`**: *(Literal booleano que representa el valor de verdad `True`)*.  
  Ejemplo: `mi_interruptor = cierto_es`
* **`falso_es`** / **`falso`**: *(Literal booleano que representa la falsedad `False`)*.  
  Ejemplo: `mi_interruptor = falso_es`
* **`nulo`**: *(Literal que representa ausencia de dato o valor desconocido `None`)*.  
  Ejemplo: `mi_dato_vacio = nulo`
* **Enteros (`int`):** Números enteros positivos o negativos sin decimales.  
  Ejemplo: `mi_contador = 42`
* **Decimales (`float`):** Números con punto flotante.  
  Ejemplo: `mi_decimal = 3.1416`
* **Cadenas de texto (`str`):** Textos encerrados entre comillas dobles `"..."`.  
  Ejemplo: `mi_texto = "Estacion Espacial"`
* **Identificadores (`ID`):** Nombres asignados a variables, columnas o funciones creadas por el programador.  
  Ejemplos: `mi_tabla`, `total_victorias`, `mi_mision_1`.

### 2.2 El Analizador Sintáctico (Parser) y Gramática Formal
El parser valida que la secuencia de tokens respete las reglas gramaticales libres de contexto (EBNF).

#### Jerarquía de Reglas Gramaticales
* `programa`: Secuencia de cero o más sentencias finalizadas con EOF (`sentencia* EOF`).
* `sentencia`: Regla de selección que ramifica hacia las diferentes operaciones del lenguaje:
  * `declaracionMision`
  * `sentenciaAsignacion`
  * `sentenciaCondicional`
  * `sentenciaHolograma`
  * `sentenciaArchivado`
  * `sentenciaTransmision`

#### Estructura del Pipeline Hiperespacial
La regla `expresionPipeline` modela la composición funcional:
```antlr
expresionPipeline
    : expresionBase (OP_PIPE operacionPipeline)*
    ;
```
Esto permite escribir construcciones fluidas donde el resultado de la expresión base se canaliza hacia múltiples etapas de transformación sucesivas:
```holocron
resultado = abrir_holocron "datos.csv"
    |> purgar donde escudos > 100
    |> ordenar por victorias descendente
```

#### Precedencia y Asociatividad de Operadores
La gramática resuelve formalmente la precedencia de operadores dividiendo las expresiones en niveles jerárquicos:
1. **Nivel Aritmético:**
   * Mayor precedencia: Paréntesis `(...)`, literales, variables y llamadas a misiones.
   * Exponenciación (`^`): Asociatividad hacia la derecha.
   * Multiplicación (`*`), División (`/`), Módulo (`%`): Asociatividad hacia la izquierda.
   * Suma (`+`), Resta (`-`): Menor precedencia, asociatividad hacia la izquierda.
2. **Nivel Relacional:** Comparaciones (`==`, `!=`, `<`, `<=`, `>`, `>=`) evalúan entre expresiones aritméticas.
3. **Nivel Booleano:**
   * Mayor precedencia: Negación (`no`).
   * Precedencia intermedia: Conjunción (`y`).
   * Menor precedencia: Disyunción (`o`).

### 2.3 Manejador de Errores Sintácticos (`HolocronErrorListener`)
Ubicado en `src/compiler/error_listener.py`, extiende la clase `BaseErrorListener` de ANTLR4:
* Desactiva los listeners de consola predeterminados de ANTLR para evitar mensajes en inglés crípticos.
* Intercepta el método `syntaxError()`.
* Almacena objetos de error con: número de línea, posición en columna, token ofensivo y una sugerencia de corrección pedagógica en español.

---

## 3. Entrega 2: Análisis Semántico, Intérprete y Bibliotecas Propias

### 3.1 Diferencia Fundamental entre Sintaxis y Semántica
* **Sintaxis:** Verifica que la estructura externa del código cumpla la gramática formal (que las palabras y símbolos estén en el orden correcto).
  * Ejemplo: `x = "Alderaan" / 10` es sintácticamente válido (ID = STRING / INT), pero carece de sentido lógico.
* **Semántica:** Verifica el significado, coherencia de tipos, existencia de identidades en memoria y validez operativa antes o durante la ejecución.
  * El compilador detecta que no es posible dividir un texto entre un número y lanza `TipoIncompatibleError`.

### 3.2 Tabla de Símbolos y Gestión Jerárquica de Ámbitos (Scopes)
La tabla de símbolos (`src/interpreter/symbol_table.py`) es la estructura de datos que rastrea las entidades activas en el entorno de ejecución.

#### Jerarquía de Clases
* `Scope`: Representa un ámbito léxico individual. Contiene:
  * `nombre`: Identificador del ámbito (por ejemplo, `global` o el nombre de una misión).
  * `simbolos`: Diccionario clave-valor con las variables locales.
  * `padre`: Puntero hacia el ámbito contenedor superior (`Optional[Scope]`).
* `MisionInfo`: Registro de funciones definidas por el usuario. Almacena: nombre, lista formal de parámetros, nodos AST de las sentencias del cuerpo, nodo AST de la expresión de retorno y coordenadas en el código fuente.
* `SymbolTable`: Administra la pila o árbol de ámbitos.

#### Algoritmo de Resolución de Variables (Look-up)
Cuando el intérprete encuentra un identificador:
1. Inspecciona el diccionario local del ámbito activo (`self.ambito_actual.simbolos`).
2. Si existe, retorna su valor.
3. Si no existe, delega recursivamente en el ámbito padre (`self.ambito_actual.padre`).
4. Si se alcanza la raíz (`padre is None`) y no se encuentra, se lanza una excepción `VariableNoDefinidaError`.

#### Sombreado de Variables (Variable Shadowing)
Una misión puede declarar una variable local con el mismo nombre que una variable del ámbito global. La variable local ocultará o "sombreará" a la variable externa dentro del cuerpo de la misión, sin modificar ni destruir el valor global.

### 3.3 El Intérprete Evaluador: Patrón Visitor
En `src/interpreter/visitor.py`, la clase `HolocronInterpreter` hereda de `HolocronDSLVisitor` (generado por ANTLR4).

#### ¿Por qué Visitor en lugar de Listener?
* **Listener:** Es un patrón pasivo. El `ParseTreeWalker` de ANTLR recorre cada nodo en un recorrido primero en profundidad, disparando eventos `enterNodo` y `exitNodo`. No permite interrumpir fácilmente el recorrido ni omitir ramas, lo que dificulta implementar estructuras condicionales (`if/else`) o ciclos, donde solo se debe ejecutar una rama específica.
* **Visitor:** Es un patrón activo y orientado a evaluación. El desarrollador controla manualmente la navegación invocando `self.visit(hijo)`. Esto permite:
  1. **Control de Flujo:** En `evaluar_fuerza`, se evalúa la condición booleana; si resulta verdadera se visita exclusivamente la `senda_luminosa`; si es falsa, se visita exclusivamente la `senda_oscura`. La otra rama nunca se ejecuta.
  2. **Retorno Directo de Valores:** Cada método `visit...()` puede retornar valores de cómputo directos (un número, una cadena, un booleano o una `HolocronTable`), facilitando la propagación de resultados hacia arriba en el árbol de análisis sintáctico.

---

## 4. Las Cuatro Bibliotecas Propias (Sin Dependencias Prohibidas)

Para cumplir con la directiva estricta de no utilizar herramientas de alto nivel como pandas o numpy, ni generadores SVG, se implementaron cuatro motores modulares independientes:

```
src/runtime/
├── math_engine.py       -> Biblioteca propia de calculos y estadistica (HolocronMath)
├── io_engine.py         -> Biblioteca propia de lectura/escritura CSV y Excel (HolocronIO)
├── holocron_table.py    -> Estructura tabular funcional e inmutable (HolocronTable)
└── graphics_engine.py   -> Motor de proyeccion visual exclusivamente PNG (HolocronPlotter)
```

### 4.1 Biblioteca Matemática y Estadística (`HolocronMath`)
Implementación de algoritmos puros en Python para análisis estadístico univariado sin recurrir a paquetes numéricos externos:
* `suma(valores)`: Acumulación de valores ignorando nulos.
* `promedio(valores)`: Media aritmética calculada como cociente entre la suma y la cantidad de valores válidos.
* `mediana(valores)`: Ordenamiento interno; si la cantidad es impar toma el valor central exacto; si es par calcula el promedio de los dos elementos centrales.
* `cenit(valores)` / `maximo(valores)`: Búsqueda del valor numérico más alto.
* `nadir(valores)` / `minimo(valores)`: Búsqueda del valor numérico más bajo.
* `conteo(valores)`: Recuento cardinal de registros no nulos.
* `varianza(valores)`: Media de las desviaciones cuadráticas respecto a la media poblacional.
* `desviacion(valores)`: Raíz cuadrada de la varianza.
* `division_segura(dividendo, divisor)`: Detección proactiva de cero en el denominador para lanzar `DivisionPorCeroError` tipado.

#### Ejemplo de Funcionamiento Interno (Python):
```python
from src.runtime.math_engine import HolocronMath

# Lista con valores numericos y un valor nulo para probar robustez
mi_muestra = [120, 180, None, 200, 220, 120]

total = HolocronMath.suma(mi_muestra)          # 840 (ignora None)
media = HolocronMath.promedio(mi_muestra)      # 168.0
mediana = HolocronMath.mediana(mi_muestra)     # 180
maximo = HolocronMath.cenit(mi_muestra)        # 220
minimo = HolocronMath.nadir(mi_muestra)        # 120
cantidad = HolocronMath.conteo(mi_muestra)     # 5 registros validos
dispersion = HolocronMath.desviacion(mi_muestra) # 41.18
```

#### Ejemplo Equivalente en Código HolocronDSL:
```holocron
mi_tabla_flota = abrir_holocron "datos/flota.csv"

mi_analisis_estadistico = mi_tabla_flota
    |> resumir [
        total_puntos = acumular(victorias),
        promedio_escudos = equilibrio(escudos),
        mediana_escudos = mediana(escudos),
        maximo_escudos = cenit(escudos),
        minimo_escudos = nadir(escudos),
        dispersion_escudos = desviacion(escudos)
    ]

transmitir mi_analisis_estadistico
```
*Explicación del ejemplo:*  
- `mi_tabla_flota`: Variable con la tabla cargada.  
- `victorias` y `escudos`: Columnas numéricas del archivo CSV.  
- `mi_analisis_estadistico`: Tabla resumen de una sola fila con todas las métricas calculadas.

---

### 4.2 Biblioteca de Entrada/Salida (`HolocronIO`)
* **Parser CSV propio:** Lee archivos de texto plano caracter a caracter. Reconoce delimitadores personalizados, preserva campos que contienen comas dentro de comillas dobles y decodifica comillas escapadas (`""`).
* **Inferencia automática de tipos:**  
  * Enteros: `"120"` -> `120`  
  * Decimales: `"98.5"` -> `98.5`  
  * Booleanos galácticos: `"cierto_es"`, `"verdadero"` -> `True`; `"falso_es"`, `"falso"` -> `False`  
  * Nulos: `"nulo"`, `"NaN"`, `""` -> `None`  
  * Cadenas: cadenas de texto libres.
* **Exportador a Excel (.xls) nativo:** Genera documentos en formato **XML Spreadsheet 2003**. Este formato estándar permite que Microsoft Excel y LibreOffice Calc (en Kali Linux) abran el archivo directamente reconociendo columnas, filas y tipos de datos numéricos y de texto sin requerir librerías externas de terceros.
* **Creación automática de directorios:** Utiliza `path.parent.mkdir(parents=True, exist_ok=True)` de modo que, si el usuario o docente especifica una subcarpeta inexistente (por ejemplo `"salidas/reportes/flota.xls"`), el motor crea la jerarquía completa de carpetas sin abortar.

#### Ejemplo de Lectura con Inferencia Automática (Python):
```python
from src.runtime.io_engine import HolocronIO

# Lectura directa con parseo manual caracter por caracter
columnas, registros = HolocronIO.leer_csv("datos/flota.csv", delimitador=",")
# columnas: ["id", "modelo", "escudos", "activo"]
# registros: [
#     {"id": "TIE-01", "modelo": "Interceptor", "escudos": 120, "activo": True},
#     {"id": "XW-05",  "modelo": "X-Wing",      "escudos": 180, "activo": True}
# ]
```

#### Ejemplo de Exportación a CSV y Excel en Código HolocronDSL:
```holocron
mi_tabla_datos = abrir_holocron "datos/flota.csv"

// Caso 1: Exportar a texto CSV delimitado
archivar_holocron mi_tabla_datos en "salidas/resultado_flota.csv"

// Caso 2: Exportar a hoja de calculo Excel (.xls) en subcarpeta nueva
archivar_holocron mi_tabla_datos en "salidas/subcarpeta_profesor/resultado_flota.xls"
```
*Explicación del ejemplo:*  
- En el **Caso 1**, se genera un archivo de texto plano delimitado por comas.  
- En el **Caso 2**, el motor detecta la terminación `.xls`, crea la carpeta `subcarpeta_profesor/` automáticamente y genera un libro de cálculo real que se abre de inmediato en LibreOffice Calc o Excel con columnas y celdas tipadas.

---

### 4.3 Estructura de Datos Tabular (`HolocronTable`)
Representa un conjunto de datos en memoria (`columnas: List[str]`, `filas: List[Dict[str, Any]]`).

#### Inmutabilidad Funcional
Cada operación sobre la tabla no modifica la instancia actual; en su lugar, produce y retorna una nueva instancia de `HolocronTable`. Esto previene efectos secundarios indeseados y garantiza la reproducibilidad de los pipelines.

#### Ejemplo de Pipeline de Transformación en Código HolocronDSL:
```holocron
// 1. Cargar datos originales
mi_tabla_base = abrir_holocron "datos/flota.csv"

// 2. Encadenar operaciones funcionales sucesivas
mi_tabla_analizada = mi_tabla_base
    |> purgar donde escudos > 100 y victorias >= 3
    |> forjar rango_combate = escudos + victorias * 15
    |> ordenar por rango_combate descendente
    |> revelar [ identificador, modelo, faccion, rango_combate ]

// Demostracion de inmutabilidad:
// 'mi_tabla_base' permanece intacta con todas sus columnas y filas originales.
// 'mi_tabla_analizada' es un nuevo objeto con las transformaciones aplicadas.
transmitir mi_tabla_analizada
```
*Explicación del ejemplo:*  
- `mi_tabla_base`: Variable original que no sufre ninguna alteración (inmutabilidad).  
- `purgar`: Filtra las filas según la condición booleana.  
- `forjar`: Agrega la columna calculada `rango_combate`.  
- `ordenar`: Ordena las filas de mayor a menor según el rango.  
- `revelar`: Conserva únicamente las 4 columnas de interés.

#### Ejemplo de Agrupamiento y Resumen Estadístico:
```holocron
mi_censo = abrir_holocron "datos/censo.csv"

mi_resumen_planetas = mi_censo
    |> agrupar por [ sector ]
    |> resumir [
        total_mundos = recuento(),
        poblacion_total = acumular(poblacion),
        poblacion_promedio = equilibrio(poblacion),
        max_poblacion = cenit(poblacion)
    ]
    |> ordenar por poblacion_total descendente

transmitir mi_resumen_planetas
```
*Explicación del ejemplo:*  
- `sector`: Columna por la cual se agrupan los planetas.  
- `recuento()`, `acumular()`, `equilibrio()`, `cenit()`: Funciones aplicadas a cada sector.  
- `mi_resumen_planetas`: Tabla final condensada que contiene un registro por cada sector distinto.

---

### 4.4 Motor Gráfico (`HolocronPlotter`)
* Generación exclusiva de gráficos en formato **PNG** a 300 DPI utilizando el backend no interactivo `Agg` de Matplotlib (óptimo para entornos de consola Linux sin interfaz gráfica activa).
* **Prohibición de SVG:** Si el usuario intenta guardar con extensión `.svg`, el sistema rechaza la operación de forma inmediata con un `HolocronSemanticError`.
* **Estilo Visual Galáctico:** Fondo oscuro obsidiana (`#0B0E14`), ejes y rejillas tenues, paleta de colores cian (`#00E5FF`) y ámbar (`#FFB300`).
* **Tipos de Gráficas Soportadas:**
  * `barras`: Comparación categórica discreta.
  * `lineas`: Tendencias o series temporales continuas.
  * `dispersion`: Correlación entre dos variables cuantitativas.
  * `histograma`: Distribución de frecuencias univariadas.
  * `caja`: Diagramas de caja y bigotes para análisis de dispersión y cuartiles.

#### Ejemplo de Proyección de Hologramas en Código HolocronDSL:
```holocron
mi_tabla_naves = abrir_holocron "datos/flota.csv"

// Ejemplo 1: Grafico de barras para comparar facciones
proyectar_holograma barras mi_tabla_naves [
    eje_x = "faccion",
    eje_y = "victorias",
    titulo = "Total de Victorias por Faccion",
    guardar = "salidas/grafica_barras_faccion.png"
]

// Ejemplo 2: Grafico de dispersion para correlacionar escudos vs victorias
proyectar_holograma dispersion mi_tabla_naves [
    eje_x = "escudos",
    eje_y = "victorias",
    titulo = "Correlacion entre Escudos y Victorias",
    guardar = "salidas/grafica_dispersion_defensa.png"
]

// Ejemplo 3: Histograma para analizar la distribucion de escudos
proyectar_holograma histograma mi_tabla_naves [
    eje_x = "escudos",
    titulo = "Distribucion de Frecuencia de Escudos",
    guardar = "salidas/grafica_histograma_escudos.png"
]
```
*Explicación del ejemplo:*  
- Cada llamada a `proyectar_holograma` lee la tabla indicada en el segundo argumento (`mi_tabla_naves`).  
- Los parámetros entre corchetes especifican qué columnas mapear a cada eje y el título.  
- El archivo resultante se guarda en disco en formato `.png` en la ruta especificada en `guardar`.  
- El sistema imprime en la consola la confirmación con la ruta absoluta donde quedó guardada la imagen.

---

## 5. Ejecución en Entorno Linux (Kali Linux en VirtualBox)

### 5.1 Requisitos del Sistema en Kali Linux
Antes de ejecutar el compilador en una máquina virtual de Kali Linux, se deben verificar los paquetes esenciales del sistema:
```bash
sudo apt update
sudo apt install -y python3 python3-venv make antlr4
```

### 5.2 Manejo del Entorno Virtual (PEP 668)
Las versiones recientes de Debian y Kali Linux protegen los paquetes del sistema marcando el entorno como externamente administrado (`externally-managed-environment`). Por esta razón, ejecutar `pip install` de forma global genera un error del sistema operativo.

El proyecto resuelve este problema de dos maneras:
1. **Automática mediante Makefile:** Al ejecutar `make install`, `make test` o `make run-examples`, el Makefile detecta si existe la carpeta `.venv`. Si no existe, la crea automáticamente con `python3 -m venv .venv`, instala las dependencias de `requirements.txt` dentro del entorno virtual y ejecuta las órdenes utilizando el binario `.venv/bin/python3`.
2. **Manual por consola:**
```bash
# 1. Crear el entorno virtual
python3 -m venv .venv

# 2. Activar el entorno en la terminal actual
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

### 5.3 Catálogo de Comandos `make`
El proyecto incluye un `Makefile` compatible con terminales Linux y Windows:
* `make help`: Muestra el resumen de todos los comandos disponibles.
* `make install`: Crea el entorno virtual e instala los requerimientos.
* `make grammar`: Compila el archivo ANTLR4 `HolocronDSL.g4` hacia Python en `src/generated/`.
* `make test`: Ejecuta la suite completa de 93 pruebas unitarias e integrales.
* `make test-lexer`: Ejecuta únicamente las pruebas del analizador léxico.
* `make test-parser`: Ejecuta las pruebas del analizador sintáctico.
* `make test-semantic`: Ejecuta las pruebas semánticas y del evaluador Visitor.
* `make test-ds`: Ejecuta pruebas de estructuras de datos (Arreglos, Pilas, Colas, Bucles).
* `make test-ml`: Ejecuta pruebas de algoritmos de Machine Learning propios.
* `make run-examples`: Ejecuta todos los programas `.holo` de demostración y genera las salidas.
* `make run-sustentacion`: Ejecuta los 5 programas y análisis de la sustentación final.
* `make run-factorial`: Ejecuta el Ejercicio 1 (Factorial 5-100 y benchmark de rendimiento).
* `make run-sigmoide`: Ejecuta el Ejercicio 2 (Proyección de función sigmoide y su derivada).
* `make run-xor`: Ejecuta el Ejercicio 3 (Perceptrón Multicapa para XOR y Backpropagation).
* `make run-eda`: Ejecuta el Ejercicio 4 (Análisis exploratorio sobre censo_ingresos.xlsx).
* `make run-primos`: Ejecuta el Ejercicio 5 (Filtro funcional de primos del 1 al 100).
* `make clean`: Elimina archivos temporales, cachés de Python (`__pycache__`) y logs.

### 5.4 Uso de la Interfaz de Línea de Comandos (`holocron.py`)
El CLI del proyecto proporciona diferentes modos de operación:
```bash
# Modo de ejecucion completa por defecto (evalua e interpreta el programa)
python3 holocron.py examples/01_telemetria_cazas.holo

# Modo de verificacion sintactica y semantica (--check)
python3 holocron.py examples/01_telemetria_cazas.holo --check

# Modo detallado con traza informativa (--verbose)
python3 holocron.py examples/01_telemetria_cazas.holo --verbose

# Inspeccion del arbol sintactico en formato indentado (--tree)
python3 holocron.py examples/01_telemetria_cazas.holo --tree

# Inspeccion del arbol sintactico en notacion LISP / S-Expression (--lisp)
python3 holocron.py examples/01_telemetria_cazas.holo --lisp
```

### 5.5 Cómo Modificar Archivos en Vivo desde la Terminal de Kali Linux
Si el docente solicita alterar un archivo de ejemplo durante la sustentación:
1. Abrir el editor de texto en consola:
   ```bash
   nano examples/01_telemetria_cazas.holo
   ```
2. Realizar las modificaciones requeridas con el cursor y teclado.
3. Guardar los cambios: Presionar la combinación `Ctrl + O` y luego confirmar con `Enter`.
4. Salir del editor: Presionar `Ctrl + X`.
5. Ejecutar nuevamente el programa modificado:
   ```bash
   python3 holocron.py examples/01_telemetria_cazas.holo
   ```

### 5.6 Resolución del Problema de la "Ruta Perdida" al Guardar Archivos
En la sustentación del primer corte, cuando se intentó guardar un archivo en otra ruta y no se encontró, sucedieron dos situaciones:
1. **En el primer corte solo se validaba la sintaxis:** El comando `--check` verificaba que la instrucción estuviera bien escrita gramaticalmente, pero **no ejecutaba ninguna acción en el disco** porque el intérprete aún no existía.
2. **Rutas relativas en consola:** Si se ejecutaba el script desde una carpeta distinta (por ejemplo `/home/kali/`), una ruta relativa como `"salidas/datos.xls"` se creaba en `/home/kali/salidas/` y no dentro de la carpeta del proyecto.

#### Solución implementada en el segundo corte:
1. El motor crea automáticamente cualquier carpeta que no exista mediante `path.parent.mkdir(parents=True, exist_ok=True)`.
2. El intérprete imprime de inmediato en la terminal la **ruta absoluta completa** del archivo recién creado:
   ```text
   [Holocron Guardado] Holocron 'flota_operativa' exportado con exito:
     -> Formato: Excel (.xls)
     -> Registros: 10 filas | 5 columnas
     -> Ubicacion absoluta: /home/kali/Downloads/Lenguaje-propio-HolocronDSL/salidas/reporte.xls
   ```
3. Para comprobar o abrir el archivo en Kali Linux:
   ```bash
   # Ver detalles en consola
   ls -la salidas/reporte.xls

   # Abrir directamente en LibreOffice Calc
   libreoffice salidas/reporte.xls &
   ```

### 5.7 Comandos Paso a Paso para los 5 Ejercicios de Sustentación en Kali Linux

Para defender la sustentación en la máquina virtual Kali Linux, se deben ejecutar los siguientes comandos directamente en la terminal:

```bash
# Navegar a la carpeta del proyecto
cd ~/Downloads/Lenguaje-propio-HolocronDSL-main  # O la ruta donde se encuentre clonado

# Activar el entorno virtual previamente configurado
source .venv/bin/activate
```

#### Ejercicio 1: Factorial del 5 al 100 y Comparación con Python
```bash
# 1. Ejecutar el cálculo iterativo en HolocronDSL:
python3 holocron.py "Ejercicios sustentacion final/01_factorial_rendimiento.holo"

# 2. Ejecutar el benchmark comparativo frente a Python:
python3 "Ejercicios sustentacion final/benchmark_factorial.py"

# 3. Visualizar la gráfica generada en Kali Linux:
ristretto "Ejercicios sustentacion final/salidas/comparativa_rendimiento_factorial.png" &
```

#### Ejercicio 2: Visualización de la Función Sigmoide
```bash
# 1. Evaluar y proyectar la sigmoide en HolocronDSL:
python3 holocron.py "Ejercicios sustentacion final/02_visualizar_sigmoide.holo"

# 2. Generar el análisis detallado de la sigmoide y su derivada:
python3 "Ejercicios sustentacion final/generar_sigmoide.py"

# 3. Ver la gráfica de alta resolución en Kali Linux:
ristretto "Ejercicios sustentacion final/salidas/grafica_sigmoide_completa.png" &
```

#### Ejercicio 3: Perceptrón Multicapa para XOR (Estimador y Gráficas)
```bash
# 1. Entrenar y estimar XOR con el MLP en HolocronDSL:
python3 holocron.py "Ejercicios sustentacion final/03_perceptron_multicapa_xor.holo"

# 2. Generar el análisis teórico, curva de pérdida y frontera 2D:
python3 "Ejercicios sustentacion final/analisis_mlp_xor.py"

# 3. Visualizar la frontera de decisión no lineal y la convergencia en Kali:
ristretto "Ejercicios sustentacion final/salidas/frontera_decision_xor.png" &
ristretto "Ejercicios sustentacion final/salidas/convergencia_perdida_xor.png" &
```

#### Ejercicio 4: Análisis Exploratorio de Datos (EDA) sobre `censo_ingresos.xlsx`
```bash
# 1. Ejecutar el análisis sobre los 10,280 registros en HolocronDSL:
python3 holocron.py "Ejercicios sustentacion final/04_analisis_exploratorio_xlsx.holo"

# 2. Ejecutar el script descriptivo complementario:
python3 "Ejercicios sustentacion final/analisis_eda_xlsx.py"

# 3. Ver los 3 gráficos proyectados (barras, cajas, histograma) en Kali:
ristretto "Ejercicios sustentacion final/salidas/eda_ingreso_por_educacion.png" &
ristretto "Ejercicios sustentacion final/salidas/eda_dispersion_ingreso_sexo.png" &
ristretto "Ejercicios sustentacion final/salidas/eda_distribucion_edad.png" &
```

#### Ejercicio 5: Filtro Funcional de Números Primos del 1 al 100
```bash
# 1. Ejecutar el filtrado de orden superior en HolocronDSL:
python3 holocron.py "Ejercicios sustentacion final/05_filtro_primos_1_100.holo"

# 2. Ejecutar la validación formal de los 25 números primos:
python3 "Ejercicios sustentacion final/verificar_primos.py"
```

#### Ejecución Automatizada Total
```bash
# Opcion A: Con el Makefile
make run-sustentacion

# Opcion B: Con el script interactivo para Kali
chmod +x "Ejercicios sustentacion final/ejecutar_en_kali.sh"
./"Ejercicios sustentacion final/ejecutar_en_kali.sh" 1
```

---

## 6. Banco de Preguntas y Respuestas para la Sustentación Oral

A continuación se presentan las preguntas más probables que el profesor puede formular, junto con la respuesta técnica y conceptual recomendada:

### Pregunta 1: "¿Por qué en la primera entrega no se generaban archivos en disco y en esta entrega sí?"
* **Respuesta del estudiante:**  
  "En el primer corte el objetivo académico era la construcción del Front-End del compilador: el análisis léxico, el análisis sintáctico y la construcción del árbol de derivación (AST). Por ende, el sistema únicamente verificaba con `--check` que la sintaxis fuera gramaticalmente correcta, sin ejecutar sentencias. En este segundo corte implementamos el Back-End de evaluación: el patrón Visitor, la tabla de símbolos y los motores de entrada y salida (`HolocronIO`). Ahora el intérprete recorre semánticamente los nodos del árbol y ejecuta físicamente la persistencia de datos en disco."

### Pregunta 2: "¿Por qué decidieron utilizar el patrón Visitor en lugar del patrón Listener para el intérprete?"
* **Respuesta del estudiante:**  
  "El patrón Listener recorre el árbol de forma pasiva y automática mediante eventos `enter` y `exit`. Ese modelo es rígido y no permite controlar el flujo de ejecución. En nuestro lenguaje contamos con estructuras condicionales (`evaluar_fuerza`), donde solo se debe evaluar una de las dos ramas (`senda_luminosa` o `senda_oscura`), y misiones parametrizadas cuyos cuerpos solo deben ejecutarse cuando son invocadas. El patrón Visitor nos otorga control total sobre la navegación del árbol, permitiéndonos decidir qué nodos visitar, en qué orden y propagar el valor de retorno directamente entre llamadas recursivas."

### Pregunta 3: "¿Cómo administra el lenguaje el ámbito (scope) y qué sucede si una variable local tiene el mismo nombre que una global?"
* **Respuesta del estudiante:**  
  "Diseñamos una tabla de símbolos jerárquica basada en una estructura de árbol de ámbitos (`Scope`). Cada ámbito almacena un diccionario de símbolos locales y un puntero hacia su ámbito contenedor padre. Cuando se invoca una misión, se crea un nuevo ámbito local. Si dentro de la misión se define una variable con el mismo nombre que una global, se produce el fenómeno de 'sombreado de variables' (*variable shadowing*): la variable local enmascara a la variable externa dentro de la función sin sobreescribir su valor en el ámbito global. Al finalizar la misión, el ámbito local se descarta y el valor global permanece intacto."

### Pregunta 4: "¿Cómo funciona internamente el operador pipeline `|>`?"
* **Respuesta del estudiante:**  
  "El operador `|>` es asociativo hacia la izquierda. En el árbol sintáctico, la regla `expresionPipeline` evalúa primero la expresión base (que puede ser la carga de un archivo con `abrir_holocron` o una variable existente). Luego, toma el objeto `HolocronTable` resultante y lo entrega como argumento de entrada al primer método de transformación (por ejemplo, `seleccionar`). Ese método retorna una nueva instancia transformada que a su vez se convierte en la entrada del siguiente eslabón del pipeline. De este modo, los datos fluyen funcionalmente de etapa en etapa sin mutar los estados intermedios."

### Pregunta 5: "¿Cómo implementaron las funciones estadísticas como promedio o mediana sin usar numpy ni pandas?"
* **Respuesta del estudiante:**  
  "Construimos una biblioteca matemática propia en `src/runtime/math_engine.py` llamada `HolocronMath`. Para el promedio, calculamos la sumatoria de elementos numéricos filtrando valores nulos y la dividimos entre la cardinalidad válida. Para la mediana, ordenamos la lista internamente: si la longitud es impar, extraemos el elemento de la posición central exacta; si es par, calculamos la media aritmética de los dos elementos centrales. La varianza y desviación típica las calculamos mediante sumatorias de diferencias cuadráticas respecto a la media. Esto garantiza independencia total de librerías externas de análisis numérico."

### Pregunta 6: "¿Qué ocurre si en un filtro (`purgar`) se compara una columna numérica contra un texto o si se divide por cero?"
* **Respuesta del estudiante:**  
  "El sistema cuenta con un subsistema de excepciones semánticas tipadas en `src/errors/semantic_error.py`. En caso de comparar tipos incompatibles mediante operadores relacionales (`<`, `>`, `<=`, `>=`), el intérprete captura la incompatibilidad y arroja un `TipoIncompatibleError`. En el caso de divisiones, `HolocronMath` intercepta un denominador cero antes de ejecutar la operación y arroja un `DivisionPorCeroError`, indicando la línea y la columna exacta del error junto con un mensaje orientativo en la terminal."

### Pregunta 7: "¿Por qué no utilizaron SVG para graficar y cómo está construido el motor de visualización?"
* **Respuesta del estudiante:**  
  "Por requerimientos de diseño del lenguaje descartamos totalmente el formato vectorial SVG para evitar complejidades de renderizado en diferentes navegadores y visores. Nuestro motor `HolocronPlotter` utiliza Matplotlib configurado con el backend no interactivo `Agg`. Este backend dibuja directamente sobre mapas de bits en memoria sin requerir un servidor gráfico X11, lo cual es ideal para entornos de servidor o terminales Linux en máquinas virtuales. Todas las proyecciones se exportan exclusivamente en archivos matriciales PNG a 300 DPI con una paleta visual de alto contraste."

### Pregunta 8: "¿Cómo genera HolocronDSL archivos de Excel (.xls) sin usar pandas ni openpyxl?"
* **Respuesta del estudiante:**  
  "Implementamos un serializador propio en `HolocronIO.escribir_excel_xls()` que genera la especificación oficial **XML Spreadsheet 2003**. Este formato estructura el libro, las hojas de cálculo, las filas y las celdas mediante etiquetas XML (`<Workbook>`, `<Worksheet>`, `<Row>`, `<Cell>`, `<Data ss:Type="Number|String">`). Es un estándar que tanto Microsoft Excel como LibreOffice Calc reconocen de forma nativa como una hoja de cálculo real con celdas tipadas, sin necesidad de compilar formatos binarios complejos ni recurrir a paquetes externos pesados."

### Pregunta 9: "¿Cómo garantiza el lenguaje la inmutabilidad de los datos?"
* **Respuesta del estudiante:**  
  "Dentro de `HolocronTable`, los registros se almacenan como una lista de diccionarios. Cada vez que se ejecuta una operación (como `purgar`, `forjar` u `ordenar`), el método genera copias superficiales de las filas pertinentes y retorna una nueva instancia de `HolocronTable`. El objeto original nunca se modifica. Si un usuario desea conservar el resultado, debe asignarlo a una nueva variable o sobreescribir la referencia explícitamente mediante una sentencia de asignación."

### Pregunta 10: "Modifique en vivo este programa para agregar una columna calculada y guardarlo en una nueva carpeta."
* **Acción paso a paso del estudiante:**  
  1. Abrir el archivo con `nano examples/01_telemetria_cazas.holo`.
  2. Dentro del pipeline, agregar una etapa de forja:
     ```holocron
     |> forjar potencia_total = escudos + victorias * 10
     ```
  3. Modificar la sentencia de archivado para apuntar a la nueva carpeta solicitada:
     ```holocron
     archivar_holocron flota_operativa en "salidas_evaluacion/resultado_nuevo.xls"
     ```
  4. Guardar (`Ctrl+O`, `Enter`) y cerrar (`Ctrl+X`).
  5. Ejecutar en consola: `python3 holocron.py examples/01_telemetria_cazas.holo`.
  6. Señalar en la pantalla la confirmación del sistema donde aparece la ruta absoluta y verificar con `ls -la salidas_evaluacion/resultado_nuevo.xls`.

---

## 7. Consejos Prácticos para la Sustentación en Pareja

### 7.1 Distribución del Discurso
* **Andrés Sebastián:** Puede introducir la arquitectura del proyecto, la compilación de la gramática en ANTLR4, el flujo de ejecución mediante el patrón Visitor y la demostración práctica en la terminal de Kali Linux.
* **Carol:** Puede exponer la tabla de símbolos y la resolución de ámbitos, las reglas semánticas y cómo las bibliotecas propias (`HolocronTable`, `HolocronMath`, `HolocronIO` y `HolocronPlotter`) procesan los datos e interactúan de forma inmutable.

### 7.2 Manejo de la Pantalla y Terminal
* Tener abiertas dos pestañas en la terminal de Kali Linux:
  * **Pestaña 1:** Ubicada en la raíz del proyecto para ejecutar pruebas y programas (`make test`, `python3 holocron.py ...`).
  * **Pestaña 2:** Lista para editar código con `nano` o revisar los archivos resultantes en la carpeta `salidas/`.
* Si el profesor pide comprobar la suite de pruebas automatizadas, ejecutar `make test` o `python3 run_tests.py --all`. Al ver las 69 pruebas pasar con éxito en menos de 2 segundos, se demuestra la solidez y estabilidad del compilador.

### 7.3 Comandos de Rescate Rápido en Kali Linux
* **Si falta el entorno virtual:**
  ```bash
  make install
  ```
* **Si se modificó la gramática (`.g4`) y se necesita recompilar:**
  ```bash
  make grammar
  ```
* **Si se necesita limpiar archivos generados:**
  ```bash
  make clean
  ```
* **Si se desea ver la estructura sintáctica de cualquier script:**
  ```bash
  python3 holocron.py examples/01_telemetria_cazas.holo --tree
  ```

---

## 8. Tercera Entrega (Fase 3): Modelado Estadístico, Regresión Lineal y Caso de Estudio

La tercera entrega consolida a HolocronDSL como una solución integral de ciencia de datos, integrando capacidades analíticas avanzadas, modelado matemático formal y un caso de estudio real con 5 tipos de visualizaciones.

### 8.1 Regresión Lineal Simple por Mínimos Cuadrados Ordinarios (OLS)
El lenguaje no recurre a paquetes externos como `scikit-learn` ni `statsmodels`. El ajuste se resuelve analíticamente en `HolocronMath.regresion_lineal`:

1. **Fórmulas de estimación:**
   $$\text{Pendiente } m = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}$$
   $$\text{Intercepto } b = \bar{y} - m\bar{x}$$
   $$\text{Coeficiente de determinación } R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$
   $$\text{Correlación de Pearson } r = \frac{\text{Cov}(X,Y)}{S_x S_y}$$

2. **Sintaxis en HolocronDSL:**
   ```holocron
   modelo = tabla
       |> trazar_regresion [
           eje_x = "distancia_parsecs",
           eje_y = "latencia_ms",
           destino = "latencia_predicha"
       ]
   ```

3. **Estructura `HolocronRegressionResult`:**
   El resultado es una subclase especializada de `HolocronTable` que contiene tanto la tabla enriquecida con la columna de predicciones como los metadatos del modelo ($m$, $b$, $R^2$, $r$, $S_e$, residuos). Esto permite continuar encadenando operaciones en el pipeline si se desea.

### 8.2 Visualizaciones Holográficas (5 Tipos Matriciales PNG a 300 DPI)
HolocronDSL ofrece soporte nativo para 5 representaciones gráficas completas:
1. `barras`: Comparaciones categóricas discretas (ej. latencia media por sector).
2. `histograma`: Distribuciones continuas de frecuencia (ej. distribución de latencia).
3. `caja` (boxplot): Análisis de dispersión, medianas y cuartiles (ej. ancho de banda).
4. `lineas`: Series ordenadas o perfiles de degradación.
5. `regresion` / `tendencia`: Diagrama de dispersión de puntos reales con la recta ajustada y leyenda con $R^2$ y ecuación.

**Regla estricta:** Todas las imágenes se generan en formato raster PNG a 300 DPI utilizando el backend no interactivo `Agg` de Matplotlib, descartando explícitamente el uso de SVG para evitar inconsistencias de visualización.

### 8.3 Resumen del Caso de Estudio Final
Ubicado en `examples/06_caso_estudio_final.holo`:
- **Dominio:** Telemetría de 30 repetidores de telecomunicaciones galácticas en 10 sectores astronómicos.
- **Pipeline aplicado:** Filtrado de nodos operativos, saneamiento de nulos, forja de tasa de pérdida de paquetes y carga efectiva, ordenamiento, agregación multidimensional por sector y ajuste de regresión OLS entre distancia y latencia.
- **Resultados obtenidos:** $m = 1.0967$, $b = 4.0152$, $R^2 = 0.9842$, $r = 0.9921$.
- **Archivos generados:** 5 imágenes PNG a 300 DPI, 1 tabla CSV consolidada y 1 libro de cálculo Excel (.xls) nativo con datos y predicciones.

---

## 9. Banco de Preguntas Orales para la Sustentación del Tercer Corte

### Pregunta 11: "¿Cómo implementaron la regresión lineal en HolocronDSL sin usar scikit-learn ni bibliotecas de machine learning?"
* **Respuesta del estudiante:**  
  "Desarrollamos las fórmulas matemáticas analíticas del método de Mínimos Cuadrados Ordinarios (OLS) directamente en Python puro dentro de `src/runtime/math_engine.py`. El método `regresion_lineal()` limpia pares válidos de números, calcula las medias aritméticas $\bar{x}$ y $\bar{y}$, la covarianza muestral, la varianza de $x$ y obtiene directamente la pendiente $m$ y el intercepto $b$. A partir de allí evalúa la suma de cuadrados de los residuos y la suma total de cuadrados para calcular el coeficiente de determinación $R^2$ y el coeficiente de correlación de Pearson $r$. De este modo no requerimos ninguna dependencia externa pesada para modelar."

### Pregunta 12: "¿Por qué no utilizaron el formato vectorial SVG para los gráficos y cómo garantizan que funcione en una máquina virtual de Linux sin entorno gráfico?"
* **Respuesta del estudiante:**  
  "Descartamos deliberadamente el formato SVG porque su visualización depende de renderizadores vectoriales del navegador o visores externos que pueden alterar fuentes, tamaños y estilos. En su lugar, generamos imágenes rasterizadas PNG de alta resolución fija a 300 DPI. Para que funcione sin problemas en servidores o máquinas virtuales Linux como Kali, configuramos el backend `Agg` (Anti-Grain Geometry) de Matplotlib al inicio de `graphics_engine.py`. Este backend dibuja directamente sobre mapas de bits en la memoria RAM y guarda el PNG en disco, sin requerir un servidor de pantallas X11 ni interfaz gráfica de usuario activa."

### Pregunta 13: "¿Qué es `HolocronRegressionResult` y cómo mantiene la coherencia del lenguaje?"
* **Respuesta del estudiante:**  
  "`HolocronRegressionResult` es una subclase de `HolocronTable`. Al ser una tabla, hereda todas las propiedades de inmutabilidad y puede seguirse encadenando con otras operaciones del pipeline (como `purgar`, `ordenar` o `archivar_holocron`). Sin embargo, almacena adicionalmente un diccionario con los parámetros del modelo matemático ($m$, $b$, $R^2$, $r$, residuos) y sobreescribe el método de representación para que al ejecutar `transmitir modelo`, la consola muestre tanto el resumen estadístico de la ecuación ajustada como la tabla de datos extendida con la nueva columna de predicciones."

### Pregunta 14: "¿Cómo sustentan que HolocronDSL es totalmente original frente a otros proyectos del curso?"
* **Respuesta del estudiante:**  
  "HolocronDSL posee una identidad temática, sintáctica y semántica completamente única basada en la ciencia de datos y el universo galáctico. Nuestro vocabulario utiliza términos formales como `abrir_holocron`, `revelar`, `purgar donde`, `forjar`, `agrupar por`, `resumir`, `trazar_regresion`, `proyectar_holograma` y `transmitir`. No comparte absolutamente ninguna palabra clave, convención ni estructura con otros repositorios del curso. Además, todas las bibliotecas de procesamiento tabular (`HolocronTable`), matemáticas (`HolocronMath`) y exportación a Excel XML 2003 (`HolocronIO`) fueron escritas desde cero por nosotros sin utilizar librerías típicas como pandas o numpy."

### Pregunta 15: "Durante la sustentación, modifique el caso de estudio para cambiar la variable dependiente de la regresión o agregar una condición de filtro."
* **Acción paso a paso del estudiante:**  
  1. Abrir el archivo con `nano examples/06_caso_estudio_final.holo`.
  2. Localizar la instrucción `trazar_regresion`:
     ```holocron
     modelo_nuevo = red_operativa
         |> trazar_regresion [
             eje_x = "distancia_parsecs",
             eje_y = "tasa_perdida",
             destino = "perdida_estimada"
         ]
     ```
  3. Guardar con `Ctrl + O`, `Enter` y salir con `Ctrl + X`.
  4. Ejecutar: `python3 holocron.py examples/06_caso_estudio_final.holo`.
  5. Señalar en la consola los nuevos coeficientes calculados para el modelo ajustado y la generación exitosa de los reportes.

---

## 10. Estructuras de Datos Nativas y Control Iterativo (Fase 3 Ampliada)

Para dar respuesta rigurosa a los requerimientos avanzados de transducción y compilación, HolocronDSL incorpora estructuras de datos lineales y jerárquicas nativas implementadas desde cero en `src/runtime/data_structures.py`, sin recurrir a bibliotecas de terceros.

### 10.1 Arreglos y Listas Dimensionadas
HolocronDSL ofrece la clase `HolocronArray`, la cual admite literales de arreglos, indexación con verificación de límites y dimensionamiento explícito:

1. **Creación de listas con tamaño predeterminado (por ejemplo, 10 posiciones):**
   ```holocron
   mi_lista = crear_lista(10, 0)
   transmitir mi_lista
   ```
   *Explicación:* Crea un arreglo de 10 posiciones inicializadas con el valor `0`: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`.

2. **Indexación y Asignación por Índice:**
   Los arreglos son indexados desde `0`. Se admiten tanto lecturas como modificaciones directas por posición:
   ```holocron
   mi_lista[0] = 100
   mi_lista[5] = 555
   mi_lista[9] = 999
   primer_elemento = mi_lista[0]
   ```
   *Seguridad semántica:* Si se intenta acceder a una posición fuera del rango válido (por ejemplo `mi_lista[15]`), el intérprete detiene la ejecución arrojando una excepción semántica `IndiceFueraDeRangoError` indicando el índice infractor y la longitud actual de la estructura.

3. **Operaciones y Métodos Nativos de Arreglos:**
   - `longitud(coleccion)`: Retorna la cantidad de elementos presentes.
   - `agregar(arreglo, elemento)`: Añade un elemento al final del arreglo.
   - `insertar(arreglo, indice, elemento)`: Inserta un elemento en una posición específica desplazando los posteriores.
   - `remover(arreglo, indice)`: Elimina y retorna el elemento en el índice indicado.
   - `obtener(arreglo, indice)`: Recupera el valor en el índice dado.
   - `subarreglo(arreglo, inicio, fin)`: Retorna una nueva lista que es una rebanada desde `inicio` hasta `fin`.
   - `invertir(arreglo)`: Retorna un nuevo arreglo con los elementos en orden inverso.
   - `ordenar_lista(arreglo, descendente)`: Ordena numéricamente o alfabéticamente los elementos (por defecto ascendente; pasar `cierto_es` para orden descendente).

### 10.2 Pilas (Estructura LIFO: Last-In, First-Out)
La clase `HolocronPila` modela una pila de memoria protegida para almacenamiento temporal de estados:
```holocron
mi_pila = crear_pila()
apilar(mi_pila, "Plan_Alfa")
apilar(mi_pila, "Plan_Beta")
apilar(mi_pila, "Plan_Gamma")

elemento_superior = cima(mi_pila)         // Retorna "Plan_Gamma" sin retirarlo
elemento_extraido = desapilar(mi_pila)     // Extrae y retorna "Plan_Gamma"
vacia = esta_vacia(mi_pila)                // Retorna falso_es
```
*Seguridad semántica:* Invocar `desapilar` o `cima` sobre una pila vacía produce un error controlado `EstructuraVaciaError`.

### 10.3 Colas (Estructura FIFO: First-In, First-Out)
La clase `HolocronCola` modela colas de procesamiento secuencial para despacho de tareas o naves:
```holocron
mi_cola = crear_cola()
encolar(mi_cola, "Caza_01")
encolar(mi_cola, "Caza_02")
encolar(mi_cola, "Caza_03")

proximo = frente(mi_cola)                 // Retorna "Caza_01" sin extraerlo
atendido = desencolar(mi_cola)            // Retorna "Caza_01" y lo retira de la cola
```
*Seguridad semántica:* Invocar `desencolar` o `frente` sobre una cola vacía produce un error controlado `EstructuraVaciaError`.

### 10.4 Estructuras de Control Iterativas (Bucles)
HolocronDSL introduce tres construcciones cíclicas de alto nivel:

1. **Bucle Condicional (`mientras`):**
   Ejecuta un bloque de sentencias de forma repetitiva mientras una condición booleana sea verdadera:
   ```holocron
   contador = 0
   mientras (contador < 5)
       contador = contador + 1
   fin_mientras
   ```

2. **Bucle de Rango Numérico (`para ... desde ... hasta`):**
   Itera una variable contadora en un intervalo entero cerrado $[inicio, fin]$ con paso unitario automático:
   ```holocron
   total = 0
   para i desde 1 hasta 10
       total = total + i
   fin_para
   ```

3. **Bucle de Colección (`recorrer ... en`):**
   Itera directamente sobre los elementos de un arreglo, lista o columna:
   ```holocron
   naves = ["Destructor", "Corbeta", "Fragata"]
   recorrer nave en naves
       transmitir nave
   fin_recorrer
   ```

### 10.5 Árbol de Decisión como Estructura de Datos Jerárquica
La clase `NodoArbolDecision` modela los nodos de un árbol binario de partición:
- **Atributos:** `es_hoja` (booleano), `columna_particion` (nombre de variable), `umbral` (valor de corte numérico o categórico), `clase_predicha` (etiqueta mayoritaria en nodos hoja), `impureza_gini` (métrica de pureza local), `muestras` (cantidad de registros que alcanzaron el nodo), `hijo_izquierdo` (rama donde el valor $\le$ umbral), `hijo_derecho` (rama donde el valor $>$ umbral).
- **Inspección visual:** Método `imprimir_arbol()` que renderiza la jerarquía completa del árbol en texto plano ASCII legible en consola.

---

## 11. Motor Propio de Machine Learning (`src/runtime/ml_engine.py`)

HolocronDSL no delega ningún cálculo en librerías de terceros (no utiliza `scikit-learn`, `numpy` ni `pandas`). Todo el cálculo numérico y matricial está programado desde cero.

### 11.1 Algoritmos Soportados
1. **Árbol de Decisión Clasificador (`ArbolDecisionGalactico`):**
   - **Algoritmo:** Implementación del algoritmo CART (Classification and Regression Trees).
   - **Criterio de corte:** Maximización de la Ganancia de Información mediante la reducción de la impureza de Gini:
     $$I_G(S) = 1 - \sum_{k=1}^C p_k^2$$
     $$\Delta I_G = I_G(S) - \left( \frac{|S_I|}{|S|} I_G(S_I) + \frac{|S_D|}{|S|} I_G(S_D) \right)$$
   - **Parámetros:** `profundidad_maxima` y `minimo_muestras_corte`.
   - **Inferencia:** Clasificación multiclase recursiva sobre nuevas observaciones.

2. **Perceptrón Binario de Rosenblatt (`PerceptronGalactico`):**
   - **Modelo:** Clasificador lineal con regla de actualización estocástica:
     $$z = \mathbf{w}^T \mathbf{x} + b = \sum_{j=1}^d w_j x_j + b$$
     $$\hat{y} = \begin{cases} 1 & \text{si } z \ge 0 \\ 0 & \text{si } z < 0 \end{cases}$$
   - **Regla de aprendizaje:**
     $$\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} + \eta (y - \hat{y}) \mathbf{x}$$
     $$b^{(t+1)} = b^{(t)} + \eta (y - \hat{y})$$
   - **Parámetros:** `tasa_aprendizaje` ($\eta$, por defecto 0.05), `epocas` (por defecto 100).

3. **Agrupamiento K-Means (`KMeansGalactico`):**
   - **Algoritmo:** Aprendizaje no supervisado mediante minimización de la inercia intracluster:
     $$J = \sum_{i=1}^k \sum_{\mathbf{x} \in C_i} \|\mathbf{x} - \boldsymbol{\mu}_i\|^2$$
   - **Inicialización:** K-Means++ determinístico basado en distancias euclidianas máximas para evitar estancamiento en mínimos locales.
   - **Parámetros:** `k` (número de clusters) y `max_iteraciones`.

### 11.2 Filtros y Preprocesamiento de Datos
- **Normalización Min-Max:** Escala las columnas continuas al intervalo cerrado $[0, 1]$:
  $$x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$
- **Estandarización Z-Score:** Transforma la variable para que tenga media $\mu = 0$ y desviación estándar $\sigma = 1$:
  $$z = \frac{x - \mu}{\sigma}$$
- **Codificación de Etiquetas Categóricas:** Convierte cadenas de texto (ej. `"Imperio"`, `"Alianza"`) a enteros determinísticos $[0, 1, \dots, C-1]$.

### 11.3 Métricas de Evaluación
- `evaluar_exactitud(y_real, y_pred)`: Proporción de predicciones correctas sobre el total:
  $$\text{Accuracy} = \frac{\sum [y_i = \hat{y}_i]}{n}$$
- `matriz_confusion(y_real, y_pred)`: Tabla de contingencia bidimensional cruzando clases reales y predichas.
- `calcular_impureza_gini(etiquetas)`: Impureza de Gini de un conjunto de clases.
- `calcular_entropia(etiquetas)`: Entropía de Shannon de un conjunto de clases:
  $$H(S) = - \sum_{k=1}^C p_k \log_2(p_k)$$

### 11.4 Integración en Pipelines de HolocronDSL
Los modelos y preprocesadores se encadenan fluidamente en los flujos tabulares:
```holocron
tabla_ml = abrir_holocron "examples/datos/telemetria_flota.csv"
    |> normalizar_minmax [ columnas = ["escudos", "victorias"] ]
    |> agrupar_kmeans [
        columnas = ["escudos", "victorias"],
        k = 2,
        destino = "cluster_tactico"
    ]
    |> clasificar_arbol [
        caracteristicas = ["escudos", "tripulantes"],
        objetivo = "faccion",
        destino = "prediccion_faccion"
    ]
```

---

## 12. Banco de Preguntas Orales para la Sustentación Final (Estructuras y ML)

### Pregunta 16: "¿Cómo maneja HolocronDSL una lista de 10 posiciones y qué ocurre si se desbordan los límites?"
* **Respuesta del estudiante:**  
  "En HolocronDSL una lista de 10 posiciones se define mediante la función de biblioteca `crear_lista(10, valor_inicial)`, por ejemplo `mi_lista = crear_lista(10, 0)`. Esto instancia un objeto `HolocronArray` que reserva exactamente 10 elementos. Los elementos se leen o modifican mediante indexación `mi_lista[0] = 100` o `mi_lista[9] = 999`. Si se intenta acceder a un índice negativo o mayor o igual a 10 (por ejemplo `mi_lista[10]`), nuestro evaluador no produce un fallo silencioso ni una excepción no controlada de Python, sino que arroja una excepción de lenguaje `IndiceFueraDeRangoError`, indicando con exactitud la línea del programa, el índice intentado y los límites del arreglo."

### Pregunta 17: "¿Cómo se diferencian conceptual y operativamente las Pilas y las Colas en HolocronDSL?"
* **Respuesta del estudiante:**  
  "Ambas son estructuras de datos nativas implementadas en `src/runtime/data_structures.py`. La Pila (`HolocronPila`) sigue la semántica LIFO (Last-In, First-Out), manipulándose con `apilar(pila, elem)`, `desapilar(pila)` y `cima(pila)`. La Cola (`HolocronCola`) sigue la semántica FIFO (First-In, First-Out), gestionándose con `encolar(cola, elem)`, `desencolar(cola)` y `frente(cola)`. En caso de que se intente desapilar o desencolar cuando la estructura no contiene elementos, se lanza una excepción semántica `EstructuraVaciaError`."

### Pregunta 18: "¿Cómo desarrollaron el árbol de decisión y el algoritmo K-Means sin usar librerías de Machine Learning como Scikit-Learn?"
* **Respuesta del estudiante:**  
  "Programamos las formulaciones matemáticas originales directamente en Python puro en `src/runtime/ml_engine.py`:
  - Para el Árbol de Decisión (`ArbolDecisionGalactico`), implementamos el algoritmo CART. En cada nodo se evalúa la impureza de Gini de la variable objetivo y se buscan todos los umbrales de corte posibles en cada columna predictora para encontrar el corte que maximice la reducción de impureza (ganancia de Gini). La estructura jerárquica del árbol se almacena en objetos `NodoArbolDecision`.
  - Para el K-Means (`KMeansGalactico`), implementamos el cálculo de la distancia euclidiana n-dimensional, una inicialización determinística K-Means++ que escoge centroides distantes entre sí, y un bucle de convergencia que reasigna cada muestra al centroide más cercano y recalcula las coordenadas de los centroides como el vector promedio de sus miembros hasta que la inercia se estabiliza.
  Todo el cálculo se realiza con listas y diccionarios nativos, garantizando 100% de originalidad y cero dependencias prohibidas."

### Pregunta 19: "¿Cuáles son y cómo funcionan las nuevas estructuras de control de bucles en la gramática?"
* **Respuesta del estudiante:**  
  "Incorporamos tres tipos de bucles formales en `grammar/HolocronDSL.g4`:
  1. `mientras (condicion) ... fin_mientras`: Bucle controlado por condición booleana arbitraria.
  2. `para id desde inicio hasta fin ... fin_para`: Bucle para progresiones aritméticas en un rango entero inclusivo.
  3. `recorrer id en coleccion ... fin_recorrer`: Bucle iterativo de alto nivel para recorrer secuencias de datos (arreglos o columnas).
  El Visitor (`HolocronVisitor`) evalúa las condiciones dinámicamente y ejecuta el bloque de sentencias hijas en un ámbito de ejecución local seguro."

### Pregunta 20: "¿Cómo se prueba y valida todo el sistema en Linux?"
* **Respuesta del estudiante:**  
  "El proyecto cuenta con un archivo `Makefile` y un ejecutor automatizado `run_tests.py` que compilan la gramática ANTLR4 y ejecutan un total de 93 pruebas unitarias e integrales organizadas en módulos:
  - `make test` o `python3 run_tests.py --all`: Ejecuta la suite completa de 93 pruebas pasando al 100%.
  - `make test-ds`: Ejecuta las 12 pruebas específicas de Arreglos, Pilas, Colas, Bucles y Nodos de Árbol.
  - `make test-ml`: Ejecuta las 12 pruebas del motor de Machine Learning y pipelines de clasificación y clustering.
  - `make run-examples`: Ejecuta secuencialmente los 7 ejemplos del lenguaje (incluyendo `07_estructuras_y_machine_learning.holo`), generando todos los reportes CSV, Excel XLS y gráficos PNG en la carpeta `salidas/`."

---

## 13. Banco de Preguntas Específicas para los 5 Ejercicios de Sustentación Final

En la carpeta `Ejercicios sustentacion final/` se encuentran los 5 programas implementados para defender la sustentación práctica. A continuación se presentan las preguntas orales esperadas y las respuestas formales recomendadas:

### Pregunta 21: "¿Cómo calcularon el factorial del 5 al 100 y a qué se debe la diferencia de rendimiento frente a Python?"
* **Respuesta del estudiante:**  
  "Implementamos una misión iterativa `factorial(n)` en HolocronDSL (`01_factorial_rendimiento.holo`) que utiliza un bucle `para i desde 2 hasta n` multiplicando un acumulador. Ambos lenguajes manejan enteros de precisión arbitraria (BigInt), calculando con exacta precisión los 158 dígitos de 100! sin desbordamiento.
  En cuanto al rendimiento:
  - **Ambos algoritmos tienen una complejidad temporal O(n)**.
  - **La diferencia de tiempo radica en el nivel de abstracción de ejecución:** Python compila el código fuente a bytecode de bajo nivel que una máquina virtual en lenguaje C (CPython) ejecuta en nanosegundos con acceso directo a registros. Por el contrario, HolocronDSL es un **intérprete sobre el árbol de sintaxis abstracta (AST)** que utiliza el patrón Visitor; cada multiplicación implica recorrer nodos de la gramática ANTLR4, buscar identificadores en la Tabla de Símbolos, verificar tipos y despachar métodos polimórficos. Esa sobrecarga de despacho dinámico en memoria es la esperada formalmente en cualquier intérprete AST respecto a un motor de bytecode optimizado."

### Pregunta 22: "¿Qué propiedades matemáticas tiene la función sigmoide y por qué es indispensable en redes neuronales?"
* **Respuesta del estudiante:**  
  "La función sigmoide logística está definida como:
  $$\sigma(x) = \frac{1}{1 + e^{-x}}$$
  Sus propiedades matemáticas fundamentales son:
  1. Su dominio son todos los reales $(-\infty, +\infty)$ y su rango es el intervalo continuo $(0.0, 1.0)$.
  2. Su punto de simetría e inflexión ocurre en $\sigma(0) = 0.5$.
  3. Su derivada tiene una elegante forma cerrada: $\sigma'(x) = \sigma(x) \cdot (1 - \sigma(x))$, cuya pendiente máxima es exactamente 0.25 en $x = 0$.
  En redes neuronales es indispensable porque introduce **no linealidad**. Sin funciones de activación no lineales en las capas intermedias, una red neuronal de múltiples capas equivaldría matemáticamente a una simple combinación lineal de matrices ($W_2 \cdot W_1 \cdot x = W_{comb} \cdot x$), imposibilitando resolver problemas complejos."

### Pregunta 23: "¿Por qué un perceptrón simple no puede resolver XOR y qué algoritmo usamos en el Perceptrón Multicapa (MLP)?"
* **Respuesta del estudiante:**  
  "Un perceptrón simple de una sola capa solo puede trazar un hiperplano de separación lineal (una línea recta en 2D). En 1969, Minsky y Papert demostraron matemáticamente que la función lógica XOR es **no linealmente separable**: los puntos de clase 1 [(0,1) y (1,0)] y los de clase 0 [(0,0) y (1,1)] se cruzan diagonalmente, por lo que ninguna línea recta puede separarlos sin error.
  Para resolverlo desarrollamos el **Perceptrón Multicapa (`PerceptronMulticapaGalactico`)** con arquitectura 2-4-1:
  - **Algoritmo de Optimización:** Utilizamos **Retropropagación (Backpropagation) basado en Descenso de Gradiente (Gradient Descent)**.
  - **Función de Pérdida:** Error Cuadrático Medio ($L = \frac{1}{2} (y - \hat{y})^2$).
  - **Mecánica:** Mediante la regla de la cadena, el error cometido en la salida se propaga hacia atrás, calculando las derivadas parciales $\frac{\partial L}{\partial W}$ para cada peso y umbral de sesgo, y actualizando los pesos mediante $W \leftarrow W - \eta \frac{\partial L}{\partial W}$ con tasa $\eta = 1.5$.
  - Las 4 neuronas ocultas sigmoideas deforman el espacio de entrada a un espacio latente donde las clases se vuelven linealmente separables, logrando **100% de exactitud y convergencia perfecta**."

### Pregunta 24: "¿Cómo implementaron el análisis exploratorio de datos sobre el archivo `.xlsx` de 10,280 filas sin librerías externas?"
* **Respuesta del estudiante:**  
  "El formato moderno `.xlsx` es en realidad un archivo empaquetado ZIP que contiene documentos XML conformes al estándar Office OpenXML. Construimos el motor de lectura nativo en `src/runtime/io_engine.py` utilizando únicamente la biblioteca estándar de Python (`zipfile` y `xml.etree.ElementTree`):
  1. Descomprimimos el paquete en memoria y analizamos el archivo `xl/sharedStrings.xml` para construir la tabla indexada de cadenas de texto.
  2. Parseamos la primera hoja `xl/worksheets/sheet1.xml`, decodificando las referencias alfanuméricas de cada celda y asociando los valores tipados (enteros, flotantes o cadenas).
  3. En `04_analisis_exploratorio_xlsx.holo`, cargamos las 10,280 observaciones en menos de un segundo, sanamos valores vacíos y agrupamos por nivel educativo y género, calculando promedio, mediana, mínimo, máximo y desviación estándar con `HolocronMath`.
  4. Finalmente, proyectamos 3 gráficos PNG a 300 DPI y exportamos los resúmenes en formatos `.csv` y `.xls` nativos."

### Pregunta 25: "¿Cómo opera el filtro funcional de números primos del 1 al 100 en HolocronDSL?"
* **Respuesta del estudiante:**  
  "En el programa `05_filtro_primos_1_100.holo` implementamos:
  1. **Algoritmo de Primalidad:** Una misión `es_primo(numero)` con complejidad $O(\sqrt{n})$, descartando pares mayores a 2 y evaluando únicamente factores impares hasta $\sqrt{n}$.
  2. **Paradigma Funcional:** Incorporamos en el Visitor la función de orden superior `filtrar_lista(coleccion, "es_primo")`, la cual toma una lista de datos y el identificador de una misión como función predicado de primer orden, devolviendo un nuevo arreglo con los elementos que satisfacen la condición booleana.
  3. **Verificación:** Se compara contra un bucle `recorrer elemento en numeros` con condicional `evaluar_fuerza`, comprobando que ambos enfoques aíslan exactamente los **25 números primos** que existen entre el 1 y el 100."

