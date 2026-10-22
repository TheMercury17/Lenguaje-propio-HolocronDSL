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
* `make test`: Ejecuta la suite completa de 61 pruebas unitarias e integrales.
* `make test-lexer`: Ejecuta únicamente las pruebas del analizador léxico.
* `make test-parser`: Ejecuta las pruebas del analizador sintáctico.
* `make test-semantic`: Ejecuta las pruebas semánticas y del evaluador Visitor.
* `make run-examples`: Ejecuta todos los programas `.holo` de demostración y genera las salidas.
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
* Si el profesor pide comprobar la suite de pruebas automatizadas, ejecutar `make test` o `python3 run_tests.py --all`. Al ver las 61 pruebas pasar con éxito en menos de 1 segundo, se demuestra la solidez y estabilidad del compilador.

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

## 8. Hoja de Comandos Rápidos de Terminal para la Sustentación (Linux / Kali)

### 8.1 Visualización de la Gramática Formal (.g4) en Consola
Para mostrar la gramática ANTLR4 directamente en la terminal:
```bash
# Opcion A: Ver todo el archivo continuo
cat src/grammar/HolocronDSL.g4

# Opcion B: Verlo paginado (navegar con flechas arriba/abajo, buscar con '/' y salir con 'q')
less src/grammar/HolocronDSL.g4

# Opcion C: Ver las primeras 40 lineas (reglas de tokens principales)
head -n 40 src/grammar/HolocronDSL.g4

# Opcion D: Ver con numeros de linea en pantalla
nl -ba src/grammar/HolocronDSL.g4 | less
```

### 8.2 Edición de Archivos en la Terminal de Linux
Para modificar ejemplos, gramática o código fuente:
```bash
# Editar un ejemplo especifico (.holo)
nano examples/01_telemetria_cazas.holo

# Editar la gramatica ANTLR4 (.g4)
nano src/grammar/HolocronDSL.g4

# Atajos esenciales dentro del editor nano:
# Ctrl + O   -> Guardar cambios (presionar Enter para confirmar el nombre)
# Ctrl + X   -> Salir del editor
# Ctrl + W   -> Buscar una palabra o regla
# Alt  + U   -> Deshacer ultimo cambio
```

### 8.3 Recompilación de la Gramática ANTLR4
Si durante la sustentación el docente solicita añadir o modificar una regla en `HolocronDSL.g4`:
```bash
# 1. Recompilar la gramatica a codigo Python (actualiza src/generated/)
make grammar

# Equivalente manual en caso de no usar make:
python3 -m antlr4 -Dlanguage=Python3 -visitor -no-listener -o src/generated src/grammar/HolocronDSL.g4
```

### 8.4 Ejecución de Ejemplos Puntuales con el CLI (`holocron.py`)
```bash
# Ejecutar normalmente un ejemplo puntual (interpreta, calcula y guarda archivos)
python3 holocron.py examples/01_telemetria_cazas.holo

# Ejecutar el ejemplo 2 (agrupamiento y estadisticas de censo)
python3 holocron.py examples/02_censo_galactico.holo

# Ejecutar el ejemplo 3 (proyeccion de graficos PNG)
python3 holocron.py examples/03_proyeccion_holografica.holo

# Ejecutar en modo detallado (muestra trazabilidad de operaciones)
python3 holocron.py examples/01_telemetria_cazas.holo --verbose

# Validar UNICAMENTE la sintaxis sin ejecutar ni modificar disco
python3 holocron.py examples/01_telemetria_cazas.holo --check

# Visualizar el Arbol de Analisis Sintactico (AST) en formato indentado
python3 holocron.py examples/01_telemetria_cazas.holo --tree

# Visualizar el AST en notacion LISP (S-Expressions)
python3 holocron.py examples/01_telemetria_cazas.holo --lisp
```

### 8.5 Inspección y Verificación de los Archivos de Salida Generados
Cuando el programa guarde resultados en la carpeta `salidas/`:
```bash
# 1. Listar los archivos generados con fechas y tamanos
ls -la salidas/

# 2. Ver el contenido de un archivo CSV generado de forma alineada en columnas
column -t -s, salidas/flota_operativa.csv | head -n 15

# 3. Ver las primeras lineas de un archivo Excel (.xls) para comprobar el encabezado XML
head -n 20 salidas/flota_exportada.xls

# 4. Abrir el archivo Excel (.xls) directamente en LibreOffice Calc (interfaz grafica)
libreoffice salidas/flota_exportada.xls &

# 5. Abrir una imagen PNG generada en el visor predeterminado de Kali Linux
xdg-open salidas/victorias_por_faccion.png &
# O con el visor liviano Ristretto habitual en Kali:
ristretto salidas/victorias_por_faccion.png &
```

### 8.6 Ejecución y Revisión de Pruebas Automatizadas
Para demostrar ante el docente que la suite de pruebas valida el sistema al 100%:
```bash
# Ejecutar toda la suite (61 pruebas unitarias e integrales)
make test

# Ejecutar mediante el runner propio del proyecto
python3 run_tests.py --all

# Ejecutar unicamente las pruebas del analizador lexico
make test-lexer

# Ejecutar unicamente las pruebas sintacticas validas
make test-parser

# Ejecutar unicamente las pruebas semanticas y del interprete Visitor
make test-semantic

# Ejecutar un archivo de prueba puntual directamente con unittest
python3 -m unittest tests/test_semantic_execution.py -v
python3 -m unittest tests/test_io_engine.py -v
python3 -m unittest tests/test_math_engine.py -v
```

### 8.7 Gestión del Entorno Virtual en Linux
En caso de clonar o ejecutar en una máquina virtual limpia de Kali:
```bash
# Activar el entorno virtual si ya esta creado
source .venv/bin/activate

# Instalar dependencias si se clono recientemente
make install

# Limpiar archivos temporales y caches de Python (__pycache__)
make clean
```
