def mostrar_bienvenida():
    print("\n" + "="*50)
    print("       🎢 SISTEMA DE MONTAÑA RUSA 🎢")
    print("="*50)

def pedir_altura():
    while True:
        try:
            altura = float(input("\n📏 Altura en metros (ej: 1.50): ").replace(',', '.'))
            if altura > 0:
                return altura
            print("⚠️  La altura debe ser positiva")
        except:
            print("❌ Ingresa un número válido")

def pedir_si_o_no(pregunta):
    while True:
        respuesta = input(f"\n{pregunta} (s/n): ").lower()
        if respuesta in ['s', 'si', 'sí']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        print("❌ Responde 's' o 'n'")

def pedir_edad():
    while True:
        try:
            return int(input("\n🎂 Edad del acompañante: "))
        except:
            print("❌ Ingresa un número entero")

def mostrar_resultado(resultado):
    print("\n" + "═"*50)
    print("✅ Acceso permitido" if resultado[0] else "❌ Acceso denegado")
    print(resultado[1])
    print("═"*50)