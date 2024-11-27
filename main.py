import telebot
import random

TOKEN = '7557019428:AAHDisl1swHU3TUoYA4LR_IJM1CyxIO6aR0'
bot = telebot.TeleBot(TOKEN)

# Diccionarios para almacenar las respuestas
respuestas_humillalo = [
    "k pedo con el azteca este",
    "Pinche pito chico",
    "Mi compa el color llanta",
    "El pendejoo el pendejooo", 
]
respuestas_golpealo = [
    "No se sienta un culo mijo *lo verguea*",
    "Apoco si bien vergas *Le sumne la mollera*",
    "*Le mete el puño*",
    "*Le mete el brazo*",
]
respuestas_coquetalo = [
    "Que bonitos ojos tiene compadre",
    "Nice dick",
    "*Lo nalguea*",
    "*Le da un beso*",
    "*Le da un beso de lengua*",
]

# Función para obtener una respuesta aleatoria
def obtener_respuesta(lista_respuestas):
    return random.choice(lista_respuestas)
##EN ESTE BLOQUE VEMOS LOS COMANDOS
# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola, me presento mi nombre es Pepebot y vengo a humillarlos jsjs")

# Manejador para la palabra "pito" (debe ir primero para que se detecte antes que el echo)
@bot.message_handler(func=lambda message: message.text and "pito" in message.text.lower())
def responder_pito(message):
    bot.reply_to(message, "chupo")

# Comando /humillalo con respuestas variadas
@bot.message_handler(commands=['humillalo'])
def send_humillalo(message):    
    respuesta = obtener_respuesta(respuestas_humillalo)
    bot.reply_to(message, respuesta)

# Comando /golpealo con respuestas variadas
@bot.message_handler(commands=['golpealo'])
def send_golpealo(message):    
    respuesta = obtener_respuesta(respuestas_golpealo)
    bot.reply_to(message, respuesta)

# Comando /coquetealo con respuestas variadas
@bot.message_handler(commands=['coquetealo'])
def send_coqueteo(message):    
    respuesta = obtener_respuesta(respuestas_coquetalo)
    bot.reply_to(message, respuesta)

# Comando /ayuda
@bot.message_handler(commands=['ayuda'])
def send_ayuda(message):
    bot.reply_to(message, "Comandos disponibles:\n/humillalo\n/golpealo\n/coquetealo")
##AQUI TERMINA EL BLOQUE DE COMANDOS 

##imagenes 
@bot.message_handler(commands=['foto'])
def send_image(message):
    img_url = "https://th.bing.com/th/id/OIP.pwl12Lj4plzT6DbKzyqDVgHaGi?w=210&h=186&c=7&r=0&o=5&pid=1.7"
    bot.send_photo(chat_id=message.chat.id, photo=img_url,caption='guevos perro')    

# Echo handler para texto no reconocido (último en el orden)
# Este debe ser el último para que no repita mensajes ya procesados
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Este manejador es ahora un "catch-all", pero no responderá si ya se respondió a la palabra "pito"
    pass

if __name__ == '__main__':
    bot.polling(none_stop=True)
