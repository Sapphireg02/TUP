# Contexto: Hay dos días de atención: Lunes y Martes. Cada día tiene cupos fijos: Lunes: 4 turnos, Martes: 3 turnos.
salir = False
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

#---NOMBRE DEL OPERADOR---
nombre = input("Ingrese el nombre del operador: ").lower().replace(" ", "")
# Valida que sean solo letras y elimina espacios.
while nombre == "" or not nombre.isalpha():
    print("Nombre inválido. Por favor, ingrese solo letras.")
    nombre = input("Ingrese el nombre del operador: ").lower().replace(" ", "")

#---MENÚ---
while salir==False:
    opc = input("""-------------------- MENU DE OPCIONES ----------------------
    1) Reservar turno
    2) Cancelar turno
    3) Ver agenda del día
    4) Ver resumen general
    5) Cerrar sistema
    """)

    # Valida que la opción sea un número entre 1 y 5.
    if not opc.isdigit() or (opc != "1" and opc != "2" and opc != "3" and opc != "4" and opc != "5"):
        print("Opción inválida. Ingrese un número del 1 al 5.")
        continue

    # Reservar turno.
    if opc == "1":
        dia = input("Ingrese el número correspondiente al día a reservar: (1) Lunes o (2) Martes:")
        nombre_paciente = input("Ingrese el nombre del paciente: ").lower().replace(" ", "")

        while nombre_paciente == "" or not nombre_paciente.isalpha():
            print("Nombre inválido. Por favor, ingrese solo letras.")
            nombre_paciente = input("Ingrese el nombre del paciente: ").lower().replace(" ", "")

        # Reserva el día deseado.
        #-LUNES-
        if dia == "1":
            if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                print("El paciente ya tiene un turno reservado para el lunes.")
            elif lunes1 == "":
                lunes1 = nombre_paciente
                print("Turno reservado correctamente.")
            elif lunes2 == "":
                lunes2 = nombre_paciente
                print("Turno reservado correctamente.")
            elif lunes3 == "":
                lunes3 = nombre_paciente
                print("Turno reservado correctamente.")
            elif lunes4 == "":
                lunes4 = nombre_paciente
                print("Turno reservado correctamente.")
            else:
                print("No hay turnos disponibles para el lunes.")
        #-MARTES-
        elif dia == "2":
            if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                print("El paciente ya tiene un turno reservado para el martes.")
            elif martes1 == "":
                martes1 = nombre_paciente
                print("Turno reservado correctamente.")
            elif martes2 == "":
                martes2 = nombre_paciente
                print("Turno reservado correctamente.")
            elif martes3 == "":
                martes3 = nombre_paciente
                print("Turno reservado correctamente.")
            else:
                print("No hay turnos disponibles para el martes.")
        else:
            print("Día inválido. Ingrese 1 para lunes o 2 para martes.")

    # Cancelar turno.
    elif opc == "2":
        dia = input("Ingrese el número correspondiente al día a cancelar: (1) Lunes o (2) Martes:")
        nombre_paciente = input("Ingrese el nombre del paciente: ").lower().replace(" ", "")

        while nombre_paciente == "" or not nombre_paciente.isalpha():
            print("Nombre inválido. Por favor, ingrese solo letras.")
            nombre_paciente = input("Ingrese el nombre del paciente: ").lower().replace(" ", "")

        # Cancela el turno del día deseado.
        #-LUNES-
        if dia == "1":
            if nombre_paciente == lunes1:
                lunes1 = ""
                print("Turno cancelado correctamente.")
            elif nombre_paciente == lunes2:
                lunes2 = ""
                print("Turno cancelado correctamente.")
            elif nombre_paciente == lunes3:
                lunes3 = ""
                print("Turno cancelado correctamente.")
            elif nombre_paciente == lunes4:
                lunes4 = ""
                print("Turno cancelado correctamente.")
            else:
                print("El paciente no tiene un turno reservado para el lunes.")
        #-MARTES-
        elif dia == "2":
            if nombre_paciente == martes1:
                martes1 = ""
                print("Turno cancelado correctamente.")
            elif nombre_paciente == martes2:
                martes2 = ""
                print("Turno cancelado correctamente.")
            elif nombre_paciente == martes3:
                martes3 = ""
                print("Turno cancelado correctamente.")
            else:
                print("El paciente no tiene un turno reservado para el martes.")
        else:
            print("Día inválido. Ingrese 1 para lunes o 2 para martes.")

    # Ver agenda del día.
    elif opc == "3":
        print(f"""---*---Agenda del día:---*---
    Lunes:
    1) {lunes1 if lunes1 != "" else "Libre"}
    2) {lunes2 if lunes2 != "" else "Libre"}
    3) {lunes3 if lunes3 != "" else "Libre"}
    4) {lunes4 if lunes4 != "" else "Libre"}

    Martes:
    1) {martes1 if martes1 != "" else "Libre"}
    2) {martes2 if martes2 != "" else "Libre"}
    3) {martes3 if martes3 != "" else "Libre"}
---*---*---*---*---*---*---*---
        """)

    # Ver resumen general.
    elif opc == "4":
        ocupados_lunes = 0
        ocupados_martes = 0
        # Cuenta los turnos ocupados para cada día.
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1
        # Calcula los turnos disponibles para cada día.
        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes
        # Determina cuál día tiene más turnos ocupados.
        if ocupados_lunes > ocupados_martes:
            dia_mas_ocupado = "Lunes"
        elif ocupados_martes > ocupados_lunes:
            dia_mas_ocupado = "Martes"
        else:
            dia_mas_ocupado = "Ambos días tienen la misma cantidad de turnos ocupados"

        print(f"""---*---Resumen general:---*---
    Lunes:
    Turnos ocupados: {ocupados_lunes}
    Turnos disponibles: {disponibles_lunes}

    Martes:
    Turnos ocupados: {ocupados_martes}
    Turnos disponibles: {disponibles_martes}

    Día con más turnos ocupados: {dia_mas_ocupado}
    """)

    # Cerrar sistema.
    elif opc == "5":
        salir = True