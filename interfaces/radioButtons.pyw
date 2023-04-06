from tkinter import *
root = Tk()

varOpcion = IntVar() #Radiobutton seleccionado

def imprimir():
    #print(varOpcion.get()) #para imprimir el valor del radio button pulsado
    if varOpcion.get() == 1:
        etiqueta.config(text='Has elegido masculino')
    else:
        etiqueta.config(text='Has elegido femenino')

    
Label(root, text='genero: ').pack()

Radiobutton(root, text='Masculino', variable=varOpcion, value=1, command=imprimir).pack()#varuable es 'el grupo' al que pertenecen
Radiobutton(root, text='Femenino', variable=varOpcion, value=2, command=imprimir).pack()#Value es la 'id' del boton

etiqueta = Label(root, text='')
etiqueta.pack()

root.mainloop()