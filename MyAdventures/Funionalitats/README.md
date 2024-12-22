LA BRANCA BONA ÉS "MARC"

Aquest projecte tracta de la implementació d'alguns bots dins d'un servidor de Minecraft. Tenim l'insultBot, TNTBot i l'OracleBot. Hem implementat el patró de disseny "state", el qual permet canviar de Bot dins de la partida. 

Per utilitzar OracleBot
És necessari almenys tenir la versió 3 de python al teu entorn.
Els següents passos són des de la terminal de l'entorn que voleu fer servir.
Per instal·lar l'API de Gemini, fer:
python3 -m pip install -q -U google-generativeai

i després:
python -m pip install Ipython --user

Si el paquet IPython dona algun error, prova amb:
python3 -m pip install IPython

Un cop fet això caldrà entrar al directori de Funcionalitats.
És possible que faci falta fer la següent comanda dins d'aquest repositori:
python3 -m pip install Ipython --no-cache-dir

o la següent:
python3 -m pip install Ipython

Per utilitzar l'OracleBot caldrà crear una clau d'API que podrem trobar en aquesta pàgina:
https://ai.google.dev/gemini-api/docs?hl=es-419


Per a executar el programa caldrà posar a la terminal:
python3 Main.py

Un cop estem al joc, podem comprovar que el programa funciona escrivint al xat "hola", i ens haurà de retornar "hola que tal”. Aquest seria l’estat base.

Per a escollir un bot hem d'escriure pel xat “changeto” seguit d'un dels bots: “tntBot”, “insultBot”, “OracleBot”. Si tot ha anat bé, al xat s’escriurà la resposta “bot changed to insult bot”.
Exemple: “changeto tntBot”

Per utilitzar el bot primer caldrà escriure la comanda “perform”. En cada Bot tenim diferents opcions:

insultBot:
	Posarà un insult al xat sempre que s'escrigui “insultam”.
tntBot:
	Posarà una tnt encesa al teu costat sempre que s'escrigui “tnt”.
OracleBot:
	La intel·ligència artificial “Gemini” contestarà a totes les entrades del xat.

Es pot saber en quin bot estem escrivint “typeOf”.

IMPORTANT: Quan es vulgui canviar de bot, caldrà finalitzar l’execució de l’actual escrivint “end performance”. Així tornaràs a l’estat base.
