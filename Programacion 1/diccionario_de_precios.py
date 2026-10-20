# ---Ejercicio 1---
def diccionario_precios():
    """Crea un diccionario con frutas y sus precios."""
    precios_frutas = {
        "Banana": 1200,
        "Ananá": 2500,
        "Melón": 3000,
        "Uva": 1450
    }
    return precios_frutas

def mostrar_diccionario(diccionario):
    """Muestra los elementos del diccionario."""
    for fruta, precio in diccionario.items():
        print(f"{fruta}: ${precio:.2f}")
    tecla = input("--------------------------------------------\nPresiona enter para continuar...\n")

def agregar_fruta(diccionario, fruta, precio):
    """Agrega una fruta y su precio al diccionario."""
    diccionario[fruta] = precio
    print(f"Se ha agregado {fruta} con un precio de ${precio:.2f} al diccionario.")

# ---Ejercicio 2---
def actualizar_precio(diccionario, fruta, nuevo_precio):
    """Actualiza el precio de una fruta en el diccionario."""
    diccionario[fruta] = nuevo_precio
    print(f"Se ha actualizado el precio de {fruta} a ${nuevo_precio:.2f}.")

# ---Ejercicio 3---
def lista_frutas(diccionario):
        """Crea una lista con las frutas del diccionario."""
        return list(diccionario.keys())

def mostrar_lista(lista):
    """Muestra los elementos de la lista."""
    for elemento in lista:
        print(f" - {elemento}")
    tecla = input("--------------------------------------------\nPresiona enter para continuar...\n")
    
def main():
    # Ejercicio 1: Dado el diccionario de precios, agrega frutas con sus respectivos precios.
    # Crea y muestra el diccionario de precios inicial.
    diccionario = diccionario_precios()
    mostrar_diccionario(diccionario)

    # Agrega nuevas frutas al diccionario.
    agregar_fruta(diccionario, "Naranja", 1200)
    agregar_fruta(diccionario, "Manzana", 1500)
    agregar_fruta(diccionario, "Pera", 2300)
    mostrar_diccionario(diccionario)

    # Ejercicio 2: Siguiendo con el diccionario, se actualizan precios de frutas.
    actualizar_precio(diccionario, "Banana", 1330)
    actualizar_precio(diccionario, "Manzana", 1700)
    actualizar_precio(diccionario, "Melón", 2800)
    mostrar_diccionario(diccionario)

    # Ejercicio 3: Crea una lista con las frutas del diccionario.
    frutas = lista_frutas(diccionario)
    print("Frutas en el diccionario:")
    mostrar_lista(frutas)

if __name__ == "__main__":
    main()