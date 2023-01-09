# Imports go at the top
from microbit import *
# Variable contador
nombre= "Lucas"
while True:
    if button_a.was_pressed():
        nombre
        display.scroll(nombre)