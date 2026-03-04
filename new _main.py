print("Bienvenido al parqueadero RIWI")
sw = True
ocupancia = 5

while sw:
    proceso = input("¿quiere ingresar o sacar carros? (ingresar/sacar o True/False): \n").strip().lower()

    if proceso in ('true', 't', '1', 'yes', 'y', 'si', 's', 'ingresar', 'entrar'):

        ocupancia = ocupancia + 1

        if ocupancia > 10:
            print("No hay suficiente espacio para ingresar todos los carros. Solo pueden ingresar 10 carros a la vez.")
        else:
            print("el carro puede ingresar al parqueadero.")

        continuar = input("¿Desea realizar otra operación? (si/no): \n").strip().lower()

        if continuar in ('no', 'n', 'false', 'f', '0'):
            sw = False
            print("Gracias por usar el registro de parqueadero.")
        else:
            sw = True
            
    elif proceso in ('false', 'f', '0', 'no', 'n', 'sacar', 'salir'):

        ocupancia = ocupancia - 1
        continuar = input("¿Desea realizar otra operación? (si/no): \n").strip().lower()

        if continuar in ('no', 'n', 'false', 'f', '0'):
            sw = False
            print("Gracias por usar el registro de parqueadero.")
        else:
            sw = True
    
    else:
        print("Entrada inválida. Responda '1'/'0', 'si'/'no' o 'True'/'False'.")