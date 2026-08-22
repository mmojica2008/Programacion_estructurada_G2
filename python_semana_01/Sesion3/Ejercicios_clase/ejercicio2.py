# Actividad 2: promedio
# Lee tres calificaciones decimales, calcula el promedio y muéstralo con dos cifras decimales.

CorteI = int(input("Ingrese la primer nota: "))
CorteII = int(input("Ingrese la segunda nota: "))
CorteIII = int(input("Ingrese la tercer nota: "))

print("Primer corte:", CorteI)
print("Segundo corte:", CorteII)
print("Tercer corte:", CorteIII)

Promedio = (CorteI + CorteII +CorteIII) / 3
print(f"El promedio de las tres notas es: {Promedio:.2f}")