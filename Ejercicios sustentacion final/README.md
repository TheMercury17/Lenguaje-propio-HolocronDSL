# EJERCICIOS PRACTICOS PARA LA SUSTENTACION FINAL DE HOLOCRONDDSL

**Proyecto:** HolocronDSL (Lenguaje de Dominio Especifico para Ciencia de Datos y Visualizacion)  
**Asignatura:** Lenguajes de Programacion y Transduccion  
**Universidad:** Universidad Sergio Arboleda  
**Semestre:** 2026-2  
**Docente:** Prof. Joaquin F. Sanchez  
**Grupo 5:**
- Andres Sebastian Coral Vallejo
- Carol Arenas Cardona

---

## 1. INTRODUCCION Y RESUMEN GENERAL

Este directorio reune los 5 programas y analisis especificos implementados para la sustentacion final del proyecto. Todos los programas operan sobre los motores nativos construidos integramente desde cero para HolocronDSL:

1. **Motor de E/S (`HolocronIO`):** Lectura nativa de archivos `.csv`, `.xlsx` (mediante descompresion y analisis de XML de OpenXML) y `.xls` (formato XML Spreadsheet 2003), sin dependencias de `pandas` ni `openpyxl`.
2. **Motor Matematico (`HolocronMath`):** Estadistica descriptiva completa (media, mediana, desviacion estandar muestral, minimos, maximos, cuantiles) y operadores aritmeticos sin librerias de calculo externas.
3. **Motor Grafico (`HolocronPlotter`):** Renderizado directo en formato raster PNG a 300 DPI (lineas, barras, dispersion, histogramas y cajas), evitando estrictamente el uso de SVG.
4. **Motor de Aprendizaje Automatico y Redes Neuronales (`HolocronML`):** Arboles de decision CART, agrupamiento K-Means, regresion lineal por minimos cuadrados ordinarios (OLS), Perceptron simple y Perceptron Multicapa (MLP) con Retropropagacion y Descenso de Gradiente.
5. **Estructuras de Datos y Paradigma Funcional:** Arreglos dinamicos (`HolocronArray`), Pilas LIFO (`HolocronPila`), Colas FIFO (`HolocronCola`), bucles iterativos (`mientras`, `para`, `recorrer`) y funciones de orden superior (`filtrar_lista`, `mapear_lista`).

---

## 2. DETALLE DE LOS 5 EJERCICIOS DE SUSTENTACION

### EJERCICIO 1: Calculo del Factorial (5 al 100) y Benchmark de Rendimiento frente a Python

- **Archivo HolocronDSL:** `01_factorial_rendimiento.holo`
- **Script de Benchmark y Graficacion:** `benchmark_factorial.py`
- **Grafico Generado:** `salidas/comparativa_rendimiento_factorial.png`

#### Descripcion y Metodologia:
El programa calcula el factorial \(n!\) para cada entero \(n \in [5, 100]\) mediante una mision iterativa en HolocronDSL. Se evalua la exactitud computacional frente a la implementacion de Python nativo y se realiza un benchmark comparando los tiempos de ejecucion a traves de 10 iteraciones por valor de \(n\).

#### Fundamentacion Teorica del Rendimiento:
1. **Complejidad Algoritmica:** Ambos enfoques presentan una complejidad temporal teorica de \(O(n)\) y espacial de \(O(1)\) auxiliar.
2. **Precision Aritmetica Arbitraria (BigInt):** Ambos entornos gestionan enteros de precision arbitraria sin desbordamiento de memoria (overflow), calculando el valor exacto de \(100!\), el cual posee 158 digitos decimales.
3. **Causa del Overhead en HolocronDSL:**
   - **HolocronDSL:** Opera mediante un **interprete sobre el Arbol de Sintaxis Abstracta (AST)** siguiendo el patron de diseño Visitor. Cada operacion elemental involucra la navegacion recursiva de nodos ANTLR4, busquedas dinamicas en la Tabla de Simbolos (`SymbolTable`) con resolucion de ambitos lexicos, despacho polimorfico y creacion de marcos de ejecucion en memoria.
   - **Python (CPython):** Precompila el codigo fuente a **bytecode optimizado**, el cual es despachado en un bucle central escrito en lenguaje C altamente afinado con acceso directo a registros y memoria contigua.
   - Por esta razon arquitectonica, HolocronDSL requiere entre 1.5 y 3.5 ms por calculo, mientras que CPython lo resuelve en fracciones de microsegundo, lo cual es el comportamiento formalmente esperado entre un interprete AST y una maquina virtual de bytecode optimizada en C.

