import math

print("Hola Mundo!")

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
pais = input("Ingresa tu país de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area} y el perímetro es: {perimetro}")

segundos = int(input("Ingresa un número de segundos para mostrar a cuantas horas equivale: "))
horas = segundos // 3600
print(f"{segundos} segundos equivalen a {horas} horas")

numero = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}: \n {numero} x 1= {1 * numero} \n {numero} x 2= {2 * numero} \n {numero} x 3= {3 * numero} \n {numero} x 4= {4 * numero} \n {numero} x 5= {5 * numero} \n {numero} x 6= {6 * numero} \n {numero} x 7= {7 * numero} \n {numero} x 8= {8 * numero} \n {numero} x 9= {9 * numero} \n {numero} x 10= {10 * numero}")

entero1 = int(input("Ingresa el primer número entero distinto de 0: "))
entero2 = int(input("Ingresa el segundo número entero distinto de 0: "))
print(f"El resultado de la suma es: {entero1 + entero2} \n El resultado de la resta es: {entero1 - entero2} \n El resultado de la multiplicación es: {entero1 * entero2} \n El resultado de la división es: {entero1 / entero2}")

altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal es: {imc}")

temperatura_celsius = float(input("Ingresa una temperatura en grados Celsius para convertir a Fahrenheit: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print(f"{temperatura_celsius} grados Celsius equivalen a {temperatura_fahrenheit} grados Fahrenheit")

num1 = float(input("Ingresa el primer número para calcular el promedio: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")