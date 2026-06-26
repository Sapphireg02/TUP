#1. Solicita al usuario que ingrese su edad y determina si es mayor de edad o no.
edad = int(input("Ingrese su edad: "))
if (edad > 18):
    print("Es mayor de edad")

#2. Solicita su nota al usuario y determina si aprobó o no. (Nota de aprobación: 6)
nota = int(input("Ingrese su nota: "))
if (nota >= 6):
    if (nota > 10):
        print("La nota ingresada no es válida")
    else:
        print("Aprobado")
else:
    print("Desaprobado")

#3. Verifica si el número ingresado es par.
par = int(input("Ingrese un número par: "))
if (par % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor ingrese un número par")

#4. Con la edad ingresada en (1) imprime a que categoría pertenece (Niño, Adolescente, Adulto joven, Adulto)
if (edad < 12):
    print("Niño")
elif (edad >= 12 and edad < 18):
    print("Adolescente")
elif (edad >= 18 and edad < 30):
    print("Adulto joven")
else:
    print("Adulto")

#5. Solicita introducir una contraseña de entre 8 y 14 caracteres inclusive y verifica si es válida.
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if (len(contraseña) >= 8 and len(contraseña) <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6. Indica la categoría de consumo de energía eléctrica del usuario según la cantidad de kWh consumidos en el mes.
kwh = int(input("Ingrese la cantidad de kWh consumidos en el mes: "))
if (kwh < 150):
    print("Consumo bajo")
elif (kwh >= 150 and kwh <= 300):
    print("Consumo medio")
else:
    print("Consumo alto")
    if (kwh > 500):
        print("Considere medidas de ahorro energético")

#7. Detecta vocales al final de la frase o palabra y añade un signo de exclamación.
frase = input("Ingrese una frase o palabra: ")
if (frase[-1] in "aeiouAEIOU"):
    print(f"{frase}!")
else:
    print(frase)

#8. El usuario ingresa su nombre y si prefiere que esté en mayúsculas, minúsculas o solo la primera letra en mayúscula.
nombre = input("Ingrese su nombre: ")
opcion = input(""" Ingrese:
                1. Para que su nombre esté en mayúsculas
                2. Para que su nombre esté en minúsculas
                3. Para que su nombre tenga solo la primera letra en mayúscula
                ---> """)
if (opcion == "1"):
    print(nombre.upper())
elif (opcion == "2"):
    print(nombre.lower())
elif (opcion == "3"):
    print(nombre.title())
else:
    print("Opción no válida")

#9. Clasifica la magnitud de un terremoto según la escala de Richter.
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if (magnitud < 3.0):
    print("Muy leve (imperceptible)")
elif (magnitud >= 3.0 and magnitud < 4.0):
    print("Leve (ligeramente perceptible)")
elif (magnitud >= 4.0 and magnitud < 5.0):
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif (magnitud >= 5.0 and magnitud < 6.0):
    print("Fuerte (puede causar daños en estructuras débiles)")
elif (magnitud >= 6.0 and magnitud < 7.0):
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10. Muestra si el usuario se encuentra en otoño, invierno, primavera o verano según el día, mes y hemisferio ingresado.
hemisferio = input("Ingrese N si es del hemisferio norte, o S si es del hemisferio sur: ")
dia = int(input("Ingrese el día (1-31): "))
mes = int(input("Ingrese el mes (1-12): "))
if (hemisferio.upper() == "N"):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Otoño")

elif (hemisferio.upper() == "S"):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Primavera")
else:
    print("Hemisferio no válido")