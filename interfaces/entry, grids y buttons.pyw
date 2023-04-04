from tkinter import *

root = Tk() 
miFrame = Frame(root, width=500, height=400)
miFrame.pack()

miNombre = StringVar()


nombreEntry = Entry(miFrame, textvariable=miNombre) #El texto dentro de nombreEntry se guardará en variable miNombre
nombreEntry.grid(row=0, column=1, padx=10) #row, column (vertical, horizontal), empieza a contar desde 0

nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky='n') #Con sticky lo pegamos a un lado del grid usando puntos cardinales
#Podemos usar pady o padx para ponerle padding en y o x

passwordEntry = Entry(miFrame)
passwordEntry.config(show='*') #Para censurar el password
passwordLabel = Label(miFrame, text='Contraseña:')
passwordLabel.grid(row=1, column=0)
passwordEntry.grid(row=1, column=1, padx=10)



#Crear TEXT
comentariosLabel = Label(miFrame, text='Comentarios:')
comentariosLabel.grid(row=2, column=0)
textoComentario = Text(miFrame, width=20, height=5)
textoComentario.grid(row=2, column=1, padx=10, pady=10)


#Crear barra de scroll para el text
scrollVert = Scrollbar(miFrame, command=textoComentario.yview) #el command indica que es de textoComentario y scrollea en el eje Y
scrollVert.grid(row=2, column=2, sticky=NSEW) #El column debe ser 1 mayor al del TEXT que pertenece, con sticky hace que se adapte al tamaño de el campo de texto
textoComentario.config(yscrollcommand=scrollVert.set) #Para que el scroll funcione bn al desplazar la barrita

#Crear botón
def recibirDatos():
    miNombre.set('cesar') #ver declaracion de miNombre
    miNombre.get()

botonSubmit = Button(root, text='Enviar', command=recibirDatos) #Al pulsar el boton llama a recibirDatos
botonSubmit.pack()


root.mainloop()