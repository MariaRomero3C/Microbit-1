from microbit import*


contador=0
while True:
    if button_a.get_presses():
        contador=contador+1
        numero=0
    elif button_b.get_presses():
        contador=contador-1
    else:
        display.show(contador)
