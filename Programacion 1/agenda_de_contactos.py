# ---Ejercicio 4---
def almacenar_contactos():
    """Crea un diccionario para almacenar contactos."""
    contactos = {}
    agregar = input("¿Desea agregar un contacto? (s/n): ")
    while agregar.lower() == "s":
        nombre = input("Ingrese el nombre del contacto: ").strip().title()
        while nombre in contactos:
            print("Ese nombre ya está en la agenda. Ingrese uno diferente.")
            nombre = input("Ingrese el nombre del contacto: ").strip().title()
        numero = input("Ingrese el número de teléfono del contacto: ")
        contactos[nombre] = numero
        agregar = input("¿Desea agregar otro contacto? (s/n): ")
    return contactos

def mostrar_numero(contactos, nombre):
    """Muestra el número de teléfono de un contacto."""
    buscar = "s"
    while buscar.lower() == "s":
        if nombre in contactos:
            print(f"El número de teléfono de {nombre} es: {contactos[nombre]}")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")
        buscar = input("¿Desea buscar otro contacto? (s/n): ")
        if buscar.lower() == "s":
            nombre = input("Ingrese el nombre del contacto para mostrar su número: ").strip().title()

def main():
    # Ejercicio 4: Almacena y consulta contactos en un diccionario.
    contactos = almacenar_contactos()
    # title hace que la primera letra de cada palabra sea mayúscula, para que coincida con el formato de los nombres almacenados.
    nombre = input("Ingrese el nombre del contacto para mostrar su número: ").strip().title()
    mostrar_numero(contactos, nombre)

if __name__ == "__main__":
    main()