def mostrar_bienevenida_1():
    print("\n" + "="*50)
    print("Bienvenido a la calculadora de\n operaciones matemáticas básicas\n Por favor elija una operación matemática \n1 +\n2 -\n3 *\n4 /\n5 **")
    print("="*50)
    
def pedir_primer_numero():
    while True:
        try:
            n1 = float(input("Ingresa el primer número: "))
            return n1
            
        except:
            print("❌ Ingresa un número: ")
            
def pedir_segundo_numero():
    while True:
        try:
            n2 = float(input("Ingresa el segundo número: "))
            return n2
        except Exception as e:
            print("❌ Ingresa un número+: ",{e})
            
#Módulo inicial funcionando correctamente

def operacion():
    """Solicita la operación a realizar."""
    print("\nOperaciones disponibles:")
    print("  + : Suma")
    print("  - : Resta")
    print("  * : Multiplicación")
    print("  / : División")
    print("  **: Potencia")
    print("  0 : Salir")
    
    oper = input("\nPor favor ingrese la operación a realizar: ").strip()
    return oper
