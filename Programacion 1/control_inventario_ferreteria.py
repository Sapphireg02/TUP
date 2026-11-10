"""Programa con menú interactivo que controla el inventario de una ferretería."""

def cargar_herramientas(inventario):
    """Carga de herramientas con existencias iniciales.
    Registra las herramientas que se pondrán a la venta."""
    # Cantidad de herramientas distintas a cargar.
    while True:
        try:
            cant = int(input("Ingrese cuántas herramientas distintas desea cargar (debe ser un número entero mayor que cero): "))

            if cant <= 0:
                raise ValueError("La cantidad debe ser un número entero mayor que cero.")
            break

        except ValueError as e:
            print(f"Error: {e}")

    for i in range(cant):
        # Nombre de la herramienta a cargar.
        while True:
            try:
                herramienta = input(f"\nIngrese el nombre de la herramienta {i + 1}: ").strip()

                if herramienta == "":
                    raise ValueError("El nombre de la herramienta no puede estar vacío.")

                for producto in inventario:
                    if producto['herramienta'].lower() == herramienta.lower():
                        raise ValueError(f"La herramienta '{herramienta}' ya existe en el inventario.")
                    
                break

            except ValueError as e:
                print(f"Error: {e}")

        # Stock inicial de la herramienta a cargar.
        while True:
            try:
                cantidad = int(input(f"Ingrese el stock inicial de {herramienta} (debe ser un número entero mayor o igual a cero): "))
                                
                if cantidad < 0:
                    raise ValueError("El stock debe ser un número entero mayor o igual a cero.")

                break

            except ValueError as e:
                print(f"Error: {e}")

        inventario.append({'herramienta': herramienta, 'cantidad': cantidad})
        print(f"\nHerramienta '{herramienta}' cargada con éxito con un stock inicial de {cantidad} unidades.")

def mostrar_inventario(inventario):
    """Visualización de inventario.
    Muestra el listado completo de herramientas junto a su stock actual.
    Si todavía no hay herramientas cargadas, lo informa con un mensaje."""
    if not inventario:
        print("Todavía no hay herramientas en el inventario.")
    else:
        print("Inventario:")

        for producto in inventario:
            print(f"  {producto['herramienta']}: {producto['cantidad']} unidades")

def consultar_stock(inventario):
    """Consulta de stock.
    Busca una herramienta por su nombre y muestra cuántas unidades hay disponibles."""
    if not inventario:
        print("Todavía no hay herramientas en el inventario.")
        return
    
    try:
        nombre = input("Ingrese el nombre de la herramienta a consultar: ").strip()

        if nombre == "":
            raise ValueError("El nombre de la herramienta no puede estar vacío.")

    except ValueError as e:
        print(f"Error: {e}")
        return

    for producto in inventario:
        if producto['herramienta'].lower() == nombre.lower():
            print(f"Stock de {producto['herramienta']}: {producto['cantidad']} unidades")
            return

    print(f"No se encontró la herramienta '{nombre}' en el inventario.")

def reporte_agotados(inventario):
    """Reporte de agotados.
    Lista únicamente aquellos productos cuyo stock sea igual a cero.
    Si todavía no hay herramientas cargadas, lo informa con un mensaje.
    Si hay herramientas cargadas pero ninguna está agotada, lo informa con un mensaje."""
    cont=0
    if not inventario:
        print("Todavía no hay herramientas en el inventario.")
        return

    print("Productos agotados:")
    for producto in inventario:
        if producto['cantidad'] == 0:
            print(f"  {producto['herramienta']}: {producto['cantidad']} unidades")
            cont+=1

    if cont==0:
        print("No hay productos agotados en el inventario.")

def alta_producto(inventario):
    """Alta de nuevo producto.
    Agrega una nueva herramienta al final de inventario, junto con su stock inicial."""      
    herramienta = input(f"\nIngrese el nombre de la herramienta: ").strip()
    
    if herramienta == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")
    
    for producto in inventario:
        if producto['herramienta'].lower() == herramienta.lower():
            raise ValueError(f"La herramienta '{herramienta}' ya existe en el inventario.")
    
        # Stock inicial de la herramienta a cargar.
    cantidad = int(input(f"Ingrese el stock inicial de {herramienta} (debe ser un número entero mayor o igual a cero): "))

    if cantidad < 0:
        raise ValueError("El stock debe ser un número entero mayor o igual a cero.")
    
    inventario.append({'herramienta': herramienta, 'cantidad': cantidad})
    print(f"\nHerramienta '{herramienta}' cargada con éxito con un stock inicial de {cantidad} unidades.")

def actualizar_stock(inventario):
    """Actualización de stock (venta/ingreso).
    Permite modificar el stock de una herramienta existente."""
    if not inventario:
        print("Todavía no hay herramientas en el inventario.")
        return

    nombre = input("Ingrese el nombre de la herramienta a actualizar: ").strip()

    if nombre == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    encontrado = False

    for producto in inventario:
        if producto['herramienta'].lower() == nombre.lower():
            encontrado = True
            movimiento = input("Ingrese '1' para registrar una venta o '2' para registrar un ingreso: ").strip()
            # Venta.
            if movimiento == "1":
                cantidad = int(input(f"Ingrese la cantidad vendida de {producto['herramienta']}: "))

                if cantidad < 1:
                    raise ValueError("La cantidad vendida debe ser un número entero mayor a cero.")
                
                if cantidad > producto['cantidad']:
                    raise ValueError(f"No hay suficiente stock para vender {cantidad} unidades de {producto['herramienta']}. Stock disponible: {producto['cantidad']} unidades.")
                
                producto['cantidad'] -= cantidad
                print(f"Venta registrada. Nuevo stock de {producto['herramienta']}: {producto['cantidad']} unidades.")

            # Ingreso.
            elif movimiento == "2":
                cantidad = int(input(f"Ingrese la cantidad ingresada de {producto['herramienta']}: "))

                if cantidad < 1:
                    raise ValueError("La cantidad ingresada debe ser un número entero mayor a cero.")

                producto['cantidad'] += cantidad
                print(f"\nIngreso registrado. Nuevo stock de {producto['herramienta']}: {producto['cantidad']} unidades.")
            
            else:
                raise ValueError("Opción inválida. Debe ingresar '1' o '2'.")

    if not encontrado:
        print(f"\nNo se encontró la herramienta '{nombre}' en el inventario.")

def main():
    inventario = [] # Lista de diccionarios.
    opcion = 0
    while opcion != 7:
        try:
            opcion = int(input("""Seleccione una opción: 
            
            1. Carga de herramientas con existencias iniciales.
            2. Visualización de inventario.
            3. Consulta de stock.
            4. Reporte de agotados.
            5. Alta de nuevo producto.
            6. Actualización de stock (venta/ingreso).
            7. Salir.
            
            ---> """))
            if opcion == 1:
                # Carga de herramientas con existencias iniciales.
                cargar_herramientas(inventario)
            elif opcion == 2:
                # Visualización de inventario.
                mostrar_inventario(inventario)
            elif opcion == 3:
                # Consulta de stock.
                consultar_stock(inventario)
            elif opcion == 4:
                # Reporte de agotados.
                reporte_agotados(inventario)
            elif opcion == 5:
                # Alta de nuevo producto.
                alta_producto(inventario)
            elif opcion == 6:
                # Actualización de stock (venta/ingreso).
                actualizar_stock(inventario)
            elif opcion == 7:
                print("Finalizando ejecución del sistema.")
            elif opcion != 7:
                raise ValueError("Opción fuera de rango (1 a 7).")
            
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()