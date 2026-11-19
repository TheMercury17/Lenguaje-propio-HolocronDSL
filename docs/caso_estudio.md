# Caso de Estudio Final: Optimización y Telemetría de Redes de Comunicación Galáctica

**Universidad Sergio Arboleda**  
**Programa de Ciencias de la Computación e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programación y Transducción (Semestre 2026-2)  
**Docente:** Joaquín F. Sánchez  
**Equipo de Desarrollo (Grupo 5):**  
- Andrés Sebastián Coral Vallejo  
- Carol Arenas Cardona  

---

## 1. Descripción del Conjunto de Datos

El caso de estudio seleccionado aborda el análisis de telemetría y desempeño en infraestructuras de telecomunicaciones de largo alcance, contextualizado dentro de la red de repetidores hiperespaciales de la galaxia.

El conjunto de datos original se encuentra ubicado en:
`examples/datos/telemetria_redes_galacticas.csv`

El archivo comprende registros correspondientes a 30 nodos o repetidores situados en diversos cuadrantes y sectores de la galaxia (Coruscant, Corellia, Kuat, Mandalore, Tatooine, Fondor, Eriadu, Naboo, Kashyyyk y Ryloth). Cada registro contiene métricas operativas y de transmisión recolectadas durante un periodo de monitoreo:

| Nombre de Columna | Tipo de Dato | Descripción Funcional |
| :--- | :--- | :--- |
| `nodo_id` | Texto | Identificador unívoco del repetidor de comunicaciones (ej. `NX-101`, `NX-201`). |
| `sector` | Texto | Sector astronómico donde opera la estación transmisora. |
| `distancia_parsecs` | Decimal | Distancia física respecto a la estación central de control (en pársecs). |
| `ancho_banda_gbps` | Decimal | Capacidad nominal del canal de transmisión (en gigabits por segundo). |
| `latencia_ms` | Decimal | Retardo de propagación de los paquetes de datos (en milisegundos). |
| `paquetes_totales` | Entero | Número total de paquetes de telemetría transmitidos durante la ventana de observación. |
| `paquetes_perdidos` | Entero | Número de paquetes no entregados o descartados por congestión. |
| `estado` | Texto | Estado operativo reportado (`Operativo`, `Degradado`, `Mantenimiento`). |

El conjunto de datos incluye intencionalmente valores que requieren saneamiento (registros con estados no operativos, filas con datos atípicos o faltantes) para poner a prueba las capacidades de filtrado y preparación del lenguaje.

---

## 2. Preguntas de Análisis

Para guiar la investigación técnica y comprobar la expresividad del DSL, se formularon las siguientes cinco interrogantes clave:

1. **¿Cuál es la relación matemática existente entre la distancia física (en pársecs) y la latencia de transmisión (en milisegundos)?**  
   Se requiere ajustar un modelo de regresión lineal simple por mínimos cuadrados ordinarios (OLS) para obtener la pendiente, el intercepto y el coeficiente de determinación ($R^2$).
2. **¿Cómo se distribuye la capacidad de ancho de banda y la latencia a lo largo de los sectores galácticos?**  
   Determinar qué sectores presentan mayor dispersión en sus tiempos de respuesta y cuáles mantienen un rendimiento más homogéneo.
3. **¿Cuál es la tasa porcentual de pérdida de paquetes y la carga de transmisión efectiva procesada por cada nodo?**  
   Calcular nuevas variables derivadas mediante expresiones aritméticas compuestas.
4. **¿Cuáles sectores concentran el mayor tráfico consolidado y las latencias promedio más críticas?**  
   Estructurar agrupamientos categóricos con múltiples funciones de agregación simultáneas (suma, promedio, conteo, mínimo y máximo).
5. **¿Qué comportamiento sigue la degradación temporal de las señales a medida que se saturan los canales de transmisión?**  
   Visualizar perfiles de evolución para identificar cuellos de botella en la infraestructura.

---

## 3. Programa Escrito en el DSL

El flujo de procesamiento, modelado y visualización se encuentra implementado en el archivo:
`examples/06_caso_estudio_final.holo`

A continuación se presenta el código íntegro del programa:

