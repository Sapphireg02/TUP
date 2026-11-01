import math

# ---EJERCICIO 1---
def imprimir_hola_mundo():
    """Ejercicio 1: Función que imprime 'Hola Mundo!' en la consola."""
    print("Hola Mundo!")

# ---EJERCICIO 2---
def saludar_usuario(nombre):
    """Ejercicio 2: Función que recibe un nombre como parámetro y devuelve un saludo personalizado."""
    return f"Hola {nombre}!"

# Validación de entrada.
def verificar_entrada(entrada):
    """Comprueba que la entrada no esté vacía y contenga solo letras y espacios."""
    entrada = entrada.strip()
    return bool(entrada) and entrada.replace(" ", "").isalpha()

# Validación de entero.
def verificar_entero(entrada):
    """Comprueba que la entrada sea un entero mayor que cero."""
    entrada = entrada.strip()
    return bool(entrada) and entrada.isdecimal() and int(entrada) > 0

# Validación de flotante.
def verificar_flotante(entrada):
    """Comprueba que la entrada sea un número positivo."""
    # Quita espacios y normaliza la coma a punto.
    entrada = entrada.strip().replace(",", ".")
    if not entrada:
        return False

    # Si hay signo, lo elimina para validar el número.
    if entrada[0] in "+-":
        entrada = entrada[1:]

    # Rechaza un signo solo.
    if not entrada:
        return False

    # Rechaza más de un punto decimal.
    if entrada.count(".") > 1:
        return False

    # Si hay punto decimal, valida la parte entera y la decimal.
    if "." in entrada:
        parte_entera, parte_decimal = entrada.split(".", 1)
        # Rechaza si falta la parte decimal.
        if not parte_decimal:
            return False
        # Rechaza si la parte entera no es numérica.
        if not (parte_entera.isdigit() or parte_entera == ""):
            return False
        # Rechaza si la parte decimal no es numérica.
        if not parte_decimal.isdigit():
            return False
    # Si no hay punto, la cadena debe ser un entero válido.
    elif not entrada.isdigit():
        return False

    return True

# Validación de número (sin exigir que sea positivo).
def verificar_numero(entrada):
    """Comprueba que la entrada sea un número, positivo o negativo."""
    entrada = entrada.strip().replace(",", ".")
    if not entrada:
        return False

    # Borra el signo si está presente para validar.
    if entrada[0] in "+-":
        entrada = entrada[1:]

    # Revisa si la entrada quedó vacía después de quitar el signo.
    if not entrada:
        return False

    # Verifica si hay más de un punto decimal.
    if entrada.count(".") > 1:
        return False

    # Verifica que el número tenga un formato válido.
    if "." in entrada:
        parte_entera, parte_decimal = entrada.split(".", 1)
        if not parte_decimal:
            return False
        return (parte_entera.isdigit() or parte_entera == "") and parte_decimal.isdigit()

    return entrada.isdigit()

# Solicita entrada (número sin exigir positivo).
def solicitar_numero(mensaje, mensaje_error):
    """Solicita un número (positivo o negativo) hasta que la entrada sea válida."""
    entrada = input(mensaje).strip()
    while not verificar_numero(entrada):
        print(mensaje_error)
        entrada = input(mensaje).strip()
    return float(entrada.replace(",", "."))

# Solicita entrada (palabras).
def solicitar_entrada(mensaje, mensaje_error):
    """Pide una cadena de texto y repite la consulta hasta que sea una palabra válida."""
    entrada = input(mensaje).strip()
    while not verificar_entrada(entrada):
        print(mensaje_error)
        entrada = input(mensaje).strip()
    return entrada

# Solicita entrada (entero).
def solicitar_entero(mensaje, mensaje_error):
    """Solicita un entero mayor que cero hasta que la entrada sea válida."""
    entrada = input(mensaje).strip()
    while not verificar_entero(entrada):
        print(mensaje_error)
        entrada = input(mensaje).strip()
    return int(entrada)

# Solicita entrada (flotante).
def solicitar_flotante(mensaje, mensaje_error):
    """Solicita un número positivo hasta que la entrada sea válida."""
    entrada = input(mensaje).strip()
    while not verificar_flotante(entrada):
        print(mensaje_error)
        entrada = input(mensaje).strip()
    return float(entrada.replace(",", "."))

# ---EJERCICIO 3---
def informacion_personal(nombre, apellido, edad, residencia):
    """Ejercicio 3: Recibe los datos del usuario y devuelve un mensaje personalizado."""
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

# ---EJERCICIO 4---
def calcular_area_circulo(radio):
    """Ejercicio 4: Recibe el radio de un círculo y devuelve su área."""
    return f"Area del círculo: {math.pi * radio ** 2:.2f}"

def calcular_perimetro_circulo(radio):
    """Ejercicio 4: Recibe el radio de un círculo y devuelve su perímetro."""
    return f"Perímetro del círculo: {2 * math.pi * radio:.2f}"

