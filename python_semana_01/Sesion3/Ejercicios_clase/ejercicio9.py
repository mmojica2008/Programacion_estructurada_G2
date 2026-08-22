# Actividad 9
# Mayor de tres números
# Solicita tres números enteros. Determina cuál es el mayor y muéstralo en pantalla.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("El numero mayor es el: ", numero1)

elif numero2 > numero1 and numero2 > numero3:
    print("El numero mayor es el: ", numero2)
    
else:
    print("El numero mayor es el: ", numero3)