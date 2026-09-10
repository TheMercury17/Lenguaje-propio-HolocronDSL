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
- **Las transformaciones son el Hiperespacio:** En lugar de alterar la tabla original, los datos se canalizan a traves de una ruta hiperespacial mediante el conector `|>`, donde cada estacion realiza un procesamiento especifico (filtrar, ordenar, calcular).
- **El resultado final:** Se obtiene un nuevo conjunto de datos limpio, listo para ser archivado o proyectado como un **holograma** visual.

### 1.2 Estructura de un Programa en 3 Lineas
La sencillez y expresividad del paradigma de HolocronDSL se ilustra a continuacion:

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
Al examinar una linea de codigo en HolocronDSL, cada palabra o simbolo pertenece a una de las siguientes cinco categorias:

1. **Palabras Reservadas (Las ordenes fijas del lenguaje):**
   Son verbos y palabras clave predefinidas en el compilador. **No se pueden alterar ni modificar arbitrariamente**. Le indican al procesador que accion precisa ejecutar:
   *Ejemplos:* `abrir_holocron`, `revelar`, `purgar`, `donde`, `forjar`, `ordenar`, `resumir`, `holograma`, `mostrar`.

2. **Nombres de Variables (Identificadores creados por el programador):**
   Son los nombres libres que se eligen para almacenar tablas o resultados intermedios en memoria. Deben comenzar con una letra, sin espacios.
   *Ejemplos:* `flota_imperial`, `cazas_pesados`, `resumen_ciudades`, `datos_limpios`.

3. **Nombres de Columnas (Los campos de la tabla):**
   Son los encabezados de las columnas definidos dentro del archivo CSV. El compilador las busca dentro de la tabla para operar sobre ellas.
   *Ejemplos:* `modelo`, `faccion`, `escudos`, `victorias`, `precio`, `ciudad`.

4. **Operadores y Signos de Puntuacion:**
   Simbolos que conectan o transforman los datos:
   * `=` : Asignar o guardar en una variable.
   * `|>` : Conector de pipeline (pasar el resultado a la siguiente operacion).
   * `[ ... ]` : Corchetes para agrupar listas de columnas.
   * `( ... )` : Parentesis para envolver argumentos de funciones y expresiones.
   * `+`, `-`, `*`, `/` : Operaciones matematicas.
   * `>`, `<`, `==`, `!=` : Comparaciones logicas.

5. **Literales (Valores fijos constantes):**
   Los datos concretos especificados directamente en el codigo:
   * Numeros: `50`, `100`, `3.14`.
   * Cadenas entre comillas: `"datos/flota.csv"`, `"Imperio"`.
   * Booleanos: `cierto_es`, `falso_es`.

---

### 2.5 Desglose con Lupa: Analizando una Linea Real

A continuacion se examina una linea de codigo representativa:
```holocron
cazas_elite = flota |> purgar donde escudos > 50 y victorias >= 5
```

Al desarmar la instruccion elemento por elemento:
* **`cazas_elite`** : **Nombre de Variable Nueva** (etiqueta definida para almacenar el resultado).
* **`=`** : **Operador de Asignacion** (guarda el resultado de la derecha en la variable de la izquierda).
* **`flota`** : **Nombre de Variable Existente** (la tabla original cargada previamente).
* **`|>`** : **Operador de Pipeline** (toma `flota` y la envia a la siguiente etapa).
* **`purgar`** : **Palabra Reservada** (la orden de filtrar filas).
* **`donde`** : **Palabra Reservada** (conector para introducir la condicion logica).
* **`escudos`** : **Nombre de Columna** (atributo presente dentro de la tabla `flota`).
* **`>`** : **Operador de Comparacion** (mayor que).
* **`50`** : **Literal Numerico** (el umbral de comparacion).
* **`y`** : **Operador Logico** (exige que ambas condiciones se satisfagan conjuntamente).
* **`victorias`** : **Nombre de Columna** (segundo atributo de la tabla evaluado).
* **`>=`** : **Operador de Comparacion** (mayor o igual que).
* **`5`** : **Literal Numerico**.

---

### 2.6 Diccionario Completo de Palabras Reservadas

A continuacion se presenta el significado formal y el rol de las palabras reservadas del lenguaje:

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

## Capitulo 8: Guia de Despliegue y Ejecucion Multiplataforma

