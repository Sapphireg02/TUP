# Objetivo: Login con intentos + menú de acciones con validación estricta.
import random
# Credenciales fijas:
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos_maximos = 3
intentos = 0
salir = False

# ---Ingreso de credenciales---
usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

# Validación de credenciales con límite de intentos
while (usuario != usuario_correcto or clave != clave_correcta) and intentos < intentos_maximos:
    intentos += 1
    print(f"Credenciales incorrectas. Intento {intentos} de {intentos_maximos}.")
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    # Si se alcanza el máximo de intentos se bloquea la cuenta.
    if intentos == intentos_maximos and (usuario != usuario_correcto or clave != clave_correcta):
        print("---*---*---*---*---*---\n---*Cuenta bloqueada*---\n---*---*---*---*---*---")

while (usuario == usuario_correcto and clave == clave_correcta) and salir==False:
    opc = input("""-------------------- MENU DE OPCIONES ----------------------
    1) Ver estado de inscripción
    2) Cambiar clave
    3) Mostrar mensaje motivacional
    4) Salir
    """)

    # Valida que la opción sea un número entre 1 y 4.
    if not opc.isdigit() or opc not in ("1", "2", "3", "4"):
        print("Opción inválida. Ingrese un número del 1 al 4.")
        continue

    # Mostrar estado de inscripción.
    if opc == "1":
        print("Inscripto")

    # Cambiar clave.
    elif opc == "2":
        listo = False
        while not listo:
            nueva_clave = input("Ingrese su nueva clave: ")
            confirmacion = input("Confirme su nueva clave: ")
            if len(nueva_clave) >= 6 and nueva_clave == confirmacion:
                clave_correcta = nueva_clave
                clave = nueva_clave
                print("Clave cambiada.")
                listo = True
            # Valida que la nueva clave tenga al menos 6 caracteres.
            elif len(nueva_clave) < 6:
                print("La clave debe tener al menos 6 caracteres, intente nuevamente.")
            else:
                print("Las claves no coinciden. Intente nuevamente.")

    # Mostrar mensaje motivacional.
    elif opc == "3":
        mensaje = random.randint(1, 5)
        if mensaje == 1:
            print("Aunque el camino sea difícil, sigue avanzando; algún día mirarás atrás y verás cuánto creciste.")
        elif mensaje == 2:
            print("No tengas miedo de caer; cada vez que te levantas te vuelves más fuerte.")
        elif mensaje == 3:
            print("Sé tú mismo, porque no hay nadie en el mundo que pueda hacerlo mejor que tú.")
        elif mensaje == 4:
            print("Tu valor no depende de lo que los demás piensen de ti; tú decides quién quieres ser.")
        else:
            print("No dejes que tus límites de hoy decidan quién serás mañana.")

    # Salir.
    elif opc == "4":
        salir = True