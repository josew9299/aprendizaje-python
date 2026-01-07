#!/usr/bin/env python3
"""
Script para ejecutar el sistema de calculadora
"""

import sys
import os

# Importar y ejecutar directamente
from src.__main__ import main

# Agregar la carpeta raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido. ¡Hasta luego!")
    except TypeError as e:
        print(f"\n❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()