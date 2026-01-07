"""
Módulo de lógica matemática para la calculadora.
Contiene todas las operaciones y validaciones matemáticas.
"""


def sumar(a, b):
    """Retorna la suma de dos números."""
    return a + b


def restar(a, b):
    """Retorna la resta de dos números (a - b)."""
    return a - b


def multiplicar(a, b):
    """Retorna el producto de dos números."""
    return a * b


def dividir(a, b):
    """
    Retorna la división de a entre b.
    
    Raises:
        ZeroDivisionError: Si b es 0
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


def potenciar(base, exponente):
    """Retorna la base elevada al exponente."""
    return base ** exponente


def calcular(operacion, num1, num2):
    """
    Ejecuta la operación solicitada con validación completa.
    
    Args:
        operacion: Símbolo de la operación (+, -, *, /, **)
        num1: Primer operando
        num2: Segundo operando
    
    Returns:
        float: Resultado de la operación
    
    Raises:
        ValueError: Si la operación no es válida
        ZeroDivisionError: En división entre cero
    """
    if operacion == "+":
        return sumar(num1, num2)
    elif operacion == "-":
        return restar(num1, num2)
    elif operacion == "*":
        return multiplicar(num1, num2)
    elif operacion == "/":
        return dividir(num1, num2)
    elif operacion == "**":
        return potenciar(num1, num2)
    else:
        raise ValueError(f"Operación no válida: {operacion}")