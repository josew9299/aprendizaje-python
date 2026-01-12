# 🌐 Virtual Environments Cheatsheet

## 🎯 ¿QUÉ ES Y POR QUÉ USARLO?

### ¿Qué es un virtual environment?
Un entorno virtual aislado donde instalar paquetes de Python sin afectar el sistema global.

### ¿Por qué usar venv?
````
✅ Aislamiento de proyectos
✅ Diferentes versiones de paquetes por proyecto
✅ No contaminas el Python del sistema
✅ Fácil de recrear y compartir (requirements.txt)
✅ No necesitas sudo/administrador
````

### Sin venv vs Con venv
````
❌ Sin venv:
python install tensorflow
# ¡Instala globalmente! Afecta TODOS los proyectos

✅ Con venv:
source venv/Scripts/activate
pip install tensorflow
# Solo en este proyecto
````

---

## 🚀 CREAR VIRTUAL ENVIRONMENT

### Método estándar (venv)
````bash
# Crear venv llamado "venv"
python -m venv venv

# Crear con nombre diferente
python -m venv mi_entorno

# Con Python específico
python3.12 -m venv venv
/usr/bin/python3.12 -m venv venv
````

### Dónde crear
````bash
# EN LA CARPETA DEL PROYECTO (recomendado)
cd ~/Documents/Python-Learning/02_proyectos/mi-proyecto
python -m venv venv

# Estructura resultante:
mi-proyecto/
├── venv/              ← Virtual environment
├── src/
└── requirements.txt
````

---

## ⚡ ACTIVAR Y DESACTIVAR

### Activar (Git Bash / Linux / Mac)
````bash
# Git Bash en Windows
source venv/Scripts/activate

# Linux / Mac
source venv/bin/activate

# Verificar activación
which python           # Debe mostrar ruta con venv
echo $VIRTUAL_ENV      # Debe mostrar ruta del venv
python --version       # Ver versión de Python
````

### Activar (Windows CMD)
````cmd
venv\Scripts\activate.bat
````

### Activar (Windows PowerShell)
````powershell
venv\Scripts\Activate.ps1

# Si da error de permisos
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
````

### Desactivar
````bash
deactivate            # Funciona en todos los sistemas
````

### Verificar si está activo
````bash
# Método 1: Prompt
(venv) $             # Debe aparecer (venv) al inicio

# Método 2: Which python
which python         # Debe mostrar ruta con venv

# Método 3: Variable de entorno
echo $VIRTUAL_ENV    # Debe mostrar ruta del venv

# Método 4: Python
python -c "import sys; print(sys.prefix)"
````

---

## 📦 GESTIÓN DE PAQUETES EN VENV

### Instalar paquetes
````bash
# SIEMPRE con venv activado
source venv/Scripts/activate

# Instalar paquete
pip install paquete

# Instalar múltiples
pip install paquete1 paquete2 paquete3

# Versión específica
pip install paquete==1.2.3
pip install 'paquete>=1.0,<2.0'

# Desde requirements.txt
pip install -r requirements.txt
````

### Ver paquetes instalados
````bash
# Listar todos
pip list

# Solo los no dependencias
pip list --not-required

# Buscar paquete específico
pip list | grep numpy

# Ver info de paquete
pip show paquete
````

### Desinstalar
````bash
pip uninstall paquete

# Sin confirmación
pip uninstall -y paquete

# Desinstalar todos (CUIDADO)
pip freeze | xargs pip uninstall -y
````

---

## 📋 REQUIREMENTS.TXT

### Crear requirements.txt
````bash
# Con venv activado
pip freeze > requirements.txt

# Ver contenido
cat requirements.txt
# numpy==1.24.3
# pandas==2.0.3
# requests==2.31.0
````

### Instalar desde requirements.txt
````bash
# Crear venv nuevo
python -m venv venv
source venv/Scripts/activate

# Instalar todo
pip install -r requirements.txt
````

### Requirements.txt con comentarios
````txt
# Análisis de datos
numpy==1.24.3
pandas==2.0.3

# Web scraping
requests==2.31.0
beautifulsoup4==4.12.2

# Testing
pytest==7.4.3
````

### Requirements.txt sin versiones exactas
````txt
# Permite versiones más nuevas
numpy>=1.24
pandas>=2.0
requests
````

---

## 🔧 TROUBLESHOOTING

### Venv no se activa
````bash
# Verificar que existe
ls venv/Scripts/activate

# Recrear venv
rm -rf venv/
python -m venv venv
source venv/Scripts/activate
````

### Python no es del venv
````bash
# Verificar
which python

# Si no muestra venv, desactivar y reactivar
deactivate
source venv/Scripts/activate

# Verificar de nuevo
which python
````

### VS Code no detecta venv
````bash
# Recargar ventana
Ctrl+Shift+P → "Reload Window"

# Seleccionar intérprete manualmente
Ctrl+Shift+P → "Python: Select Interpreter"
# Seleccionar el que dice "venv"
````

### Pip instala en ubicación incorrecta
````bash
# Verificar pip
which pip            # Debe estar en venv
pip --version        # Debe mostrar ruta con venv

# Si no, usar módulo
python -m pip install paquete
````

