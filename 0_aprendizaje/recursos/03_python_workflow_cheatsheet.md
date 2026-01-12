# 🐍 Python Workflow Cheatsheet

## 🚀 INICIO DE PROYECTO NUEVO

### 1. Crear estructura
```bash
# Navegar a carpeta de proyectos
cd ~/Documents/Python-Learning/02_proyectos

# Crear carpeta del proyecto
mkdir 05_mi-nuevo-proyecto
cd 05_mi-nuevo-proyecto

# Crear estructura básica
mkdir src data docs tests
touch README.md
touch .gitignore
```

### 2. Crear virtual environment
```bash
# Crear venv
python -m venv venv

# Activar venv (Git Bash en Windows)
source venv/Scripts/activate

# Verificar que está activo
which python        # Debería mostrar ruta con venv
echo $VIRTUAL_ENV   # Debería mostrar ruta del venv
```

### 3. Instalar dependencias iniciales
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar herramientas de desarrollo
pip install pylint autopep8 black pytest ipython

# Si tienes requirements.txt
pip install -r requirements.txt

# Guardar dependencias
pip freeze > requirements.txt
```

### 4. Inicializar Git
```bash
# Inicializar repo
git init

# Crear .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
venv/
.pytest_cache/

# IDEs
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
EOF

# Primer commit
git add .
git commit -m "chore: Inicializar proyecto"
```

---

## 📝 WORKFLOW DIARIO

### Abrir proyecto existente
```bash
# 1. Navegar al proyecto
cd ~/Documents/Python-Learning/02_proyectos/mi-proyecto

# 2. Activar venv
source venv/Scripts/activate

# 3. Abrir en VS Code
code .
```

### Durante desarrollo
```bash
# Ver qué cambió
git status
git diff

# Ejecutar código
python src/main.py
python -m src.main

# Ejecutar tests
pytest
pytest tests/test_main.py
pytest -v                    # Verbose

# Formatear código
black src/
autopep8 --in-place src/main.py

# Linting
pylint src/main.py
```

### Al terminar sesión
```bash
# 1. Ver cambios
git status
git diff

# 2. Agregar cambios
git add .

# 3. Commit
git commit -m "feat: Descripción del cambio"

# 4. Push (si usas GitHub)
git push

# 5. Desactivar venv
deactivate
```

---

## 🐍 EJECUTAR CÓDIGO PYTHON

### Formas básicas
```bash
# Ejecutar archivo
python archivo.py
python src/main.py

# Ejecutar módulo
python -m módulo
python -m src.main

# Python interactivo
python
ipython                      # Mejor que python

# Ejecutar y quedarse en interactivo
python -i script.py
```

### Con argumentos
```bash
# Pasar argumentos
python script.py arg1 arg2

# Usar en el script
import sys
print(sys.argv)  # ['script.py', 'arg1', 'arg2']
```

---

## 📦 GESTIÓN DE PAQUETES

### Instalar
```bash
# Instalar paquete
pip install nombre-paquete

# Instalar versión específica
pip install paquete==1.2.3
pip install 'paquete>=1.0,<2.0'

# Instalar desde requirements
pip install -r requirements.txt

# Instalar en modo editable (desarrollo)
pip install -e .
```

### Ver y actualizar
```bash
# Ver instalados
pip list
pip list --outdated

# Ver info de paquete
pip show paquete

# Actualizar paquete
pip install --upgrade paquete
pip install -U paquete

# Desinstalar
pip uninstall paquete
```

### Requirements.txt
```bash
# Generar
pip freeze > requirements.txt

# Instalar desde archivo
pip install -r requirements.txt

# Contenido típico
cat requirements.txt
# requests==2.31.0
# beautifulsoup4==4.12.2
# pytest==7.4.3
```

---

## 🧪 TESTING

### Ejecutar tests
```bash
# Todos los tests
pytest

# Archivo específico
pytest tests/test_main.py

# Test específico
pytest tests/test_main.py::test_suma

# Con verbose
pytest -v

# Con coverage
pytest --cov=src

# Solo tests que fallaron
pytest --lf
```

### Crear test
```python
# tests/test_calculadora.py
def test_suma():
    from src.calculadora import suma
    assert suma(2, 3) == 5
def test_division_por_cero():
    from src.calculadora import dividir
    import pytest
    with pytest.raises(ValueError):
    dividir(10, 0)
---

## 🔍 DEBUGGING

### Métodos básicos
```python
# Print debugging
print(f"Variable x: {x}")
print(f"Tipo: {type(x)}")

# Mejor: logging
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Valor de x: %s", x)
```

