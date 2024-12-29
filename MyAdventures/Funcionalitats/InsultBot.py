import random
from mcpi.minecraft import Minecraft

insults = [
    "saboc", "no vals un fuckin duro",
    "Algun dia jugaras en los ulls oberts", "tens menos habilitat que nepe, i es dir molt...",
    "vaia ascla", "Osti xec, no val ni un duro lo paio...",
    "Onso", "Sol de veuret jugar he agafat clamidia"
]

class InsultBot:
    def __init__(self, mc_instance=None):
        # Utilitza l'instància real de Minecraft si no es proporciona cap instància simulada
        self.mc = mc_instance or Minecraft.create()

    def perform(self):
        # Selecciona un insult aleatori
        r = random.randint(0, len(insults) - 1)
        insult = insults[r]
        # Envia l'insult al xat de Minecraft
        self.mc.postToChat(insult)

    def typeOf(self):
        self.mc.postToChat("InsultBot")
