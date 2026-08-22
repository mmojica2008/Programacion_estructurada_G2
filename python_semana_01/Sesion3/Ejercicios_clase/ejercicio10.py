# Actividad 10
# Conversión de dinero
# Solicita una cantidad en dólares y una tasa de cambio. Calcula y muestra cuánto representa esa cantidad en córdobas.

dolares = float(input("Ingrese la cantidad en dolares: "))
tasa_cambio = float(input("Ingrese la tasa de cambio (Córdobas por dólar y centavos): "))

cordobas = dolares * tasa_cambio
print(f"La cantidad en cordobas es: {cordobas}")