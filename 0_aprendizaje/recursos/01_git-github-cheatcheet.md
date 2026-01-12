# 🔀 Git & GitHub Cheatsheet (Git Bash)

## 📦 CONFIGURACIÓN INICIAL

### Primera vez (solo una vez)
```bash
# Configurar identidad
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Editor predeterminado (VS Code)
git config --global core.editor "code --wait"

# Verificar configuración
git config --list
git config user.name
```

### Inicializar repositorio
```bash
# Crear repo en carpeta actual
git init

# Ver estado
git status
```

---

## 📊 WORKFLOW DIARIO

### 1. Ver cambios
```bash
git status                # Estado completo
git status -s             # Resumido (M=modificado, A=agregado, ??=sin seguimiento)
git diff                  # Diferencias no staged
git diff archivo.py       # Diferencias de archivo específico
git diff --staged         # Diferencias ya en staging
```

### 2. Agregar al staging
```bash
git add archivo.py        # Un archivo
git add .                 # Todos los cambios
git add *.py              # Todos los .py
git add src/              # Toda una carpeta
git add -p                # Interactivo (elige qué agregar)
```

### 3. Hacer commit
```bash
# Commit simple
git commit -m "Mensaje descriptivo"

# Commit con detalle
git commit -m "Título corto (max 50 chars)

- Detalle 1
- Detalle 2
- Detalle 3"

# Agregar y commit en un paso (solo archivos ya trackeados)
git commit -am "Mensaje"
```

### 4. Ver historial
```bash
git log                   # Completo
git log --oneline         # Compacto (RECOMENDADO)
git log -5                # Últimos 5
git log --oneline --graph --all  # Con gráfico
git log --since="2 weeks ago"    # Desde hace 2 semanas
git log --author="Tu Nombre"     # Por autor
```

---

## ⏮️ DESHACER CAMBIOS

### Antes de git add
```bash
# Descartar cambios en archivo
git restore archivo.py
git checkout -- archivo.py     # Forma antigua

# Descartar todos los cambios
git restore .
git checkout -- .              # Forma antigua
```

### Después de git add (quitar de staging)
```bash
# Quitar archivo de staging (mantiene cambios)
git restore --staged archivo.py
git reset HEAD archivo.py      # Forma antigua

# Quitar todo de staging
git restore --staged .
git reset HEAD .               # Forma antigua
```

### Modificar último commit
```bash
# Agregar archivo olvidado al último commit
git add archivo_olvidado.py
git commit --amend --no-edit

# Cambiar mensaje del último commit
git commit --amend -m "Nuevo mensaje"

# Abrir editor para modificar mensaje
git commit --amend
```

### Volver a commit anterior
```bash
# Ver últimos commits
git log --oneline

# Volver manteniendo cambios
git reset --soft HEAD~1

# Volver descartando cambios (PELIGROSO)
git reset --hard HEAD~1

# Volver a commit específico
git reset --soft abc1234
git reset --hard abc1234
```

---

## 🏷️ TAGS (VERSIONES)
```bash
# Crear tag simple
git tag v1.0.0

# Tag con mensaje (recomendado)
git tag -a v1.0.0 -m "Primera versión funcional"

# Tag en commit específico
git tag -a v0.9.0 abc1234 -m "Versión beta"

# Listar tags
git tag
git tag -l "v1.*"

# Ver info de tag
git show v1.0.0

# Eliminar tag
git tag -d v1.0.0

# Subir tags a remoto
git push origin v1.0.0
git push origin --tags
```

---

## 🌿 BRANCHES (RAMAS)

### Crear y cambiar
```bash
# Ver ramas
git branch                     # Locales
git branch -a                  # Todas (locales + remotas)
git branch -v                  # Con último commit

# Crear rama
git branch feature/nueva-funcionalidad

# Cambiar de rama
git checkout feature/nueva-funcionalidad
git switch feature/nueva-funcionalidad      # Forma moderna

# Crear y cambiar en un comando
git checkout -b feature/nueva-funcionalidad
git switch -c feature/nueva-funcionalidad   # Forma moderna
```

