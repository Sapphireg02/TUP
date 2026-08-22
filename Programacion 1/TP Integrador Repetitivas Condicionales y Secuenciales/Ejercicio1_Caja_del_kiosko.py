#Objetivo: Simular una compra con validaciones y cálculo de total.

#---NOMBRE DEL CLIENTE---
nombre = input("Ingrese su nombre: ").lower().replace(" ", "")
# Valida que sean solo letras y elimina espacios.
while nombre == "" or not nombre.isalpha():
    print("Nombre inválido. Por favor, ingrese solo letras.")
    nombre = input("Ingrese su nombre: ").lower().replace(" ", "")

#---CANTIDAD DE PRODUCTOS---
cantidad = input("Ingrese la cantidad de productos que desea comprar: ")
# Valida que sea un número entero positivo.
while not (cantidad.isdigit() and int(cantidad) > 0):
    print("Cantidad inválida. Por favor, ingrese un número entero positivo.")
    cantidad = input("Ingrese la cantidad de productos que desea comprar: ")

#---PRECIO DE CADA PRODUCTO---
total_sin_dto = 0
total_con_dto = 0

for i in range(int(cantidad)):
    precio = input(f"Ingrese el precio del producto {i + 1}: ")

    # Valida que sea un número entero.
    while not (precio.isdigit() and int(precio) > 0):
        print("Precio inválido. Por favor, ingrese un número entero positivo.")
        precio = input(f"Ingrese el precio del producto {i + 1}: ")

    # Suma el precio al total sin descuento.
    total_sin_dto += int(precio)
    
    # Pregunta si tiene descuento.
    descuento = input(f"¿El producto {i + 1} tiene descuento? (s/n): ").strip().lower()
    while descuento not in ['s', 'n']:
        print("Respuesta inválida. Por favor, ingrese 's' para sí o 'n' para no.")
        descuento = input(f"¿El producto {i + 1} tiene descuento? (s/n): ").strip().lower()

    # Aplica el descuento si la respuesta es 's'.
    if descuento == 's':
        precio = int(precio) * 0.9 #(10% de descuento)
    total_con_dto += int(precio)

print(f"---*---*---*---*---*---*---*---\nCliente: {nombre}\nCantidad de productos: {cantidad}\nTotal sin descuentos: ${total_sin_dto}")
# Verifica si hubo descuentos.
if total_sin_dto == total_con_dto:
    print("No hubo descuentos aplicados.")
else:
    print(f"Total con descuentos: ${total_con_dto}\nAhorro total: ${total_sin_dto - total_con_dto}")

print(f"Promedio por producto: ${total_con_dto / float(cantidad):.2f}\n---*---*---*---*---*---*---*---")