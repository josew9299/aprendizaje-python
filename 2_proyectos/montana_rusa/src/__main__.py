from . import logica
from . import interfaz

def main():
    interfaz.mostrar_bienvenida()
    
    while True:
        print("\n" + "-"*50)
        
        altura = interfaz.pedir_altura()
        viene_acompañado = interfaz.pedir_si_o_no("¿Vienes acompañado?")
        
        edad_acompañante = None
        if viene_acompañado:
            if interfaz.pedir_si_o_no("¿Ingresar edad del acompañante?"):
                edad_acompañante = interfaz.pedir_edad()
        
        resultado = logica.verificar_acceso(altura, viene_acompañado, edad_acompañante)
        interfaz.mostrar_resultado(resultado)
        
        if not interfaz.pedir_si_o_no("\n¿Verificar otra persona?"):
            print("\n👋 ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()