# ---Ejercicio 1---
def ejercicio1():
    """Ejercicio de identificación de errores."""
    a = 10
    b = input("Introduce un número: ")
    result = a/b # Error: TypeError: "b" es un string y no permite la división.
    print(f"Resultado: {result}")

    numbers = [1, 2, 3]
    print(numbers[5]) # Error: IndexError: El índice 5 está fuera del rango de la lista "numbers".

# ---Ejercicio 2---
def ejercicio2():
    """Ejercicio 1 sin errores."""
    a = 10
    b = float(input("Introduce un número: "))
    result = a/b # Ahora b es un float y permite la división.
    print(f"Resultado: {result}")

    numbers = [1, 2, 3]
    print(numbers[2]) # El índice 2 está dentro del rango de la lista "numbers".

# ---Ejercicio 3---
def ejercicio3():
    """Ejercicio 1 con try-except."""
    a = 10
    b = input("Introduce un número: ")
    try:
        result = a/b # Error: TypeError: "b" es un string y no permite la división.
        print(f"Resultado: {result}")
    except:
        print("Error: No se puede dividir un número por un string.")

    numbers = [1, 2, 3]
    try:
        print(numbers[5]) # Error: IndexError: El índice 5 está fuera del rango de la lista "numbers".
    except:
        print("Error: Índice fuera de rango para la lista.")

# ---Ejercicio 4---
def ejercicio4():
    """Ejercicio 3 con excepciones que hacen alusión a los tipos de errores detectados."""
    a = 10
    b = input("Introduce un número: ")
    try:
        result = a/b # Error: TypeError: "b" es un string y no permite la división.
        print(f"Resultado: {result}")
    except TypeError:
        print("Error: No se puede dividir un número por un string.")

    numbers = [1, 2, 3]
    try:
        print(numbers[5]) # Error: IndexError: El índice 5 está fuera del rango de la lista "numbers".
    except IndexError:
        print("Error: Índice fuera de rango para la lista.")

# ---Ejercicio 5---
def ejercicio5():
    """Ejercicio 4 con bloques else y finally."""
    a = 10
    b = input("Introduce un número: ")
    try:
        result = a/b # Error: TypeError: "b" es un string y no permite la división.
        print(f"Resultado: {result}")
    except TypeError:
        print("Error: No se puede dividir un número por un string.")
    else:
        print("La división se realizó correctamente.")
    finally:
        print("Fin de la operación.")

    numbers = [1, 2, 3]
    try:
        print(numbers[5]) # Error: IndexError: El índice 5 está fuera del rango de la lista "numbers".
    except IndexError:
        print("Error: Índice fuera de rango para la lista.")
    else:
        print("El acceso al índice se realizó correctamente.")
    finally:
        print("Fin de la operación.")

# ---Ejercicio 6 Y 7---
def solicitar_numero():
    """Solicita un número al usuario y maneja excepciones. Ej 7: Permite ingresar un nuevo número luego de encontrar un error."""
    while True:
        try:
            numero = float(input("Introduce un número: "))
        except ValueError:
            print("Debe ingresar un número válido.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {type(e).__name__}")
            print(f"Detalles del error: {e}")
        else:
            print(numero)
            break

def main():
    #ejercicio1()
    ejercicio2()
    ejercicio3()
    ejercicio4()
    ejercicio5()
    solicitar_numero()

if __name__== "__main__":
    main()