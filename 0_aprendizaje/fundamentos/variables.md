import os
# Variables in python
#Variables are containers for storing date values.
X = 5
Y =  "John"
print(X)
print(Y)

print(f"{X} {Y}")

x = 4
X = "Sally"
print(x)
print(X)

x = str(3)
y = (3)
z = float(3)

x = 5
y = "John"
print(type(x))
print(type(y))
print(type(z))


#De esta manera se puede nombrar varias variables en una sola linea
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


#Así se puede asignar el mismo nombre a varias variables /
# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)


#Global variables can be used by everyone, both inside of functions and outside.
# Tis is a global variable
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

c1 = 2 + 3j
c2 = 1 - 2j
# Addition
result_add = c1 + c2  # (3-1j)
print(type(result_add))

# Subtraction
result_sub = c1 - c2  # (1+5j)

# Multiplication
result_mul = c1 * c2  # (8-1j)

# Division
result_div = c1 / c2  # (-0.8+1.4j)

#Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

numero = 35e3
print(int(numero))  # Output: 35000
print(type(int(numero)))#type int
print(type(numero))# Type float

numero = 35000
print(f"{numero:.0e}")  # Output: 4e+03 (notación automática)
# O específicamente:
print("35e3")  # Como string, si necesitas ese formato exacto.

print(35e3 == 35000)  # Output: True (son equivalentes).
print(type(35e3 == 35000))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

print(x)
print(y)
print(z)

txt = " Hello World " # Elimina espacios al principio y al final
x = txt.strip()
print(x)



nano = "3"

print(type(nano))
print(int(nano))
print(type(int(nano)))



print(os.environ.get('TEMP'))  # Imprime la ruta de tu carpeta Temp


