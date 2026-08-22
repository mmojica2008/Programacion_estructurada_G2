# Actividad 8
# Número par o impar
# Solicita un número entero. Determina si el número es par o impar y muestra el resultado.

numero = int(input("Inserte un numero entero: "))

if numero % 2 == 0:
    print(f"{numero} Es un número par")
else:
    print(f"{numero} Es un número impar")