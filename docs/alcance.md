# Documento de Alcance y Delimitacion del Lenguaje: HolocronDSL

**Universidad Sergio Arboleda**  
**Programa de Ciencias de la Computacion e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programacion y Transduccion (Semestre 2026-2)  
**Docente:** Joaquin F. Sanchez  
**Equipo de Desarrollo (Grupo 5):**  
- Andres Sebastian Coral Vallejo  
- Carol Arenas Cardona  

---

## 1. Descripcion General y Dominio

HolocronDSL es un Lenguaje de Dominio Especifico (DSL) declarativo y funcional concebido para el analisis, depuracion, transformacion y visualizacion de datos en flujos reproducibles de ciencia de datos. 

Inspirado conceptualmente en el universo galactico de Star Wars, el lenguaje adopta una metafora coherente donde las fuentes de informacion representan archivos holocronicos, las secuencias de transformacion fluyen mediante hiperespacio a traves del operador de pipeline (`==>`), las operaciones de preparacion purgan anomalías y forjan nuevos indicadores, y las visualizaciones se proyectan como hologramas tacticos.

El diseño prioriza instrucciones legibles y compactas, eliminando el ruido sintactico de los lenguajes de proposito general y garantizando una separacion estricta entre la especificacion sintactica formal (procesada con ANTLR4) y la ejecucion semantica posterior.

---

## 2. Perfil de Usuario y Casos de Uso

### 2.1 Usuarios Objetivo
- **Analistas e investigadores de datos:** Profesionales que requieren describir transformaciones y resumenes de datos sin necesidad de implementar estructuras de control complejas de bajo nivel.
- **Estudiantes de ciencias de la computacion:** Usuarios que buscan comprender la relacion formal entre gramaticas, analisis lexico-sintactico, arboles de derivacion y compiladores.

### 2.2 Casos de Uso Principales
1. **Ingestion y almacenamiento estructurado:** Carga de registros tabulares en formato CSV con soporte para delimitadores configurables y asociacion a identificadores inmutables.
2. **Preparacion y depuracion de registros:** Seleccion de variables de interes, filtrado bajo condiciones logico-relacionales, eliminacion de registros duplicados (`eliminar_clones`) y saneamiento de valores nulos (`sanar_vacios`).
3. **Ingenieria de caracteristicas:** Forja de nuevas variables numericas derivadas mediante expresiones aritmeticas completas con precedencia formal.
4. **Agrupamiento y consolidacion estadistica:** Calculo de metricas descriptivas (conteo, suma, media armonica/equilibrio, mediana, maximo, minimo y desviacion estandar) por sector o categorias.
5. **Proyeccion visual:** Definicion declarativa de graficos de barras, lineas, dispersion, histogramas y cajas con exportacion directa a archivos graficos PNG.
6. **Modularizacion mediante misiones:** Encapsulacion de rutinas de transformacion reutilizables con paso de parametros y retorno de conjuntos de datos.

---

## 3. Entradas, Salidas y Restricciones

### 3.1 Entradas
- Archivos de codigo fuente con extension `.holo` codificados en UTF-8.
- Conjuntos de datos estructurados en formato CSV (Comma-Separated Values) o delimitados por caracteres especificos como tabuladores.

### 3.2 Salidas
- Tablas intermedias y finales exportables a formato CSV.
- Representaciones visuales de datos en archivos de imagen PNG.
- Transmisiones de telemetria y mensajes diagnósticos formateados en la terminal.
- Representaciones jerarquicas del arbol sintactico (CST/AST) para validacion y depuracion formal.

### 3.3 Restricciones y Supuestos de Diseño
- El lenguaje no busca ser un equivalente generico de Python ni C++; evita construcciones imperativas tradicionales como ciclos `while` o `for` indexados, privilegiando el encadenamiento declarativo sobre conjuntos de datos completos.
- Las transformaciones operan bajo inmutabilidad conceptual: cada operacion de pipeline recibe un conjunto y produce un resultado nuevo, evitando efectos colaterales sobre las variables previas.
- Todas las sentencias y nombres de columnas son sensibles a mayusculas y minusculas (case-sensitive).

---

## 4. Arquitectura Modular

El sistema se compone de los siguientes modulos delimitados:
1. **Modulo de Gramatica (`grammar/`):** Archivo `HolocronDSL.g4` con la definicion formal lexica y sintactica en ANTLR4.
2. **Modulo Front-end Generado (`src/generated/`):** Clases del Lexer, Parser y Visitor generadas de forma automatizada por ANTLR4 para Python 3.
3. **Modulo de Manejo de Errores (`src/errors/`):** Interceptor `HolocronErrorListener` que reporta numero de linea, columna y sugerencia contextual legible.
4. **Modulo de Control y Driver (`src/compiler/`):** Fachada de ejecucion para tokenizar, parsear e imprimir arboles sintacticos de archivos o cadenas en linea.
5. **Interfaz de Linea de Comandos (`src/cli.py`):** Punto de entrada para el usuario final que permite inspeccionar y verificar programas `.holo`.
