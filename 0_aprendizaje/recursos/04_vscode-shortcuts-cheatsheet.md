# ⌨️ VS Code Shortcuts Cheatsheet

## 🎯 ATAJOS ESENCIALES (LOS MÁS USADOS)

### Navegación básica
````
Ctrl+P              Abrir archivo rápidamente (Quick Open)
Ctrl+Shift+P        Command Palette (paleta de comandos)
Ctrl+B              Toggle sidebar (mostrar/ocultar barra lateral)
Ctrl+`              Toggle terminal integrada
Ctrl+Shift+E        Explorador de archivos
Ctrl+Shift+F        Buscar en todos los archivos
Ctrl+Shift+G        Control de Git
Ctrl+Shift+X        Extensiones
````

### Edición rápida
````
Ctrl+S              Guardar
Ctrl+Shift+S        Guardar como
Ctrl+N              Nuevo archivo
Ctrl+W              Cerrar archivo actual
Ctrl+Shift+T        Reabrir archivo cerrado
Ctrl+Tab            Cambiar entre archivos abiertos
````

---

## 📝 EDICIÓN DE CÓDIGO

### Selección
````
Ctrl+A              Seleccionar todo
Ctrl+L              Seleccionar línea completa
Ctrl+D              Seleccionar siguiente ocurrencia
Ctrl+Shift+L        Seleccionar todas las ocurrencias
Alt+Click           Multi-cursor (múltiples cursores)
Ctrl+Alt+↑/↓        Multi-cursor arriba/abajo
Shift+Alt+↑/↓       Duplicar línea arriba/abajo
````

### Mover y modificar
````
Alt+↑/↓             Mover línea arriba/abajo
Ctrl+Shift+K        Eliminar línea
Ctrl+Enter          Insertar línea abajo
Ctrl+Shift+Enter    Insertar línea arriba
Ctrl+]              Indentar
Ctrl+[              Des-indentar
Ctrl+/              Comentar/descomentar línea
Shift+Alt+A         Comentar/descomentar bloque
````

### Copiar y pegar
````
Ctrl+C              Copiar (o copiar línea si no hay selección)
Ctrl+X              Cortar (o cortar línea si no hay selección)
Ctrl+V              Pegar
Ctrl+Shift+V        Pegar y coincidir formato
Ctrl+Z              Deshacer
Ctrl+Y              Rehacer
Ctrl+Shift+Z        Rehacer (alternativa)
````

---

## 🔍 BÚSQUEDA Y REEMPLAZO

### Buscar
````
Ctrl+F              Buscar en archivo actual
Ctrl+H              Buscar y reemplazar en archivo
Ctrl+Shift+F        Buscar en todos los archivos
Ctrl+Shift+H        Reemplazar en todos los archivos
F3                  Ir a siguiente resultado
Shift+F3            Ir a resultado anterior
Alt+Enter           Seleccionar todas las ocurrencias
````

### Navegación en archivo
````
Ctrl+G              Ir a línea
Ctrl+Shift+O        Ir a símbolo (funciones, clases)
Ctrl+T              Ir a símbolo en workspace
F12                 Ir a definición
Alt+F12             Peek definition (ver sin ir)
Shift+F12           Ver todas las referencias
Ctrl+K Ctrl+I       Mostrar información hover
````

---

## 🐍 PYTHON ESPECÍFICO

### Ejecución
````
Ctrl+F5             Ejecutar sin debugging
F5                  Ejecutar con debugging
Shift+Enter         Ejecutar línea/selección en terminal
Ctrl+Shift+P        "Python: Select Interpreter"
Ctrl+Shift+P        "Python: Run Python File in Terminal"
````

### Debugging
````
F9                  Toggle breakpoint
F5                  Continuar/Iniciar debug
F10                 Step over (siguiente línea)
F11                 Step into (entrar en función)
Shift+F11           Step out (salir de función)
Shift+F5            Detener debugging
Ctrl+K Ctrl+I       Mostrar valor de variable (hover)
````

---

## 📂 EXPLORADOR DE ARCHIVOS

### En el explorador
````
Ctrl+Shift+E        Abrir explorador
Ctrl+N              Nuevo archivo
Ctrl+K Ctrl+N       Nuevo archivo en carpeta actual
Ctrl+Shift+N        Nueva ventana
F2                  Renombrar archivo
Delete              Eliminar archivo
Ctrl+C              Copiar archivo
Ctrl+V              Pegar archivo
````

### Navegación entre archivos
````
Ctrl+Tab            Lista de archivos abiertos
Ctrl+1/2/3          Ir a grupo de editor 1/2/3
Ctrl+\              Dividir editor
Ctrl+K Ctrl+←/→     Mover a grupo de editor anterior/siguiente
````

---

## 💻 TERMINAL INTEGRADA
````
Ctrl+`              Toggle terminal
Ctrl+Shift+`        Nueva terminal
Ctrl+Shift+5        Dividir terminal
Ctrl+Shift+C        Copiar (en terminal)
Ctrl+Shift+V        Pegar (en terminal)
Ctrl+↑/↓            Scroll terminal
Ctrl+Home/End       Scroll al inicio/fin
Ctrl+K              Limpiar terminal
````

---

## 🎨 VISTA Y DISEÑO

### Layout
````
Ctrl+B              Toggle sidebar
Ctrl+Shift+E        Explorador
Ctrl+Shift+F        Búsqueda
Ctrl+Shift+G        Git
Ctrl+Shift+D        Debug
Ctrl+Shift+X        Extensiones
F11                 Toggle pantalla completa
Ctrl+K Z            Modo Zen (sin distracciones)
Escape Escape       Salir de modo Zen
````

### Zoom
````
Ctrl++              Zoom in
Ctrl+-              Zoom out
Ctrl+0              Reset zoom
````

---

## 🔧 REFACTORING Y CÓDIGO

### Refactoring
````
F2                  Renombrar símbolo
Ctrl+.              Quick fix (soluciones rápidas)
Shift+Alt+F         Formatear documento
Ctrl+K Ctrl+F       Formatear selección
Ctrl+Shift+I        Formatear documento (alternativa)
````

### IntelliSense
````
Ctrl+Space          Trigger IntelliSense
Ctrl+Shift+Space    Trigger Parameter Hints
Ctrl+K Ctrl+I       Trigger Hover
Alt+Click           Insertar cursor adicional
````

---

## 📋 MÚLTIPLES CURSORES
````
Alt+Click           Agregar cursor en posición
Ctrl+Alt+↑/↓        Agregar cursor arriba/abajo
Ctrl+D              Seleccionar siguiente ocurrencia
Ctrl+Shift+L        Seleccionar todas las ocurrencias
Ctrl+U              Deshacer última selección de cursor
Escape              Cancelar múltiples cursores
````

### Ejemplo de uso:
````python
# Selecciona "variable" con Ctrl+D varias veces
variable = 1
print(variable)
result = variable * 2
# Ahora edita todas a la vez con múltiples cursores
````

---

## 🔀 GIT EN VS CODE
````
Ctrl+Shift+G        Abrir panel de Git
Ctrl+Enter          Commit (en mensaje de commit)
Ctrl+K Ctrl+P       Git: Push
Ctrl+Shift+P        "Git: Pull"
Ctrl+Shift+P        "Git: Checkout to..."
Ctrl+Shift+P        "Git: Create Branch"
````

### En diff view
````
F7                  Siguiente cambio
Shift+F7            Cambio anterior
Ctrl+Shift+P        "Git: Stage Changes"
Ctrl+Shift+P        "Git: Unstage Changes"
````

---

## 🎯 COMMAND PALETTE (MÁS USADOS)
````
Ctrl+Shift+P → Escribir...

"reload"            Developer: Reload Window
"format"            Format Document
"python select"     Python: Select Interpreter
"python run"        Python: Run Python File
"settings"          Preferences: Open Settings
"keyboard"          Preferences: Open Keyboard Shortcuts
"theme"             Preferences: Color Theme
"wrap"              Toggle Word Wrap
"sort"              Sort Lines Ascending
````

---

## ⚡ SNIPPETS Y EMMET

### Python snippets (escribir y Tab)
````
def                 Crear función
class               Crear clase
for                 For loop
if                  If statement
try                 Try/except
with                With statement
````

### Crear snippet personalizado
````
Ctrl+Shift+P → "Snippets: Configure User Snippets"
````

---

## 🎨 PERSONALIZACIÓN

### Abrir archivos de configuración
````
Ctrl+Shift+P → "settings json"      Settings JSON
Ctrl+Shift+P → "keyboard"           Keyboard Shortcuts
Ctrl+,                               Settings UI
````

### Settings JSON útiles
````json
{
  "editor.formatOnSave": true,
  "editor.fontSize": 14,
  "editor.tabSize": 4,
  "files.autoSave": "afterDelay",
  "python.linting.enabled": true,
  "workbench.colorTheme": "One Dark Pro Darker"
}
````

---

## 🔌 EXTENSIONES ÚTILES

### Python Development
````
Python (Microsoft)
Pylance
Python Indent
autoDocstring
Python Test Explorer
````

### Utilidades
````
Better Comments
Bracket Pair Colorizer
Path Intellisense
GitLens
indent-rainbow
Error Lens
````

### Temas
````
One Dark Pro
Dracula Official
Night Owl
Material Icon Theme
````

---

## 💡 TIPS Y TRUCOS

### Quick Open (Ctrl+P)
````
Ctrl+P              Abrir archivo
Ctrl+P >            Command Palette (= Ctrl+Shift+P)
Ctrl+P :            Ir a línea (= Ctrl+G)
Ctrl+P @            Ir a símbolo (= Ctrl+Shift+O)
Ctrl+P #            Buscar símbolo en workspace
````

### Splits y grupos
````
Ctrl+\              Dividir editor
Ctrl+1/2/3          Ir a grupo 1/2/3
Ctrl+W              Cerrar editor
Ctrl+K W            Cerrar todos los editores
Ctrl+K Ctrl+W       Cerrar grupo de editores
````

### Markdown preview
````
Ctrl+Shift+V        Preview Markdown
Ctrl+K V            Preview lado a lado
````

---

## 🎯 WORKFLOW RECOMENDADO

### Inicio de sesión
````
1. Ctrl+Shift+E     Abrir explorador
2. Ctrl+P           Quick open al archivo
3. Ctrl+`           Abrir terminal
4. Ctrl+Shift+P     "Python: Select Interpreter"
````

