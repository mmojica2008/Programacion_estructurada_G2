# Actividad 6
# Cálculo de edad
# Solicita el año de nacimiento de una persona. Calcula aproximadamente su edad tomando como referencia el año actual.

print("----Cálculo de edad----")
año_nacimiento = int(input("¿En que año nacio la criatura?: "))
año_actual = int(input("Ingresa el año actual: "))

edad = año_actual - año_nacimiento
print(f"Tu edad es: {edad} años")