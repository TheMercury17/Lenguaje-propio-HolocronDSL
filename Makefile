# =============================================================================
# Makefile para HolocronDSL
# Lenguajes de Programacion y Transduccion (Semestre 2026-2)
# Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
# =============================================================================

PYTHON ?= python
ANTLR4 ?= antlr4

.PHONY: help install grammar test test-lexer test-parser test-invalid check-examples clean

help:
	@echo Comandos disponibles para HolocronDSL:
	@echo   make install        - Instalar dependencias del proyecto desde requirements.txt
	@echo   make grammar        - Compilar la gramatica ANTLR4 a codigo Python en src/generated
	@echo   make test           - Ejecutar la suite completa de pruebas unitarias
	@echo   make test-lexer     - Ejecutar pruebas del analizador lexico
	@echo   make test-parser    - Ejecutar pruebas sintacticas de construcciones validas
	@echo   make test-invalid   - Ejecutar pruebas sintacticas negativas (deteccion de errores)
	@echo   make check-examples - Validar sintacticamente todos los programas .holo en examples/
	@echo   make clean          - Limpiar caches de Python y archivos temporales

install:
	$(PYTHON) -m pip install -r requirements.txt

grammar:
	$(ANTLR4) -Dlanguage=Python3 -visitor -o src/generated grammar/HolocronDSL.g4

test:
	$(PYTHON) -m unittest discover -s tests

test-lexer:
	$(PYTHON) -m unittest tests/test_lexer.py

test-parser:
	$(PYTHON) -m unittest tests/test_parser_valid.py

test-invalid:
	$(PYTHON) -m unittest tests/test_parser_invalid.py

check-examples:
	$(PYTHON) src/cli.py examples/01_telemetria_cazas.holo --check
	$(PYTHON) src/cli.py examples/02_censo_galactico.holo --check
	$(PYTHON) src/cli.py examples/03_proyeccion_holografica.holo --check
	$(PYTHON) src/cli.py examples/04_mision_avanzada.holo --check
	$(PYTHON) src/cli.py examples/05_proyecto_completo.holo --check

clean:
	$(PYTHON) -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').rglob('__pycache__')]"
