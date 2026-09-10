#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Punto de entrada directo en la raiz del proyecto para HolocronDSL
# Permite ejecutar archivos .holo simplemente con: python holocron.py ruta_al_archivo.holo

import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

# Re-ejecutar con el interprete de .venv o venv si existe y no esta activado
if "VIRTUAL_ENV" not in os.environ:
    for venv_name in [".venv", "venv"]:
        venv_py = ROOT_DIR / venv_name / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python3")
        if not venv_py.exists() and sys.platform != "win32":
            venv_py = ROOT_DIR / venv_name / "bin/python"
        if venv_py.exists() and sys.executable != str(venv_py):
            try:
                os.execv(str(venv_py), [str(venv_py)] + sys.argv)
            except Exception:
                pass

# Asegurar que los paquetes de .venv se encuentren en sys.path prioritariamente
for venv_name in [".venv", "venv"]:
    vdir = ROOT_DIR / venv_name
    if vdir.is_dir():
        for sp in vdir.glob("lib/python*/site-packages"):
            if sp.is_dir() and str(sp) not in sys.path:
                sys.path.insert(0, str(sp))
        sp_win = vdir / "Lib" / "site-packages"
        if sp_win.is_dir() and str(sp_win) not in sys.path:
            sys.path.insert(0, str(sp_win))

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.cli import main

if __name__ == "__main__":
    main()
