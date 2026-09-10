# Manual y Guia de Aprendizaje: Programacion en HolocronDSL

**Universidad Sergio Arboleda**  
**Programa de Ciencias de la Computacion e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programacion y Transduccion (2026-2)  
**Equipo de Desarrollo (Grupo 5):**  
- Andres Sebastian Coral Vallejo  
- Carol Arenas Cardona  

---

## Prologo: Bienvenido a la Fuerza de los Datos

Este documento esta diseñado para cualquier persona interesada en el analisis de datos, **incluso si jamas en su vida ha escrito una sola linea de codigo**.

Aprender a programar no tiene por que ser intimidante ni requerir memorizar simbolos complejos. **HolocronDSL** es un **Lenguaje de Dominio Especifico (DSL)** creado para hacer una cosa y hacerla bien: **cargar, limpiar, transformar, analizar y visualizar datos de forma limpia, intuitiva y directa**, utilizando la tematica de **Star Wars**.

---

## Capitulo 1: La Filosofia del Lenguaje

### 1.1 La Metafora Galactica
- **Los archivos de datos son Holocrones:** Un holocron es una capsula de informacion (como una hoja de calculo o un archivo CSV) con filas y columnas.
- **Las transformaciones son el Hiperespacio:** En lugar de alterar la tabla original, canalizas los datos a traves de una ruta hiperespacial con el conector `|>` donde cada estacion hace un trabajo especifico (filtrar, ordenar, calcular).
- **El resultado final:** Obtienes un nuevo conjunto de datos limpio, listo para ser archivado o proyectado como un **holograma** visual.

### 1.2 Tu Primer Programa en 3 Lineas
Asi de simple e intuitivo es escribir en HolocronDSL:

```holocron
-- 1. Cargamos el archivo de datos
flota = abrir_holocron "examples/datos/telemetria_flota.csv"

-- 2. Filtramos solo las naves con escudos potentes
cazas_pesados = flota |> purgar donde escudos >= 100

-- 3. Guardamos el resultado en un archivo nuevo
archivar_holocron cazas_pesados en "salidas/cazas_pesados.csv"
```

No hay simbolos extraños ni flechas invertidas: se usa el signo igual `=` que todo el mundo conoce y el conector de flujo `|>`.

---

## Capitulo 2: Conceptos Basicos

### 2.1 Variables y el Signo Igual (`=`)
Una **variable** es simplemente un nombre o etiqueta que le das a un dato o tabla para guardarla:

```holocron
mi_flota = abrir_holocron "datos.csv"
umbral_defensa = 50
planeta_base = "Coruscant"
```

El nombre va a la izquierda y el contenido a la derecha del signo `=`.

### 2.2 Tipos de Informacion
1. **Numeros:** Enteros (`10`, `500`) o decimales (`3.14`, `0.5`). Sin comillas.
2. **Textos:** Siempre entre comillas dobles: `"Imperio"`, `"X-Wing"`, `"datos.csv"`.
3. **Valores logicos:** `cierto_es` o `verdadero` para Si; `falso_es` o `falso` para No.

### 2.3 Comentarios: Dejando notas en el codigo
- **De una linea:** Comienza con dos guiones `--`.
  ```holocron
  -- Esta es una nota explicativa
  ```
- **De bloque (varias lineas):** Inicia con `/-` y termina con `-/`.
  ```holocron
  /-
    Informe tactico sobre los cazas estelares.
  -/
  ```

### 2.4 Anatomia del Codigo: ¿Que papel cumple cada palabra?
Cuando ves una linea de codigo en HolocronDSL, cada palabra pertenece a una de estas cinco categorias:

1. **Palabras Reservadas (Las ordenes fijas del lenguaje):**
   Son verbos y palabras clave que ya vienen programadas en el lenguaje. **No las puedes cambiar ni inventar**. Le dicen a la computadora que accion ejecutar:
   *Ejemplos:* `abrir_holocron`, `revelar`, `purgar`, `donde`, `forjar`, `ordenar`, `resumir`, `holograma`, `mostrar`.

2. **Nombres de Variables (Las etiquetas que tu inventas):**
   Son los nombres libres que tu eliges para bautizar tus tablas o resultados intermedios. Deben comenzar con una letra, sin espacios.
   *Ejemplos:* `flota_imperial`, `cazas_pesados`, `resumen_ciudades`, `datos_limpios`.

3. **Nombres de Columnas (Los campos de tu tabla):**
   Son los titulos de las columnas que vienen dentro de tu archivo CSV. El lenguaje las busca dentro de la tabla para operar sobre ellas.
   *Ejemplos:* `modelo`, `faccion`, `escudos`, `victorias`, `precio`, `ciudad`.

