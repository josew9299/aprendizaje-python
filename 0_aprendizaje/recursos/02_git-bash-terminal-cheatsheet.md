# 🖥️ Git Bash Terminal Cheatsheet

## 📁 NAVEGACIÓN

### Comandos básicos
```bash
pwd                    # Print Working Directory (dónde estoy)
ls                     # Listar archivos
ls -la                 # Listar con detalles y archivos ocultos
ls -lh                 # Con tamaños legibles
cd ruta/carpeta        # Change Directory (ir a carpeta)
cd ..                  # Subir un nivel
cd ~                   # Ir a home
cd -                   # Volver a carpeta anterior
```

### Rutas
```bash
# Ruta absoluta (desde raíz)
cd /c/Users/remli/Documents/Python-Learning

# Ruta relativa (desde donde estás)
cd ../02_proyectos
cd ./src

# Atajos
~          # Home del usuario
.          # Directorio actual
..         # Directorio padre
-          # Directorio anterior
```

---

## 📝 CREAR Y ELIMINAR

### Crear
```bash
touch archivo.txt           # Crear archivo vacío
touch file1.txt file2.txt   # Crear múltiples

mkdir carpeta               # Crear carpeta
mkdir -p path/to/folder     # Crear con subcarpetas

mkdir {proyecto,tests,docs} # Crear varias carpetas
```

### Eliminar
```bash
rm archivo.txt              # Eliminar archivo
rm -r carpeta/              # Eliminar carpeta y contenido
rm -rf carpeta/             # Forzar eliminación (CUIDADO)
rm *.txt                    # Eliminar todos los .txt

rmdir carpeta/              # Eliminar carpeta vacía
```

---

## 📋 COPIAR Y MOVER
```bash
# Copiar
cp origen.txt destino.txt   # Copiar archivo
cp -r carpeta1/ carpeta2/   # Copiar carpeta

# Mover / Renombrar
mv viejo.txt nuevo.txt      # Renombrar
mv archivo.txt carpeta/     # Mover a carpeta
mv carpeta1/ carpeta2/      # Mover carpeta
```

---

## 👀 VER CONTENIDO
```bash
cat archivo.txt             # Ver contenido completo
cat file1.txt file2.txt     # Concatenar archivos

less archivo.txt            # Ver con paginación (q para salir)
head archivo.txt            # Primeras 10 líneas
head -n 20 archivo.txt      # Primeras 20 líneas
tail archivo.txt            # Últimas 10 líneas
tail -f logfile.txt         # Seguir archivo en tiempo real

wc archivo.txt              # Contar líneas, palabras, caracteres
wc -l archivo.txt           # Solo líneas
```

---

## 🔍 BUSCAR

### Buscar archivos
```bash
find . -name "*.py"         # Buscar archivos .py
find . -type f -name "test*" # Buscar archivos que empiecen con "test"
find . -type d -name "venv"  # Buscar carpetas llamadas "venv"
```

### Buscar en contenido
```bash
grep "palabra" archivo.txt  # Buscar palabra en archivo
grep -r "función" .         # Buscar recursivamente en carpeta
grep -i "error" log.txt     # Búsqueda case-insensitive
grep -n "def" *.py          # Mostrar números de línea
```

---

## 🔗 COMBINACIONES Y PIPES
```bash
# Redirigir salida a archivo
ls > lista.txt              # Sobrescribe
ls >> lista.txt             # Agrega al final

# Pipe (pasar salida como entrada)
ls -l | grep ".py"          # Filtrar salida
cat archivo.txt | wc -l     # Contar líneas
history | grep "git"        # Buscar en historial

# Encadenar comandos
cd proyecto && ls -la       # Si primero exitoso, ejecuta segundo
mkdir test || echo "Error"  # Si primero falla, ejecuta segundo
```

---

## 🎨 PERSONALIZACIÓN

### Prompt
```bash
# Ver prompt actual
echo $PS1

# Personalizar temporalmente
PS1='\u@\h:\w\$ '

# Colores en prompt (agregar a ~/.bashrc)
PS1='\[\e[32m\]\u@\h\[\e[0m\]:\[\e[34m\]\w\[\e[0m\]\$ '
```

