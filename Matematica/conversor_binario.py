"""Conversión de números decimales y binarios.

El archivo puede ejecutarse para usar el menú o importarse para llamar
directamente a ``programa_decimal_a_binario`` y
``programa_binario_a_decimal``. Los flujos solicitan y validan la entrada;
las funciones de conversión realizan únicamente el cálculo.
"""


def verificar_numero(entrada):
    """Indica si el texto representa un entero decimal no negativo.

    Se permiten espacios al inicio o al final. El valor cero es válido.

    Args:
        entrada: Texto que se desea comprobar.

    Returns:
        True si contiene solamente dígitos decimales; False en caso contrario.
    """
    
    entrada = entrada.strip()

    if not entrada.isdecimal():
        return False

    return int(entrada) >= 0


def solicitar_numero(mensaje, mensaje_error):
    """Solicita un entero decimal no negativo hasta recibir uno válido.

    Args:
        mensaje: Texto que se muestra al pedir el dato.
        mensaje_error: Texto que se muestra cuando la entrada no es válida.

    Returns:
        El valor ingresado convertido a entero.
    """

    entrada = input(mensaje).strip()

    while not verificar_numero(entrada):
        print(mensaje_error)
        entrada = input(mensaje).strip()

    return int(entrada)


def verificar_binario(entrada):
    """Indica si el texto contiene uno o más dígitos binarios.

    Se permiten espacios al inicio o al final y el cero es válido.

    Args:
        entrada: Texto que se desea comprobar.

    Returns:
        True si, sin contar espacios exteriores, contiene solo 0 y 1;
        False si está vacío o contiene otros caracteres.
    """

    entrada = entrada.strip()
    return (
        bool(entrada)
        and all(digito == "0" or digito == "1" for digito in entrada)
    )


def solicitar_binario(mensaje, mensaje_error):
    """Solicita una cadena binaria hasta recibir una entrada válida.

    Args:
        mensaje: Texto que se muestra al pedir el dato.
        mensaje_error: Texto que se muestra cuando la entrada no es válida.

    Returns:
        La cadena binaria ingresada, sin espacios exteriores.
    """

    entrada = input(mensaje).strip()

    while not verificar_binario(entrada):
        print(mensaje_error)
        entrada = input(mensaje).strip()

    return entrada


def decimal_a_binario(decimal):
    """Convierte un entero decimal no negativo a su representación binaria.

    Args:
        decimal: Entero no negativo que se desea convertir.

    Returns:
        Una cadena con los dígitos binarios. El cero se representa como "0".
    """

    # Se usa texto para concatenar cada resto y conservar los dígitos binarios en orden.
    binario = ""
    while decimal > 0 or binario == "":
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2

    return binario


def binario_a_decimal(binario):
    """Convierte una cadena binaria válida a un entero decimal.

    Args:
        binario: Cadena no vacía compuesta únicamente por 0 y 1.

    Returns:
        El valor decimal equivalente.

    Note:
        La entrada debe validarse antes de llamar a esta función.
    """

    decimal = 0
    potencia =  0
    posicion = len(binario) - 1

    while posicion >= 0:
        decimal += int(binario[posicion]) * (2 ** potencia)
        potencia += 1
        posicion -= 1

    return decimal


def programa_decimal_a_binario():
    """Ejecuta el flujo interactivo de decimal a binario.

    Solicita y valida un entero no negativo, realiza la conversión y muestra
    el resultado. Puede llamarse directamente sin usar el menú.
    """

    decimal = solicitar_numero(
        "Ingrese un número decimal no negativo: ",
        "Debe ingresar un entero mayor o igual que cero.",
    )
    binario = decimal_a_binario(decimal)
    print(f"El número binario es: {binario}\n")


def programa_binario_a_decimal():
    """Ejecuta el flujo interactivo de binario a decimal.

    Solicita y valida una cadena binaria, realiza la conversión y muestra
    el resultado. Puede llamarse directamente sin usar el menú.
    """

    binario = solicitar_binario(
        "Ingrese un número binario no negativo: ",
        "Debe ingresar un número binario válido (solo 0 y 1).",
    )
    decimal = binario_a_decimal(binario)
    print(f"El número decimal es: {decimal}\n")


if __name__ == "__main__":
    opc = ""
    while opc != "3":
        opc = input("""Seleccione una opción: 
        1. Convertir decimal a binario
        2. Convertir binario a decimal
        3. Salir

        --> """).strip()

        if opc == "1":
            programa_decimal_a_binario()

        elif opc == "2":
            programa_binario_a_decimal()

        elif opc == "3":
            print("Saliendo del programa.")

        else:
            print("Opción no válida. Por favor, intente nuevamente.")