4. **Operadores y Signos de Puntuacion:**
   Simbolos que conectan o transforman los datos:
   * `=` : Asignar o guardar en una variable.
   * `|>` : Conector de pipeline (pasar el resultado a la siguiente operacion).
   * `[ ... ]` : Corchetes para agrupar listas de columnas.
   * `( ... )` : Paréntesis para envolver argumentos de funciones.
   * `+`, `-`, `*`, `/` : Operaciones matematicas.
   * `>`, `<`, `==`, `!=` : Comparaciones logicas.

5. **Literales (Los valores fijos):**
   Los datos concretos que tu escribes directamente:
   * Numeros: `50`, `100`, `3.14`.
   * Cadenas entre comillas: `"datos/flota.csv"`, `"Imperio"`.
   * Booleanos: `cierto_es`, `falso_es`.

---

### 2.5 Desglose con Lupa: Analizando una Linea Real

Observa esta linea de codigo:
```holocron
cazas_elite = flota |> purgar donde escudos > 50 y victorias >= 5
```

Si la desarmamos pieza por pieza:
* **`cazas_elite`** : **Nombre de Variable Nueva** (etiqueta que tu inventaste para guardar el resultado).
* **`=`** : **Operador de Asignacion** (guarda lo que esta a la derecha en la variable de la izquierda).
* **`flota`** : **Nombre de Variable Existente** (la tabla original que cargaste antes).
* **`|>`** : **Operador de Pipeline** (toma `flota` y la envia a la siguiente estacion).
* **`purgar`** : **Palabra Reservada** (la orden de filtrar filas).
* **`donde`** : **Palabra Reservada** (conector para introducir la condicion).
* **`escudos`** : **Nombre de Columna** (atributo que esta adentro de la tabla `flota`).
* **`>`** : **Operador de Comparacion** (mayor que).
* **`50`** : **Literal Numerico** (el umbral de comparacion).
* **`y`** : **Operador Logico** (exige que ambas condiciones se cumplan).
* **`victorias`** : **Nombre de Columna** (otra columna de la tabla).
* **`>=`** : **Operador de Comparacion** (mayor o igual que).
* **`5`** : **Literal Numerico**.

---

### 2.6 Diccionario Completo de Palabras Reservadas

A continuacion tienes el significado exacto de todas las palabras reservadas fijas del lenguaje:

| Palabra Reservada | ¿Que significa en español simple? | ¿Para que se usa? |
| :--- | :--- | :--- |
| `abrir_holocron` | Cargar / Leer archivo | Abre un archivo CSV del disco para empezar a usarlo. |
| `delimitado_por` | Con separador | Indica si las columnas estan separadas por comas, puntos y comas o tabuladores. |
| `archivar_holocron` | Guardar / Exportar | Escribe una tabla procesada en un nuevo archivo CSV en el disco. |
| `en` | Hacia la ruta | Conector que antecede la ruta del archivo donde se guardara. |
| `revelar` | Seleccionar columnas | Elige que columnas quieres conservar, descartando las demas. |
| `purgar` | Filtrar registros | Elimina las filas que no cumplan con la condicion indicada. |
| `donde` | Bajo la condicion | Conector opcional para dar fluidez gramatical despues de `purgar`. |
| `forjar` | Calcular nueva columna | Crea una columna nueva calculando formulas matematicas con las existentes. |
| `ordenar` | Organizar filas | Ordena las filas de la tabla segun el valor de una columna. |
| `por` | Segun el campo | Conector que indica cual columna gobernara el orden. |
| `ascendente` | De menor a mayor | Criterio de orden de menor a mayor (A-Z o 0-9). |
| `descendente` | De mayor a menor | Criterio de orden de mayor a menor (Z-A o 9-0). |
| `eliminar_clones` | Quitar duplicados | Busca filas exactamente identicas repetidas y deja solo una. |
| `sanar_vacios` | Arreglar nulos | Repara celdas vacias o incompletas de la tabla. |
| `con` | Rellenar usando | Conector que indica con que valor se rellenaran los vacios (ej. `con 0`). |
| `descartar` | Borrar la fila | Instruccion para suprimir cualquier fila que tenga datos faltantes. |
| `agrupar` | Clasificar en grupos | Junta las filas que comparten el mismo valor en una categoria. |
| `resumir` | Calcular estadisticas | Aplica funciones de sintesis (promedios, sumas) sobre cada grupo. |
| `recuento()` | Contar filas | Cuenta cuantas filas pertenecen a cada categoria. |
| `acumular(col)` | Sumar valores | Suma todos los numeros de esa columna. |
| `equilibrio(col)` | Sacar el promedio | Calcula la media aritmetica (el equilibrio de la Fuerza en los datos). |
| `mediana(col)` | Dato del medio | Encuentra el valor central exacto de la columna. |
| `cenit(col)` | Valor maximo | Devuelve el valor mas alto registrado. |
| `nadir(col)` | Valor minimo | Devuelve el valor mas bajo registrado. |
| `desviacion(col)` | Dispersion | Mide que tan dispersos o variados estan los numeros respecto al promedio. |
| `holograma` | Crear grafico | Inicia la construccion de una representacion visual. |
| `barras`, `lineas`, `dispersion`, `histograma`, `caja` | Tipos de graficos | El formato visual en que se proyectaran los datos. |
| `eje_x` | Variable horizontal | Asigna que columna va en la base horizontal del grafico. |
| `eje_y` | Variable vertical | Asigna que columna va en la altura vertical del grafico. |
| `titulo` | Encabezado | Define el texto superior que llevara el grafico. |
| `guardar` | Guardar imagen | Define la ruta de la imagen PNG que se creara en el disco. |
| `mision` | Definir funcion | Inicia una rutina de codigo personalizada y reutilizable. |
| `retornar` | Devolver resultado | Entrega la tabla final producida por la mision. |
| `fin_mision` | Fin de funcion | Cierra el bloque de la mision. |
| `evaluar_fuerza` | Condicional / Si | Evalua una condicion de si es verdad o mentira. |
| `senda_luminosa` | Si es verdadero | Bloque que se ejecuta si la condicion se cumplio. |
| `senda_oscura` | Si es falso | Bloque alternativo que se ejecuta si la condicion no se cumplio. |
| `fin_evaluar` | Fin de condicional | Cierra el bloque condicional. |
| `mostrar` / `transmitir` | Imprimir en pantalla | Muestra un texto, numero o mensaje en la terminal de la computadora. |
| `y`, `o`, `no` | Conectores logicos | Operadores para unir o negar condiciones booleanas. |
| `cierto_es`, `falso_es` | Verdadero o Falso | Los dos estados posibles de la verdad logica. |

