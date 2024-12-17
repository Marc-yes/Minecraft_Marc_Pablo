import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import mcpi.minecraft as Minecraft
import mcpi.block as block

mc = Minecraft.Minecraft.create()

class TNTBot():
    def perform(self):
        mc.events.pollChatPosts()
        active_loop = True
        while active_loop:
            chatEvent = mc.events.pollChatPosts()
            for mensaje in chatEvent:
                if mensaje.message == "tnt":
                    x, y, z = mc.player.getTilePos()
                    mc.setBlock(x+1, y, z, block.TNT)
                    mc.setBlock(x+1, y+1, z, block.FIRE)
                    
                elif mensaje.message == "end performance":
                    active_loop = False
