calificaciones = [0]
i = j = 0
num = int(input("Cuantas calificaciones vas a ingresar? "))
promedio = 1
while j < num:
    meme = int(input("Ingresa calificacion: "))
    calificaciones.append(meme)
    j += 1

for i in enumerate[calificaciones]:
    promedio = promedio + calificaciones[i]
    i += 1
promedio = promedio / i