### IPython
```bash
# Iniciar IPython
ipython

# Comandos útiles en IPython
%run script.py              # Ejecutar script
%debug                      # Debugger después de error
%pdb                        # Auto-debugger en errores
%timeit funcion()           # Medir tiempo
dir(objeto)                 # Ver atributos
help(funcion)               # Ver documentación
?funcion                    # Info rápida
??funcion                   # Ver código fuente
```

### PDB (Python Debugger)
```python
# Agregar breakpoint en código
import pdb; pdb.set_trace()

# Python 3.7+
breakpoint()

# Comandos en pdb
n           # next (siguiente línea)
s           # step (entrar en función)
c           # continue (hasta siguiente breakpoint)
l           # list (ver código)
p variable  # print (ver variable)
q           # quit (salir)
```

---

## 📊 LINTING Y FORMATO

### Pylint
```bash
# Analizar archivo
pylint src/main.py

# Score objetivo
pylint src/main.py --fail-under=8.0

# Ignorar warnings específicos
pylint --disable=C0111,W0621 src/main.py

# Config en .pylintrc
```

### Black (formateador)
```bash
# Formatear archivo
black archivo.py

# Formatear carpeta
black src/

# Ver qué cambiaría sin aplicar
black --check src/

# Usar en proyecto
black .
```

### Autopep8
```bash
# Formatear archivo
autopep8 --in-place archivo.py

# Formatear agresivamente
autopep8 --in-place --aggressive archivo.py
```

---

## 📁 ESTRUCTURA DE PROYECTO

### Proyecto simple
mi-proyecto/
├── venv/
├── src/
│   ├── init.py
│   └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── README.md
└── requirements.txt

### Proyecto modular
mi-proyecto/
├── venv/
├── src/
│   ├── init.py
│   ├── main.py
│   ├── modulo1/
│   │   ├── init.py
│   │   └── archivo.py
│   └── modulo2/
│       ├── init.py
│       └── archivo.py
├── tests/
├── data/
├── docs/
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py

---

## 🔄 IMPORTS

### Imports básicos
```python
# Importar módulo
import modulo

# Importar con alias
import numpy as np

# Importar específico
from modulo import funcion

# Importar todo (NO recomendado)
from modulo import *

# Importar relativo (dentro de paquete)
from . import modulo
from .. import modulo_padre
from .submodulo import funcion
```

### Troubleshooting imports
```bash
# Ver sys.path
python -c "import sys; print('\n'.join(sys.path))"

# Agregar al PYTHONPATH temporalmente
export PYTHONPATH="${PYTHONPATH}:/ruta/a/proyecto"

# En código
import sys
sys.path.insert(0, '/ruta/a/proyecto')
```

---

## 🎯 BEST PRACTICES

### Antes de commit
```bash
# 1. Formatear código
black .

# 2. Linting
pylint src/

# 3. Tests
pytest

# 4. Ver cambios
git diff

# 5. Commit
git add .
git commit -m "tipo: descripción"
```

### Docstrings
```python
def funcion(param1, param2):
    """
    Descripción breve de la función.
    
    Args:
        param1 (tipo): Descripción
        param2 (tipo): Descripción
    
    Returns:
        tipo: Descripción del retorno
    
    Raises:
        ValueError: Cuando...
    
    Examples:
        >>> funcion(1, 2)
        3
    """
    pass
```

### Type hints
```python
def suma(a: int, b: int) -> int:
    """Suma dos números."""
    return a + b

from typing import List, Dict, Optional

def procesar(datos: List[str]) -> Dict[str, int]:
    """Procesa lista de strings."""
    return {"count": len(datos)}
```

---

## 🆘 TROUBLESHOOTING

### ModuleNotFoundError
```bash
# Verificar venv activo
which python

# Verificar paquete instalado
pip list | grep paquete

# Reinstalar
pip install --force-reinstall paquete
```

### Permission errors
```bash
# No usar sudo con pip
# Usar venv en lugar de instalación global

# Si es necesario
pip install --user paquete
```

### Conflictos de versiones
```bash
# Ver árbol de dependencias
pip show paquete

# Verificar requirements
pip check

# Recrear venv
deactivate
rm -rf venv/
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

---

## 💡 TIPS ÚTILES

### Crear alias útiles
```bash
# En ~/.bashrc
alias activate='source venv/Scripts/activate'
alias pytest='python -m pytest'
alias format='black . && autopep8 --in-place --recursive .'
```

### Script de setup
```bash
# setup.sh
#!/bin/bash
python -m venv venv
source venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Ejecutar sin activar venv
```bash
# Sin activar
./venv/Scripts/python script.py

# O
venv/Scripts/python -m módulo
```

---

**💾 Guarda este archivo en:** `04_recursos/03_python-workflow-cheatsheet.md`