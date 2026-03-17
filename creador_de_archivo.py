print("Bienvenido al parqueadero RIWI")
print('que proceso le gustaria hacer?')
print('1. Consultar parqueadero')
print('2. Ingresar un carro al parqueadero')
print('3. Sacar un carro del parqueadero')
print('4. Salir.')

sw = True

with open('parqueo.txt', 'r') as archivo:
    parqueo = archivo.readlines()


while sw:
    
    proceso = input().strip().lower()

    match proceso:
        
        case "consultar":
            print(parqueo)
        
        case "ingresar":
            
            placa=input('porfavor ingrese la placa del vehiculo a ingresar')

            for "_" in parqueo:
                indice =parqueo.index("_")
                parqueo[indice] = placa
                print(f'su vehiculo {placa} ha sido asignado a el espacio de parqueo{indice +1}')

                with open("parqueo.txt", "w") as archivo:
                    archivo.writelines(parqueo)
        
        case "sacar":
            
            placa=input('porfavor ingrese la placa del vehiculo que quiere sacar. ')

            for placa in parqueo:
                salida = parqueo.index(placa)
                parqueo[salida] = "_"
                print(f'su vehiculo {placa} ha sido retirado, Gracias por usar el parqueadero. ')

                with open("parqueo.txt", "w") as archivo:
                    archivo.writelines(parqueo)
        
        case "salir":
            
            print('gracias por usar el registro de parqueo')
            sw = False

        case _:
            print('opcion invalida, intentelo denuevo')
            continue




