import random

#1. Muestra todos los números enteros de 0 a 100
for i in range(101):
    print(i)

#2. Determina la cantidad de dígitos que contiene un número entero
entero = int(input("Ingrese un número entero: "))
digitos = len(str(entero))
print(f"El número {entero} tiene {digitos} dígitos")

#3. Suma todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(num1 + 1, num2):
    suma += i
print(f"La suma de los números entre {num1} y {num2} es: {suma}")

#4. Suma números enteros ingresados por el usuario. Se detiene y muestra el total acumulado cuando el usuario ingresa 0
num_acum = 0
num = int(input("Ingrese un número entero (0 para terminar): "))
while num != 0:
    num_acum += num
    num = int(input("Ingrese un número entero (0 para terminar): "))
print(f"El total acumulado es: {num_acum}")

#5. El usuario debe adivinar el número aleatorio entre 0 y 9. Al finalizar muestra la cantidad de intentos
numero_aleatorio = random.randint(0, 9)
intentos = 0
num_usuario = int(input("Adivina el número entre 0 y 9: "))
while num_usuario != numero_aleatorio:
    intentos += 1
    num_usuario = int(input("Incorrecto. Intenta nuevamente: "))
intentos += 1
print(f"Adivinaste! El número era: {numero_aleatorio}. Lo lograste en {intentos} intentos.")

#6. Imprime en pantalla todos los números pares comprendidos entre 0 y 100 en orden decreciente
for i in range(100, -1, -2):
    print(i)

#7. Calcula la suma de todos los números comprendidos entre 0 y un número positivo entero indicado por el usuario
num_positivo = int(input("Ingrese un número positivo entero: "))
while num_positivo < 0:
    print("El número ingresado no es positivo. Por favor, ingrese un número positivo entero.")
    num_positivo = int(input("Ingrese un número positivo entero: "))

calculo_suma = 0
for i in range(num_positivo + 1):
    calculo_suma += i
print(f"La suma de todos los números entre 0 y {num_positivo} es: {calculo_suma}")

#8 y 9. El usuario ingresa 100 números enteros. Muestra cuantos son pares, cuantos son impares, cuantos son positivos y cuantos son negativos. Calcula la media de los valores ingresados
pares = 0
impares = 0
positivos = 0
negativos = 0
media = 0
for i in range(100):
    num_ent = int(input(f"Ingrese el número entero {i + 1}: "))
    media += num_ent
    if num_ent % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num_ent > 0:
        positivos += 1
    else:
        negativos += 1
print("--------------------------------------")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Media de los valores ingresados: {media / 100}")

#10. Invierte el orden de los dígitos de un número ingresado por el usuario
num_a_invertir = input("Ingrese el número a invertir: ")
num_invertido = num_a_invertir[::-1]
print(f"El número invertido es: {num_invertido}")