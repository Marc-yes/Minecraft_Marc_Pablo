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

# Connect to the Minecraft game  
mc = Minecraft.Minecraft.create()


insults=["saboc", "no vals un fuckin duro", "Algun dia jugaras en los ulls oberts", "tens menos habilitat que nepe, i es dir molt...",
         "vaia ascla", "Osti xec, no val ni un duro lo paio...", "Onso", "Sol de veuret jugar he agafat clamidia"]

mc.postToChat("nana")

insult_bot  = InsultBot()
bot_manager = BotManager(insult_bot)
bot_manager.typeOf()

chatEvent = mc.events.pollChatPosts()
for mensaje in chatEvent:
    assert mensaje.message == "InsultBot"

mc.postToChat("end performance")

#bot_manager.perform()


#chatEvent = mc.events.pollChatPosts()
#for mensaje in chatEvent:
#    assert mensaje.message == "InsultBot"
