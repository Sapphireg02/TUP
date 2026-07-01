# Seguimiento de calificaciones parciales y diagnóstico automatizado de rendimiento.
cantidad_parciales = 0
cantidad_parciales = input("Ingrese la cantidad total de parciales rendidos: ")

#Verifica si el valor ingresado no es válido (no es entero) o no está entre 1 y 10.
while not cantidad_parciales.isdigit() or not (1 <= int(cantidad_parciales) <= 10):
    print(f"----El valor ingresado: {cantidad_parciales}, no es válido----\nDebe ser un número entero entre 1 y 10.")
    cantidad_parciales = input("Ingrese la cantidad total de parciales rendidos: ")

#Convierte el valor ingresado en un número entero. Para la verificación de isdigit() se necesita que el número sea un string.
cantidad_parciales = int(cantidad_parciales)

#Si el número ingresado es un número entero entre 1 y 10 continua con el programa.
#Permite salir del bucle while si el valor ingresado es válido.
valido = False
#Inicialización de variables para notas.
nota_maxima = 0
nota_minima = 10
suma_notas = 0
notas_aprobadas = 0
notas_desaprobadas = 0
#Se solicitan las notas obtenidas en cada parcial.
for i in range(cantidad_parciales):
    parcial = input(f"Ingrese la calificación del parcial {i + 1}. Debe ser un número entre 0 y 10: ")

    #Verifica si el valor ingresado no es válido (es una cadena de texto) o no está entre 0 y 10.
    while (not parcial.isdigit() or not (0 <= float(parcial) <= 10)) and valido == False:
        #Si el número es decimal es válido y no muestra el mensaje de error. Se realizó esta verificación porque isdigit() no reconoce los números decimales.
        if "." in parcial:
            valido = True
        else: 
            print(f"----El valor ingresado: {parcial}, no es válido----\nDebe ser un número entre 0 y 10.")
            parcial = input(f"Ingrese la calificación del parcial {i + 1}: ")

    #Convierte el valor en un número decimal.
    parcial = float(parcial)

    #Verificación del valor ingresado.
    print(f"----- * -----\nSe ha registrado la calificación del parcial {i + 1}: {parcial}\n----- * -----")
    #Guarda la nota máxima.
    if parcial > nota_maxima:
        nota_maxima = parcial
    #Guarda la nota mínima.
    if parcial < nota_minima:
        nota_minima = parcial
    #Acumula el valor para el posterior cálculo del promedio.
    suma_notas += parcial
    #Clasifica y contabiliza las notas aprobadas y desaprobadas.
    if parcial >= 6:
        notas_aprobadas += 1
    else:
        notas_desaprobadas += 1
promedio_notas = suma_notas / cantidad_parciales
print(f"----- * -----\nSe han registrado {cantidad_parciales} parciales.\nLa nota máxima obtenida es: {nota_maxima}\nLa nota mínima obtenida es: {nota_minima}\nEl promedio de las notas es: {promedio_notas}\nCantidad de parciales aprobados: {notas_aprobadas}\nCantidad de parciales desaprobados: {notas_desaprobadas}\n----- * -----")

#--Diagnóstico de condición final--
#El sistema evalúa el promedio final y determina de forma automática la situación académica del estudiante.
print("Situación académica del estudiante: ")
if promedio_notas >= 7:
    print("Promocionado")
elif promedio_notas >= 4 and promedio_notas < 7:
    print("Regular")
else:
    print("Libre")