### 8.1 ¿En que carpeta se debe estar posicionado?
Para que los comandos se ejecuten correctamente, la terminal del sistema operativo debe estar ubicada en el directorio raiz del proyecto:

* **En entornos Linux (Kali Linux, Debian, Ubuntu):**
  1. En caso de clonar el repositorio:
     ```bash
     git clone https://github.com/TheMercury17/Lenguaje-propio-HolocronDSL.git
     cd Lenguaje-propio-HolocronDSL
     ```
  2. En caso de contar con el directorio ya presente en el equipo:
     ```bash
     cd ruta/hacia/Lenguaje-propio-HolocronDSL
     ```
  3. Al comprobar con `ls -la`, deben observarse archivos como `Makefile`, `run_tests.py`, `requirements.txt` y los directorios `src`, `docs`, `grammar` y `examples`.

* **En entornos Windows:**
  1. Abrir PowerShell o CMD y situarse en la carpeta donde reside el proyecto:
     ```powershell
     cd ruta\hacia\Lenguaje-propio-HolocronDSL
     ```
  2. Al ejecutar `dir`, se verificara la presencia de los mismos archivos y carpetas del repositorio.

---

### 8.2 Preparacion del entorno e instalacion de librerias

#### En distribuciones Linux (especialmente Kali Linux en VirtualBox):
En sistemas basados en Debian modernos, la politica PEP 668 protege los paquetes del sistema, por lo que se debe emplear un entorno virtual aislado:

1. **Instalar dependencias del sistema operativo (en caso de no poseerlas):**
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv make default-jre
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar los paquetes oficiales requeridos:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verificar o compilar los analizadores de ANTLR4:**
   ```bash
   python3 run_tests.py --grammar
   ```

#### En Windows:
1. **Crear y activar entorno virtual:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Instalar librerias:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Verificar analizadores de ANTLR4:**
   ```powershell
   python run_tests.py --grammar
   ```

---

### 8.3 ¿Como se ejecutan y analizan los programas en HolocronDSL (.holo)?
Los archivos `.holo` contienen codigo fuente de HolocronDSL. Para analizarlos sintacticamente y examinar el arbol de derivacion, se utiliza el lanzador `holocron.py` o el controlador `src/cli.py`:

1. **Verificacion sintactica rapida (modo `--check`):**
   - En Linux / Kali Linux:
     ```bash
     python3 holocron.py examples/01_telemetria_cazas.holo --check
     ```
   - En Windows:
     ```powershell
     python holocron.py examples/01_telemetria_cazas.holo --check
     ```
   *Respuesta esperada:* `Sintaxis verificada con exito: la Fuerza fluye en perfecta armonia.`

2. **Inspeccion visual del Arbol Sintactico Concreto (CST jerarquico):**
   - En Linux / Kali Linux:
     ```bash
     python3 src/cli.py examples/01_telemetria_cazas.holo --tree
     ```
   - En Windows:
     ```powershell
     python src/cli.py examples/01_telemetria_cazas.holo --tree
     ```

3. **Prueba en linea de una sentencia directa:**
   ```bash
   python3 src/cli.py --codigo "flota = abrir_holocron \"flota.csv\" |> purgar donde escudos > 50" --tree
   ```

---

### 8.4 ¿Como se ejecutan las pruebas unitarias?
El script `run_tests.py` permite ejecutar las pruebas tanto de forma global como de manera modular:

* **Suite completa de pruebas unitarias:**
  ```bash
  python3 run_tests.py
  ```
  *(O en Windows: `python run_tests.py`)*

* **Pruebas modulares por subsistema:**
  - Analizador lexico (tokens, palabras reservadas):
    ```bash
    python3 run_tests.py --lexer
    ```
  - Analizador sintactico (programas validos):
    ```bash
    python3 run_tests.py --parser
    ```
  - Manejo y reporte de errores sintacticos:
    ```bash
    python3 run_tests.py --invalid
    ```
  - Verificacion de todos los archivos de ejemplo en `examples/`:
    ```bash
    python3 run_tests.py --examples
    ```

* **Automatizacion mediante Makefile (en entornos Unix y Kali Linux):**
  ```bash
  make test           # Ejecuta todas las pruebas
  make test-lexer     # Solo pruebas lexicas
  make test-parser    # Solo pruebas sintacticas validas
  make test-invalid   # Solo pruebas de deteccion de errores
  make check-examples # Valida los 5 ejemplos del lenguaje
  make clean          # Limpia directorios __pycache__
  ```
