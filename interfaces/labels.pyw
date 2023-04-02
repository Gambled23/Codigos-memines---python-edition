from tkinter import *

root = Tk() 
miFrame = Frame(root, width=500, height=400)
miFrame.pack()

miLabel = Label(miFrame, text='holiwis :3', fg='red') #Crear label
#miLabel.pack() #empaquetar label, se cambia el tamaño de la raiz
miLabel.place(x=100, y=200) #ubica el label dentro de unas coordenadas x|y
#otra forma de hacer esto es 
#Label(miFrame, text='holiwis :3').place(x=100, y=200)

#Para usar imagenes
miImagen = PhotoImage(file='interfaces\\tierra.gif')
Label(miFrame, image=miImagen).place(x=10, y=10)

root.mainloop()