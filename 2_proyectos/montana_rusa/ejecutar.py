#!/usr/bin/env python3
"""
Script para ejecutar el sistema de montaña rusa
"""
import sys
import os

# Añadir la carpeta src al path para poder importar
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Ejecutar el módulo principal
if __name__ == "__main__":
    try:
        # Esto ejecuta el módulo src como un script
        import runpy
        runpy.run_module('src', run_name='__main__')
    except ImportError as e:
        print(f"Error: {e}")
        print("\nAsegúrate de que tienes estos archivos en src/:")
        print("  - __init__.py (vacío)")
        print("  - __main__.py")
        print("  - logica.py")
        print("  - interfaz.py")