# ---EJERCICIO 5---
def segundos_a_horas(segundos):
    """Ejercicio 5: Recibe una cantidad de segundos y devuelve la cantidad de horas correspondientes."""
    return segundos / 3600

# ---EJERCICIO 6---
def tabla_multiplicar(numero):
    """Ejercicio 6: Recibe un número y muestra su tabla de multiplicar del 1 al 10."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# ---EJERCICIO 7---
def operaciones_basicas(a, b):
    """Ejercicio 7: Recibe dos números y devuelve una tupla con suma, resta, multiplicación y división."""
    return (a + b, a - b, a * b, a / b)

# ---EJERCICIO 8---
def calcular_imc(peso, altura):
    """Ejercicio 8: Recibe el peso y la altura de una persona y devuelve su IMC."""
    imc = peso / (altura ** 2)
    return f"El IMC es: {imc:.2f}"

# ---EJERCICIO 9---
def celsius_a_fahrenheit(celsius):
    """Ejercicio 9: Recibe una temperatura en grados Celsius y devuelve su equivalente en grados Fahrenheit."""
    return (celsius * 9/5) + 32

# ---EJERCICIO 10---
def calcular_promedio(a, b, c):
    """Ejercicio 10: Recibe tres números y devuelve su promedio."""
    return (a + b + c) / 3

# ---PROGRAMA PRINCIPAL---
if __name__ == "__main__":
    # Ejercicio 1
    imprimir_hola_mundo()

    # Ejercicio 2
    nombre = solicitar_entrada(
        "Ingrese su nombre: ",
        "Ingrese un nombre válido (solo letras y espacios).",
    )
    print(saludar_usuario(nombre))

    # Ejercicio 3
    apellido = solicitar_entrada(
        "Ingrese su apellido: ",
        "Ingrese un apellido válido (solo letras y espacios).",
    )

    edad = solicitar_entero(
        "Ingrese su edad: ",
        "Ingrese una edad válida (un entero mayor que cero).",
    )
    
    residencia = solicitar_entrada(
        "Ingrese su residencia: ",
        "Ingrese una residencia válida (solo letras y espacios).",
    )
    print(informacion_personal(nombre, apellido, edad, residencia))

    # Ejercicio 4
    radio = solicitar_flotante(
        "Ingrese el radio del círculo: ",
        "Ingrese un radio válido (un número mayor que cero).",
    )
    print(calcular_area_circulo(radio))
    print(calcular_perimetro_circulo(radio))

    # Ejercicio 5
    segundos = solicitar_entero(
        "Ingrese la cantidad de segundos: ",
        "Ingrese una cantidad de segundos válida (un entero mayor que cero).",
    )
    print(f"La cantidad de horas correspondientes es: {segundos_a_horas(segundos):.2f}")

    # Ejercicio 6
    numero = solicitar_entero(
        "Ingrese un número para mostrar su tabla de multiplicar: ",
        "Ingrese un número válido (un entero mayor que cero).",
    )
    tabla_multiplicar(numero)

    # Ejercicio 7
    primer_numero = solicitar_numero(
        "Ingrese el primer número para operar: ",
        "Ingrese un número válido.",
    )
    segundo_numero = solicitar_numero(
        "Ingrese el segundo número para operar: ",
        "Ingrese un número válido.",
    )
    if segundo_numero == 0:
        print("No se puede dividir por cero.")
    else:
        suma, resta, multiplicacion, division = operaciones_basicas(primer_numero, segundo_numero)
        print(f"Suma: {suma:.2f}")
        print(f"Resta: {resta:.2f}")
        print(f"Multiplicación: {multiplicacion:.2f}")
        print(f"División: {division:.2f}")

    # Ejercicio 8
    peso = solicitar_flotante(
        "Ingrese su peso en kg: ",
        "Ingrese un peso válido (mayor que cero).",
    )
    altura = solicitar_flotante(
        "Ingrese su altura en metros: ",
        "Ingrese una altura válida (mayor que cero).",
    )
    print(calcular_imc(peso, altura))

    # Ejercicio 9
    celsius = solicitar_numero(
        "Ingrese la temperatura en grados Celsius: ",
        "Ingrese una temperatura válida.",
    )
    print(f"{celsius} °C equivalen a {celsius_a_fahrenheit(celsius):.2f} °F")

    # Ejercicio 10
    a = solicitar_numero(
        "Ingrese el primer número para calcular el promedio: ",
        "Ingrese un número válido.",
    )
    b = solicitar_numero(
        "Ingrese el segundo número para calcular el promedio: ",
        "Ingrese un número válido.",
    )
    c = solicitar_numero(
        "Ingrese el tercer número para calcular el promedio: ",
        "Ingrese un número válido.",
    )
    print(f"El promedio de {a}, {b} y {c} es: {calcular_promedio(a, b, c):.2f}")