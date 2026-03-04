print("Bienvenido al parqueadero RIWI")
sw = True

while sw:

    ocupancia = int(input("cuantos carros hay ya en el parqueadero? \n"))
    proceso = input("¿quiere ingresar o sacar carros? (ingresar/sacar o True/False): \n").strip().lower()

    if proceso in ('true', 't', '1', 'yes', 'y', 'si', 's', 'ingresar', 'entrar'):

        entry = int(input("cuantos carros quiere ingresar al parqueadero? \n"))
        registro = ocupancia + entry

        if registro > 10:
            print("No hay suficiente espacio para ingresar todos los carros. Solo pueden ingresar", 10 - ocupancia, "carros.")
        else:
            print("Los carros pueden ingresar al parqueadero.")

        continuar = input("¿Desea realizar otra operación? (si/no): \n").strip().lower()

        if continuar in ('no', 'n', 'false', 'f', '0'):
            sw = False
            print("Gracias por usar el registro de parqueadero.")
        else:
            sw = True
            
    elif proceso in ('false', 'f', '0', 'no', 'n', 'sacar', 'salir'):

        salida = int(input("cuantos carros quieren salir del parqueadero? \n"))
        registro = ocupancia - salida
        print("Gracias por usar el parqueadero.")
        continuar = input("¿Desea realizar otra operación? (si/no): \n").strip().lower()

        if continuar in ('no', 'n', 'false', 'f', '0'):
            sw = False
            print("Gracias por usar el registro de parqueadero.")

        else:
            sw = True
    else:
        print("Entrada inválida. Responda '1'/'0', 'si'/'no' o 'True'/'False'.")