### Durante codeo
````
1. Ctrl+Space       IntelliSense
2. Ctrl+.           Quick fixes
3. Ctrl+D           Seleccionar ocurrencias
4. Alt+↑/↓          Mover líneas
5. Ctrl+/           Comentar
6. Shift+Alt+F      Formatear
7. Ctrl+S           Guardar
````

### Debugging
````
1. F9               Breakpoints
2. F5               Start debugging
3. F10              Step over
4. F11              Step into
5. Shift+F5         Stop
````

---

## 🆘 TROUBLESHOOTING

### IntelliSense no funciona
````
Ctrl+Shift+P → "Python: Select Interpreter"
Verificar que venv está seleccionado
Reload window: Ctrl+Shift+P → "reload"
````

### Terminal no activa venv
````
Ctrl+Shift+P → "Terminal: Select Default Profile"
Seleccionar "Git Bash" o "Command Prompt"
````

### Shortcuts no funcionan
````
Ctrl+K Ctrl+S       Abrir keyboard shortcuts
Buscar el comando y verificar conflictos
````

---

## 🔗 RECURSOS

- Keyboard Shortcuts PDF: `Help → Keyboard Shortcut Reference`
- Documentación: https://code.visualstudio.com/docs
- Tips & Tricks: https://code.visualstudio.com/docs/getstarted/tips-and-tricks
- Keyboard Shortcuts Editor: `Ctrl+K Ctrl+S`

---

## 📋 CHEATSHEET RÁPIDA

**Los 20 más usados:**
````
Ctrl+P              Quick Open
Ctrl+Shift+P        Command Palette
Ctrl+S              Guardar
Ctrl+`              Terminal
Ctrl+B              Toggle Sidebar
Ctrl+D              Seleccionar siguiente
Alt+↑/↓             Mover línea
Ctrl+/              Comentar
Shift+Alt+F         Formatear
Ctrl+F              Buscar
Ctrl+H              Reemplazar
F12                 Ir a definición
Ctrl+Space          IntelliSense
Ctrl+.              Quick Fix
F5                  Debug
F9                  Breakpoint
Ctrl+Tab            Cambiar archivo
Ctrl+\              Dividir editor
Ctrl+G              Ir a línea
Ctrl+Shift+E        Explorador
````

---

**💾 Guarda este archivo en:** `04_recursos/04_vscode-shortcuts-cheatsheet.md`