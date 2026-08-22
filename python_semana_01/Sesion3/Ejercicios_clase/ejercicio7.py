# Actividad 7
# Precio con descuento
# Solicita el precio de un producto y el porcentaje de descuento. 
# Calcula y muestra el descuento aplicado y el precio final.

print("Oferta de descuento")
precio = float(input("¿Cual es el valor original del producto? "))
descuento_percentage = float(input("¿De cuanto es el porcentaje de descuento? "))

descuento = precio * (descuento_percentage / 100)
precio_final = precio - descuento

print(f"El descuento aplicado es: {descuento}")
print(f"El precio final es: {precio_final}")