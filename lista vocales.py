# Imports go at the top
from microbit import *

lista_vocales=["a","e","i","o","u"]

for i in lista_vocales:
    display.scroll(i)
    sleep(1000)
