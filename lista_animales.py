# Imports go at the top
from microbit import *


lista_animales=("leon", "serpiente", "oso", "perro", "caballo")
for i in lista_animales:
    display.scroll(i)
    sleep(1000)
