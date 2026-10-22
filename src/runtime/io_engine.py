# Biblioteca propia de lectura y escritura de archivos tabulares para HolocronDSL
# Implementacion de parser y serializador CSV independiente (Grupo 5)

import os
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from src.errors.semantic_error import ArchivoNoEncontradoError


class HolocronIO:
    """
    Motor propio de entrada y salida (I/O) de archivos para HolocronDSL.
    Lee, analiza tipos de datos e infiere esquemas para archivos tabulares (CSV).
    """

    @staticmethod
    def inferir_tipo(valor_texto: str) -> Any:
        """Convierte una cadena de texto a su tipo atomico mas adecuado (int, float, bool, None, str)."""
        texto = valor_texto.strip()
        if not texto:
            return None

        # Valores nulos / ausentes
        if texto.lower() in ("nulo", "null", "none", "nan", "na", "\\n"):
            return None

        # Valores booleanos galacticos y estandar
        if texto.lower() in ("cierto_es", "verdadero", "true"):
            return True
        if texto.lower() in ("falso_es", "falso", "false"):
            return False

        # Intentar entero
        if (texto.startswith("-") and texto[1:].isdigit()) or texto.isdigit():
            try:
                return int(texto)
            except ValueError:
                pass

        # Intentar punto flotante
        try:
            val_float = float(texto)
            return val_float
        except ValueError:
            pass

        # Despojar comillas si venia entrecomillado
        if (texto.startswith('"') and texto.endswith('"')) or (texto.startswith("'") and texto.endswith("'")):
            if len(texto) >= 2:
                return texto[1:-1]

        return texto

    @staticmethod
    def separar_linea_csv(linea: str, delimitador: str = ",") -> List[str]:
        """
        Analizador sintactico de linea CSV con soporte para campos entrecomillados
        y comillas escapadas.
        """
        campos = []
        campo_actual = []
        en_comillas = False
        i = 0
        n = len(linea)

        while i < n:
            caracter = linea[i]
            if caracter == '"':
                if en_comillas and i + 1 < n and linea[i + 1] == '"':
                    campo_actual.append('"')
                    i += 1
                else:
                    en_comillas = not en_comillas
            elif caracter == delimitador and not en_comillas:
                campos.append("".join(campo_actual).strip())
                campo_actual = []
            else:
                campo_actual.append(caracter)
            i += 1

        campos.append("".join(campo_actual).strip())
        return campos

    @classmethod
    def leer_csv(
        cls,
        ruta: str,
        delimitador: str = ",",
        linea_origen: Optional[int] = None,
        columna_origen: Optional[int] = None
    ) -> Tuple[List[str], List[Dict[str, Any]]]:
        """
        Lee un archivo CSV desde disco utilizando la biblioteca propia de I/O.
        Retorna la tupla: (lista_columnas, lista_de_registros_diccionarios).
        """
        path_archivo = Path(ruta)
        if not path_archivo.is_file():
            raise ArchivoNoEncontradoError(str(ruta), linea_origen, columna_origen)

        try:
            with open(path_archivo, "r", encoding="utf-8-sig") as f:
                lineas = [l.rstrip("\r\n") for l in f if l.strip()]
        except Exception as e:
            raise ArchivoNoEncontradoError(f"{ruta} (Error del sistema operativo: {str(e)})", linea_origen, columna_origen)

        if not lineas:
            return [], []

        # Fila de encabezados
        encabezados_crudos = cls.separar_linea_csv(lineas[0], delimitador)
        columnas = [h.strip().strip('"').strip("'") for h in encabezados_crudos if h]

        registros: List[Dict[str, Any]] = []
        for idx_linea, linea_texto in enumerate(lineas[1:], start=2):
            if not linea_texto or linea_texto.startswith("#") or linea_texto.startswith("--"):
                continue

            valores_crudos = cls.separar_linea_csv(linea_texto, delimitador)
            fila_dict: Dict[str, Any] = {}
            for col_idx, col_nombre in enumerate(columnas):
                if col_idx < len(valores_crudos):
                    val = cls.inferir_tipo(valores_crudos[col_idx])
                else:
                    val = None
                fila_dict[col_nombre] = val
            registros.append(fila_dict)

        return columnas, registros

    @classmethod
    def escribir_csv(
        cls,
        ruta: str,
        columnas: List[str],
        registros: List[Dict[str, Any]],
        delimitador: str = ","
    ) -> str:
        """
        Serializa y escribe una tabla a disco en formato CSV usando el formato de HolocronDSL.
        """
        path_archivo = Path(ruta)
        if path_archivo.parent:
            path_archivo.parent.mkdir(parents=True, exist_ok=True)

        with open(path_archivo, "w", encoding="utf-8", newline="") as f:
            # Escribir encabezado
            f.write(delimitador.join(columnas) + "\n")

            # Escribir filas
            for fila in registros:
                campos_serializados = []
                for col in columnas:
                    val = fila.get(col, None)
                    if val is None:
                        campos_serializados.append("")
                    elif isinstance(val, bool):
                        campos_serializados.append("cierto_es" if val else "falso_es")
                    elif isinstance(val, (int, float)):
                        campos_serializados.append(str(val))
                    else:
                        cadena = str(val)
                        if delimitador in cadena or '"' in cadena or "\n" in cadena:
                            cadena_escapada = cadena.replace('"', '""')
                            campos_serializados.append(f'"{cadena_escapada}"')
                        else:
                            campos_serializados.append(cadena)
                f.write(delimitador.join(campos_serializados) + "\n")

        return str(path_archivo.resolve())