---

## Capitulo 3: El Pipeline de Hiperespacio (`|>`)

Para transformar datos paso a paso, usamos el conector `|>`. Imagina una linea de ensamblaje: cada paso recibe la tabla anterior y produce una nueva:

```holocron
resultado = datos_iniciales
    |> operacion_uno
    |> operacion_dos
    |> operacion_tres
```

---

## Capitulo 4: Catalogo de Operaciones de Transformacion

### 4.1 Seleccionar Columnas (`revelar`)
Quedate solo con las columnas que necesitas:

```holocron
datos_reducidos = flota
    |> revelar [ identificador, modelo, escudos ]
```

### 4.2 Filtrar Filas (`purgar donde`)
Conserva unicamente las filas que cumplan una condicion:

```holocron
cazas_fuertes = flota
    |> purgar donde escudos > 50 y victorias >= 5
```

Operadores disponibles: `==` (igual), `!=` (diferente), `>`, `<`, `>=`, `<=`.  
Conectores simples: `y` (ambas deben cumplirse), `o` (al menos una), `no` (negacion).

### 4.3 Crear Nuevas Columnas (`forjar`)
Calcula un nuevo atributo matematico con el signo igual `=`:

```holocron
flota_calculada = flota
    |> forjar indice = victorias * 10 + escudos / 2
```

Operaciones matematicas: `+`, `-`, `*`, `/`, `%` (modulo), `^` (potencia).

### 4.4 Ordenar Registros (`ordenar por`)
Organiza las filas segun una columna:

```holocron
flota_ordenada = flota
    |> ordenar por victorias descendente
```

### 4.5 Eliminar Duplicados (`eliminar_clones`)
Suprime filas repetidas en un solo paso:

```holocron
sin_repetidos = flota
    |> eliminar_clones
```

### 4.6 Manejo de Vacios (`sanar_vacios`)
- Rellenar nulos con un valor: `sanar_vacios con 0`
- Descartar filas con nulos: `sanar_vacios descartar`

---

## Capitulo 5: Resumen Estadistico y Agrupaciones

Para resumir informacion por grupos (por ejemplo, por faccion):

```holocron
resumen = flota
    |> agrupar por [ faccion ]
    |> resumir
        total_naves = recuento(),
        promedio_escudos = equilibrio(escudos),
        maximas_victorias = cenit(victorias)
```

