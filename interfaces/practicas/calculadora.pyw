from tkinter import *

root = Tk()
miFrame = Frame(root)

miFrame.pack()

operacion = ''
resultado = 0

#Pantalla
numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, pady=10, padx=10, columnspan=4) #Con columnspan decimos que ocupe 4 columnas
pantalla.config(bg='black', fg='#03f943', justify='right')

#pulsacionesTeclado
def escribirPantalla(textoPulsado):
    global operacion 
    if operacion != '': #Si el usuario ya pulsó un boton de operacion
        numeroPantalla.set(textoPulsado)
        operacion = ''
    else:
        numeroPantalla.set(numeroPantalla.get() + textoPulsado) #Lo que haya más el 4

    

def pulsarSuma(num):
    global operacion 
    global resultado

    resultado += int(num) #sumar
    operacion = 'suma'

    numeroPantalla.set(resultado)

def pulsarResultado():
    global resultado

    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0


#fila 1
boton7 = Button(miFrame, text='7', width=3, command=lambda: escribirPantalla('7'))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text='8', width=3, command=lambda: escribirPantalla('8'))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text='9', width=3, command=lambda: escribirPantalla('9'))
boton9.grid(row=2, column=3)
botonMult = Button(miFrame, text='X', width=3) 
botonMult.grid(row=2, column=4)

#fila 2
boton4 = Button(miFrame, text='4', width=3, command=lambda: escribirPantalla('4')) #Para pasar argumentos en un command es necesario usar lambda
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text='5', width=3, command=lambda: escribirPantalla('5'))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text='6', width=3, command=lambda: escribirPantalla('6'))
boton6.grid(row=3, column=3)
botonDiv = Button(miFrame, text='/', width=3)
botonDiv.grid(row=3, column=4)

#fila 3
boton1 = Button(miFrame, text='1', width=3, command=lambda: escribirPantalla('1'))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text='2', width=3, command=lambda: escribirPantalla('2'))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text='3', width=3, command=lambda: escribirPantalla('3'))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text='-', width=3)
botonRest.grid(row=4, column=4)

#fila 4
botonPunto = Button(miFrame, text='.', width=3, command=lambda: escribirPantalla('.'))
botonPunto.grid(row=5, column=1)
boton0 = Button(miFrame, text='0', width=3, command=lambda: escribirPantalla('0'))
boton0.grid(row=5, column=2)
botonIgual = Button(miFrame, text='=', width=3, command=lambda: pulsarResultado())
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame, text='+', width=3, command=lambda: pulsarSuma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)
root.mainloop()