Hoy 20/06/2026 aprendí a ponerle decimales a los precios(valores)
Estudié el string formating
egg:
x = 25
print(x.2f)

Condicionales / Cuando dos variables llevan los mismos valores 
puedo crearlas con la sintaxis (x=y=z= "Hello) y todas quedarán con al mismo valor
Ahora, si necesito que dos variables tengan los mismos valores u opciones(En este caso, usuarios de un juego, personas)
Hago una variable y a la siguiente la pongo que es igual a la anterior
egg. 
p1= ["Pollo","carne", "Pescado", "Huevo"]
p2 = p1
print(p1,p2)


Función eval()
The eval() function in Python is a built-in function that evaluates a given string as a Python expression
 and returns the result. It allows for the dynamic execution of Python code at runtime.
Syntax:
Python

eval(expression, globals=None, locals=None)
expression: A string containing the Python expression to be evaluated.
globals (optional): A dictionary that specifies the global namespace for the evaluation. If omitted, the current global namespace is used.
locals (optional): A dictionary that specifies the local namespace for the evaluation. If omitted, the current local namespace is used.
How it works:
When eval() is called, it parses the expression string, compiles it into bytecode, and then evaluates
 it as a Python expression. The result of this evaluation is then returned.
Examples:
Python

# Evaluating a simple mathematical expression
result = eval("5 + 3 * 2")
print(result)  # Output: 11

# Evaluating an expression with variables
x = 10
y = 5
result = eval("x - y")
print(result)  # Output: 5
# Evaluating a simple mathematical expression
result = eval("5 + 3 * 2")
print(result)  # Output: 11

# Evaluating an expression with variables
x = 10
y = 5
result = eval("x - y")
print(result)  # Output: 5

# Evaluating an expression with custom globals and locals
my_globals = {'pi': 3.14159}
my_locals = {'radius': 2}
area = eval("pi * radius * radius", my_globals, my_locals)
print(area)  # Output: 12.56636


# Evaluating an expression with custom globals and locals
my_globals = {'pi': 3.14159}
my_locals = {'radius': 2}
area = eval("pi * radius * radius", my_globals, my_locals)
print(area)  # Output: 12.56636
Security Considerations:
While powerful, eval() should be used with caution, especially when dealing with untrusted user input.
Because it can execute arbitrary Python code, malicious input could lead to security vulnerabilities,
such as code injection or system compromise. It is crucial to carefully sanitize any input passed to 
eval() or, whenever possible, consider alternative approaches like exec() or the ast module for more
controlled code execution.

# Evaluating a simple mathematical expression
result = eval("5 + 3 * 2")
print(result)  # Output: 11

# Evaluating an expression with variables
x = 10
y = 5
result = eval("x - y")
print(result)  # Output: 5

# Evaluating an expression with custom globals and locals
my_globals = {'pi': 3.14159}
my_locals = {'radius': 2}
area = eval("pi * radius * radius", my_globals, my_locals)
print(area)  # Output: 12.56636

#String formating
name = "John"
age = 36
txt = "My name is " + name + "and I am "+ str(age) + "years old"
print(txt)
txt = f"My name is {name} and I am {age} years old"
print(txt)

#Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