### Alias
```bash
# Ver alias actuales
alias

# Crear alias temporal
alias ll='ls -la'
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'

# Hacer permanente (agregar a ~/.bashrc)
echo "alias ll='ls -la'" >> ~/.bashrc
source ~/.bashrc
```

---

## 🛠️ UTILIDADES

### Historial
```bash
history                     # Ver historial de comandos
history | grep "git"        # Buscar en historial
!123                        # Ejecutar comando #123 del historial
!!                          # Repetir último comando
!$                          # Último argumento del comando anterior
```

### Clear y navegación
```bash
clear                       # Limpiar pantalla (Ctrl+L)
Ctrl+C                      # Cancelar comando actual
Ctrl+D                      # Cerrar terminal
Ctrl+A                      # Ir al inicio de línea
Ctrl+E                      # Ir al final de línea
Ctrl+U                      # Borrar hasta inicio de línea
Ctrl+K                      # Borrar hasta final de línea
Ctrl+R                      # Buscar en historial (interactivo)
```

---

## 📦 PERMISOS (IMPORTANTE EN LINUX/MAC)
```bash
# Ver permisos
ls -l

# Cambiar permisos
chmod +x script.sh          # Hacer ejecutable
chmod 755 archivo           # rwxr-xr-x
chmod 644 archivo           # rw-r--r--

# Cambiar dueño
chown usuario:grupo archivo
```

---

## 🐍 PYTHON EN TERMINAL
```bash
# Ejecutar Python
python archivo.py
python3 archivo.py

# Python interactivo
python
python -i script.py         # Interactivo después de ejecutar

# Módulo como script
python -m módulo

# Pip
pip install paquete
pip install -r requirements.txt
pip list
pip freeze > requirements.txt
```

---

## 🌐 VIRTUAL ENVIRONMENTS
```bash
# Crear venv
python -m venv venv

# Activar (Git Bash en Windows)
source venv/Scripts/activate

# Activar (Linux/Mac)
source venv/bin/activate

# Desactivar
deactivate

# Verificar venv activo
which python
echo $VIRTUAL_ENV
```

---

## 📊 INFORMACIÓN DEL SISTEMA
```bash
# Ver info del sistema
uname -a                    # Sistema operativo
whoami                      # Usuario actual
hostname                    # Nombre del host
date                        # Fecha y hora

# Procesos
ps aux                      # Ver procesos
ps aux | grep python        # Filtrar procesos
kill PID                    # Terminar proceso
killall nombre              # Terminar todos los procesos con ese nombre

# Espacio en disco
df -h                       # Espacio en particiones
du -sh carpeta/             # Tamaño de carpeta
du -sh *                    # Tamaño de cada elemento
```

---

## 🔧 VARIABLES DE ENTORNO
```bash
# Ver variables
env                         # Todas las variables
echo $PATH                  # PATH
echo $HOME                  # Home directory
echo $SHELL                 # Shell actual

# Definir variable (temporal)
export MI_VAR="valor"
echo $MI_VAR

# Agregar al PATH
export PATH=$PATH:/nueva/ruta

# Hacer permanente (agregar a ~/.bashrc)
echo 'export PATH=$PATH:/nueva/ruta' >> ~/.bashrc
source ~/.bashrc
```

---

## 📝 ARCHIVOS DE CONFIGURACIÓN
```bash
# Archivos importantes
~/.bashrc                   # Configuración de Bash
~/.bash_profile             # Ejecutado al login
~/.gitconfig                # Configuración de Git

# Editar configuración
code ~/.bashrc
nano ~/.bashrc
vim ~/.bashrc

# Recargar configuración
source ~/.bashrc
```

---

## 🎯 ATAJOS DE TECLADO
```
Ctrl+C          Cancelar comando
Ctrl+D          EOF / Cerrar terminal
Ctrl+L          Limpiar pantalla
Ctrl+A          Inicio de línea
Ctrl+E          Final de línea
Ctrl+U          Borrar hasta inicio
Ctrl+K          Borrar hasta final
Ctrl+W          Borrar palabra anterior
Ctrl+R          Buscar en historial
Ctrl+Z          Suspender proceso (bg para continuar)
Tab             Autocompletar
Tab Tab         Mostrar opciones
↑/↓             Navegar historial
```

