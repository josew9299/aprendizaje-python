# 🐍 Python Syntax Quick Reference

## 📊 TIPOS DE DATOS

### Números
````python
# Enteros
x = 10
y = -5

# Flotantes
pi = 3.14159
resultado = 2.5

# Operaciones
suma = 10 + 5          # 15
resta = 10 - 3         # 7
mult = 10 * 2          # 20
div = 10 / 3           # 3.333...
div_entera = 10 // 3   # 3
modulo = 10 % 3        # 1
potencia = 2 ** 3      # 8

# Conversiones
int("10")              # 10
float("3.14")          # 3.14
str(42)                # "42"
````

### Strings
````python
# Definir strings
texto = "Hola"
texto2 = 'Mundo'
multilinea = """
Varias
líneas
"""

# F-strings (Python 3.6+)
nombre = "Juan"
edad = 25
mensaje = f"Hola {nombre}, tienes {edad} años"
numero = f"{3.14159:.2f}"  # "3.14"

# Métodos útiles
texto.upper()          # "HOLA"
texto.lower()          # "hola"
texto.strip()          # Quitar espacios
texto.replace("a", "x")
texto.split(",")       # Lista de strings
"_".join(["a", "b"])   # "a_b"
texto.startswith("H")  # True/False
texto.endswith("a")    # True/False

# Indexing y slicing
texto[0]               # Primer carácter
texto[-1]              # Último carácter
texto[1:4]             # Del índice 1 al 3
texto[:3]              # Primeros 3
texto[2:]              # Desde índice 2 hasta el final
texto[::-1]            # Invertir string
````

### Booleanos
````python
verdadero = True
falso = False

# Operadores lógicos
and                    # Y lógico
or                     # O lógico
not                    # Negación

# Ejemplos
True and False         # False
True or False          # True
not True               # False

# Valores que evalúan a False
None, 0, 0.0, "", [], {}, ()
````

---

## 📦 ESTRUCTURAS DE DATOS

### Listas (mutables, ordenadas)
````python
# Crear
lista = [1, 2, 3, 4, 5]
vacia = []
mixta = [1, "hola", 3.14, True]

# Acceder
lista[0]               # Primer elemento
lista[-1]              # Último elemento
lista[1:3]             # Sublista [2, 3]

# Modificar
lista[0] = 10          # Cambiar elemento
lista.append(6)        # Agregar al final
lista.insert(0, 0)     # Insertar en posición
lista.extend([7, 8])   # Agregar múltiples
lista.remove(5)        # Eliminar valor
del lista[0]           # Eliminar por índice
valor = lista.pop()    # Quitar y retornar último
lista.clear()          # Vaciar lista

# Operaciones
len(lista)             # Longitud
5 in lista             # ¿Está el 5?
lista.count(3)         # Cuántos 3 hay
lista.index(4)         # Índice del 4
lista.sort()           # Ordenar en lugar
sorted(lista)          # Nueva lista ordenada
lista.reverse()        # Invertir en lugar

# List comprehension
cuadrados = [x**2 for x in range(10)]
pares = [x for x in range(10) if x % 2 == 0]
````

### Tuplas (inmutables, ordenadas)
````python
# Crear
tupla = (1, 2, 3)
simple = (1,)          # Tupla de un elemento
vacia = ()

# Acceder (igual que listas)
tupla[0]
tupla[1:3]

# No se pueden modificar
# tupla[0] = 10        # ERROR

# Desempaquetado
x, y, z = (1, 2, 3)
a, *resto = (1, 2, 3, 4)  # a=1, resto=[2,3,4]
````

### Diccionarios (clave-valor, mutables)
````python
# Crear
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}
vacio = {}

# Acceder
persona["nombre"]       # "Juan"
persona.get("edad")     # 25
persona.get("tel", None)  # None si no existe

# Modificar
persona["edad"] = 26    # Actualizar
persona["email"] = "..."  # Agregar nuevo
del persona["ciudad"]   # Eliminar
persona.pop("edad")     # Eliminar y retornar

# Operaciones
len(persona)            # Número de cl