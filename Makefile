# =============================================================================
# Makefile para HolocronDSL
# Lenguajes de Programacion y Transduccion (Semestre 2026-2)
# Grupo 5: Andres Sebastian Coral Vallejo, Carol Arenas Cardona
# =============================================================================

VENV ?= .venv

ifeq ($(OS),Windows_NT)
    PYTHON_SYS ?= python
    VENV_BIN = $(VENV)/Scripts
    VENV_PY = $(VENV_BIN)/python.exe
    VENV_PIP = $(VENV_BIN)/pip.exe
    ifneq ($(wildcard $(VENV_PY)),)
        PYTHON ?= $(VENV_PY)
        PIP ?= $(VENV_PIP)
    else
        PYTHON ?= $(PYTHON_SYS)
        PIP ?= $(PYTHON_SYS) -m pip
    endif
else
    PYTHON_SYS ?= python3
    VENV_BIN = $(VENV)/bin
    VENV_PY = $(VENV_BIN)/python
    VENV_PIP = $(VENV_BIN)/pip
    ifneq ($(wildcard $(VENV_PY)),)
        PYTHON ?= $(VENV_PY)
        PIP ?= $(VENV_PIP)
    else ifneq ($(VIRTUAL_ENV),)
        PYTHON ?= $(PYTHON_SYS)
        PIP ?= $(PYTHON_SYS) -m pip
    else
        PYTHON ?= $(VENV_PY)
        PIP ?= $(VENV_PIP)
    endif
endif

ANTLR4 ?= antlr4

.PHONY: help install prepare grammar test test-lexer test-parser test-invalid check-examples clean

help:
	@echo "Comandos disponibles para HolocronDSL:"
	@echo "  make install        - Instalar dependencias (crea entorno virtual .venv automaticamente en Linux)"
	@echo "  make grammar        - Compilar la gramatica ANTLR4 a codigo Python en src/generated"
	@echo "  make test           - Ejecutar la suite completa de pruebas unitarias"
	@echo "  make test-lexer     - Ejecutar pruebas del analizador lexico"
	@echo "  make test-parser    - Ejecutar pruebas sintacticas de construcciones validas"
	@echo "  make test-invalid   - Ejecutar pruebas sintacticas negativas (deteccion de errores)"
	@echo "  make check-examples - Validar sintacticamente todos los programas .holo en examples/"
	@echo "  make clean          - Limpiar caches de Python y archivos temporales"

install:
ifeq ($(OS),Windows_NT)
	$(PYTHON) -m pip install -r requirements.txt
else
	@if [ -n "$$VIRTUAL_ENV" ]; then \
		echo "Detectado entorno virtual activo ($$VIRTUAL_ENV). Instalando dependencias..."; \
		$(PYTHON_SYS) -m pip install -r requirements.txt; \
	elif [ -d "$(VENV)" ]; then \
		echo "Instalando dependencias en entorno virtual existente $(VENV)..."; \
		$(VENV_PIP) install -r requirements.txt; \
	else \
		echo "Creando entorno virtual aislado en $(VENV)..."; \
		if $(PYTHON_SYS) -m venv $(VENV) 2>/dev/null; then \
			echo "Entorno virtual creado exitosamente. Instalando dependencias..."; \
			$(VENV_PIP) install -r requirements.txt; \
		else \
			echo "Aviso: no se pudo crear venv con python3-venv."; \
			echo "Instalando con --break-system-packages (compatible con Kali Linux)..."; \
			$(PYTHON_SYS) -m pip install -r requirements.txt --break-system-packages; \
		fi; \
	fi
	@echo "Instalacion completada exitosamente."
endif

prepare:
ifeq ($(OS),Windows_NT)
	@rem Windows no requiere paso previo obligatorio
else
	@if [ -z "$$VIRTUAL_ENV" ] && [ ! -f "$(VENV_PY)" ]; then \
		echo "No se encontro entorno virtual ni dependencias. Ejecutando 'make install'..."; \
		$(MAKE) install; \
	fi
endif

grammar:
	$(ANTLR4) -Dlanguage=Python3 -visitor -o src/generated grammar/HolocronDSL.g4

test: prepare
	$(PYTHON) -m unittest discover -s tests

test-lexer: prepare
	$(PYTHON) -m unittest tests/test_lexer.py

test-parser: prepare
	$(PYTHON) -m unittest tests/test_parser_valid.py

test-invalid: prepare
	$(PYTHON) -m unittest tests/test_parser_invalid.py

check-examples: prepare
	$(PYTHON) src/cli.py examples/01_telemetria_cazas.holo --check
	$(PYTHON) src/cli.py examples/02_censo_galactico.holo --check
	$(PYTHON) src/cli.py examples/03_proyeccion_holografica.holo --check
	$(PYTHON) src/cli.py examples/04_mision_avanzada.holo --check
	$(PYTHON) src/cli.py examples/05_proyecto_completo.holo --check

clean:
	$(PYTHON_SYS) -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').rglob('__pycache__')]"

