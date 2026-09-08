# Práctico 5: Listas
import random

# ---Ejercicio 1: Lista con la nota de 10 estudiantes, calcula el promedio y la nota más alta y más baja---

notas_ejercicio_1 = [8, 7, 9, 6, 10, 5, 8, 7, 9, 6]
numero_estudiante = 1

# Muestra la lista completa.
for nota in notas_ejercicio_1:
    print(f"Estudiante {numero_estudiante}: {nota}")
    numero_estudiante += 1

# Muestra el promedio de las notas.
promedio_notas = sum(notas_ejercicio_1) / len(notas_ejercicio_1)
print(f"\nPromedio: {promedio_notas}")

# Indica la nota más alta y la más baja.
nota_maxima = max(notas_ejercicio_1)
nota_minima = min(notas_ejercicio_1)
print(f"\nNota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")

# ---Ejercicio 2: Pide al usuario cargar 5 productos a una lista, la ordena alfabéticamente y pide al usuario eliminar un producto---

productos_ejercicio_2 = []

# Pide al usuario cargar 5 productos a la lista y comprueba que sean letras para poder ordenarlo alfabéticamente después.
for numero_producto in range(5):
    valido = False
    while not valido:
        producto = input(f"Ingrese el producto {numero_producto + 1}: ").lower()
        if producto.replace(" ", "").isalpha():
            productos_ejercicio_2.append(producto)
            valido = True
        else:
            print("Error: El producto debe contener solo letras y espacios. Intente nuevamente.")

# Muestra la lista ordenada alfabéticamente.
productos_ejercicio_2 = sorted(productos_ejercicio_2)
print(f"\nProductos ordenados alfabéticamente: ")
for producto in productos_ejercicio_2:
    print(f"- {producto}")

# Pregunta al usuario qué producto desea eliminar y actualiza la lista.
eliminado = False
while not eliminado:
    producto_a_eliminar = input("\nIngrese el producto que desea eliminar: ").lower()

    # Verifica que sea válido.
    if not producto_a_eliminar.replace(" ", "").isalpha():
        print("Error: El producto debe contener solo letras y espacios.")

    # Elimina al producto si es válido y se encuentra en la lista.
    elif producto_a_eliminar in productos_ejercicio_2:
        productos_ejercicio_2.remove(producto_a_eliminar)
        print(f"Producto eliminado: {producto_a_eliminar}")
        eliminado = True
    else:
        print("El producto no se encuentra en la lista.")

# Lista actualizada.
print(f"\nLista actualizada de productos: ")
for producto in productos_ejercicio_2:
    print(f"- {producto}")

# ---Ejercicio 3: Genera una lista con 15 números al azar entre 1 y 100. Crea una lista con los pares y otra con los impares. Muestra cuantos números tiene cada lista---

# Genera una lista con 15 números al azar entre 1 y 100.
numeros_azar = []
for contador in range(15):
    numeros_azar.append(random.randint(1, 100))
print("Lista de números generada: ")
for numero in numeros_azar:
    print(f" {numero}")

# Crea una lista con los números pares y otra con los impares.
pares = []
impares = []
for numero in numeros_azar:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

#  Muestra cuantos números tiene cada lista.
print(f"Cantidad de números pares: {len(pares)}")
print(f"Cantidad de números impares: {len(impares)}")

# ---Ejercicio 4: Dada una lista con valores repetidos, crea una nueva lista sin elementos repetidos y muestra el resultado---

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
print("Lista de datos original: ")
for dato in datos:
    print(f" {dato}")

# Crea una nueva lista sin elementos repetidos.
sin_repetidos = []
for x in datos:
    if x not in sin_repetidos:
        sin_repetidos.append(x)

# Muestra la lista sin elementos repetidos.
print("Lista sin elementos repetidos: ")
for dato in sin_repetidos:
    print(f" {dato}")

# ---Ejercicio 5: A partir de una lista con nombres de 8 estudiantes, pregunta al usuario si quiere agregar uno nuevo o eliminar uno existente. Muestra la lista actualizada---

estudiantes_presentes = ["guillermina", "juan", "maria", "pedro", "luis", "carla", "jose", "laura"]

print("Lista de estudiantes:")
for estudiante in estudiantes_presentes:
    print(f"- {estudiante}")

