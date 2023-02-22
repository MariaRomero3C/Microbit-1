# Imports go at the top
from microbit import *
import radio
import music

radio.on
radio.config(channel=10)
#Funcion que dado texto se pasa a la lista
def texto_lista(texto):
    return texto.split(",")
    #Siempre en ejecucion
while True:
    message=radio.receive()
    sleep(20)
    if message is not None:
        try:
            notas=texto_lista(message)
            music.play(notas)
        except:
            display.scroll(message)
