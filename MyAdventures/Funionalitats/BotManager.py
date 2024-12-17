import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import mcpi.minecraft as Minecraft
import mcpi.block as block

class BotManager:
    def __init__(self, bot_type):
        self.bot_state = bot_type

    def set_bot_type(self, bot_type):
        self.bot_state = bot_type

    def perform(self):
        self.bot_state.perform()
