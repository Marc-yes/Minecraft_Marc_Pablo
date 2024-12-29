# tests/test_InsultBot.py
import unittest
from unittest.mock import MagicMock
import sys
import os

# Afegir el directori arrel (MyAdventures) al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar la classe InsultBot
from Funcionalitats.TNTBot import TNTBot

class TestTNTBot(unittest.TestCase):

    def test_perform_TNT(self):
                # Crear una instància simulada de Minecraft
        mock_mc = MagicMock()

        # Crear mocks que simulin els blocs TNT i FIRE
        mock_tnt = MagicMock()
        mock_tnt.id = 46  # ID de TNT a Minecraft
        mock_tnt.data = 0
        mock_fire = MagicMock()
        mock_fire.id = 51  # ID de FIRE a Minecraft
        mock_fire.data = 0

        # Assignar els mocks als blocs
        mock_mc.block.TNT = mock_tnt
        mock_mc.block.FIRE = mock_fire

        # Crear una instància del bot amb l'instància simulada
        tnt_bot = TNTBot(mc_instance=mock_mc)

        # Proporcionar una posició simulada
        player_pos = (10, 64, 10)

        # Executar el mètode perform amb la posició simulada
        tnt_bot.perform(player_pos)

        # Verificar que els blocs correctes s'han col·locat a les coordenades esperades
        mock_mc.setBlock.assert_any_call(11, 64, 10, mock_tnt)
        mock_mc.setBlock.assert_any_call(11, 65, 10, mock_fire)
        

    def test_typeOf_TNTBot(self):
        # Crear una instància simulada de Minecraft
        mock_mc = MagicMock()

        # Crear una instància del bot amb l'instància simulada
        tnt_bot = TNTBot(mc_instance=mock_mc)

        # Executar el mètode typeOf
        result = tnt_bot.typeOf()

        # Verificar que s'ha cridat postToChat amb "TNTBot"
        mock_mc.postToChat.assert_called_with("TNTBot")


if __name__ == '__main__':
    unittest.main()