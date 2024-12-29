import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import mcpi.minecraft as Minecraft
import mcpi.block as block

# Importamos el paquete recien instalado
import google.generativeai as genai

# Esto es para usar secrets, la nueva opción de Google Colab, para almacenar la API key. Si no estás usando Google Colab, deberás importarla de otro modo equivalente
import textwrap
from IPython.display import display
from IPython.display import Markdown


# Esta función se usa para dejar el formato Markdown que devuelve Gemini en formato compatible con Colab
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Configuramos nuestra instancia del modelo con nuestra API key
GOOGLE_API_KEY = "AIzaSyDb-8KZkaIGBaMtf5LK63ejhVi7nK6Pzh8"

genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')


# Connect to the Minecraft game  
mc = Minecraft.Minecraft.create()

class OracleBot():
    def perform(self):
        mc.events.pollChatPosts()
        active_loop = True
        while active_loop:
            chatEvent = mc.events.pollChatPosts()
            for mensaje in chatEvent:
                if mensaje.message == "end performance":
                    active_loop = False

                elif mensaje.message == "typeOf":
                    self.typeOf()

                else:
                    response = model.generate_content(mensaje.message)
                    response_text = response.text.replace("\n", "  ")
                    mc.postToChat(response_text)


    def typeOf(self):
        mc.postToChat("OracleBot")
        return "OracleBot"
