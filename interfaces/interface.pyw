from tkinter import *

#Debe ser archivo .pyw para que no abra una consola detrás
raiz = Tk() #Crea la ventana raiz
raiz.title('Ventana de prueba') #Cambia el titulo
raiz.resizable(True, False) #El primero pertenece al width y el segundo al height
raiz.iconbitmap('') #El icono que va a tener la ventana
raiz.geometry('650x200') #Tamaño por defecto de ventana
raiz.config(bg='gray') #Fondo de la ventana


raiz.mainloop() #Ejecuta la ventana