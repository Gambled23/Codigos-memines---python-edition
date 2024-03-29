from tkinter import *
from tkinter import messagebox #Importar librería de ventana emergente
root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300) #Posicionar barra de menu

#funciones de menu
def ventanaEmergente():
    messagebox.showinfo('Abrir archivos', 'Buenas tardes uwu')
    messagebox.showwarning('cuidao', 'ojo cuidao')

def salir():
    valor = messagebox.askquestion('salir', 'Deseas salir?')
    if valor=='yes':
        root.destroy() #destroy cierra la ventana

    messagebox.askokcancel('salir', 'oliwis')
    #unas ventanas devuelven un true/false

#Inicializar submenus
archivoMenu = Menu(barraMenu, tearoff=0) #tearoff es para quitar la opcion por defecto del submenu 
archivoMenu.add_command(label='Abrir archivo', command=ventanaEmergente) #Todas las opciones del submenu archivo
archivoMenu.add_command(label='Cerrar archivo')
archivoMenu.add_separator() #Esta es una barra horizontal para separar las opciones
archivoMenu.add_command(label='Salir', command=salir)
edicionMenu = Menu(barraMenu)

herramientasMenu = Menu(barraMenu)

ayudaMenu = Menu(barraMenu)

barraMenu.add_cascade(label='Menu', menu=archivoMenu) #Para colocar submenus en la barraMenu
barraMenu.add_cascade(label='Edicion', menu=edicionMenu)
barraMenu.add_cascade(label='Herramientas', menu=herramientasMenu)
barraMenu.add_cascade(label='Ayuda', menu=ayudaMenu)



root.mainloop()