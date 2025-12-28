"""Verificar dependencias del proyecto"""

import os
from pathlib import Path
import re

def find_imports(directory="."):
    """Encuentra todos los imports en archivos .py"""
    imports = set()
    
    for py_file in Path(directory).rglob("*.py"):
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # import algo
                imports.update(re.findall(r'^\s*import\s+(\w+)', content, re.MULTILINE))
                
                # from algo import ...
                imports.update(re.findall(r'^\s*from\s+(\w+)', content, re.MULTILINE))
        except:
            pass
    
    return imports

# Librerías estándar de Python
stdlib = {
    'os', 'sys', 're', 'json', 'time', 'datetime', 'random', 'math',
    'collections', 'itertools', 'functools', 'pathlib', 'typing',
    'unittest', 'csv', 'pickle', 'copy', 'enum', 'asyncio'
}

print("=" * 60)
print("ANÁLISIS DE DEPENDENCIAS")
print("=" * 60)

imports = find_imports()
external = imports - stdlib

print(f"\nTotal imports encontrados: {len(imports)}")
print(f"Librerías estándar: {len(imports - external)}")
print(f"Librerías externas: {len(external)}")

if external:
    print("\n" + "=" * 60)
    print("LIBRERÍAS EXTERNAS NECESARIAS:")
    print("=" * 60)
    for lib in sorted(external):
        print(f"  • {lib}")
    
    print("\nPara instalar:")
    print(f"pip install {' '.join(sorted(external))}")
else:
    print("\n✅ No necesita librerías externas!")
    print("Solo usa librerías estándar de Python.")

print("=" * 60)