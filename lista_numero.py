# Imports go at the top
from microbit import *

lista_numeros=[2,5,4,1,3]
total=0
i=0
while i <len(lista_numeros):
    total=total+lista_numeros[i]
    i=i+1



    display.scroll(total)
