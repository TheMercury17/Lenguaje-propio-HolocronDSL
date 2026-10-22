# Biblioteca propia de visualizacion grafica y proyeccion holografica para HolocronDSL
# Genera graficos exclusivamente en formato PNG con estetica galactica de alto contraste (Grupo 5)
# NOTA: No utiliza formato SVG bajo ninguna circunstancia (cumplimiento estricto de requisitos).

import os
from pathlib import Path
from typing import Optional, List, Dict, Any, Union

# Configurar Matplotlib en modo 'Agg' (sin interfaz de ventanas) para ejecucion headless en Linux/Kali y Windows
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.runtime.holocron_table import HolocronTable
from src.errors.semantic_error import ColumnaInexistenteError, HolocronSemanticError


class HolocronPlotter:
    """
    Motor propio de generacion grafica (Hologramas) para HolocronDSL.
    Produce directamente archivos rasterizados en formato PNG con tema espacial de alto contraste.
    """

    COLOR_FONDO = "#090D16"        # Espacio profundo
    COLOR_FONDO_AX = "#0F172A"     # Panel tactico
    COLOR_TEXTO = "#E2E8F0"        # Texto cian suave
    COLOR_REJILLA = "#1E293B"      # Rejilla sutil
    COLOR_CIAN = "#00F0FF"         # Laser cian de la Alianza
    COLOR_AMBAR = "#FFE81F"        # Amarillo Star Wars clasico
    COLOR_ROJO = "#FF2A55"         # Laser rojo del Imperio
    COLOR_VERDE = "#10B981"        # Hiperimpulsor verde
    COLOR_PURPURA = "#A855F7"      # Sable purpura

    PALETA_LASER = [COLOR_CIAN, COLOR_AMBAR, COLOR_ROJO, COLOR_VERDE, COLOR_PURPURA]

    @classmethod
    def _aplicar_estilo_galactico(cls, fig, ax, titulo: Optional[str], eje_x: Optional[str], eje_y: Optional[str]):
        """Configura la estetica galactica espacial de alto contraste sobre la figura."""
        fig.patch.set_facecolor(cls.COLOR_FONDO)
        ax.set_facecolor(cls.COLOR_FONDO_AX)

        ax.tick_params(colors=cls.COLOR_TEXTO, labelsize=9)
        ax.xaxis.label.set_color(cls.COLOR_TEXTO)
        ax.yaxis.label.set_color(cls.COLOR_TEXTO)

        for spine in ax.spines.values():
            spine.set_color("#334155")
            spine.set_linewidth(1.2)

        ax.grid(True, linestyle="--", alpha=0.3, color=cls.COLOR_REJILLA)

        if titulo:
            ax.set_title(titulo, color=cls.COLOR_AMBAR, fontsize=13, fontweight="bold", pad=14)
        if eje_x:
            ax.set_xlabel(eje_x, color=cls.COLOR_TEXTO, fontsize=10, labelpad=8)
        if eje_y:
            ax.set_ylabel(eje_y, color=cls.COLOR_TEXTO, fontsize=10, labelpad=8)

    @classmethod
    def proyectar_holograma(
        cls,
        tipo: str,
        tabla: HolocronTable,
        propiedades: Dict[str, str],
        linea: Optional[int] = None,
        columna: Optional[int] = None
    ) -> str:
        """
        Ejecuta la sentencia 'holograma' del DSL y guarda la imagen exclusivamente en formato PNG.
        Tipos soportados: 'barras', 'lineas', 'dispersion', 'histograma', 'caja'.
        """
        eje_x = propiedades.get("eje_x", None)
        eje_y = propiedades.get("eje_y", None)
        titulo = propiedades.get("titulo", f"Proyeccion Holografica ({tipo})")
        ruta_salida = propiedades.get("guardar", None)

        if not ruta_salida:
            ruta_salida = f"salidas/holograma_{tipo}.png"

        # Validar extension estrictamente PNG
        path_salida = Path(ruta_salida)
        if path_salida.suffix.lower() == ".svg":
            raise HolocronSemanticError(
                "La directiva de proyeccion no admite formato SVG. Especifique extension .png",
                linea, columna, "Modifique el archivo de salida para utilizar extension '.png'."
            )
        if not path_salida.suffix or path_salida.suffix.lower() != ".png":
            path_salida = path_salida.with_suffix(".png")

        # Asegurar creacion de directorio destino
        if path_salida.parent:
            path_salida.parent.mkdir(parents=True, exist_ok=True)

        tipo_normalizado = tipo.lower()
        fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)

        try:
            if tipo_normalizado == "barras":
                cls._generar_barras(ax, tabla, eje_x, eje_y, linea, columna)
            elif tipo_normalizado == "lineas":
                cls._generar_lineas(ax, tabla, eje_x, eje_y, linea, columna)
            elif tipo_normalizado == "dispersion":
                cls._generar_dispersion(ax, tabla, eje_x, eje_y, linea, columna)
            elif tipo_normalizado == "histograma":
                cls._generar_histograma(ax, tabla, eje_x, linea, columna)
            elif tipo_normalizado in ("caja", "cajas"):
                cls._generar_caja(ax, tabla, eje_x, eje_y, linea, columna)
            else:
                raise HolocronSemanticError(
                    f"Tipo de holograma no soportado: '{tipo}'. Tipos validos: barras, lineas, dispersion, histograma, caja.",
                    linea, columna
                )

            cls._aplicar_estilo_galactico(fig, ax, titulo, eje_x, eje_y)
            plt.tight_layout()
            fig.savefig(str(path_salida), format="png", facecolor=fig.get_facecolor(), edgecolor="none")
        finally:
            plt.close(fig)

        return str(path_salida.resolve())

    @classmethod
    def _generar_barras(cls, ax, tabla: HolocronTable, eje_x: str, eje_y: str, linea, columna):
        if not eje_x or not eje_y:
            raise HolocronSemanticError("El holograma de barras requiere 'eje_x' y 'eje_y'.", linea, columna)

        tabla.validar_columna(eje_x, linea, columna)
        tabla.validar_columna(eje_y, linea, columna)

        valores_x = [str(v) if v is not None else "nulo" for v in tabla.obtener_columna(eje_x)]
        valores_y_crudos = tabla.obtener_columna(eje_y)
        valores_y = [float(v) if v is not None and isinstance(v, (int, float)) else 0.0 for v in valores_y_crudos]

        barras = ax.bar(
            valores_x,
            valores_y,
            color=cls.COLOR_CIAN,
            edgecolor=cls.COLOR_AMBAR,
            linewidth=1.2,
            alpha=0.88,
            width=0.55
        )
        # Rotar etiquetas si son extensas
        ax.set_xticks(range(len(valores_x)))
        if any(len(x) > 6 for x in valores_x) or len(valores_x) > 5:
            ax.set_xticklabels(valores_x, rotation=25, ha="right")
        else:
            ax.set_xticklabels(valores_x)

    @classmethod
    def _generar_lineas(cls, ax, tabla: HolocronTable, eje_x: str, eje_y: str, linea, columna):
        if not eje_x or not eje_y:
            raise HolocronSemanticError("El holograma de lineas requiere 'eje_x' y 'eje_y'.", linea, columna)

        tabla.validar_columna(eje_x, linea, columna)
        tabla.validar_columna(eje_y, linea, columna)

        valores_x = tabla.obtener_columna(eje_x)
        valores_y = [float(v) if v is not None and isinstance(v, (int, float)) else 0.0 for v in tabla.obtener_columna(eje_y)]

        ax.plot(
            range(len(valores_x)),
            valores_y,
            color=cls.COLOR_CIAN,
            marker="o",
            markersize=5,
            linewidth=2.2,
            label=eje_y
        )
        ax.set_xticks(range(len(valores_x)))
        ax.set_xticklabels([str(x) for x in valores_x], rotation=25, ha="right")

    @classmethod
    def _generar_dispersion(cls, ax, tabla: HolocronTable, eje_x: str, eje_y: str, linea, columna):
        if not eje_x or not eje_y:
            raise HolocronSemanticError("El holograma de dispersion requiere 'eje_x' y 'eje_y'.", linea, columna)

        tabla.validar_columna(eje_x, linea, columna)
        tabla.validar_columna(eje_y, linea, columna)

        crudos_x = tabla.obtener_columna(eje_x)
        crudos_y = tabla.obtener_columna(eje_y)

        puntos_x = []
        puntos_y = []
        for x, y in zip(crudos_x, crudos_y):
            if x is not None and y is not None and isinstance(x, (int, float)) and isinstance(y, (int, float)):
                puntos_x.append(float(x))
                puntos_y.append(float(y))

        ax.scatter(
            puntos_x,
            puntos_y,
            color=cls.COLOR_AMBAR,
            edgecolors=cls.COLOR_ROJO,
            s=70,
            alpha=0.85,
            linewidth=1.2
        )

    @classmethod
    def _generar_histograma(cls, ax, tabla: HolocronTable, eje_x: str, linea, columna):
        if not eje_x:
            raise HolocronSemanticError("El holograma de histograma requiere especificar 'eje_x'.", linea, columna)

        tabla.validar_columna(eje_x, linea, columna)
        crudos = tabla.obtener_columna(eje_x)
        valores = [float(v) for v in crudos if v is not None and isinstance(v, (int, float))]

        if not valores:
            valores = [0.0]

        ax.hist(
            valores,
            bins=min(10, max(3, len(valores) // 2)),
            color=cls.COLOR_CIAN,
            edgecolor=cls.COLOR_AMBAR,
            linewidth=1.2,
            alpha=0.8
        )

    @classmethod
    def _generar_caja(cls, ax, tabla: HolocronTable, eje_x: Optional[str], eje_y: Optional[str], linea, columna):
        col_medir = eje_y if eje_y else eje_x
        if not col_medir:
            raise HolocronSemanticError("El holograma de caja requiere al menos una variable numerica en eje_y o eje_x.", linea, columna)

        tabla.validar_columna(col_medir, linea, columna)
        crudos = tabla.obtener_columna(col_medir)
        valores = [float(v) for v in crudos if v is not None and isinstance(v, (int, float))]

        if not valores:
            valores = [0.0]

        bp = ax.boxplot(
            valores,
            patch_artist=True,
            boxprops=dict(facecolor=cls.COLOR_CIAN, color=cls.COLOR_AMBAR, alpha=0.7),
            capprops=dict(color=cls.COLOR_AMBAR),
            whiskerprops=dict(color=cls.COLOR_AMBAR),
            flierprops=dict(color=cls.COLOR_ROJO, markeredgecolor=cls.COLOR_ROJO),
            medianprops=dict(color=cls.COLOR_ROJO, linewidth=2)
        )
        ax.set_xticklabels([col_medir])
