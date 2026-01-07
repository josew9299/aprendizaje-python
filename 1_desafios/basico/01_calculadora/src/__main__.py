"""
Módulo principal de la calculadora.
Solo contiene el flujo de control del programa.
"""

from src import interfaz
from src import logica


def ejecutar_calculadora():
    """Función principal que coordina el flujo de la calculadora."""
    interfaz.mostrar_bienvenida()
    
    while True:
        # Obtener operación
        operacion = interfaz.obtener_operacion()
        
        # Salir si el usuario elige '0'
        if operacion == "0":
            interfaz.mostrar_despedida()
            break
        
        # Obtener números
        num1 = interfaz.obtener_numero("Ingrese el primer número: ")
        num2 = interfaz.obtener_numero("Ingrese el segundo número: ")
        
        try:
            # Ejecutar cálculo
            resultado = logica.calcular(operacion, num1, num2)
            
            # Mostrar resultado
            interfaz.mostrar_resultado(num1, operacion, num2, resultado)
            
        except ZeroDivisionError as e:
            print(f"\n❌ Error matemático: {e}")
            print("   Por favor, intente con otros números.")
            
        except ValueError as e:
            print(f"\n❌ Error: {e}")
            
        except Exception as e:
            print(f"\n⚠️  Error inesperado: {e}")
            print("   Por favor, intente nuevamente.")


if __name__ == "__main__":
    ejecutar_calculadora()