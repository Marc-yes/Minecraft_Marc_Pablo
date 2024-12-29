from mcpi.minecraft import Minecraft
from mcpi import block

class TNTBot():
    def __init__(self, mc_instance=None):
        # Utilitza una instància simulada si no es proporciona cap instància real
        self.mc = mc_instance or Minecraft.create()

    def perform(self, player_pos=None):
        # Si no es proporciona una posició, utilitza l'API real
        if player_pos is None:
            x, y, z = self.mc.player.getTilePos()
        else:
            x, y, z = player_pos

        self.mc.setBlock(x+1, y, z, block.TNT)
        self.mc.setBlock(x+1, y+1, z, block.FIRE)


    def typeOf(self):
        self.mc.postToChat("TNTBot")