# Agrega un nuevo estudiante o elimina uno existente.
continuar = True
while continuar:
    accion_valida = False
    while not accion_valida:
        accion = input("¿Desea agregar un nuevo estudiante (1) o eliminar uno existente (2)? ").lower()
        
        if accion == "1":
            nombre_valido = False
            while not nombre_valido:
                nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ").lower()
                # Validación.
                if nuevo_estudiante.replace(" ", "").isalpha():
                    # Agrega el nuevo estudiante a la lista.
                    estudiantes_presentes.append(nuevo_estudiante)
                    print(f"Estudiante agregado: {nuevo_estudiante}")
                    nombre_valido = True
                    accion_valida = True
                else:
                    print("Error: El nombre debe contener solo letras y espacios. Intente nuevamente.")

        elif accion == "2":
            nombre_valido = False
            while not nombre_valido:
                estudiante_a_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ").lower()
                # Validación.
                if estudiante_a_eliminar.replace(" ", "").isalpha():
                    # Elimina al estudiante si se encuentra en la lista.
                    if estudiante_a_eliminar in estudiantes_presentes:
                        estudiantes_presentes.remove(estudiante_a_eliminar)
                        print(f"Estudiante eliminado: {estudiante_a_eliminar}")
                        nombre_valido = True
                        accion_valida = True
                    else:
                        print("El estudiante no se encuentra en la lista. Intente nuevamente.")
                else:
                    print("Error: El nombre debe contener solo letras y espacios. Intente nuevamente.")
        else:
            print("Acción inválida. Por favor, ingrese '1' para agregar o '2' para eliminar.")
    
    # Pregunta si desea continuar modificando.
    mas_cambios = input("\n¿Desea realizar otra acción? (s/n): ").lower()
    if mas_cambios != "s":
        continuar = False

# Muestra la lista actualizada de estudiantes.
print("\nLista actualizada de estudiantes:")
for estudiante in estudiantes_presentes:
    print(f"- {estudiante}")

# ---Ejercicio 6: Dada una lista con 7 números, rota todos los elementos una posición hacia la derecha (el último pasa a ser el primero)---
numeros_rotados = [1, 2, 3, 4, 5, 6, 7]
print ("\nLista original de números: ")
for numero in numeros_rotados:
    print(f" {numero}")
    
# Rota los elementos una posición hacia la derecha.
numeros_rotados.insert(0, numeros_rotados.pop())
print("\nLista de números rotada hacia la derecha:")
for numero in numeros_rotados:
    print(f" {numero}")

# ---Ejercicio 7: Con una matriz de 7x2 con las temperaturas mínimas y máximas de una semana, calcula el promedio y muestra que día se registró la mayor amplitud térmica---

temperaturas = [
    [7, 27],  # Lunes
    [10, 31],  # Martes
    [8, 22],  # Miércoles
    [8, 21],  # Jueves
    [3, 14],  # Viernes
    [2, 13],  # Sábado
    [5, 18]   # Domingo
]

# Promedio de mínimas y máximas.
suma_minimas = 0
suma_maximas = 0
# Se suman las máximas y mínimas de cada día.
for temperatura in temperaturas:
    suma_minimas += temperatura[0]
    suma_maximas += temperatura[1]

# Calcula el promedio.
promedio_minimas = suma_minimas / len(temperaturas)
promedio_maximas = suma_maximas / len(temperaturas)

print(f"Promedio de temperaturas mínimas: {promedio_minimas:.2f}")
print(f"Promedio de temperaturas máximas: {promedio_maximas:.2f}")

# Muestra en que día se registró la mayor amplitud térmica.
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
mayor_amplitud = 0
dia_mayor_amplitud = ""

for numero_dia in range(len(temperaturas)):
    # Resta la mínima a la máxima para obtener la amplitud térmica de cada día.
    amplitud = temperaturas[numero_dia][1] - temperaturas[numero_dia][0]

    # Guarda la mayor amplitud y el día correspondiente.
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias_semana[numero_dia]

print(f"Mayor amplitud térmica: {mayor_amplitud}°C, el día {dia_mayor_amplitud}")

# ---Ejercicio 8: Matriz con notas de 5 estudiantes en 3 materias, muestra el promedio de cada estudiante y de cada materia---

materias = ["Programación", "Matemática", "Inglés"]

notas_estudiantes = [
    [8, 7, 9],
    [6.50, 8, 7],
    [10, 9.25, 8],
    [7, 6, 8],
    [9.15, 10, 9]
]

# Muestra el promedio de cada estudiante.
print("\nPromedio de cada estudiante:")
for estudiante_matriz in range(len(notas_estudiantes)):
    suma_notas = 0
    for nota in notas_estudiantes[estudiante_matriz]:
        suma_notas += nota
    promedio_estudiante = suma_notas / len(notas_estudiantes[estudiante_matriz])
    print(f"Estudiante {estudiante_matriz + 1}: {promedio_estudiante:.2f}")

# Muestra el promedio de cada materia.
print("\nPromedio de cada materia:")
for numero_materia in range(len(materias)):
    suma_notas = 0
    for estudiante in notas_estudiantes:
        suma_notas += estudiante[numero_materia]
    promedio_materia = suma_notas / len(notas_estudiantes)
    print(f"{materias[numero_materia]}: {promedio_materia:.2f}")