```holocron
-- =========================================================================
-- Caso de Estudio Final: Telemetria y Modelado de Redes Galacticas
-- Lenguaje: HolocronDSL (Fase 3: Visualizacion, Analisis y Regresion Lineal)
-- Autores: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
-- =========================================================================

-- 1. Ingestion de datos desde el holocron de telemetria
red_galactica = abrir_holocron "examples/datos/telemetria_redes_galacticas.csv"

-- 2. Limpieza, filtrado e ingenieria de caracteristicas
red_operativa = red_galactica
    |> purgar donde estado == "Operativo" y paquetes_totales > 0
    |> sanar_vacios con 0
    |> forjar paquetes_exitosos = paquetes_totales - paquetes_perdidos
    |> forjar tasa_perdida = (paquetes_perdidos / paquetes_totales) * 100
    |> forjar carga_efectiva = (ancho_banda_gbps * 1000) / latencia_ms
    |> ordenar por latencia_ms ascendente

-- 3. Transmision de los primeros registros limpios a la terminal
transmitir "Telemetria de Redes Galacticas Limpias y Forjadas:"
transmitir red_operativa

-- 4. Agrupamiento estadistico y agregaciones por sector galactico
resumen_sectores = red_operativa
    |> agrupar por [sector]
    |> resumir nodos_activos = recuento(),
               latencia_media = equilibrio(latencia_ms),
               latencia_maxima = cenit(latencia_ms),
               latencia_minima = nadir(latencia_ms),
               ancho_banda_total = acumular(ancho_banda_gbps),
               perdida_promedio = equilibrio(tasa_perdida)
    |> ordenar por latencia_media ascendente

transmitir "Resumen Consolidado por Sector Galactico:"
transmitir resumen_sectores

-- 5. Exportacion de tablas resultantes en formatos CSV y Excel nativo (.xls)
archivar_holocron resumen_sectores en "salidas/caso_estudio_resumen_sectores.csv"

-- 6. Modelado Estadistico: Regresion Lineal Simple (Distancia vs Latencia)
modelo_latencia = red_operativa
    |> trazar_regresion [
        eje_x = "distancia_parsecs",
        eje_y = "latencia_ms",
        destino = "latencia_predicha"
    ]

transmitir "Resumen del Modelo de Regresion Lineal OLS (Distancia vs Latencia):"
transmitir modelo_latencia

-- Exportacion del modelo con predicciones y residuos a hoja de calculo Excel nativa
archivar_holocron modelo_latencia en "salidas/caso_estudio_predicciones.xls"

-- 7. Generacion de Visualizaciones Holograficas (Minimo 4 requeridas; 5 generadas)

-- Grafico 1: Diagrama de Barras - Latencia Media por Sector
proyectar_holograma barras resumen_sectores [
    titulo = "Latencia Media de Transmision por Sector Galactico",
    eje_x = "sector",
    eje_y = "latencia_media",
    guardar_en = "salidas/caso_estudio_01_barras_sectores.png"
]

-- Grafico 2: Histograma - Distribucion de Frecuencia de la Latencia
proyectar_holograma histograma red_operativa [
    titulo = "Distribucion de Frecuencias de Latencia en Nodos Operativos",
    eje_x = "latencia_ms",
    guardar_en = "salidas/caso_estudio_02_histograma_latencia.png"
]

-- Grafico 3: Diagrama de Caja (Boxplot) - Dispersion del Ancho de Banda
proyectar_holograma caja red_operativa [
    titulo = "Dispersion de Capacidad de Ancho de Banda (Gbps)",
    eje_y = "ancho_banda_gbps",
    guardar_en = "salidas/caso_estudio_03_caja_ancho_banda.png"
]

-- Grafico 4: Grafico de Lineas - Perfil de Degradacion de Señal Ordenado
proyectar_holograma lineas red_operativa [
    titulo = "Curva de Crecimiento de Latencia vs Nodos de Monitoreo",
    eje_x = "nodo_id",
    eje_y = "latencia_ms",
    guardar_en = "salidas/caso_estudio_04_lineas_degradacion.png"
]

-- Grafico 5: Dispersion con Recta de Regresion Lineal Ajustada (OLS)
proyectar_holograma regresion red_operativa [
    titulo = "Modelo de Regresion Lineal: Distancia vs Latencia de Señal",
    eje_x = "distancia_parsecs",
    eje_y = "latencia_ms",
    guardar_en = "salidas/caso_estudio_05_regresion_latencia.png"
]

transmitir "Caso de estudio completado con exito. Todos los reportes han sido generados."
```

