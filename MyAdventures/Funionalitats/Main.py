from InsultBot import InsultBot
from TNTBot import TNTBot
from OracleBot import OracleBot
from BotManager import BotManager
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import mcpi.minecraft as Minecraft
import mcpi.block as block

mc = Minecraft.Minecraft.create()

insult_bot  = InsultBot()
tnt_bot = TNTBot()
oracle_bot = OracleBot()
bot_manager = BotManager(insult_bot)

while True:
    chatEvent = mc.events.pollChatPosts()
    for mensaje in chatEvent:
        if mensaje.message == "changeto insultBot":
            bot_manager.set_bot_type(insult_bot)
            mc.postToChat("bot changed to insult bot")

        elif mensaje.message == "changeto tntBot":
            bot_manager.set_bot_type(tnt_bot)
            mc.postToChat("bot changed to tnt bot")

        elif mensaje.message == "changeto OracleBot":
            bot_manager.set_bot_type(oracle_bot)
            mc.postToChat("bot changed to oracle bot")
            
        elif mensaje.message == "perform":
            bot_manager.perform()
            mc.postToChat("performance ended")
            mc.events.pollChatPosts()

        elif mensaje.message == "hola":
            mc.postToChat("hola que tal")