---

## 💡 TIPS ÚTILES

### Autocompletado
```bash
# Presiona Tab para autocompletar
cd Doc[Tab]                 # Se completa a Documents/
git che[Tab]                # Se completa a checkout

# Tab Tab para ver opciones
git ch[Tab][Tab]            # Muestra: checkout, cherry-pick, etc.
```

### Comodines (Wildcards)
```bash
*           # Cualquier cadena
?           # Un carácter
[abc]       # a, b, o c
[a-z]       # Cualquier letra minúscula
[0-9]       # Cualquier número

# Ejemplos
ls *.py                     # Todos los .py
ls test_*.py                # test_ seguido de cualquier cosa
ls file[123].txt            # file1.txt, file2.txt, file3.txt
rm temp*                    # Todos los que empiezan con temp
```

### Comandos útiles combinados
```bash
# Ver archivos Python ordenados por tamaño
ls -lhS *.py

# Buscar y contar
find . -name "*.py" | wc -l

# Crear backup
cp archivo.py archivo.py.bak

# Buscar y reemplazar en múltiples archivos
find . -name "*.py" -exec sed -i 's/viejo/nuevo/g' {} \;
```

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Terminal no responde
```bash
Ctrl+C          # Cancelar comando
Ctrl+Z          # Suspender
Ctrl+D          # Salir
```

### No encuentra comando
```bash
# Ver si está instalado
which python
which git

# Ver PATH
echo $PATH

# Agregar a PATH temporalmente
export PATH=$PATH:/ruta/a/programa
```

### Permisos denegados
```bash
# Ver permisos
ls -l archivo

# Dar permisos de ejecución
chmod +x script.sh

# Si es necesario sudo (Linux/Mac)
sudo comando
```

---

## 🔗 RECURSOS

- Bash Guide: https://mywiki.wooledge.org/BashGuide
- Explain Shell: https://explainshell.com/
- ShellCheck: https://www.shellcheck.net/
- Bash Scripting Tutorial: https://linuxconfig.org/bash-scripting-tutorial

---

**💾 Guarda este archivo en:** `04_recursos/02_git-bash-terminal-cheatsheet.md`# 🖥️ Git Bash Terminal Cheatsheet

## 📁 NAVEGACIÓN

### Comandos básicos
```bash
pwd                    # Print Working Directory (dónde estoy)
ls                     # Listar archivos
ls -la                 # Listar con detalles y archivos ocultos
ls -lh                 # Con tamaños legibles
cd ruta/carpeta        # Change Directory (ir a carpeta)
cd ..                  # Subir un nivel
cd ~                   # Ir a home
cd -                   # Volver a carpeta anterior
```

### Rutas
```bash
# Ruta absoluta (desde raíz)
cd /c/Users/remli/Documents/Python-Learning

# Ruta relativa (desde donde estás)
cd ../02_proyectos
cd ./src

# Atajos
~          # Home del usuario
.          # Directorio actual
..         # Directorio padre
-          # Directorio anterior
```

---

## 📝 CREAR Y ELIMINAR

### Crear
```bash
touch archivo.txt           # Crear archivo vacío
touch file1.txt file2.txt   # Crear múltiples

mkdir carpeta               # Crear carpeta
mkdir -p path/to/folder     # Crear con subcarpetas

mkdir {proyecto,tests,docs} # Crear varias carpetas
```

### Eliminar
```bash
rm archivo.txt              # Eliminar archivo
rm -r carpeta/              # Eliminar carpeta y contenido
rm -rf carpeta/             # Forzar eliminación (CUIDADO)
rm *.txt                    # Eliminar todos los .txt

rmdir carpeta/              # Eliminar carpeta vacía
```

---

## 📋 COPIAR Y MOVER
```bash
# Copiar
cp origen.txt destino.txt   # Copiar archivo
cp -r carpeta1/ carpeta2/   # Copiar carpeta

# Mover / Renombrar
mv viejo.txt nuevo.txt      # Renombrar
mv archivo.txt carpeta/     # Mover a carpeta
mv carpeta1/ carpeta2/      # Mover carpeta
```

---

