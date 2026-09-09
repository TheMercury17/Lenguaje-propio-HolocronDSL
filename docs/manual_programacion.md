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

## Capitulo 8: Ejecucion en Consola

```bash
-- Validar si el archivo esta bien escrito:
python src/cli.py mi_programa.holo --check

-- Ver la estructura del arbol sintactico:
python src/cli.py mi_programa.holo --tree

-- Ejecutar la suite completa de pruebas:
python -m unittest discover -s tests
```
