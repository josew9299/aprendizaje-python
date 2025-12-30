def verificar_acceso(altura, viene_acompañado=False, edad_acompañante=None):
    if altura > 1.40:
        return True, f"✅ Acceso permitido: mide {altura}m (>1.40m)"
    
    if not viene_acompañado:
        return False, f"❌ Acceso denegado: mide {altura}m (≤1.40m) y no viene acompañado"
    
    if edad_acompañante is None:
        return False, "❌ Acceso denegado: viene acompañado pero no se proporcionó la edad"
    
    if edad_acompañante >= 18:
        return True, f"✅ Acceso permitido: acompañado por adulto de {edad_acompañante} años"
    else:
        return False, f"❌ Acceso denegado: acompañante tiene {edad_acompañante} años (menor de 18)"