## 👀 VER CONTENIDO
```bash
cat archivo.txt             # Ver contenido completo
cat file1.txt file2.txt     # Concatenar archivos

less archivo.txt            # Ver con paginación (q para salir)
head archivo.txt            # Primeras 10 líneas
head -n 20 archivo.txt      # Primeras 20 líneas
tail archivo.txt            # Últimas 10 líneas
tail -f logfile.txt         # Seguir archivo en tiempo real

wc archivo.txt              # Contar líneas, palabras, caracteres
wc -l archivo.txt           # Solo líneas
```

---

## 🔍 BUSCAR

### Buscar archivos
```bash
find . -name "*.py"         # Buscar archivos .py
find . -type f -name "test*" # Buscar archivos que empiecen con "test"
find . -type d -name "venv"  # Buscar carpetas llamadas "venv"
```

### Buscar en contenido
```bash
grep "palabra" archivo.txt  # Buscar palabra en archivo
grep -r "función" .         # Buscar recursivamente en carpeta
grep -i "error" log.txt     # Búsqueda case-insensitive
grep -n "def" *.py          # Mostrar números de línea
```

---

## 🔗 COMBINACIONES Y PIPES
```bash
# Redirigir salida a archivo
ls > lista.txt              # Sobrescribe
ls >> lista.txt             # Agrega al final

# Pipe (pasar salida como entrada)
ls -l | grep ".py"          # Filtrar salida
cat archivo.txt | wc -l     # Contar líneas
history | grep "git"        # Buscar en historial

# Encadenar comandos
cd proyecto && ls -la       # Si primero exitoso, ejecuta segundo
mkdir test || echo "Error"  # Si primero falla, ejecuta segundo
```

---

## 🎨 PERSONALIZACIÓN

### Prompt
```bash
# Ver prompt actual
echo $PS1

# Personalizar temporalmente
PS1='\u@\h:\w\$ '

# Colores en prompt (agregar a ~/.bashrc)
PS1='\[\e[32m\]\u@\h\[\e[0m\]:\[\e[34m\]\w\[\e[0m\]\$ '
```

### Alias
```bash
# Ver alias actuales
alias

# Crear alias temporal
alias ll='ls -la'
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'

# Hacer permanente (agregar a ~/.bashrc)
echo "alias ll='ls -la'" >> ~/.bashrc
source ~/.bashrc
```

---

## 🛠️ UTILIDADES

### Historial
```bash
history                     # Ver historial de comandos
history | grep "git"        # Buscar en historial
!123                        # Ejecutar comando #123 del historial
!!                          # Repetir último comando
!$                          # Último argumento del comando anterior
```

### Clear y navegación
```bash
clear                       # Limpiar pantalla (Ctrl+L)
Ctrl+C                      # Cancelar comando actual
Ctrl+D                      # Cerrar terminal
Ctrl+A                      # Ir al inicio de línea
Ctrl+E                      # Ir al final de línea
Ctrl+U                      # Borrar hasta inicio de línea
Ctrl+K                      # Borrar hasta final de línea
Ctrl+R                      # Buscar en historial (interactivo)
```

---

## 📦 PERMISOS (IMPORTANTE EN LINUX/MAC)
```bash
# Ver permisos
ls -l

# Cambiar permisos
chmod +x script.sh          # Hacer ejecutable
chmod 755 archivo           # rwxr-xr-x
chmod 644 archivo           # rw-r--r--

# Cambiar dueño
chown usuario:grupo archivo
```

---

## 🐍 PYTHON EN TERMINAL
```bash
# Ejecutar Python
python archivo.py
python3 archivo.py

# Python interactivo
python
python -i script.py         # Interactivo después de ejecutar

# Módulo como script
python -m módulo

# Pip
pip install paquete
pip install -r requirements.txt
pip list
pip freeze > requirements.txt
```

---

## 🌐 VIRTUAL ENVIRONMENTS
```bash
# Crear venv
python -m venv venv

# Activar (Git Bash en Windows)
source venv/Scripts/activate

# Activar (Linux/Mac)
source venv/bin/activate

# Desactivar
deactivate

# Verificar venv activo
which python
echo $VIRTUAL_ENV
```

---

