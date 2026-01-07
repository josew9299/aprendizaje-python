##!/usr/bin/env python3
"""
Punto de entrada alternativo para la calculadora.
Permite ejecutar desde la raíz del proyecto.
"""

import sys
import os

# Agregar directorio actual al path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Importar desde el paquete src
    from src.__main__ import ejecutar_calculadora
    
    if __name__ == "__main__":
        ejecutar_calculadora()
        
except KeyboardInterrupt:
    print("\n\n👋 Programa interrumpido por el usuario.")
    
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    print("Asegúrate de tener la estructura correcta:")
    print("  01_calculadora/")
    print("  ├── src/")
    print("  │   ├── __init__.py")
    print("  │   ├── main.py")
    print("  │   ├── interfaz.py")
    print("  │   └── logica.py")
    print("  └── ejecutar.py")
    
except Exception as e:
    print(f"\n❌ Error inesperado: {e}")
    import traceback
    traceback.print_exc()