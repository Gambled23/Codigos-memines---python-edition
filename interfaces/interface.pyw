from tkinter import *

#Debe ser archivo .pyw para que no abra una consola detrás
raiz = Tk() #Crea la ventana raiz
raiz.title('Ventana de prueba') #Cambia el titulo
raiz.resizable(True, True) #El primero pertenece al width y el segundo al height
raiz.iconbitmap('') #El icono que va a tener la ventana
#raiz.geometry('650x200') #Tamaño por defecto de ventana
raiz.config(bg='gray') #Fondo de la ventana

miFrame = Frame() #Construir frame
miFrame.pack(anchor='ne') #Meter frame dentro de raiz
#side es a donde se queda anclado en la raiz en un solo lado
#anchor es para anclarlo a un punto cardinal
#miFrame.pack(anchor='ne', fill = 'x')
#fill es para rellenar la raiz hacia los costados, fill both se expande hacia los lados y hacia abajo


miFrame.config(bg='red')
miFrame.config(width='600', height='150') #La raiz se adapta a el tamaño de la raiz, pero se puede expandir
miFrame.config(border='25') #Establecer tamaño de borde
miFrame.config(relief='groove') #Establecer tipo de borde
miFrame.config(cursor='hand2') #Tipo de cursor al pasar encima del borde

raiz.mainloop() #Ejecuta la ventana