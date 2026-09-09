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

Aprender a programar no tiene por que ser intimidante ni requerir memorizar comandos extraños. En la mayoria de los lenguajes tradicionales (como C++ o Java), realizar una tarea simple sobre una tabla de datos exige aprender decenas de reglas tecnicas complejas. 

**HolocronDSL** nacio para cambiar eso. Es un **Lenguaje de Dominio Especifico (DSL)**, lo que significa que esta creado exclusivamente para resolver un problema concreto: **cargar, limpiar, transformar, analizar y visualizar datos de forma limpia, elegante y reproducible**, utilizando una tematica inspirada en el universo galactico de **Star Wars**.

En este manual aprenderas la logica del lenguaje desde cero, con explicaciones paso a paso y analogias del mundo real.

---

## Capitulo 1: La Filosofia del Lenguaje

### 1.1 La Metafora Galactica
Para entender como funciona HolocronDSL, imagina que eres el oficial cientifico de una nave estelar:
- **Los archivos de datos son Holocrones:** Un holocron es una capsula de informacion (como una hoja de calculo o un archivo CSV) que contiene registros organizados en filas y columnas.
- **Las transformaciones son el Hiperespacio:** En lugar de modificar los datos originales y arriesgarte a perder informacion, canalizas los datos a traves de una ruta hiperespacial (`==>`) donde cada estacion hace un trabajo especifico (filtrar, ordenar, calcular).
- **El resultado final:** Al final del viaje, obtienes un nuevo conjunto de datos limpio, listo para ser archivado o proyectado como un **holograma** visual.

### 1.2 Tu Primer Programa en 3 Lineas
Asi se ve un programa real en HolocronDSL:

```holocron
-- 1. Cargamos el archivo de datos
flota <- abrir_holocron "examples/datos/telemetria_flota.csv"

-- 2. Filtramos solo las naves con escudos potentes
cazas_pesados <- flota ==> purgar_donde escudos >= 100

-- 3. Guardamos el resultado en un archivo nuevo
archivar_holocron cazas_pesados en "salidas/cazas_pesados.csv"
```

Nota que el codigo casi se lee como una oracion en español. No hay simbolos extraños ni llaves confusas.

---

## Capitulo 2: Conceptos Basicos que Debes Conocer

Antes de escribir sentencias complejas, conozcamos los bloques basicos con los que se construye cualquier programa.

### 2.1 Variables y el Operador de Canalizacion (`<-`)
Una **variable** es simplemente una etiqueta o un nombre que le das a un conjunto de informacion para poder referirte a el mas tarde.

En HolocronDSL, para guardar algo dentro de una variable usamos la flecha de canalizacion `<-`:

```holocron
mi_flota <- abrir_holocron "datos.csv"
umbral_defensa <- 50
planeta_base <- "Coruscant"
```

*Regla de oro:* El nombre de la variable siempre va a la izquierda de la flecha `<-`, y el valor o proceso va a la derecha.

### 2.2 Tipos de Informacion
En HolocronDSL manejamos tres tipos fundamentales de datos:
1. **Numeros:** Pueden ser enteros (`10`, `450`) o decimales (`3.14`, `0.75`). Se escriben tal cual, sin comillas.
2. **Cadenas de texto:** Palabras, nombres o rutas de archivos. **Siempre** se escriben entre comillas dobles: `"Imperio"`, `"X-Wing"`, `"datos/telemetria.csv"`.
3. **Valores logicos (Booleanos):** Respuestas de Si o No. En honor a la forma de hablar del Maestro Yoda, se escriben como:
   - `cierto_es` (representa la verdad o verdadero).
   - `falso_es` (representa la falsedad o falso).

### 2.3 Comentarios: Dejando notas en el codigo
Los comentarios son notas que el computador ignora por completo. Sirven para explicarle a tus compañeros (o a ti mismo en el futuro) que hace cada parte de tu codigo:

- **Comentario de una linea:** Inicia con dos guiones `--`.
  ```holocron
  -- Esto es una explicacion de una sola linea
  ```
- **Comentario de bloque:** Para notas largas, inicia con `/-` y termina con `-/`.
  ```holocron
  /-
    Este informe analiza las bajas de la flota estelar
    durante la batalla de Endor.
  -/
  ```

---

## Capitulo 3: El Poder del Pipeline (`==>`)

