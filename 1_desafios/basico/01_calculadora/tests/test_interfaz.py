"""
Tests para el módulo interfaz.py usando unittest.mock
"""
import pytest
from unittest.mock import patch, MagicMock
from src import interfaz


class TestInterfazUsuario:
    """Tests para funciones de interfaz de usuario."""
    
    def test_mostrar_bienvenida(self, capsys):
        """Test que verifica que se muestra el mensaje de bienvenida."""
        interfaz.mostrar_bienvenida()
        
        # Capturar lo impreso en consola
        capturado = capsys.readouterr()
        salida = capturado.out
        
        # Verificar elementos clave en el mensaje
        assert "Bienvenido" in salida
        assert "operaciones matemáticas básicas" in salida
        assert "+ : Suma" in salida
        assert "0 : Salir" in salida
    
    @patch('builtins.input')
    def test_obtener_operacion_valida(self, mock_input):
        """Test de obtener operación con entrada válida."""
        # Simular que el usuario ingresa '+'
        mock_input.return_value = '+'
        
        resultado = interfaz.obtener_operacion()
        
        assert resultado == '+'
        mock_input.assert_called_once()
    
    @patch('builtins.input')
    def test_obtener_operacion_salir(self, mock_input):
        """Test que 'salir' retorna '0'."""
        mock_input.return_value = 'salir'
        
        resultado = interfaz.obtener_operacion()
        
        assert resultado == '0'
    
    @patch('builtins.input')
    def test_obtener_operacion_invalida_then_valida(self, mock_input):
        """Test de entrada inválida seguida de válida."""
        # Primero inválida, luego válida
        mock_input.side_effect = ['inválido', '+']
        
        resultado = interfaz.obtener_operacion()
        
        assert resultado == '+'
        assert mock_input.call_count == 2
    
    @patch('builtins.input')
    def test_obtener_numero_valido(self, mock_input):
        """Test de obtener número con entrada válida."""
        mock_input.return_value = '42.5'
        
        resultado = interfaz.obtener_numero("Ingrese número: ")
        
        assert resultado == 42.5
    
    @patch('builtins.input')
    def test_obtener_numero_invalido_then_valido(self, mock_input):
        """Test de número inválido seguido de válido."""
        mock_input.side_effect = ['no_es_numero', '100']
        
        resultado = interfaz.obtener_numero("Ingrese número: ")
        
        assert resultado == 100.0
        assert mock_input.call_count == 2
    
    def test_mostrar_resultado(self, capsys):
        """Test de mostrar resultado formateado."""
        interfaz.mostrar_resultado(10, '+', 5, 15)
        
        capturado = capsys.readouterr()
        salida = capturado.out
        
        assert "Resultado:" in salida
        assert "10 + 5 = 15" in salida
    
    def test_mostrar_despedida(self, capsys):
        """Test de mensaje de despedida."""
        interfaz.mostrar_despedida()
        
        capturado = capsys.readouterr()
        salida = capturado.out
        
        assert "¡Hasta luego!" in salida
        assert "Gracias" in salida