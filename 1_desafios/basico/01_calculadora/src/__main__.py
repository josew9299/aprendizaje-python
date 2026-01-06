"""
Módulo principal de la calculadora
"""

from src import interfaz
from src import logica

def main():
    """Función principal de la calculadora."""
    # Mostrar bienvenida
    interfaz.mostrar_bienevenida_1()
    
    while True:
        print("\n" + "-"*50)
        
        # Pedir operación UNA SOLA VEZ
        operacion = interfaz.operacion()
        
        # Opción para salir (agregar esto a interfaz.operacion())
        if operacion == "0" or operacion.lower() == "salir":
            print("\n👋 ¡Hasta luego!")
            break
        # Pedir números y GUARDAR los valores
        n1 = interfaz.pedir_primer_numero()
        n2 = interfaz.pedir_segundo_numero()
        
        interfaz.pedir_segundo_numero()
        # Ejecutar operación y GUARDAR resultado
        resultado = None
        
        if operacion == "+":
            resultado = logica.sum_two(n1, n2)  # Nota: corrijo el nombre
        elif operacion == "-":
            resultado = logica.subs_two(n1, n2)
        elif operacion == "*":
            resultado = logica.multiply_two(n1, n2)
        elif operacion == "/":
            if n2 == 0:
                print("❌ Error: No se puede dividir por cero")
                continue
            resultado = logica.divide_two(n1, n2)  # Si tienes esta función
        elif operacion == "**":
            resultado = logica.power(n1, n2)
        else:
            print("❌ Operación no válida")
            continue
        
        # MOSTRAR el resultado al usuario
        if resultado is not None:
            print("\n" + "=" * 50)
            print(f"   Resultado: {n1} {operacion} {n2} = {resultado}")
            print("=" * 50)


if __name__ == "__main__":
    main()