El concepto mas importante de HolocronDSL es el **pipeline** o **canalizacion**, representado por el operador de salto hiperespacial `==>`.

Imagina una linea de ensamblaje en una fabrica:
1. Entra una pieza de metal.
2. La estacion 1 la corta.
3. La estacion 2 la pinta.
4. La estacion 3 la empaca.

En HolocronDSL, la tabla de datos pasa de estacion en estacion usando `==>`:

```holocron
resultado <- datos_iniciales
    ==> operacion_uno
    ==> operacion_dos
    ==> operacion_tres
```

Cada operacion toma la tabla resultante de la linea anterior, le aplica una transformacion, y se la entrega a la siguiente estacion. Tus datos originales nunca se dañan.

---

## Capitulo 4: Catalogo de Operaciones de Transformacion

Veamos una por una todas las operaciones que puedes usar dentro de un pipeline (`==>`).

### 4.1 Seleccionar Columnas (`revelar_sectores`)
Cuando un archivo tiene demasiadas columnas y solo necesitas unas pocas, usa `revelar_sectores` seguido de los nombres de columna entre corchetes `[ ... ]`:

```holocron
datos_reducidos <- flota
    ==> revelar_sectores [ identificador, modelo, escudos ]
```

### 4.2 Filtrar Filas (`purgar_donde`)
Sirve para quedarte unicamente con los registros que cumplen una condicion. Se utiliza la palabra `purgar_donde`:

```holocron
naves_con_escudo <- flota
    ==> purgar_donde escudos > 0
```

#### Operadores de comparacion disponibles:
- `==` : Exactamente igual (ejemplo: `faccion == "Imperio"`).
- `!=` : Diferente de (ejemplo: `estado != "destruido"`).
- `>`  : Mayor que (ejemplo: `victorias > 10`).
- `<`  : Menor que (ejemplo: `tripulantes < 5`).
- `>=` : Mayor o igual que (ejemplo: `escudos >= 100`).
- `<=` : Menor o igual que (ejemplo: `danio <= 20`).

#### Combinar condiciones con la Fuerza:
Puedes unir varias condiciones usando conectores logicos galacticos:
- `y_fuerza` : Ambas condiciones deben cumplirse obligatoriamente.
- `o_fuerza` : Basta con que se cumpla al menos una de las condiciones.
- `no_fuerza` : Invierte la condicion.

```holocron
veteranos_elite <- flota
    ==> purgar_donde victorias >= 10 y_fuerza hiperimpulsor == cierto_es
```

### 4.3 Crear Nuevas Columnas (`forjar_cristal`)
Cuando necesitas calcular un nuevo indicador matematico basado en las columnas existentes, usas `forjar_cristal`, el nombre de la nueva columna y el operador de ligadura `:=`:

```holocron
flota_con_metricas <- flota
    ==> forjar_cristal potencia_fuego := victorias * 15 + escudos / 2
```

#### Operaciones matematicas permitidas:
- `+` : Suma.
- `-` : Resta.
- `*` : Multiplicacion.
- `/` : Division.
- `%` : Modulo (residuo de la division).
- `^` : Potencia (ejemplo: `radio ^ 2`).

### 4.4 Ordenar Registros (`alinear_flota`)
Organiza las filas segun el valor de una columna, ya sea de mayor a menor o de menor a mayor:

```holocron
-- De mayor a menor
campeones <- flota
    ==> alinear_flota victorias orden_descendente

-- De menor a mayor
vulnerables <- flota
    ==> alinear_flota escudos orden_ascendente
```

### 4.5 Eliminar Duplicados (`eliminar_clones`)
Si tu archivo de datos tiene filas repetidas por error, esta instruccion las suprime en un solo paso:

```holocron
datos_limpios <- flota
    ==> eliminar_clones
```

### 4.6 Manejo de Datos Faltantes (`sanar_vacios`)
En el mundo real, a veces las tablas tienen celdas vacias o registros nulos. HolocronDSL ofrece dos formas de sanarlos:

1. **Descartar las filas con vacios:**
   ```holocron
   datos_completos <- flota
       ==> sanar_vacios descartar
   ```

2. **Rellenar los vacios con un valor por defecto:**
   ```holocron
   datos_completos <- flota
       ==> sanar_vacios sustituir_con 0
   ```

---

