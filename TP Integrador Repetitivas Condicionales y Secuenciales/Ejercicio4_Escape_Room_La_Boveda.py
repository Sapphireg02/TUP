# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

turno = 1
antispam = 0

#---NOMBRE DEL AGENTE---
nombre = input("Ingrese su nombre: ").lower().replace(" ", "")
# Valida que sean solo letras y elimina espacios.
while nombre == "" or not nombre.isalpha():
    print("Nombre inválido. Por favor, ingrese solo letras.")
    nombre = input("Ingrese su nombre: ").lower().replace(" ", "")

#---MENÚ DE ACCIONES JUEGO---
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma == False or tiempo >= 3:
        print(f"*---Turno {turno}---* \nEnergía: {energia} \nTiempo: {tiempo} \nCerraduras abiertas: {cerraduras_abiertas}")
        opc = input(f""" ---MENÚ DE ACCIONES---
    1. Forzar cerradura (-20 energía, -2 tiempo)
    2. Hackear panel (-10 energía, -3 tiempo)
    3. Descansar (+15 energía (max 100), -1 tiempo, SI LA ALARMA ESTÁ ACTIVADA -10 ENERGÍA EXTRA)
    """)
    # Valida que la opción ingresada sea un número del 1 al 3.
        while not opc.isdigit() or not 1 <= int(opc) <= 3:
            print("Opción inválida. Ingrese una opción del 1 al 3.")
            opc = input(f""" ---MENÚ DE ACCIONES---
    1. Forzar cerradura (-20 energía, -2 tiempo)
    2. Hackear panel (-10 energía, -3 tiempo)
    3. Descansar (+15 energía (max 100), -1 tiempo, SI LA ALARMA ESTÁ ACTIVADA -10 ENERGÍA EXTRA)
    """)

    # ---FORZAR CERRADURA---
        if opc == "1":
            energia -= 20
            tiempo -= 2
            antispam += 1
            # Regla anti spam.
            if antispam == 3:
                print("¡¡¡ALARMA ACTIVADA!!! La cerradura se trabó.")
                alarma = True

            else:
                if energia < 40:
                    num_alarma = input("Riesgo de alarma. Ingrese un número del 1 al 3: ")
                    # Valida que el número ingresado sea un dígito y esté entre 1 y 3.
                    while not num_alarma.isdigit() or not 1 <= int(num_alarma) <= 3:
                        print("Opción inválida. Ingrese un número del 1 al 3.")
                        num_alarma = input("Riesgo de alarma. Ingrese un número del 1 al 3: ")
                    num_alarma = int(num_alarma)
                    if num_alarma == 3:
                        alarma = True
                        print("¡¡¡ALARMA ACTIVADA!!!")
                # Si no hay alarma se abre la cerradura.
                if alarma == False:
                    cerraduras_abiertas += 1
                    print(f"Cerradura forzada con éxito. Cerraduras abiertas: {cerraduras_abiertas}")

    # ---HACKEAR PANEL---
        elif opc == "2":
            energia -= 10
            tiempo -= 3
            antispam = 0
            for paso in range(4):
                codigo_parcial += "A"
                print(f"Hackeando panel: paso {paso + 1}/4")
                print(f"Código parcial: {codigo_parcial}")

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print(f"Panel hackeado con éxito. Cerraduras abiertas: {cerraduras_abiertas}")
                codigo_parcial = ""


    # ---DESCANSAR---
        elif opc == "3":
            antispam = 0
            if alarma:
                energia -= 10
            else:
                # min no permite que la energía supere 100.
                energia = min(energia + 15, 100)
                if energia == 100:
                    print("Energía al máximo.")
            tiempo -= 1

                
        turno += 1

    # Cuando la alarma está activada y el tiempo es menor a 3, se termina el juego.
    else:
        break



if alarma and tiempo < 3 and cerraduras_abiertas < 3:
    print("DERROTA la bóveda se bloqueó.")
elif cerraduras_abiertas == 3:
    print("¡VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA te quedaste sin energía o tiempo.")
