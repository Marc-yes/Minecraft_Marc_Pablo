import unittest
from unittest.mock import MagicMock
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Funcionalitats.InsultBot import InsultBot

insults = [
    "saboc", "no vals un fuckin duro",
    "Algun dia jugaras en los ulls oberts", "tens menos habilitat que nepe, i es dir molt...",
    "vaia ascla", "Osti xec, no val ni un duro lo paio...",
    "Onso", "Sol de veuret jugar he agafat clamidia"
]

class TestInsultBot(unittest.TestCase):

    def test_perform_returns_valid_insult(self):
        # Crear una instància simulada de Minecraft
        mock_mc = MagicMock()

        # Crear una instància del bot amb l'instància simulada
        insult_bot = InsultBot(mc_instance=mock_mc)

        # Executar el mètode perform
        insult = insult_bot.perform()

        # Comprovar que l'insult retornat està a la llista
        self.assertIn(insult, insults, "L'insult retornat no està a la llista d'insults.")

        # Verificar que s'ha cridat postToChat amb l'insult seleccionat
        mock_mc.postToChat.assert_called_with(insult)

    def test_typeOf_returns_correct_value(self):
        # Crear una instància simulada de Minecraft
        mock_mc = MagicMock()

        # Crear una instància del bot amb l'instància simulada
        insult_bot = InsultBot(mc_instance=mock_mc)

        # Executar el mètode typeOf
        result = insult_bot.typeOf()

        # Comprovar que el mètode retorna "InsultBot"
        self.assertEqual(result, "InsultBot", "El mètode typeOf ha de retornar 'InsultBot'.")

        # Verificar que s'ha cridat postToChat amb "InsultBot"
        mock_mc.postToChat.assert_called_with("InsultBot")


if __name__ == '__main__':
    unittest.main()
