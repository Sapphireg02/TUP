# Simulador de batalla por turnos. El objetivo es reducir los puntos de vida del oponente a cero antes de que el lo haga.

#---CONFIGURACIÓN DEL PERSONAJE---
gladiador = input("Ingrese el nombre del gladiador:").lower().replace(" ", "")
# Valida que sean solo letras y elimina espacios.
while gladiador == "" or not gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    gladiador = input("Ingrese el nombre del gladiador: ").lower().replace(" ", "")

#---INICIALIZACIÓN DE ESTADÍSTICAS---
vida_gladiador = 100
vida_enemigo = 100
cant_pociones = 3
daño_atq_pesado = 15
daño_base_enemigo = 12
turno_gladiador = True

#---CICLO DE COMBATE---
while vida_gladiador > 0 and vida_enemigo > 0:
    # Turno del gladiador.
    if turno_gladiador:
        print(f"---*---*---*---INICIO DEL COMBATE---*---*---*---\nTurno del gladiador {gladiador}:\nVida del gladiador: {vida_gladiador}\nVida del enemigo: {vida_enemigo}\nPociones disponibles: {cant_pociones}")
        opc = input("""\nSeleccione una acción:
        1. Ataque pesado
        2. Ráfaga veloz
        3. Curar
""")
        # Valida que la opción ingresada sea un número del 1 al 3.
        while not opc.isdigit() or not 1 <= int(opc) <= 3:
            print("Opción inválida. Ingrese una opción del 1 al 3.")
            opc = input("""\nSeleccione una acción:
            1. Ataque pesado
            2. Ráfaga veloz
            3. Curar
            """)

        # Lógica de las acciones:
        # Ataque pesado.
        if opc == "1":
            # Golpe critico.
            if vida_enemigo < 20:                   
                vida_enemigo -= daño_atq_pesado * 1.5
                print(f"Golpe crítico\n¡Atacaste al enemigo por {daño_atq_pesado * 1.5} puntos de daño!")

            # Golpe normal.
            else:
                vida_enemigo -= daño_atq_pesado
                print(f"¡Atacaste al enemigo por {daño_atq_pesado} puntos de daño!")

        # Ráfaga veloz.
        if opc == "2":
            for rafaga in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
        
        # Curar.
        if opc == "3":
            if cant_pociones > 0:
                vida_gladiador += 30
                cant_pociones -= 1
            else:
                print("¡No quedan pociones! ")

        turno_gladiador = False

    # Turno Enemigo.
    else: 
        print("Turno del Enemigo")
        vida_gladiador -= daño_base_enemigo
        print(f"¡El enemigo te atacó por 12 puntos de daño!")
        turno_gladiador = True

# ---FIN DEL JUEGO---
if vida_gladiador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")