---

### EJERCICIO 2: Visualizacion de la Funcion Sigmoide

- **Archivo HolocronDSL:** `02_visualizar_sigmoide.holo`
- **Script de Soporte y Proyeccion Completa:** `generar_sigmoide.py`
- **Archivos Generados:**
  - `salidas/grafica_sigmoide.png` (300 DPI)
  - `salidas/grafica_sigmoide_completa.png` (Curva y derivada con anclajes)
  - `salidas/reporte_sigmoide.csv` y `salidas/reporte_sigmoide.xls`

#### Definicion Matematica:
\[
\sigma(x) = \frac{1}{1 + e^{-x}}
\]
Su derivada formal es:
\[
\sigma'(x) = \sigma(x) \cdot (1 - \sigma(x))
\]

#### Propiedades Computacionales y Relevancia:
1. **Dominio:** \((-\infty, +\infty)\); **Rango:** \((0.0, 1.0)\).
2. **Punto de Inflexion y Simetria:** En \(x = 0\), \(\sigma(0) = 0.5\). La funcion cumple la propiedad de simetria \(\sigma(-x) = 1 - \sigma(x)\).
3. **Maxima Pendiente:** La derivada alcanza su maximo en \(x = 0\) con un valor de \(0.25\). Conforme \(|x| \to \infty\), \(\sigma'(x) \to 0\) (fenomeno conocido como desvanecimiento del gradiente o *vanishing gradient*).
4. **Rol en Aprendizaje Automatico:** Mapea combinaciones lineales a probabilidades continuas, actuando como funcion de activacion no lineal indispensable para romper la linealidad en capas ocultas.

---

### EJERCICIO 3: Analisis del Perceptron Multicapa para XOR

- **Archivo HolocronDSL:** `03_perceptron_multicapa_xor.holo`
- **Script de Analisis Teoretico y Graficas:** `analisis_mlp_xor.py`
- **Archivos Generados:**
  - `salidas/convergencia_perdida_xor.png` (Curva de error cuadratico medio)
  - `salidas/frontera_decision_xor.png` (Frontera de decision no lineal en 2D)
  - `salidas/grafica_dispersion_xor.png`
  - `salidas/reporte_estimacion_xor.csv` y `salidas/reporte_estimacion_xor.xls`

#### ¿Que algoritmo usamos y por que?
Se utiliza **Retropropagacion (Backpropagation) basado en Descenso de Gradiente (Gradient Descent)** con funcion de activacion sigmoide no lineal y calculo analitico de gradientes por la regla de la cadena.

#### Explicacion Formal para la Sustentacion:
1. **El Problema de Separabilidad Lineal:**
   - La compuerta XOR genera los pares: \((0,0) \to 0\), \((0,1) \to 1\), \((1,0) \to 1\), \((1,1) \to 0\).
   - En 1969, Marvin Minsky y Seymour Papert publicaron en su obra *Perceptrons* la demostracion matematica formal de que un Perceptron simple de una sola capa solo puede trazar un hiperplano lineal (una linea recta en 2D). Dado que los puntos de clase 1 y los de clase 0 estan en diagonales cruzadas opuestas, **no existe ninguna linea recta capaz de separar ambas clases sin error**.
2. **Resolucion mediante el Perceptron Multicapa (MLP):**
   - Se diseño una arquitectura con: **2 neuronas de entrada**, **4 neuronas en la capa oculta no lineal** y **1 neurona de salida**.
   - Cada neurona oculta proyecta las entradas a un nuevo espacio latente dimensional mediante la transformacion no lineal \(\sigma(\mathbf{W}_h \mathbf{x} + \mathbf{b}_h)\).
   - En dicho espacio latente, las muestras se tornan **linealmente separables**, permitiendo que la neurona de salida clasifique los 4 estados con **100% de exactitud**.
3. **Mecanica del Descenso de Gradiente y Retropropagacion:**
   - **Perdida (MSE):** \(L = \frac{1}{2} (y - \hat{y})^2\).
   - **Gradiente de salida:** \(\delta_o = (y - \hat{y}) \cdot \hat{y}(1 - \hat{y})\).
   - **Gradiente oculto retropropagado:** \(\delta_{h,j} = \left( \delta_o \cdot w_{j,o} \right) \cdot h_j(1 - h_j)\).
   - **Actualizacion de pesos:**
     \[
     \mathbf{W} \leftarrow \mathbf{W} + \eta \cdot \delta \cdot \mathbf{x}^T
     \]
     donde \(\eta = 1.5\) es la tasa de aprendizaje. Tras 3,000 epocas, la perdida converge de \(0.602\) a \(0.00065\), logrando una exactitud perfecta.

---

### EJERCICIO 4: Analisis Exploratorio de Datos (EDA) sobre Archivo `.xlsx`

- **Archivo HolocronDSL:** `04_analisis_exploratorio_xlsx.holo`
- **Script Complementario de Analisis:** `analisis_eda_xlsx.py`
- **Conjunto de Datos:** `datos/censo_ingresos.xlsx` (10,280 observaciones, 6 variables)
- **Archivos Generados:**
  - `salidas/eda_ingreso_por_educacion.png` (Grafico de barras de ingreso medio)
  - `salidas/eda_dispersion_ingreso_sexo.png` (Diagrama de caja para dispersion salarial)
  - `salidas/eda_distribucion_edad.png` (Histograma continuo de edades)
  - `salidas/eda_resumen_educativo.csv` y `.xls`
  - `salidas/eda_resumen_genero.csv` y `.xls`

#### Caracteristicas de la Implementacion:
1. **Lectura Nativa Directa de `.xlsx`:**
   - Desarrollada en `src/runtime/io_engine.py` mediante los modulos estandar `zipfile` y `xml.etree.ElementTree`.
   - Se descomprime el paquete Office OpenXML en memoria, se analiza la tabla de cadenas compartidas (`xl/sharedStrings.xml`) y se decodifican las celdas de la primera hoja de calculo (`xl/worksheets/sheet1.xml`), convirtiendo coordenadas alfanumericas (ej. `A1`, `BC45`) a indices matriciales.
   - Carga e infiere tipos de las 10,280 filas en menos de 0.8 segundos sin ninguna dependencia externa.
2. **Transformaciones y Agrupamientos Estadisticos:**
   - Limpieza de nulos con `sanar_vacios`.
   - Agrupamiento por `nivel_edu` y `sex` calculando: conteo, promedio, mediana, desviacion estandar, minimo y maximo.
3. **Hallazgos Estadisticos Relevantes:**
   - **Retorno a la educacion:** Existe una relacion monotona creciente entre escolaridad e ingreso. La media salarial del nivel *Medio superior y superior* (\$10,588) duplica la del nivel de *Primaria incompleta* (\$4,676).
   - **Disparidad por genero:** A pesar de que las mujeres registran una escolaridad promedio ligeramente superior (10.22 frente a 9.66 anos), su ingreso medio (\$6,286) es un 21.7% inferior al de los hombres (\$8,029), indicando una brecha estructural de ingresos en la muestra censal.

---

### EJERCICIO 5: Filtro Funcional de Numeros Primos del 1 al 100

- **Archivo HolocronDSL:** `05_filtro_primos_1_100.holo`
- **Script de Verificacion Formal:** `verificar_primos.py`
- **Salida:** Identificacion exacta de los 25 numeros primos en el rango \([1, 100]\).

#### Algoritmo de Primalidad:
Se implemento en HolocronDSL una funcion `es_primo(numero)` basada en la prueba de divisiones sucesivas optimizada hasta \(\sqrt{n}\):
1. Todo numero \(n \le 1\) se descarta como no primo.
2. Si \(n > 2\) y es divisible por 2, se descarta.
3. Se verifican unicamente divisores impares \(d \in [3, \sqrt{n}]\) con paso 2 (\(d \leftarrow d + 2\)).
4. Complejidad temporal por prueba: \(O(\sqrt{n})\).

#### Enfoque Funcional de Orden Superior:
El programa demuestra dos tecnicas de programacion:
1. **Orden Superior:** Utiliza la funcion incorporada `filtrar_lista(numeros_1_a_100, "es_primo")`, la cual recibe la coleccion y el identificador de la mision como predicado booleano, evaluando los elementos de forma funcional.
2. **Recorrido Iterativo Imperativo:** Utiliza `recorrer elemento en numeros_1_a_100` combinado con `evaluar_fuerza es_primo(elemento) == cierto_es`.
3. **Resultado:** Ambos metodos coinciden al 100%, identificando exactamente los 25 numeros primos:
   `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]`

---

## 3. GUIA PASO A PASO PARA MAQUINA VIRTUAL KALI LINUX

A continuacion se presentan los comandos exactos y secuenciales para preparar el entorno y ejecutar cada ejercicio dentro de una maquina virtual Kali Linux (en VirtualBox o VMware).

### Paso 0: Preparacion del Entorno Base en Kali Linux
Abra una terminal en Kali Linux (`kali@kali` o `root`) y asegure los paquetes del sistema:
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git default-jre antlr4
```

### Paso 1: Clonar o Actualizar el Repositorio
```bash
# Opcion A: Si se descarga por primera vez
git clone https://github.com/TheMercury17/Lenguaje-propio-HolocronDSL.git
cd Lenguaje-propio-HolocronDSL

# Opcion B: Si ya se encuentra descargado en la carpeta de descargas
cd ~/Downloads/Lenguaje-propio-HolocronDSL-main
git pull origin main
```

### Paso 2: Configuracion de Dependencias y Entorno Virtual (PEP 668)
Kali Linux aplica la proteccion PEP 668 (`externally-managed-environment`), por lo cual se recomienda crear o activar un entorno virtual:
```bash
# Opcion rapida mediante Makefile (crea y activa .venv automaticamente):
make install

# O manualmente:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Paso 3: Verificacion Inicial del Sistema
```bash
# Compilar la gramatica si fuera necesario
make grammar

# Ejecutar la suite completa de 93 pruebas unitarias
make test
# O directamente:
python3 run_tests.py --all
```

---

### Paso 4: Ejecucion Paso a Paso de Cada Ejercicio de Sustentacion

#### Ejercicio 1: Factorial (5 al 100) y Benchmark de Rendimiento
```bash
# 1.1 Ejecutar en el lenguaje propio HolocronDSL:
python3 holocron.py "Ejercicios sustentacion final/01_factorial_rendimiento.holo"

# 1.2 Ejecutar el benchmark comparativo con Python:
python3 "Ejercicios sustentacion final/benchmark_factorial.py"

# 1.3 Ver el grafico de rendimiento generado en Kali:
ristretto "Ejercicios sustentacion final/salidas/comparativa_rendimiento_factorial.png" &
```
*Via Makefile:* `make run-factorial`

---

#### Ejercicio 2: Proyeccion y Analisis de la Funcion Sigmoide
```bash
# 2.1 Ejecutar el programa en HolocronDSL (proyecta y exporta CSV y XLS):
python3 holocron.py "Ejercicios sustentacion final/02_visualizar_sigmoide.holo"

# 2.2 Ejecutar la proyeccion analitica detallada (curva y derivada):
python3 "Ejercicios sustentacion final/generar_sigmoide.py"

# 2.3 Visualizar las imagenes generadas en Kali:
ristretto "Ejercicios sustentacion final/salidas/grafica_sigmoide_completa.png" &
```
*Via Makefile:* `make run-sigmoide`

---

#### Ejercicio 3: Perceptron Multicapa para XOR (Estimador y Graficas)
```bash
# 3.1 Ejecutar el entrenamiento y clasificacion en HolocronDSL:
python3 holocron.py "Ejercicios sustentacion final/03_perceptron_multicapa_xor.holo"

# 3.2 Ejecutar el analisis teorico, frontera de decision 2D y curva de perdida:
python3 "Ejercicios sustentacion final/analisis_mlp_xor.py"

# 3.3 Ver la frontera de decision no lineal y la convergencia en Kali:
ristretto "Ejercicios sustentacion final/salidas/frontera_decision_xor.png" &
ristretto "Ejercicios sustentacion final/salidas/convergencia_perdida_xor.png" &
```
*Via Makefile:* `make run-xor`

---

#### Ejercicio 4: Analisis Exploratorio de Datos (EDA) sobre `censo_ingresos.xlsx`
```bash
# 4.1 Ejecutar el pipeline de analisis sobre 10,280 observaciones en HolocronDSL:
python3 holocron.py "Ejercicios sustentacion final/04_analisis_exploratorio_xlsx.holo"

# 4.2 Ejecutar el script descriptivo complementario:
python3 "Ejercicios sustentacion final/analisis_eda_xlsx.py"

# 4.3 Visualizar los graficos generados (barras, cajas, histograma) en Kali:
ristretto "Ejercicios sustentacion final/salidas/eda_ingreso_por_educacion.png" &
ristretto "Ejercicios sustentacion final/salidas/eda_dispersion_ingreso_sexo.png" &
ristretto "Ejercicios sustentacion final/salidas/eda_distribucion_edad.png" &
```
*Via Makefile:* `make run-eda`

---

#### Ejercicio 5: Filtro Funcional de Numeros Primos del 1 al 100
```bash
# 5.1 Ejecutar el filtrado funcional de orden superior en HolocronDSL:
python3 holocron.py "Ejercicios sustentacion final/05_filtro_primos_1_100.holo"

# 5.2 Ejecutar la verificacion formal y comparativa con filter():
python3 "Ejercicios sustentacion final/verificar_primos.py"
```
*Via Makefile:* `make run-primos`

---

### Paso 5: Opciones de Ejecucion Automatizada en Kali Linux

#### Opcion 1: Mediante Makefile
```bash
# Ejecutar los 5 ejercicios completos en una sola secuencia:
make run-sustentacion
```

#### Opcion 2: Mediante el Script Interactivo para Kali Linux
```bash
# Otorgar permisos de ejecucion
chmod +x "Ejercicios sustentacion final/ejecutar_en_kali.sh"

# Ejecutar el menu interactivo:
./"Ejercicios sustentacion final/ejecutar_en_kali.sh"

# O ejecutar los 5 de manera directa pasando el argumento '1':
./"Ejercicios sustentacion final/ejecutar_en_kali.sh" 1
```

#### Opcion 3: Explorar Todos los Archivos Generados en Kali Linux
```bash
# Abrir el gestor de archivos Thunar en la carpeta de salidas:
thunar "Ejercicios sustentacion final/salidas" &
# O con xdg-open:
xdg-open "Ejercicios sustentacion final/salidas" &
```

---

## 4. ESTRUCTURA DE ARCHIVOS DE LA CARPETA

```
Ejercicios sustentacion final/
├── 01_factorial_rendimiento.holo        # Codigo HolocronDSL: Calculo factorial 5 a 100
├── benchmark_factorial.py              # Benchmark temporal Holocron vs Python
├── 02_visualizar_sigmoide.holo          # Codigo HolocronDSL: Proyeccion curva sigmoide
├── generar_sigmoide.py                 # Generador de grafica analitica de sigmoide y derivada
├── 03_perceptron_multicapa_xor.holo     # Codigo HolocronDSL: MLP para compuerta XOR
├── analisis_mlp_xor.py                 # Analisis del MLP, frontera de decision y Backprop
├── 04_analisis_exploratorio_xlsx.holo   # Codigo HolocronDSL: EDA completo sobre .xlsx
├── analisis_eda_xlsx.py                # Script estadistico descriptivo sobre .xlsx
├── 05_filtro_primos_1_100.holo          # Codigo HolocronDSL: Filtro funcional de primos
├── verificar_primos.py                 # Verificacion formal y comparativa de primalidad
├── README.md                           # Documentacion academica exhaustiva
├── datos/                              # Conjuntos de datos fuente
│   ├── censo_ingresos.xlsx             # Dataset Excel original de 10,280 observaciones
│   ├── censo_ingresos.csv              # Version tabular en CSV
│   ├── puntos_x.csv                    # Coordenadas de prueba para la funcion sigmoide
│   └── xor_dataset.csv                 # Tabla de verdad del problema XOR
└── salidas/                            # Artefactos y reportes generados
    ├── comparativa_rendimiento_factorial.png
    ├── grafica_sigmoide.png
    ├── grafica_sigmoide_completa.png
    ├── reporte_sigmoide.csv
    ├── reporte_sigmoide.xls
    ├── convergencia_perdida_xor.png
    ├── frontera_decision_xor.png
    ├── grafica_dispersion_xor.png
    ├── reporte_estimacion_xor.csv
    ├── reporte_estimacion_xor.xls
    ├── eda_ingreso_por_educacion.png
    ├── eda_dispersion_ingreso_sexo.png
    ├── eda_distribucion_edad.png
    ├── eda_resumen_educativo.csv
    ├── eda_resumen_educativo.xls
    ├── eda_resumen_genero.csv
    └── eda_resumen_genero.xls
```