### Fusionar
```bash
# Ir a rama destino
git checkout main

# Fusionar
git merge feature/nueva-funcionalidad

# Fusionar sin fast-forward (crea commit de merge)
git merge --no-ff feature/nueva-funcionalidad

# Abortar merge si hay conflictos
git merge --abort
```

### Eliminar ramas
```bash
# Eliminar rama local (seguro)
git branch -d feature/nueva-funcionalidad

# Forzar eliminación
git branch -D feature/nueva-funcionalidad

# Eliminar rama remota
git push origin --delete feature/nueva-funcionalidad
```

---

## 🌐 GITHUB (REMOTO)

### Conectar con remoto
```bash
# Agregar remoto
git remote add origin https://github.com/usuario/repo.git

# Agregar con SSH (si configuraste SSH keys)
git remote add origin git@github.com:usuario/repo.git

# Ver remotos
git remote -v

# Cambiar URL
git remote set-url origin https://github.com/usuario/nuevo-repo.git

# Eliminar remoto
git remote remove origin
```

### Push (subir)
```bash
# Primera vez (establece upstream)
git push -u origin main

# Después
git push

# Rama específica
git push origin nombre-rama

# Todos los tags
git push origin --tags

# Forzar (PELIGROSO)
git push --force
git push --force-with-lease  # Más seguro
```

### Pull (bajar)
```bash
# Bajar y fusionar
git pull

# Bajar de rama específica
git pull origin main

# Solo bajar sin fusionar
git fetch

# Bajar todas las ramas
git fetch --all
```

### Clone (clonar)
```bash
# Clonar repo
git clone https://github.com/usuario/repo.git

# Clonar en carpeta específica
git clone https://github.com/usuario/repo.git mi-carpeta

# Clonar solo última versión (más rápido)
git clone --depth 1 https://github.com/usuario/repo.git
```

---

## 📝 .gitignore

### Crear .gitignore
```bash
# Crear archivo
touch .gitignore

# Editar en VS Code
code .gitignore
```

### Contenido para Python
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
dist/
*.egg-info/

# Virtual Environment
venv/
env/
ENV/
.venv/

# IDEs
.vscode/
.idea/
*.swp
*.swo
.DS_Store

# OS
Thumbs.db
desktop.ini

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Jupyter
.ipynb_checkpoints/
*.ipynb

# Data files (opcional)
*.csv
*.xlsx
*.json
!config.json

# Logs
*.log

# Environment variables
.env
.env.local
```

### Aplicar .gitignore a archivos ya trackeados
```bash
# Dejar de trackear archivo
git rm --cached archivo.py

# Dejar de trackear carpeta
git rm --cached -r carpeta/

# Commit
git commit -m "chore: Actualizar .gitignore"
```

---

## 🔍 BÚSQUEDA E INSPECCIÓN

### Buscar en historial
```bash
# Buscar en mensajes de commit
git log --grep="fix"
git log --grep="bug" --oneline

# Buscar cambios en código
git log -S"nombre_funcion"
git log -S"def calculate"

# Ver archivo en commit anterior
git show HEAD~1:archivo.py
git show abc1234:src/main.py

# Ver quién modificó cada línea
git blame archivo.py
git blame -L 10,20 archivo.py  # Solo líneas 10-20
```

### Inspeccionar commits
```bash
# Ver cambios de un commit
git show abc1234

# Ver archivos cambiados en commit
git show --name-only abc1234

# Ver estadísticas
git show --stat abc1234

# Comparar commits
git diff abc1234 def5678
git diff HEAD~2 HEAD
```

---

## 🆘 EMERGENCIAS Y RECUPERACIÓN

### Reflog (historial completo)
```bash
# Ver TODO el historial (incluye commits "perdidos")
git reflog