---

## 4. Limpieza y Transformación

La preparación del conjunto de datos se ejecuta de forma reproducible a través del operador funcional `|>`:

1. **Filtrado condicional relacional:** Mediante la instrucción `purgar donde estado == "Operativo" y paquetes_totales > 0`, se aíslan las estaciones activas, descartando 2 nodos que se encontraban en mantenimiento o fuera de línea.
2. **Saneamiento de valores nulos:** Se aplica `sanar_vacios con 0` para garantizar que eventuales celdas vacías no interrumpan los cálculos de razón y división.
3. **Ingeniería de variables derivadas:**
   - `paquetes_exitosos = paquetes_totales - paquetes_perdidos`: Mide el volumen neto entregado.
   - `tasa_perdida = (paquetes_perdidos / paquetes_totales) * 100`: Proporción de paquetes descartados expresada en porcentaje.
   - `carga_efectiva = (ancho_banda_gbps * 1000) / latencia_ms`: Relación entre la velocidad del enlace y el retardo, indicando la eficiencia real de transferencia.
4. **Ordenamiento secuencial:** Se reorganizan los nodos mediante `ordenar por latencia_ms ascendente` para facilitar el análisis longitudinal y la proyección de perfiles continuos.

---

## 5. Indicadores y Estadísticas Calculadas

A través de la instrucción `agrupar por [sector]` combinada con la cláusula `resumir`, se consolida una tabla agregada con métricas multivariadas:

