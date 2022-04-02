numActual = 0
juego = True
print(numActual)
while(juego == True):
    numero = int(input())
    if(numero == (numActual + 1)):
        numActual = numActual + 1
        juego = True
    else:
        juego = False
print("Fallaste!!! >:c")