# ---Ejercicio 9: Ta-Te-Ti---

tateti=[
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jugador = "X"
numero_jugador = 1
ganador = False
turnos = 0

while not ganador and turnos < 9:
    print("")
    # Muestra el tablero.
    for fila in tateti:
        print(fila)

    posicion_valida = False
    while not posicion_valida:
        posicion_fila = input(f"Jugador {numero_jugador}, ingrese la fila (1 a 3) para colocar ({jugador}): ")
        posicion_columna = input(f"Jugador {numero_jugador}, ingrese la columna (1 a 3) para colocar ({jugador}): ")

        # Verifica que la fila y la columna sean números y estén dentro del rango permitido.
        if posicion_fila.isdigit() and posicion_columna.isdigit():
            posicion_fila = int(posicion_fila)
            posicion_columna = int(posicion_columna)

            if 1 <= posicion_fila <= 3 and 1 <= posicion_columna <= 3:
                posicion_valida = True
            else:
                print("La fila y la columna deben estar entre 1 y 3.")
        else:
            print("La fila y la columna deben ser números.")

    # Se resta 1 porque las listas empiezan en la posición 0.
    posicion_fila -= 1
    posicion_columna -= 1

    # Comprobación de que la posición ingresada esté vacía.
    if tateti[posicion_fila][posicion_columna] == "-":
        tateti[posicion_fila][posicion_columna] = jugador
        turnos += 1

        # Muestra el tablero después de cada jugada válida.
        for fila in tateti:
            print(fila)

        # Verifica si hay un ganador.
        hay_ganador = False
        linea_ganadora = []
        if (tateti[0][0] == jugador and tateti[0][1] == jugador and tateti[0][2] == jugador) or (tateti[1][0] == jugador and tateti[1][1] == jugador and tateti[1][2] == jugador) or (tateti[2][0] == jugador and tateti[2][1] == jugador and tateti[2][2] == jugador):
            hay_ganador = True
            if tateti[0][0] == jugador and tateti[0][1] == jugador and tateti[0][2] == jugador:
                linea_ganadora = [[0, 0], [0, 1], [0, 2]]
            elif tateti[1][0] == jugador and tateti[1][1] == jugador and tateti[1][2] == jugador:
                linea_ganadora = [[1, 0], [1, 1], [1, 2]]
            else:
                linea_ganadora = [[2, 0], [2, 1], [2, 2]]
        elif (tateti[0][0] == jugador and tateti[1][0] == jugador and tateti[2][0] == jugador) or (tateti[0][1] == jugador and tateti[1][1] == jugador and tateti[2][1] == jugador) or (tateti[0][2] == jugador and tateti[1][2] == jugador and tateti[2][2] == jugador):
            hay_ganador = True
            if tateti[0][0] == jugador and tateti[1][0] == jugador and tateti[2][0] == jugador:
                linea_ganadora = [[0, 0], [1, 0], [2, 0]]
            elif tateti[0][1] == jugador and tateti[1][1] == jugador and tateti[2][1] == jugador:
                linea_ganadora = [[0, 1], [1, 1], [2, 1]]
            else:
                linea_ganadora = [[0, 2], [1, 2], [2, 2]]
        elif (tateti[0][0] == jugador and tateti[1][1] == jugador and tateti[2][2] == jugador) or (tateti[0][2] == jugador and tateti[1][1] == jugador and tateti[2][0] == jugador):
            hay_ganador = True
            if tateti[0][0] == jugador and tateti[1][1] == jugador and tateti[2][2] == jugador:
                linea_ganadora = [[0, 0], [1, 1], [2, 2]]
            else:
                linea_ganadora = [[0, 2], [1, 1], [2, 0]]

        # GANADOR
        if hay_ganador:
            print(f"\nGANÓ EL JUGADOR {numero_jugador} !!!!!!")
            
            for fila_tablero in range(3):
                fila_mostrada = []
                for columna_tablero in range(3):
                    if [fila_tablero, columna_tablero] in linea_ganadora:
                        fila_mostrada.append("[" + tateti[fila_tablero][columna_tablero] + "]")
                    else:
                        fila_mostrada.append(tateti[fila_tablero][columna_tablero])
                print(fila_mostrada)
            ganador = True

        # Verifica si hay empate.
        elif turnos == 9:
            print("Empate")
            ganador = True

        # Cambia al jugador 2.
        elif jugador == "X":
            jugador = "O"
            numero_jugador = 2
            print(f"Turno del jugador {numero_jugador}")

        # Cambia al jugador 1.
        else:
            jugador = "X"
            numero_jugador = 1
            print(f"Turno del jugador {numero_jugador}")
    else:
        print("Posición ocupada. Intente nuevamente.")

# ---Ejercicio 10: Una tienda registra las ventas de 4 productos durante 7 días, muestra el total vendido, el día con mayores ventas totales y el producto más vendido de la semana---

productos = ["Llaveros", "Pines", "Stickers", "Figuras 3D"]
ventas = [
    [10, 12, 8, 15, 9, 11, 14],    # Llaveros
    [15, 18, 14, 20, 13, 17, 19],  # Pines
    [20, 22, 19, 25, 18, 21, 24],  # Stickers
    [25, 30, 28, 35, 27, 29, 32]   # Figuras 3D
]

# Muestra el total vendido por cada producto y busca el producto más vendido en la semana.
print("\nTotal vendido por cada producto:")
mayor_producto = 0
producto_mas_vendido = ""

# Pasa por cada producto.
for producto_index in range(len(productos)):
    total_producto = 0
    # Pasa por cada día de determinado producto y suma las ventas.
    for venta in ventas[producto_index]:
        total_producto += venta
    print(f"{productos[producto_index]}: {total_producto}")

    if total_producto > mayor_producto:
        mayor_producto = total_producto
        producto_mas_vendido = productos[producto_index]

# Muestra el día con mayores ventas totales.
print("\nDía con mayores ventas totales:")
max_ventas = 0
dias_ventas = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dia_mayores_ventas = ""

# Suma las ventas de cada día.
for dia_ventas in range(len(dias_ventas)):
    total_dia = 0
    for producto in ventas:
        total_dia += producto[dia_ventas]

# Compara el total de ventas del día con el máximo registrado hasta ahora.
    if total_dia > max_ventas:
        max_ventas = total_dia
        dia_mayores_ventas = dias_ventas[dia_ventas]

print(f"{dia_mayores_ventas}: {max_ventas} ventas")

# Indica el producto más vendido de la semana.
print(f"\nProducto más vendido de la semana: {producto_mas_vendido}: {mayor_producto} ventas")

# ---Ejercicio 11: Crea una lista con nombres de 10 estudiantes, busca nombres, indica si se encuentra en la lista, muestra la posición y si no se encuentra informa que no está en la lista---

estudiantes = ["guillermina", "juan", "maria", "pedro", "luis", "carla", "jose", "laura", "ana", "carlos"]

nombre_a_buscar = ""
while nombre_a_buscar not in estudiantes:
    nombre_a_buscar = input("\nIngrese el nombre del estudiante que desea buscar: ").lower()

    if not nombre_a_buscar.replace(" ", "").isalpha():
        print("Error: El nombre debe contener solo letras y espacios. Intente nuevamente.")
    elif nombre_a_buscar not in estudiantes:
        print(f"El estudiante {nombre_a_buscar} no se encuentra en la lista. Intente nuevamente.")

# Busca el nombre en la lista.
posicion = estudiantes.index(nombre_a_buscar)
print(f"El estudiante {nombre_a_buscar} se encuentra en la posición {posicion} de la lista.")

# ---Ejercicio 12: Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista. Mostrar la lista original, ordenarla de menor a mayor, ordenarla de mayor a menor, uso de sorted() y reverse---

num_enteros = []
# Pide al usuario que ingrese 8 números enteros y los almacena en la lista.
for numero_ingresado in range(8):
    numero_valido = False
    while not numero_valido:
        numero = input(f"\nIngrese el número entero nro {numero_ingresado + 1}: ")
        # lstrip("-") permite que el número sea negativo y verifica que solo tenga un signo negativo.
        if numero.lstrip("-").isdigit() and numero.count("-") <= 1:
            num_enteros.append(int(numero))
            numero_valido = True
        else:
            print("Debe ingresar un número entero válido.")

print("Lista original:")
for numero in num_enteros:
    print(numero)

print("Lista ordenada de menor a mayor:")
orden_menor_mayor = sorted(num_enteros)
for numero in orden_menor_mayor:
    print(numero)

print("\nLista ordenada de mayor a menor:")
orden_mayor_menor = sorted(num_enteros, reverse=True)
for numero in orden_mayor_menor:
    print(numero)

# ---Ejercicio 13: Dada una lista de puntajes de un videojuego, muestra el puntaje más alto y más bajo, hace un ranking e indica en que posicion se encuentra el puntaje 990---
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print(f"\nPuntaje más alto: {max(puntajes)}")
print(f"Puntaje más bajo: {min(puntajes)}")
print("\nRanking de puntajes:")
ranking = sorted(puntajes, reverse=True)
for posicion in range(len(ranking)):
    puntaje = ranking[posicion]
    print(puntaje)
    if puntaje == 990:
        posicion_ranking = posicion + 1
print(f"\nPosición del puntaje 990 en el ranking: {posicion_ranking}")

print("\nRanking top 3:")
for puntaje in ranking[:3]:
    print(puntaje)