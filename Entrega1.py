"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# SALONES
#----------------------------------------------------------------------------------------------

def ingresarSalon(salones):
    ...
    return salones

#----------------------------------------------------------------------------------------------
# BANDAS
#----------------------------------------------------------------------------------------------

def ingresarBanda(bandas):
    ...
    return bandas

#----------------------------------------------------------------------------------------------
# EVENTOS
#----------------------------------------------------------------------------------------------

def registrarEvento(eventos):
    ...
    return eventos

#----------------------------------------------------------------------------------------------
# INFORMES
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    salones = {...}
    bandas = {...}
    eventos = {...}



    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 5
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de Salones")
            print("[2] Gestión de Bandas")
            print("[3] Registro de Evento")
            print("[4] Listado de Informes")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcionMenuPrincipal == "1":   # Opción 1 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE SALONES")
                    print("---------------------------")
                    print("[1] Ingresar Salón")
                    print("[2] Editar Salón")
                    print("[3] Listar Salones activos")
                    print("[4] Eliminar Salón")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    salones = ingresarSalon(salones)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE BANDAS")
                    print("---------------------------")
                    print("[1] Ingresar Banda")
                    print("[2] Editar Banda")
                    print("[3] Listar Bandas activas")
                    print("[4] Eliminar Banda")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    bandas = ingresarBanda(bandas)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            while True:
                while True:
                    opciones = 1
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > Gestión de Eventos")
                    print("---------------------------")
                    print("[1] Registro de Evento")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    eventos = registrarEvento(eventos)
                    

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > INFORMES")
                    print("---------------------------")
                    print("[1] Eventos del Mes")
                    print("[2] Resumen Anual de Eventos por Banda (Cantidades)")
                    print("[3] Resumen Anual de Eventos por Banda(Pesos)")
                    print("[4] Ranking anual de costo por salón (Ordenado de mayor costo a menor)")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    clientes = altaCliente(clientes)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()