## Capitulo 5: Resumen Estadistico y Agrupaciones

Una de las tareas mas comunes en ciencia de datos es resumir informacion por grupos (por ejemplo: ¿cuantas naves tiene cada faccion y cual es su promedio de victorias?).

En HolocronDSL esto se hace en dos pasos dentro del pipeline:
1. `agrupar_sector [ columnas_de_agrupacion ]`
2. `sintetizar_indicadores [ indicadores... ]`

```holocron
resumen_facciones <- flota
    ==> agrupar_sector [ faccion ]
    ==> sintetizar_indicadores [
        censo_total := recuento(),
        defensa_acumulada := acumular(escudos),
        equilibrio_escudos := equilibrio(escudos),
        record_victorias := cenit(victorias),
        peor_victorias := nadir(victorias),
        dispersion_victorias := desviacion(victorias)
    ]
```

### Las 7 Funciones Estadisticas de la Fuerza:
| Funcion | Significado Real | Explicacion Simple |
| :--- | :--- | :--- |
| `recuento()` | Conteo (Count) | Cuenta cuantas filas hay en el grupo. |
| `acumular(col)` | Suma (Sum) | Suma todos los valores de esa columna. |
| `equilibrio(col)` | Media / Promedio (Mean) | Calcula el promedio exacto (el equilibrio en los datos). |
| `mediana(col)` | Mediana (Median) | Encuentra el dato que queda exactamente en la mitad. |
| `cenit(col)` | Maximo (Max) | El valor mas alto registrado en esa columna. |
| `nadir(col)` | Minimo (Min) | El valor mas bajo registrado en esa columna. |
| `desviacion(col)` | Desviacion estandar (Std) | Que tan dispersos o variados estan los datos respecto al promedio. |

---

## Capitulo 6: Proyecciones Holograficas (Visualizacion de Datos)

Un analisis de datos no esta completo si no puedes mostrarlo graficamente. En HolocronDSL, los graficos se configuran de manera declarativa con el bloque `proyectar_holograma`:

### 6.1 Sintaxis General
```holocron
proyectar_holograma TIPO_GRAFICA desde TABLA_DE_DATOS
    eje_x := "nombre_columna_horizontal"
    eje_y := "nombre_columna_vertical"
    holotitulo := "Titulo de la Grafica"
    guardar_proyeccion := "ruta/salida.png"
fin_holograma
```

### 6.2 Tipos de Graficos Soportados
1. `barras`: Ideal para comparar cantidades entre categorias (ejemplo: victorias por faccion).
2. `lineas`: Ideal para ver como evoluciona una variable a lo largo del tiempo o secuencias continuas.
3. `dispersion`: Muestra puntos individuales para ver la correlacion entre dos variables numericas (ejemplo: escudos vs victorias).
4. `histograma`: Muestra la distribucion y frecuencia de una sola variable numerica (solo requiere `eje_x`).
5. `caja`: Grafico de caja y bigotes para analizar cuartiles y valores anomalos (outliers).

### 6.3 Ejemplo Practico de un Holograma
```holocron
proyectar_holograma barras desde resumen_facciones
    eje_x := "faccion"
    eje_y := "defensa_acumulada"
    holotitulo := "Capacidad defensiva total por faccion"
    guardar_proyeccion := "salidas/defensa_facciones.png"
fin_holograma
```

---

## Capitulo 7: Abstraccion y Control de Flujo

Para flujos avanzados, HolocronDSL te permite crear tus propias rutinas y tomar decisiones logicas.

### 7.1 Misiones (Funciones Propias)
Si tienes una secuencia de preparacion que necesitas usar varias veces en diferentes tablas, puedes crear una **mision**:

```holocron
-- Definimos una mision reutilizable
mision preparar_escuadron con_parametros (datos_crudos, blindaje_minimo)
    filtrados <- datos_crudos
        ==> purgar_donde escudos >= blindaje_minimo
        ==> alinear_flota victorias orden_descendente

    retornar_orden filtrados
fin_mision

-- Usamos nuestra mision cuantas veces queramos:
flota_a <- preparar_escuadron(registro_alfa, 50)
flota_b <- preparar_escuadron(registro_beta, 100)
```

*Estructura:* Inicia con `mision nombre con_parametros (...)`, finaliza obligatoriamente devolviendo los datos con `retornar_orden` y cierra con `fin_mision`.

