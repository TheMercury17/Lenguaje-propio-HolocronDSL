# Biblioteca propia de lectura y escritura de archivos tabulares para HolocronDSL
# Implementacion de parser y serializador CSV independiente (Grupo 5)

import os
import re
import zipfile
import xml.etree.ElementTree as ET
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

    @staticmethod
    def _columna_letras_a_indice(cell_ref: str) -> int:
        """Convierte una coordenada de celda (ej. 'A1', 'BC42') a su indice de columna basado en cero."""
        match = re.match(r"([A-Za-z]+)", cell_ref)
        if not match:
            return 0
        idx = 0
        for char in match.group(1).upper():
            idx = idx * 26 + (ord(char) - ord("A") + 1)
        return idx - 1

    @classmethod
    def leer_xlsx(
        cls,
        ruta: str,
        linea_origen: Optional[int] = None,
        columna_origen: Optional[int] = None
    ) -> Tuple[List[str], List[Dict[str, Any]]]:
        """
        Lee un libro de calculo Microsoft Excel moderno (.xlsx) descomprimiendo
        directamente su estructura OpenXML interna con la libreria estandar de Python,
        sin depender de librerias de terceros como openpyxl o pandas.
        """
        path_archivo = Path(ruta)
        if not path_archivo.is_file():
            raise ArchivoNoEncontradoError(str(ruta), linea_origen, columna_origen)

        try:
            with zipfile.ZipFile(path_archivo, "r") as z:
                # 1. Cargar cadenas compartidas (sharedStrings.xml)
                sst: List[str] = []
                if "xl/sharedStrings.xml" in z.namelist():
                    root_sst = ET.fromstring(z.read("xl/sharedStrings.xml"))
                    ns_main = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
                    for si in root_sst.findall(f"{ns_main}si"):
                        sst.append("".join(si.itertext()))

                # 2. Localizar la primera hoja disponible
                nombre_hoja = "xl/worksheets/sheet1.xml"
                if nombre_hoja not in z.namelist():
                    hojas = [n for n in z.namelist() if n.startswith("xl/worksheets/sheet") and n.endswith(".xml")]
                    if hojas:
                        nombre_hoja = sorted(hojas)[0]
                    else:
                        return [], []

                root_sheet = ET.fromstring(z.read(nombre_hoja))
                ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
                rows = root_sheet.findall(f".//{ns}row")

                if not rows:
                    return [], []

                # 3. Extraer encabezados de la primera fila
                header_cells = rows[0].findall(f"{ns}c")
                cols_map: Dict[int, str] = {}
                for c in header_cells:
                    r_ref = c.get("r", "A1")
                    c_idx = cls._columna_letras_a_indice(r_ref)
                    t = c.get("t")
                    v = c.find(f"{ns}v")
                    val = v.text if v is not None else ""
                    if t == "s" and val != "":
                        try:
                            val = sst[int(val)]
                        except (IndexError, ValueError):
                            pass
                    elif t == "inlineStr":
                        val = "".join(c.itertext())
                    cols_map[c_idx] = str(val).strip()

                num_cols = max(cols_map.keys()) + 1 if cols_map else 0
                columnas = [cols_map.get(i, f"columna_{i+1}") for i in range(num_cols)]
                columnas = [c if c else f"columna_{i+1}" for i, c in enumerate(columnas)]

                # 4. Extraer registros
                registros: List[Dict[str, Any]] = []
                for row in rows[1:]:
                    fila_dict: Dict[str, Any] = {col: None for col in columnas}
                    celdas = row.findall(f"{ns}c")
                    for c in celdas:
                        r_ref = c.get("r")
                        c_idx = cls._columna_letras_a_indice(r_ref) if r_ref else 0
                        if c_idx < len(columnas):
                            t = c.get("t")
                            v = c.find(f"{ns}v")
                            val = v.text if v is not None else None
                            if val is not None:
                                if t == "s":
                                    try:
                                        val = sst[int(val)]
                                    except (IndexError, ValueError):
                                        pass
                                elif t == "b":
                                    val = (val == "1")
                                elif t == "inlineStr":
                                    val = "".join(c.itertext())
                                elif t != "str":
                                    val = cls.inferir_tipo(str(val))
                            fila_dict[columnas[c_idx]] = val
                    registros.append(fila_dict)

                return columnas, registros
        except Exception as e:
            raise ArchivoNoEncontradoError(f"{ruta} (Error al leer formato .xlsx: {str(e)})", linea_origen, columna_origen)

    @classmethod
    def leer_excel_xml_2003(
        cls,
        ruta: str,
        linea_origen: Optional[int] = None,
        columna_origen: Optional[int] = None
    ) -> Tuple[List[str], List[Dict[str, Any]]]:
        """
        Lee hojas de calculo en formato XML Spreadsheet 2003 (.xls).
        """
        path_archivo = Path(ruta)
        if not path_archivo.is_file():
            raise ArchivoNoEncontradoError(str(ruta), linea_origen, columna_origen)

        try:
            tree = ET.parse(path_archivo)
            root = tree.getroot()
            ns = {"ss": "urn:schemas-microsoft-com:office:spreadsheet"}

            rows = root.findall(".//ss:Row", ns)
            if not rows:
                return [], []

            # Encabezados
            header_cells = rows[0].findall("ss:Cell", ns)
            columnas = []
            for c in header_cells:
                data = c.find("ss:Data", ns)
                columnas.append(data.text.strip() if data is not None and data.text else f"col_{len(columnas)+1}")

            registros: List[Dict[str, Any]] = []
            for row in rows[1:]:
                fila_dict: Dict[str, Any] = {col: None for col in columnas}
                cells = row.findall("ss:Cell", ns)
                for idx, c in enumerate(cells):
                    if idx < len(columnas):
                        data = c.find("ss:Data", ns)
                        if data is not None and data.text is not None:
                            tipo = data.attrib.get(f"{{{ns['ss']}}}Type", "String")
                            val_str = data.text.strip()
                            if tipo == "Number":
                                fila_dict[columnas[idx]] = cls.inferir_tipo(val_str)
                            else:
                                fila_dict[columnas[idx]] = val_str
                registros.append(fila_dict)

            return columnas, registros
        except Exception as e:
            raise ArchivoNoEncontradoError(f"{ruta} (Error al leer formato Excel XML: {str(e)})", linea_origen, columna_origen)

    @classmethod
    def leer_excel(
        cls,
        ruta: str,
        linea_origen: Optional[int] = None,
        columna_origen: Optional[int] = None
    ) -> Tuple[List[str], List[Dict[str, Any]]]:
        """
        Punto de entrada unificado para hojas de calculo Excel (.xlsx u .xls).
        Detecta automaticamente el formato interno por cabecera y extension.
        """
        path_archivo = Path(ruta)
        if not path_archivo.is_file():
            raise ArchivoNoEncontradoError(str(ruta), linea_origen, columna_origen)

        # Verificar si es un archivo comprimido ZIP (formato OpenXML .xlsx)
        if zipfile.is_zipfile(path_archivo):
            return cls.leer_xlsx(ruta, linea_origen, columna_origen)
        else:
            return cls.leer_excel_xml_2003(ruta, linea_origen, columna_origen)

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

    @classmethod
    def escribir_excel_xls(
        cls,
        ruta: str,
        columnas: List[str],
        registros: List[Dict[str, Any]]
    ) -> str:
        """
        Serializa la tabla en formato nativo XML Spreadsheet 2003 (.xls).
        Permite que Microsoft Excel y LibreOffice Calc (en Kali Linux) abran el archivo
        directamente como una hoja de calculo con celdas y tipos formateados,
        sin requerir librerias externas pesadas.
        """
        path_archivo = Path(ruta)
        if path_archivo.parent:
            path_archivo.parent.mkdir(parents=True, exist_ok=True)

        lineas = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<?mso-application progid="Excel.Sheet"?>',
            '<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"',
            ' xmlns:o="urn:schemas-microsoft-com:office:office"',
            ' xmlns:x="urn:schemas-microsoft-com:office:excel"',
            ' xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"',
            ' xmlns:html="http://www.w3.org/TR/REC-html40">',
            ' <Worksheet ss:Name="Holocron">',
            '  <Table>'
        ]

        # Fila de encabezados
        lineas.append('   <Row>')
        for col in columnas:
            col_escapada = str(col).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            lineas.append(f'    <Cell><Data ss:Type="String">{col_escapada}</Data></Cell>')
        lineas.append('   </Row>')

        # Filas de datos
        for fila in registros:
            lineas.append('   <Row>')
            for col in columnas:
                val = fila.get(col, None)
                if val is None:
                    lineas.append('    <Cell><Data ss:Type="String"></Data></Cell>')
                elif isinstance(val, bool):
                    txt_bool = "cierto_es" if val else "falso_es"
                    lineas.append(f'    <Cell><Data ss:Type="String">{txt_bool}</Data></Cell>')
                elif isinstance(val, (int, float)):
                    lineas.append(f'    <Cell><Data ss:Type="Number">{val}</Data></Cell>')
                else:
                    txt = str(val).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                    lineas.append(f'    <Cell><Data ss:Type="String">{txt}</Data></Cell>')
            lineas.append('   </Row>')

        lineas.extend([
            '  </Table>',
            ' </Worksheet>',
            '</Workbook>'
        ])

        with open(path_archivo, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas) + "\n")

        return str(path_archivo.resolve())