### Las 7 Funciones Estadisticas:
| Funcion | Significado Real | Explicacion |
| :--- | :--- | :--- |
| `recuento()` o `conteo()` | Conteo | Cantidad de registros en el grupo. |
| `acumular(col)` o `suma(col)` | Suma | Suma total de los valores. |
| `equilibrio(col)` o `promedio(col)` | Promedio / Media | Media exacta (el equilibrio en los datos). |
| `mediana(col)` | Mediana | Valor que divide los datos en la mitad. |
| `cenit(col)` o `maximo(col)` | Maximo | El valor mas alto. |
| `nadir(col)` o `minimo(col)` | Minimo | El valor mas bajo. |
| `desviacion(col)` | Desviacion Estandar | Dispersion de los datos. |

---

## Capitulo 6: Proyecciones Holograficas (Graficos)

Genera graficos de forma declarativa sin simbolos raros:

```holocron
holograma barras resumen
    eje_x "faccion"
    eje_y "total_naves"
    titulo "Cantidad de naves por faccion"
    guardar "salidas/naves_faccion.png"
```

Tipos de graficas: `barras`, `lineas`, `dispersion`, `histograma`, `caja`.

---

## Capitulo 7: Funciones y Control

### 7.1 Misiones (Funciones)
Encapsula rutinas repetitivas:

```holocron
mision filtrar_flota (datos, minimo)
    filtrados = datos
        |> purgar donde escudos >= minimo
    retornar filtrados
fin_mision

escuadron = filtrar_flota(flota, 100)
```

### 7.2 Decisiones con la Fuerza (`evaluar_fuerza`)
```holocron
evaluar_fuerza alerta > 3
senda_luminosa
    mostrar "Activar escudos maximos."
senda_oscura
    mostrar "Sistemas estables."
fin_evaluar
```

---

## Capitulo 8: Guia Paso a Paso para Ejecutar en la Terminal

### 8.1 ¿En que carpeta debo estar ubicado?
Para que los comandos funcionen, tu consola o terminal debe estar parada dentro de la carpeta raiz del proyecto:
`C:\Users\Sebas\OneDrive\Documents\Sergio Arboleda\Trabajos\Lenguajes de prog\Lenguaje propio`

**Como abrir la consola directamente en esa carpeta:**
1. Abre el Explorador de Archivos de Windows y navega hasta esa carpeta.
2. Haz clic en la barra de direcciones superior (donde aparece la ruta).
3. Escribe `powershell` y presiona la tecla `Enter`.
4. Listo: se abrira una ventana de consola azul posicionada exactamente en el proyecto.

Si ya tienes una consola abierta y quieres navegar hasta la carpeta, escribe:
```powershell
cd "C:\Users\Sebas\OneDrive\Documents\Sergio Arboleda\Trabajos\Lenguajes de prog\Lenguaje propio"
```

### 8.2 ¿Que comandos debo ejecutar primero (Preparacion)?
Antes de probar cualquier archivo, asegurate de tener instaladas las librerias necesarias. Solo se hace una vez:
```powershell
pip install -r requirements.txt
```

Y para asegurarte de que los analizadores de ANTLR4 esten generados:
```powershell
python run_tests.py --grammar
```

### 8.3 ¿Como se ejecutan los archivos de ejemplo (.holo)?
Los archivos `.holo` contienen programas en HolocronDSL. Para ejecutarlos y que la computadora los analice, usamos el script `src/cli.py`:

1. **Para verificar si un archivo esta bien escrito (sin errores sintacticos):**
   ```powershell
   python src/cli.py examples/01_telemetria_cazas.holo --check
   ```
   *Respuesta esperada:* `Sintaxis verificada con exito: la Fuerza fluye en perfecta armonia.`

2. **Para ver el arbol sintactico (CST jerarquico visual):**
   ```powershell
   python src/cli.py examples/01_telemetria_cazas.holo --tree
   ```

3. **Para probar una linea de codigo directamente sin crear un archivo:**
   ```powershell
   python src/cli.py --codigo "flota = abrir_holocron \"flota.csv\" |> purgar donde escudos > 50" --tree
   ```

### 8.4 ¿Como se ejecutan las pruebas unitarias?
Puedes correr todas las pruebas juntas o por separado usando el script `run_tests.py`:

* **Todas las pruebas:**
  ```powershell
  python run_tests.py
  ```
* **Solo pruebas del analizador lexico (tokens y palabras reservadas):**
  ```powershell
  python run_tests.py --lexer
  ```
* **Solo pruebas de sintaxis correcta (pipelines, graficas, misiones):**
  ```powershell
  python run_tests.py --parser
  ```
* **Solo pruebas de deteccion de errores (para verificar que rechace codigo mal escrito):**
  ```powershell
  python run_tests.py --invalid
  ```
* **Verificar todos los ejemplos de la carpeta examples/:**
  ```powershell
  python run_tests.py --examples
  ```
