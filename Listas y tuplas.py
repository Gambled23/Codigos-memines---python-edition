lista = [1,3,5, "pablo"]
#Agregar el elemento 3 al final
#*Se puede poner punto despues de el nombre de la lista, y ver todas las operaciones posibles, como con objetos
lista.append(3)
#Imprime todos los elementos de la lista
print(lista)

#Imprime el que queramos
print(lista[3])
#Imprime el que queramos de fin a inicio
#-1 es el ultimo elemento, 0 es el primer elemento
print(lista[-2])
#Imprime un rango de elementos 
print(lista[0:2]) #poner [:2] es lo mismo que poner [0:2]

#*TUPLAS, Como una lista pero los elementos no se pueden modificar
tupla = (1,2,4,9, "pene")
print (tupla)