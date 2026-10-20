# ---Ejercicio 5---
def palabras_unicas(frase):
    """Devuelve un conjunto de palabras únicas de la frase."""
    palabras = frase.split()
    return set(palabras)

def contar_palabras(frase):
    """Devuelve un diccionario con la cantidad de veces que aparece cada palabra."""
    palabras = frase.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

# ---Ejercicio 6---
def ingresar_alumnos():
    """Solicita nombres de 3 alumnos y 3 notas para cada uno."""
    alumnos = {}
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ").strip().title()
        while nombre == "" or nombre in alumnos:
            if nombre == "":
                print("El nombre no puede estar vacío.")
            else:
                print("Ese nombre ya fue ingresado. Ingrese uno diferente.")
            nombre = input(f"Ingrese el nombre del alumno {i + 1}: ").strip().title()
        notas = []
        for j in range(3):
            nota_ingresada = input(f"Ingrese la nota {j + 1} para {nombre}: ")
            while not nota_ingresada.isdigit() or int(nota_ingresada) < 1 or int(nota_ingresada) > 10:
                print("La nota debe ser un número entero del 1 al 10.")
                nota_ingresada = input(f"Ingrese la nota {j + 1} para {nombre}: ")
            nota = int(nota_ingresada)
            notas.append(nota)
        alumnos[nombre] = tuple(notas)
    return alumnos

def calcular_promedio(notas):
    """Calcula el promedio de notas."""
    return sum(notas) / len(notas)

# ---Ejercicio 7---
def conjunto_asistencia(asistencias):
    """Devuelve un conjunto con los nombres únicos de los asistentes."""
    return set(asistencias)

def mostrar_cantidad_asistencias(asistencias, asistencia_unica):
    """Muestra cuántas veces asistió cada persona."""
    for persona in asistencia_unica:
        print(f"{persona}: asistió {asistencias.count(persona)} veces")

# ---Ejercicio 8---
def ingresar_cantidad(mensaje):
    """Solicita una cantidad entera no negativa."""
    cantidad = input(mensaje).strip()
    while not cantidad.isdigit():
        print("Ingrese una cantidad válida usando números enteros.")
        cantidad = input(mensaje).strip()
    return int(cantidad)

def gestionar_stock(stock):
    """Permite agregar productos y sus cantidades al stock. Tambien permite consultar stock de un producto."""
    continuar = "s"
    while continuar.lower() == "s":
        producto = input("Ingrese el nombre del producto: ").strip().title()
        while producto == "":
            print("El nombre del producto no puede estar vacío.")
            producto = input("Ingrese el nombre del producto: ").strip().title()
        if producto in stock:
            print(f"El producto {producto} ya existe en el stock.")
            print(f"Stock actual de {producto}: {stock[producto]} unidades.")
            agregar = input("¿Desea agregar unidades a este producto? (s/n): ")
            if agregar.lower() == "s":
                cantidad = ingresar_cantidad(f"Ingrese la cantidad de unidades a agregar para {producto}: ")
                stock[producto] += cantidad
                print(f"Se han agregado {cantidad} unidades a {producto}. Total: {stock[producto]} unidades.")
        else:
            cantidad = ingresar_cantidad(f"Ingrese la cantidad de unidades para {producto}: ")
            stock[producto] = cantidad
            print(f"Se ha agregado el producto {producto} con {cantidad} unidades al stock.")
        continuar = input("¿Desea continuar agregando productos? (s/n): ").strip().lower()
        while continuar not in ("s", "n"):
            print("Respuesta inválida. Ingrese 's' para continuar o 'n' para salir.")
            continuar = input("¿Desea continuar agregando productos? (s/n): ").strip().lower()

def mostrar_stock(stock):
    """Muestra el stock de productos."""
    print("Stock de productos:")
    for producto, cantidad in stock.items():
        print(f"{producto}: {cantidad} unidades")

# ---Ejercicio 9---
def dia_valido(dia):
    """Comprueba que el día sea uno de los días de la semana."""
    dias_semana = (
        "lunes",
        "martes",
        "miércoles",
        "jueves",
        "viernes",
        "sábado",
        "domingo"
    )
    return dia.strip().lower() in dias_semana

def hora_valida(hora):
    """Comprueba que la hora tenga formato HH:MM y esté dentro del rango."""
    if len(hora) != 5 or hora[2] != ":":
        return False
    if not hora[:2].isdigit() or not hora[3:].isdigit():
        return False

    horas = int(hora[:2])
    minutos = int(hora[3:])
    return horas >= 0 and horas <= 23 and minutos >= 0 and minutos <= 59

def consultar_agenda(agenda):
    """Consulta la actividad programada para un día y una hora."""
    dia = input("Ingrese el día: ").strip().lower()
    while not dia_valido(dia):
        print("Día inválido. Ingrese un día de la semana.")
        dia = input("Ingrese el día: ").strip().lower()
    hora = input("Ingrese la hora (HH:MM): ").strip()
    while not hora_valida(hora):
        print("Hora inválida. Use el formato HH:MM, entre 00:00 y 23:59.")
        hora = input("Ingrese la hora (HH:MM): ").strip()
    actividad = agenda.get((dia, hora))

    if actividad is None:
        print("No hay actividades programadas para ese día y hora.")
    else:
        print(f"Actividad: {actividad}")

# ---Ejercicio 10---
def invertir_diccionario(diccionario):
    """Invierte un diccionario, intercambiando claves y valores."""
    return {valor: clave for clave, valor in diccionario.items()}

def main():
    # Ejercicio 5: Palabras únicas y conteo. Solicita una frase e imprime las palabras únicas y un diccionario con la cantidad de veces que aparece cada palabra.
    frase = input("Ingrese una frase: ").lower()
    palabras_unicas_set = palabras_unicas(frase)
    conteo_palabras = contar_palabras(frase)
    print(f"Palabras únicas: {palabras_unicas_set}")
    print(f"Conteo de palabras: {conteo_palabras}")

    #Ejercicio 6: Promedio de notas por alumno. Se ingresan nombres de tres alumnos y sus notas, luego se calcula el promedio.
    alumnos = ingresar_alumnos()
    for nombre, notas in alumnos.items():
        promedio = calcular_promedio(notas)
        print(f"{nombre}: {notas} (Promedio: {promedio:.2f})")

    # Ejercicio 7: Asistencia a una capacitación. Muestra la asistencia a la capacitación.
    asistencias = ["Ana", "Luis", "Ana", "Maria", "Luis", "Pedro", "Ana"]
    print(f"Asistencia a la capacitación: {asistencias}")
    asistencia_unica = conjunto_asistencia(asistencias)
    print(f"Asistieron al menos una vez: {asistencia_unica}")
    mostrar_cantidad_asistencias(asistencias, asistencia_unica)

    # Ejercicio 8: Stock de productos. Consultar stock, agregar unidades, agregar un nuevo producto.
    stock = {}
    gestionar_stock(stock)
    mostrar_stock(stock)

    # Ejercicio 9: Agenda por día y hora.
    agenda = {
            ("lunes", "10:00"): "Reunión",
            ("martes", "15:00"): "Clase de Matemática",
            ("miércoles", "09:00"): "Turno Dentista",
            ("jueves", "14:00"): "Almuerzo familiar"
        }
    consultar_agenda(agenda)

    # Ejercicio 10: Invierte un diccionario.
    original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
    invertido = invertir_diccionario(original)
    print(f"Diccionario original: {original}")
    print(f"Diccionario invertido: {invertido}")

if __name__ == "__main__":
    main()