### Error: pip no encontrado
````bash
# Reinstalar pip en venv
python -m ensurepip --upgrade
python -m pip install --upgrade pip
````

---

## 🎯 MEJORES PRÁCTICAS

### 1. Un venv por proyecto
````bash
proyecto1/
├── venv/           # Su propio venv
├── src/
└── requirements.txt

proyecto2/
├── venv/           # Otro venv independiente
├── src/
└── requirements.txt
````

### 2. Nombrar venv
````bash
# Estándar (recomendado)
venv/

# Alternativas aceptables
.venv/              # Oculto (bueno para no clutter)
env/
virtualenv/
````

### 3. Ignorar en Git
````bash
# .gitignore
venv/
env/
.venv/
ENV/
````

### 4. Documentar en README
````markdown
## Setup
```bash
# Crear virtual environment
python -m venv venv

# Activar
source venv/Scripts/activate  # Git Bash/Linux/Mac
venv\Scripts\activate.bat      # Windows CMD

# Instalar dependencias
pip install -r requirements.txt
```
````

### 5. Actualizar requirements.txt regularmente
````bash
# Después de instalar algo nuevo
pip install nueva-librería
pip freeze > requirements.txt
git add requirements.txt
git commit -m "chore: Actualizar dependencias"
````

---

## 🔄 WORKFLOW DIARIO

### Inicio de sesión
````bash
# 1. Navegar al proyecto
cd ~/Documents/Python-Learning/02_proyectos/mi-proyecto

# 2. Activar venv
source venv/Scripts/activate

# 3. Verificar activación
which python

# 4. Abrir VS Code
code .
````

### Durante trabajo
````bash
# Instalar algo nuevo
pip install nueva-librería

# Actualizar requirements
pip freeze > requirements.txt
````

### Fin de sesión
````bash
# Desactivar venv
deactivate
````

---

## 🆕 PROYECTO NUEVO - CHECKLIST
````bash
# 1. Crear carpeta
mkdir mi-nuevo-proyecto
cd mi-nuevo-proyecto

# 2. Crear venv
python -m venv venv

# 3. Activar
source venv/Scripts/activate

# 4. Actualizar pip
python -m pip install --upgrade pip

# 5. Instalar herramientas base
pip install pylint autopep8 pytest

# 6. Guardar dependencias
pip freeze > requirements.txt

# 7. Crear .gitignore
echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore

# 8. Inicializar Git
git init
git add .
git commit -m "chore: Inicializar proyecto"
````

---

## 🔄 CLONAR PROYECTO EXISTENTE
````bash
# 1. Clonar repo
git clone https://github.com/usuario/proyecto.git
cd proyecto

# 2. Crear venv
python -m venv venv

# 3. Activar
source venv/Scripts/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Verificar
pip list
````

---

## 🧹 LIMPIEZA Y MANTENIMIENTO

### Recrear venv desde cero
````bash
# 1. Desactivar si está activo
deactivate

# 2. Guardar dependencias (si no tienes requirements.txt)
# (activar temporalmente)
source venv/Scripts/activate
pip freeze > requirements.txt
deactivate

# 3. Eliminar venv viejo
rm -rf venv/

# 4. Crear venv nuevo
python -m venv venv

# 5. Activar
source venv/Scripts/activate

# 6. Reinstalar todo
pip install --upgrade pip
pip install -r requirements.txt
````

### Limpiar caché de pip
````bash
pip cache purge
````

### Verificar integridad
````bash
# Ver dependencias rotas
pip check

# Ver paquetes obsoletos
pip list --outdated
````

---

## 💡 TIPS AVANZADOS

### Activación automática con direnv
````bash
# Instalar direnv (opcional)
# En .envrc del proyecto:
source venv/Scripts/activate

# Ahora se activa automáticamente al entrar a la carpeta
````

### Alias útiles
````bash
# En ~/.bashrc o ~/.bash_profile
alias va='source venv/Scripts/activate'
alias vd='deactivate'
alias vr='pip freeze > requirements.txt'
````

### Script de setup
````bash
# setup.sh
#!/bin/bash
python -m venv venv
source venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Virtual environment configurado"
````

---

## 📊 COMPARACIÓN DE HERRAMIENTAS

### venv (estándar)
````
✅ Incluido en Python 3.3+
✅ No necesita instalación
✅ Simple y directo
❌ Solo Python
````

### virtualenv (alternativa)
````
✅ Más features
✅ Compatible Python 2 y 3
❌ Requiere instalación
````

### conda (para data science)
````
✅ Gestiona Python + librerías no-Python
✅ Popular en data science
❌ Pesado
❌ Requiere instalación de Anaconda/Miniconda
````

### poetry (moderno)
````
✅ Gestión de dependencias avanzada
✅ Lock files automáticos
❌ Curva de aprendizaje
❌ Requiere instalación
````

**Recomendación: Usa `venv` para empezar. Es suficiente para 99% de casos.**

---

## 🔗 RECURSOS

- Documentación oficial: https://docs.python.org/3/library/venv.html
- Real Python Guide: https://realpython.com/python-virtual-environments-a-primer/
- Python Packaging Guide: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

---

**💾 Guarda este archivo en:** `04_recursos/05_virtual-env-cheatsheet.md`