## 📊 INFORMACIÓN DEL SISTEMA
```bash
# Ver info del sistema
uname -a                    # Sistema operativo
whoami                      # Usuario actual
hostname                    # Nombre del host
date                        # Fecha y hora

# Procesos
ps aux                      # Ver procesos
ps aux | grep python        # Filtrar procesos
kill PID                    # Terminar proceso
killall nombre              # Terminar todos los procesos con ese nombre

# Espacio en disco
df -h                       # Espacio en particiones
du -sh carpeta/             # Tamaño de carpeta
du -sh *                    # Tamaño de cada elemento
```

---

## 🔧 VARIABLES DE ENTORNO
```bash
# Ver variables
env                         # Todas las variables
echo $PATH                  # PATH
echo $HOME                  # Home directory
echo $SHELL                 # Shell actual

# Definir variable (temporal)
export MI_VAR="valor"
echo $MI_VAR

# Agregar al PATH
export PATH=$PATH:/nueva/ruta

# Hacer permanente (agregar a ~/.bashrc)
echo 'export PATH=$PATH:/nueva/ruta' >> ~/.bashrc
source ~/.bashrc
```

---

## 📝 ARCHIVOS DE CONFIGURACIÓN
```bash
# Archivos importantes
~/.bashrc                   # Configuración de Bash
~/.bash_profile             # Ejecutado al login
~/.gitconfig                # Configuración de Git

# Editar configuración
code ~/.bashrc
nano ~/.bashrc
vim ~/.bashrc

# Recargar configuración
source ~/.bashrc
```

---

## 🎯 ATAJOS DE TECLADO
```
Ctrl+C          Cancelar comando
Ctrl+D          EOF / Cerrar terminal
Ctrl+L          Limpiar pantalla
Ctrl+A          Inicio de línea
Ctrl+E          Final de línea
Ctrl+U          Borrar hasta inicio
Ctrl+K          Borrar hasta final
Ctrl+W          Borrar palabra anterior
Ctrl+R          Buscar en historial
Ctrl+Z          Suspender proceso (bg para continuar)
Tab             Autocompletar
Tab Tab         Mostrar opciones
↑/↓             Navegar historial
```

---

## 💡 TIPS ÚTILES

### Autocompletado
```bash
# Presiona Tab para autocompletar
cd Doc[Tab]                 # Se completa a Documents/
git che[Tab]                # Se completa a checkout

# Tab Tab para ver opciones
git ch[Tab][Tab]            # Muestra: checkout, cherry-pick, etc.
```

### Comodines (Wildcards)
```bash
*           # Cualquier cadena
?           # Un carácter
[abc]       # a, b, o c
[a-z]       # Cualquier letra minúscula
[0-9]       # Cualquier número

# Ejemplos
ls *.py                     # Todos los .py
ls test_*.py                # test_ seguido de cualquier cosa
ls file[123].txt            # file1.txt, file2.txt, file3.txt
rm temp*                    # Todos los que empiezan con temp
```

### Comandos útiles combinados
```bash
# Ver archivos Python ordenados por tamaño
ls -lhS *.py

# Buscar y contar
find . -name "*.py" | wc -l

# Crear backup
cp archivo.py archivo.py.bak

# Buscar y reemplazar en múltiples archivos
find . -name "*.py" -exec sed -i 's/viejo/nuevo/g' {} \;
```

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Terminal no responde
```bash
Ctrl+C          # Cancelar comando
Ctrl+Z          # Suspender
Ctrl+D          # Salir
```

### No encuentra comando
```bash
# Ver si está instalado
which python
which git

# Ver PATH
echo $PATH

# Agregar a PATH temporalmente
export PATH=$PATH:/ruta/a/programa
```

### Permisos denegados
```bash
# Ver permisos
ls -l archivo

# Dar permisos de ejecución
chmod +x script.sh

# Si es necesario sudo (Linux/Mac)
sudo comando
```

---

## 🔗 RECURSOS

- Bash Guide: https://mywiki.wooledge.org/BashGuide
- Explain Shell: https://explainshell.com/
- ShellCheck: https://www.shellcheck.net/
- Bash Scripting Tutorial: https://linuxconfig.org/bash-scripting-tutorial

---

**💾 Guarda este archivo en:** `04_recursos/02_git-bash-terminal-cheatsheet.md`