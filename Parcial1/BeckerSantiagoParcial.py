# Listas paralelas
titulos = []
ejemplares = []

opcion = 0

while opcion != 8:
    print("\n=== MENÚ BIBLIOTECA ===")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion.isdigit():
        opcion = int(opcion)
    else:
        print("Opción inválida. Intente de nuevo.")
        continue

    # 1. INGRESAR TITULOS
    if opcion == 1:
        cantidad = input("Ingrese la cantidad de títulos: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            for i in range(cantidad):
                titulo = input(f"Ingrese el título {i+1}: ")
                titulos.append(titulo)
                ejemplares.append(0)  # Inicializamos con 0 ejemplares
        else:
            print("Debe ingresar un número válido.")

    # 2. INGRESAR EJEMPLARES
    elif opcion == 2:
        if len(titulos) == 0:
            print("No hay títulos cargados.")
        else:
            for i in range(len(titulos)):
                cantidad = input(f"Ingrese la cantidad de ejemplares para '{titulos[i]}': ")
                if cantidad.isdigit():
                    ejemplares[i] = int(cantidad)
                else:
                    print("Valor inválido. Se mantiene en 0.")

    # 3. MOSTRAR CATÁLOGO
    elif opcion == 3:
        if len(titulos) == 0:
            print("Catálogo vacío.")
        else:
            print("\n--- CATÁLOGO ---")
            for i in range(len(titulos)):
                print(f"{titulos[i]} - {ejemplares[i]} ejemplares")

    # 4. CONSULTAR DISPONIBILIDAD
    elif opcion == 4:
        buscar = input("Ingrese el título a buscar: ")
        encontrado = False
        for i in range(len(titulos)):
            if titulos[i].lower() == buscar.lower():
                print(f"'{titulos[i]}' tiene {ejemplares[i]} ejemplares.")
                encontrado = True
                break
        if not encontrado:
            print("Título no encontrado.")

    # 5. LISTAR AGOTADOS
    elif opcion == 5:
        agotados = 0
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                print(f"'{titulos[i]}' está agotado.")
                agotados += 1
        if agotados == 0:
            print("No hay libros agotados.")

    # 6. AGREGAR TÍTULO
    elif opcion == 6:
        nuevo_titulo = input("Ingrese el nuevo título: ")
        cant = input("Ingrese la cantidad de ejemplares: ")
        if cant.isdigit():
            titulos.append(nuevo_titulo)
            ejemplares.append(int(cant))
            print("Título agregado correctamente.")
        else:
            print("Cantidad inválida, no se agregó el libro.")

    # 7. ACTUALIZAR EJEMPLARES
    elif opcion == 7:
        if len(titulos) == 0:
            print("No hay libros cargados.")
        else:
            for i in range(len(titulos)):
                print(f"{i+1}. {titulos[i]} ({ejemplares[i]} ejemplares)")
            seleccion = input("Seleccione el número de libro: ")
            if seleccion.isdigit():
                seleccion = int(seleccion) - 1
                if 0 <= seleccion < len(titulos):
                    accion = input("¿Préstamo (p) o Devolución (d)? ").lower()
                    if accion == "p":
                        if ejemplares[seleccion] > 0:
                            ejemplares[seleccion] -= 1
                            print("Préstamo registrado.")
                        else:
                            print("No hay ejemplares disponibles.")
                    elif accion == "d":
                        ejemplares[seleccion] += 1
                        print("Devolución registrada.")
                    else:
                        print("Opción inválida.")
                else:
                    print("Selección inválida.")
            else:
                print("Debe ingresar un número válido.")

    elif opcion == 8:
        print("Saliendo del sistema...")

    else:
        print("Opción inválida, elija del 1 al 8.")