# Recuperar commit "perdido"
git checkout abc1234
git cherry-pick abc1234
```

### Conflictos de merge
```bash
# Ver archivos con conflicto
git status

# Ver diferencias del conflicto
git diff

# Aceptar cambios "nuestros"
git checkout --ours archivo.py

# Aceptar cambios "de ellos"
git checkout --theirs archivo.py

# Después de resolver manualmente
git add archivo.py
git commit

# Abortar merge
git merge --abort
```

### Stash (guardar temporalmente)
```bash
# Guardar cambios sin commit
git stash
git stash save "Descripción"

# Listar stashes
git stash list

# Ver contenido de stash
git stash show
git stash show -p  # Con diferencias

# Aplicar último stash
git stash pop      # Y elimina el stash
git stash apply    # Y mantiene el stash

# Aplicar stash específico
git stash apply stash@{2}

# Eliminar stash
git stash drop stash@{0}
git stash clear    # Eliminar todos
```

---

## 📊 TIPOS DE COMMIT (CONVENTIONAL COMMITS)
```bash
feat:      Nueva funcionalidad
fix:       Corrección de bug
docs:      Documentación
style:     Formato (sin cambio de lógica)
refactor:  Reestructuración de código
test:      Tests
chore:     Mantenimiento
perf:      Mejora de rendimiento
ci:        Integración continua
build:     Sistema de build

# Ejemplos:
git commit -m "feat: Agregar validación de entrada"
git commit -m "fix: Corregir división por cero"
git commit -m "docs: Actualizar README con ejemplos"
git commit -m "refactor: Separar lógica en módulos"
git commit -m "test: Agregar tests para calculadora"
```

---

## 🎯 ALIAS ÚTILES (ATAJOS)
```bash
# Configurar alias
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.lg 'log --oneline --graph --all'
git config --global alias.visual 'log --oneline --graph --decorate --all'

# Usar alias
git st
git lg
git visual
```

---

## 💡 TIPS Y TRUCOS

### Ver configuración
```bash
# Ver toda la configuración
git config --list

# Ver configuración específica
git config user.name
git config user.email

# Editar configuración global
code ~/.gitconfig
```

### Limpiar repo
```bash
# Ver archivos sin seguimiento
git clean -n

# Eliminar archivos sin seguimiento
git clean -f

# Eliminar archivos y carpetas
git clean -fd

# Incluir archivos ignorados
git clean -fdx
```

### Comparaciones útiles
```bash
# Ver cambios entre branches
git diff main feature/nueva

# Ver archivos diferentes entre branches
git diff --name-only main feature/nueva

# Ver cambios no commiteados
git diff HEAD

# Ver cambios entre staging y HEAD
git diff --staged HEAD
```

---

## ⚠️ COMANDOS PELIGROSOS
```bash
git reset --hard HEAD        # Pierde TODOS los cambios locales
git push --force            # Sobrescribe historial remoto
git clean -fdx              # Elimina TODO lo no trackeado
git branch -D rama          # Fuerza eliminación de rama
git rebase                  # Reescribe historial (avanzado)
```

---

## 🔗 RECURSOS

- Git Docs: https://git-scm.com/doc
- GitHub Docs: https://docs.github.com
- Git Visualizer: https://git-school.github.io/visualizing-git/
- Learn Git Branching: https://learngitbranching.js.org/
- Oh My Git! (juego): https://ohmygit.org/

---

## 🎯 WORKFLOW RECOMENDADO DIARIO
```bash
# 1. Ver estado
git status

# 2. Ver cambios específicos
git diff

# 3. Agregar cambios
git add .

# 4. Verificar staging
git status

# 5. Commit
git commit -m "tipo: descripción clara"

# 6. Ver últimos commits
git log --oneline -5

# 7. Subir (si usas GitHub)
git push
```

---

**💾 Guarda este archivo en:** `04_recursos/01_git-github-cheatsheet.md`