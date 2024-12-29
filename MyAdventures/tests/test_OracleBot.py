# tests/test_InsultBot.py
import unittest
from unittest.mock import patch
import sys
import os

# Afegir el directori arrel (MyAdventures) al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar la classe InsultBot
from Funcionalitats.OracleBot import OracleBot

class TestOracleBot(unittest.TestCase):

    def test_typeOf_OracleBot(self):
        # Crear una instància del bot
        oracle_bot = OracleBot()

        # Executar el mètode perform
        tipo = oracle_bot.typeOf(False)

        # Comprovar que l'insult retornat està dins de la llista predefinida
        assert tipo == "OracleBot"


if __name__ == '__main__':
    unittest.main()