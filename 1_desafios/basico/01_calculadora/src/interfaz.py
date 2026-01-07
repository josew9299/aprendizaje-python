"""
Módulo de interfaz de usuario para la calculadora.
Contiene todas las funciones de entrada/salida.
"""

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida y operaciones disponibles."""
    print("\n" + "=" * 50)
    print("Bienvenido a la calculadora de")
    print("operaciones matemáticas básicas")
    print("\nOperaciones disponibles:")
    print("  + : Suma")
    print("  - : Resta")
    print("  * : Multiplicación")
    print("  / : División")
    print("  **: Potencia")
    print("  0 : Salir")
    print("=" * 50)


def obtener_operacion():
    """Solicita y retorna la operación deseada."""
    while True:
        operacion = input("\nIngrese la operación (+, -, *, /, **) o '0' para salir: ").strip()
        
        # Validar operación
        if operacion in ["+", "-", "*", "/", "**", "0"]:
            return operacion
        elif operacion.lower() == "salir":
            return "0"
        else:
            print("❌ Operación no válida. Intente nuevamente.")


def obtener_numero(mensaje):
    """
    Solicita un número al usuario con validación.
    
    Args:
        mensaje: Texto a mostrar (ej: "Ingrese el primer número: ")
    
    Returns:
        float: Número validado
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("❌ Error: Debe ingresar un número válido.")


def mostrar_resultado(num1, operacion, num2, resultado):
    """Muestra el resultado formateado de la operación."""
    print("\n" + "=" * 50)
    print(f"   Resultado: {num1} {operacion} {num2} = {resultado}")
    print("=" * 50)


def mostrar_despedida():
    """Muestra mensaje de despedida."""
    print("\n👋 ¡Hasta luego! Gracias por usar la calculadora.")
