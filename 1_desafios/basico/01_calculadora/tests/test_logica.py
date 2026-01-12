"""
Tests unitarios para el módulo logica.py
"""
import pytest
from src import logica


class TestOperacionesBasicas:
    """Tests para las operaciones matemáticas básicas."""
    
    def test_sumar(self):
        """Test de suma con diferentes casos."""
        assert logica.sumar(2, 3) == 5
        assert logica.sumar(-1, 1) == 0
        assert logica.sumar(0, 0) == 0
        assert logica.sumar(2.5, 3.5) == 6.0
    
    def test_restar(self):
        """Test de resta."""
        assert logica.restar(10, 3) == 7
        assert logica.restar(0, 5) == -5
        assert logica.restar(5, 5) == 0
    
    def test_multiplicar(self):
        """Test de multiplicación."""
        assert logica.multiplicar(4, 3) == 12
        assert logica.multiplicar(0, 100) == 0
        assert logica.multiplicar(-2, 5) == -10
    
    def test_dividir(self):
        """Test de división normal."""
        assert logica.dividir(10, 2) == 5
        assert logica.dividir(5, 2) == 2.5
        assert logica.dividir(0, 5) == 0
    
    def test_dividir_por_cero(self):
        """Test que verifica que división por cero lance error."""
        with pytest.raises(ZeroDivisionError) as exc_info:
            logica.dividir(5, 0)
        
        # Verificar el mensaje de error
        assert "No se puede dividir entre cero" in str(exc_info.value)
    
    def test_potenciar(self):
        """Test de potencia."""
        assert logica.potenciar(2, 3) == 8
        assert logica.potenciar(5, 0) == 1
        assert logica.potenciar(4, 0.5) == 2  # √4 = 2


class TestFuncionCalcular:
    """Tests para la función principal calcular()."""
    
    def test_calcular_suma(self):
        """Test calcular con suma."""
        assert logica.calcular("+", 5, 3) == 8
    
    def test_calcular_resta(self):
        """Test calcular con resta."""
        assert logica.calcular("-", 10, 4) == 6
    
    def test_calcular_multiplicacion(self):
        """Test calcular con multiplicación."""
        assert logica.calcular("*", 3, 4) == 12
    
    def test_calcular_division(self):
        """Test calcular con división."""
        assert logica.calcular("/", 10, 2) == 5
    
    def test_calcular_potencia(self):
        """Test calcular con potencia."""
        assert logica.calcular("**", 2, 3) == 8
    
    def test_calcular_operacion_invalida(self):
        """Test que verifica operación inválida."""
        with pytest.raises(ValueError) as exc_info:
            logica.calcular("?", 5, 3)
        
        assert "Operación no válida" in str(exc_info.value)
    
    def test_calcular_division_por_cero(self):
        """Test que división por cero en calcular() también lance error."""
        with pytest.raises(ZeroDivisionError):
            logica.calcular("/", 5, 0)


def test_todas_operaciones_consistencia():
    """Test de consistencia entre funciones individuales y calcular()."""
    # Verificar que cada operación individual coincide con calcular()
    casos = [
        ("+", 7, 3, 10),
        ("-", 7, 3, 4),
        ("*", 7, 3, 21),
        ("/", 6, 3, 2),
        ("**", 2, 3, 8),
    ]
    
    for operacion, a, b, esperado in casos:
        resultado = logica.calcular(operacion, a, b)
        assert resultado == esperado, \
            f"calcular('{operacion}', {a}, {b}) = {resultado}, esperado {esperado}"