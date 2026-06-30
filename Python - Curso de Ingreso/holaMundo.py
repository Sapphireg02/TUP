import math

#1. Imprime por pantalla "Hola Mundo!"
print("Hola Mundo!")

#2. Saluda al usuario por su nombre
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#3. Solicita al usuario su apellido, edad y país de residencia, y luego imprime un mensaje con esa información
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
pais = input("Ingresa tu país de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

#4. Calcula el área y el perímetro de un círculo dado su radio
radio = float(input("Ingresa el radio del círculo: "))
# --Calculo del área--
area = math.pi * radio ** 2
# --Calculo del perímetro--
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area} y el perímetro es: {perimetro}")

#5. Convierte un número de segundos a horas. Una hora equivale a 3600 segundos
segundos = int(input("Ingresa un número de segundos para mostrar a cuantas horas equivale: "))
horas = segundos // 3600
print(f"{segundos} segundos equivalen a {horas} horas")

#6. Solicita al usuario un número y muestra su tabla de multiplicar del 1 al 10
numero = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}: \n {numero} x 1= {1 * numero} \n {numero} x 2= {2 * numero} \n {numero} x 3= {3 * numero} \n {numero} x 4= {4 * numero} \n {numero} x 5= {5 * numero} \n {numero} x 6= {6 * numero} \n {numero} x 7= {7 * numero} \n {numero} x 8= {8 * numero} \n {numero} x 9= {9 * numero} \n {numero} x 10= {10 * numero}")

#7. Solicita al usuario dos números enteros distintos de 0 y muestra la suma, resta, multiplicación y división de ambos
entero1 = int(input("Ingresa el primer número entero distinto de 0: "))
entero2 = int(input("Ingresa el segundo número entero distinto de 0: "))
print(f"El resultado de la suma es: {entero1 + entero2} \n El resultado de la resta es: {entero1 - entero2} \n El resultado de la multiplicación es: {entero1 * entero2} \n El resultado de la división es: {entero1 / entero2}")

#8. Solicita al usuario su altura y peso, y calcula su índice de masa corporal (IMC)
altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal es: {imc}")

#9. Solicita al usuario una temperatura en grados Celsius y la convierte a grados Fahrenheit
temperatura_celsius = float(input("Ingresa una temperatura en grados Celsius para convertir a Fahrenheit: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print(f"{temperatura_celsius} grados Celsius equivalen a {temperatura_fahrenheit} grados Fahrenheit")

#10. Solicita al usuario tres números y calcula su promedio
num1 = float(input("Ingresa el primer número para calcular el promedio: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")