### 7.2 Tomar Decisiones con la Fuerza (`evaluar_fuerza`)
Permite ejecutar ciertas acciones dependiendo de una condicion:

```holocron
evaluar_fuerza (nivel_combustible > 20)
senda_luminosa
    transmitir_mensaje "Condiciones optimas para el salto hiperespacial."
senda_oscura
    transmitir_mensaje "Alerta critica: recargar celdas de energia."
fin_evaluar
```

---

## Capitulo 8: Como Correr y Verificar tus Programas

Todo el analizador de HolocronDSL se ejecuta directamente desde la consola o terminal de tu computador usando el interprete en Python.

### 8.1 Estructura del Archivo
Guarda tu codigo en un archivo con extension `.holo` (por ejemplo: `mi_analisis.holo`).

### 8.2 Comandos Principales de la Terminal

1. **Escanear y verificar si tu codigo esta bien escrito (sin errores):**
   ```bash
   python src/cli.py mi_analisis.holo --check
   ```
   Si no hay errores, el sistema te respondera:
   `Sintaxis verificada con exito: la Fuerza fluye en perfecta armonia.`

2. **Ver como el compilador entiende la estructura de tu programa (Arbol Sintactico):**
   ```bash
   python src/cli.py mi_analisis.holo --tree
   ```
   Esto desplegara una representacion visual de todas las ramas, sentencias y tokens reconocidos en tu codigo.

3. **Ejecutar pruebas automaticas para comprobar que todo el sistema funciona:**
   ```bash
   python -m unittest discover -s tests
   ```

### 8.3 Que pasa si cometes un error?
No te preocupes. HolocronDSL cuenta con un **Manejador Diagnostico de Errores** diseñado para personas que estan aprendiendo. Si olvidas cerrar un corchete o te equivocas en una palabra, el sistema no colapsara con mensajes incomprensibles; te dira el **numero de linea**, la **columna** exacta y una pista clara de que fue lo que paso:

```text
============================================================
ALERTAS EN EL SISTEMA: Se encontraron anomalias sintacticas:
============================================================
Se detectaron 1 anomalias sintacticas en el codigo:
  - [Error Sintactico] Linea 4:18 en el token 'escudos' -> Falta un elemento requerido en la sentencia: missing ']' at 'escudos'
```

---

## Capitulo 9: Tu Primer Proyecto Completo Paso a Paso

Para finalizar este manual, analicemos este proyecto integral que utiliza casi todas las capacidades del lenguaje:

```holocron
-- ==========================================================
-- PROYECTO TACTICO: REPORTE DE LA FLOTA ESTELAR
-- ==========================================================

-- 1. Ingestion de datos
telemetria <- abrir_holocron "examples/datos/telemetria_flota.csv"

-- 2. Limpieza y filtrado
escuadron_activo <- telemetria
    ==> eliminar_clones
    ==> sanar_vacios sustituir_con 0
    ==> revelar_sectores [ identificador, modelo, faccion, escudos, victorias ]
    ==> purgar_donde escudos > 30 y_fuerza victorias > 0
    ==> forjar_cristal indice_ataque := victorias * 10
    ==> alinear_flota indice_ataque orden_descendente

-- 3. Resumen estadistico por faccion
resumen_estrategico <- escuadron_activo
    ==> agrupar_sector [ faccion ]
    ==> sintetizar_indicadores [
        naves_listas := recuento(),
        promedio_defensivo := equilibrio(escudos),
        mayor_victorias := cenit(victorias)
    ]

-- 4. Guardado de los reportes en CSV
archivar_holocron escuadron_activo en "salidas/escuadron_activo.csv"
archivar_holocron resumen_estrategico en "salidas/resumen_estrategico.csv"

-- 5. Proyeccion del holograma comparativo
proyectar_holograma barras desde resumen_estrategico
    eje_x := "faccion"
    eje_y := "naves_listas"
    holotitulo := "Distribucion de naves operativas por faccion"
    guardar_proyeccion := "salidas/naves_operativas.png"
fin_holograma

-- 6. Notificacion final
transmitir_mensaje "Analisis tactico completado y archivado satisfactoriamente."
```

Con estos conceptos tienes todo lo necesario para escribir programas claros, estructurados y reproducibles en **HolocronDSL**.
