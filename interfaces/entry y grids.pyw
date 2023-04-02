from tkinter import *

root = Tk() 
miFrame = Frame(root, width=500, height=400)
miFrame.pack()

miEntry = Entry(miFrame)
miEntry.grid(row=0, column=1, padx=10) #row, column (vertical, horizontal), empieza a contar desde 0

miLabel = Label(miFrame, text='Nombre:')
miLabel.grid(row=0, column=0, sticky='n') #Con sticky lo pegamos a un lado del grid usando puntos cardinales
#Podemos usar pady o padx para ponerle padding en y o x

passwordEntry = Entry(miFrame)
passwordEntry.config(show='*') #Para censurar el password
passwordLabel = Label(miFrame, text='Contraseña:')
passwordLabel.grid(row=1, column=0)
passwordEntry.grid(row=1, column=1, padx=10)
root.mainloop()