| Sector | Nodos Activos (`recuento`) | Latencia Media (`ms`) | Latencia Máxima (`ms`) | Latencia Mínima (`ms`) | Ancho Banda Total (`Gbps`) | Pérdida Promedio (`%`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Coruscant** | 3 | 17.50 | 21.0 | 14.2 | 1650.0 | 0.0093 |
| **Corellia** | 6 | 28.53 | 47.2 | 18.4 | 2250.0 | 0.0336 |
| **Kuat** | 5 | 41.26 | 66.8 | 21.0 | 2170.0 | 0.0285 |
| **Mandalore** | 4 | 53.63 | 73.1 | 35.2 | 1200.0 | 0.0933 |
| **Fondor** | 3 | 59.87 | 78.5 | 42.1 | 860.0 | 0.1345 |
| **Eriadu** | 3 | 66.80 | 85.3 | 48.0 | 720.0 | 0.1788 |
| **Tatooine** | 4 | 82.05 | 108.4 | 62.5 | 800.0 | 0.2852 |

### Modelado de Regresión Lineal por Mínimos Cuadrados (OLS):
Al aplicar la instrucción `trazar_regresion [eje_x = "distancia_parsecs", eje_y = "latencia_ms", destino = "latencia_predicha"]`, la biblioteca matemática interna `HolocronMath` calculó los siguientes coeficientes del modelo:

- **Pendiente ($m$):** $1.0967$
- **Intercepto ($b$):** $4.0152$
- **Ecuación ajustada:** $\text{latencia} = 1.0967 \times \text{distancia} + 4.0152$
- **Coeficiente de determinación ($R^2$):** $0.9842$ (98.42% de la varianza explicada)
- **Coeficiente de correlación de Pearson ($r$):** $+0.9921$ (correlación lineal positiva prácticamente perfecta)
- **Error estándar de estimación ($S_e$):** $3.48\text{ ms}$

---

## 6. Visualizaciones Generadas

El programa exporta de manera autónoma cinco gráficos matriciales en formato PNG de alta resolución (300 DPI) con paleta oscura táctica (`#0b0f19` de fondo, tipografías claras, cuadrículas sutiles y realces cromáticos en cian `#00e5ff` y magenta `#e040fb`):

1. **`salidas/caso_estudio_01_barras_sectores.png` (Diagrama de Barras):**  
   Compara la latencia media entre sectores astronómicos. Ilustra con claridad el contraste entre el núcleo galáctico (Coruscant con 17.50 ms) y el borde exterior (Tatooine con 82.05 ms).
2. **`salidas/caso_estudio_02_histograma_latencia.png` (Histograma):**  
   Representa la función de densidad de la latencia en la red. Presenta una concentración bimodal con un pico entre 20 y 45 ms correspondiente a mundos del núcleo, y una cola prolongada hacia la derecha que alcanza los 108 ms en el borde exterior.
3. **`salidas/caso_estudio_03_caja_ancho_banda.png` (Diagrama de Caja / Boxplot):**  
   Expone la mediana ($345\text{ Gbps}$), el rango intercuartílico ($Q_1 = 280\text{ Gbps}$, $Q_3 = 430\text{ Gbps}$) y los límites mínimo ($180\text{ Gbps}$) y máximo ($580\text{ Gbps}$) del ancho de banda disponible, confirmando la ausencia de valores extremos anómalos.
4. **`salidas/caso_estudio_04_lineas_degradacion.png` (Gráfico de Líneas):**  
   Muestra el crecimiento monótono de la latencia a lo largo de los nodos ordenados, permitiendo identificar puntos de inflexión donde la infraestructura pasa de una condición óptima a una de latencia severa.
5. **`salidas/caso_estudio_05_regresion_latencia.png` (Dispersión y Recta de Regresión Lineal OLS):**  
   Representa los 28 puntos muestrales empíricos en color cian junto con la línea de tendencia ajustada en color magenta vibrante. En la parte superior derecha se incluye un cuadro con la ecuación ajustada, el valor de $R^2 = 0.9842$ y el coeficiente de correlación $r = 0.9921$.

---

## 7. Interpretación Técnica de los Resultados

A partir del procesamiento efectuado en HolocronDSL, se extraen las siguientes conclusiones del dominio:

1. **Dependencia directa de la distancia:** La correlación de Pearson obtenida ($r = 0.9921$) confirma que el factor físico de distancia es el determinante primario de la latencia observada. Cada pársec adicional impone en promedio $1.10\text{ ms}$ de retardo al canal.
2. **Latencia base del sistema:** El intercepto de la recta ($b = 4.02\text{ ms}$) representa el costo basal de conmutación electrónica y enrutamiento en los nodos repetidores, independiente del medio de propagación.
3. **Brecha de conectividad entre regiones:** Los sectores del núcleo (Coruscant, Corellia, Kuat) operan con tasas de pérdida de paquetes insignificantes ($< 0.03\%$), mientras que en el borde exterior (Tatooine, Eriadu) la pérdida alcanza el $0.28\%$, sugiriendo la necesidad urgente de instalar repetidores intermedios en esas rutas.

---

## 8. Archivos Generados y Procedimiento de Reproducción

### 8.1 Archivos Producidos
Tras la ejecución del programa, se generan los siguientes elementos en el directorio `salidas/`:
- `salidas/caso_estudio_resumen_sectores.csv`: Archivo tabular con el consolidado por sectores.
- `salidas/caso_estudio_predicciones.xls`: Hoja de cálculo en formato XML Spreadsheet 2003 legible nativamente en LibreOffice Calc y Microsoft Excel, conteniendo todas las columnas originales junto con los valores ajustados y los residuos de regresión.
- `salidas/caso_estudio_01_barras_sectores.png`: Gráfico de barras.
- `salidas/caso_estudio_02_histograma_latencia.png`: Histograma.
- `salidas/caso_estudio_03_caja_ancho_banda.png`: Diagrama de caja.
- `salidas/caso_estudio_04_lineas_degradacion.png`: Gráfico de líneas.
- `salidas/caso_estudio_05_regresion_latencia.png`: Gráfico de regresión lineal simple.

### 8.2 Procedimiento de Reproducción en Consola (Linux / Kali Linux / Windows)

Para reproducir de forma determinística la totalidad del caso de estudio:

```bash
# Paso 1: Clonar o posicionarse en el directorio del proyecto
cd Lenguaje-propio-HolocronDSL

# Paso 2: Verificar la correcta instalacion de dependencias
make install

# Paso 3: Ejecutar el programa del caso de estudio
python3 holocron.py examples/06_caso_estudio_final.holo

# Alternativa mediante Makefile:
make run-examples
```

Para verificar de inmediato los archivos generados desde la terminal:
```bash
# Listar los reportes e imagenes generadas
ls -la salidas/caso_estudio_*

# En Linux / Kali Linux, abrir el reporte Excel generado:
libreoffice salidas/caso_estudio_predicciones.xls &

# Visualizar las imagenes PNG generadas:
xdg-open salidas/caso_estudio_05_regresion_latencia.png &
```
