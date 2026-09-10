# Punto de entrada directo en la raiz del proyecto para HolocronDSL
# Permite ejecutar archivos .holo simplemente con: python holocron.py ruta_al_archivo.holo

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.cli import main

if __name__ == "__main__":
    main()
