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
import datetime


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def inicializarSalones():
    return {
    "1": {
        "id": "1",
        "activo": True,
        "nombre": "Salón A",
        "ubicacion": "Centro",
        "capacidad": 200,
        "equipamientos": {
            "equipamiento1": "Sonido",
            "equipamiento2": "Luces",
            "equipamiento3": "Pantalla",  
        },
        "empleados": {
        "empleado1": "Juan Pérez",
        "empleado2": "Ana Gómez",
        "empleado3": "Luis Díaz",
        },
        "accesoDiscapacitados": True
        },
        "2": {
            "id": "2",
            "activo": True,
            "nombre": "Salón B",
            "ubicacion": "Norte",
            "capacidad": 150,
            "equipamientos": {
                "equipamiento1": "Proyector",
                "equipamiento2": "Micrófono"
            },
            "empleados": {
                "empleado1": "María López",
                "empleado2": "Pedro Ruiz"
            },
            "accesoDiscapacitados": False
        },
        "3": {
            "id": "3",
            "activo": True,
            "nombre": "Salón C",
            "ubicacion": "Sur",
            "capacidad": 100,
            "equipamientos": {
                "equipamiento1": "Pantalla LED"
            },
            "empleados": {
                "empleado1": "Lucía Fernández"
            },
            "accesoDiscapacitados": True
        },
        "4": {
            "id": "4",
            "activo": True,
            "nombre": "Salón D",
            "ubicacion": "Este",
            "capacidad": 250,
            "equipamientos": {
                "equipamiento1": "Luces",
                "equipamiento2": "Sonido"
            },
            "empleados": {
                "empleado1": "Jorge Castro",
                "empleado2": "Sonia Méndez"
            },
            "accesoDiscapacitados": True
        },
        "5": {
            "id": "5",
            "activo": True,
            "nombre": "Salón E",
            "ubicacion": "Oeste",
            "capacidad": 180,
            "equipamientos": {
                "equipamiento1": "Cámara"
            },
            "empleados": {
                "empleado1": "Raúl Torres"
            },
            "accesoDiscapacitados": False
        },
        "6": {
            "id": "6",
            "activo": True,
            "nombre": "Salón F",
            "ubicacion": "Centro",
            "capacidad": 220,
            "equipamientos": {
                "equipamiento1": "Sonido",
                "equipamiento2": "Luces"
            },
            "empleados": {
                "empleado1": "Marta Díaz"
            },
            "accesoDiscapacitados": True
        },
        "7": {
            "id": "7",
            "activo": True,
            "nombre": "Salón G",
            "ubicacion": "Norte",
            "capacidad": 90,
            "equipamientos": {
                "equipamiento1": "Proyector"
            },
            "empleados": {
                "empleado1": "Esteban Gil"
            },
            "accesoDiscapacitados": False
        },
        "8": {
            "id": "8",
            "activo": True,
            "nombre": "Salón H",
            "ubicacion": "Sur",
            "capacidad": 300,
            "equipamientos": {
                "equipamiento1": "Pantalla",
                "equipamiento2": "Luces"
            },
            "empleados": {
                "empleado1": "Paula Ríos"
            },
            "accesoDiscapacitados": True
        },
        "9": {
            "id": "9",
            "activo": True,
            "nombre": "Salón I",
            "ubicacion": "Este",
            "capacidad": 120,
            "equipamientos": {
                "equipamiento1": "Micrófono"
            },
            "empleados": {
                "empleado1": "Diego Luna"
            },
            "accesoDiscapacitados": False
        },
        "10": {
            "id": "10",
            "activo": True,
            "nombre": "Salón J",
            "ubicacion": "Oeste",
            "capacidad": 160,
            "equipamientos": {
                "equipamiento1": "Sonido",
                "equipamiento2": "Pantalla"
            },
            "empleados": {
                "empleado1": "Gabriela Vera"
            },
            "accesoDiscapacitados": True
        },
    }

def inicializarBandas():
    return {
        "1": {
            "id": "1",
            "activo": True,
            "nombre": "Los Rockers",
            "generoMusical": "Rock",
            "costoMediaHora": 5000.0,
            "contacto": "rockers@email.com",
            "integrantes": {
                "integrante1": "Carlos",
                "integrante2": "Miguel",
                "integrante3": "Sofía",
                }
        }
        ,
        "2": {
            "id": "2",
            "activo": True,
            "nombre": "Jazz Masters",
            "generoMusical": "Jazz",
            "costoMediaHora": 6000.0,
            "contacto": "jazzmasters@email.com",
            "integrantes": {
                "integrante1": "Lucía",
                "integrante2": "Martín"
            }
        },
        "3": {
            "id": "3",
            "activo": True,
            "nombre": "Pop Stars",
            "generoMusical": "Pop",
            "costoMediaHora": 5500.0,
            "contacto": "popstars@email.com",
            "integrantes": {
                "integrante1": "Valeria",
                "integrante2": "Tomás"
            }
        },
        "4": {
            "id": "4",
            "activo": True,
            "nombre": "Funkadelic",
            "generoMusical": "Funk",
            "costoMediaHora": 7000.0,
            "contacto": "funkadelic@email.com",
            "integrantes": {
                "integrante1": "Sergio",
                "integrante2": "Paula"
            }
        },
        "5": {
            "id": "5",
            "activo": True,
            "nombre": "Blues Band",
            "generoMusical": "Blues",
            "costoMediaHora": 4800.0,
            "contacto": "bluesband@email.com",
            "integrantes": {
                "integrante1": "Javier",
                "integrante2": "Marina"
            }
        },
        "6": {
            "id": "6",
            "activo": True,
            "nombre": "Electro Beats",
            "generoMusical": "Electrónica",
            "costoMediaHora": 8000.0,
            "contacto": "electrobeats@email.com",
            "integrantes": {
                "integrante1": "Nicolás",
                "integrante2": "Sofía"
            }
        },
        "7": {
            "id": "7",
            "activo": True,
            "nombre": "Cumbia Total",
            "generoMusical": "Cumbia",
            "costoMediaHora": 4000.0,
            "contacto": "cumbiatotal@email.com",
            "integrantes": {
                "integrante1": "Ramiro",
                "integrante2": "Carla"
            }
        },
        "8": {
            "id": "8",
            "activo": True,
            "nombre": "Ska Vivos",
            "generoMusical": "Ska",
            "costoMediaHora": 5200.0,
            "contacto": "skavivos@email.com",
            "integrantes": {
                "integrante1": "Federico",
                "integrante2": "Julieta"
            }
        },
        "9": {
            "id": "9",
            "activo": True,
            "nombre": "Metal Force",
            "generoMusical": "Metal",
            "costoMediaHora": 9000.0,
            "contacto": "metalforce@email.com",
            "integrantes": {
                "integrante1": "Agustín",
                "integrante2": "Brenda"
            }
        },
        "10": {
            "id": "10",
            "activo": True,
            "nombre": "Tango Club",
            "generoMusical": "Tango",
            "costoMediaHora": 4500.0,
            "contacto": "tangoclub@email.com",
            "integrantes": {
                "integrante1": "Elena",
                "integrante2": "Roberto"
            }
        }
    }

def inicializarEventos():
    return {
        "2025.06.10 19:00:00": {
            "id": "2025.06.10 19:00:00",
            "fecha": "2025.06.10 19:00:00",
            "idSalon": "1",
            "idBanda": "1",
            "cantidadDeMediasHoras": 2
        },
        "2025.07.15 20:00:00": {
            "id": "2025.07.15 20:00:00",
            "fecha": "2025.07.15 20:00:00",
            "idSalon": "2",
            "idBanda": "2",
            "cantidadDeMediasHoras": 3
        },
        "2025.08.05 18:30:00": {
            "id": "2025.08.05 18:30:00",
            "fecha": "2025.08.05 18:30:00",
            "idSalon": "3",
            "idBanda": "3",
            "cantidadDeMediasHoras": 4
        },
        "2025.09.12 21:00:00": {
            "id": "2025.09.12 21:00:00",
            "fecha": "2025.09.12 21:00:00",
            "idSalon": "4",
            "idBanda": "4",
            "cantidadDeMediasHoras": 2
        },
        "2025.10.20 19:45:00": {
            "id": "2025.10.20 19:45:00",
            "fecha": "2025.10.20 19:45:00",
            "idSalon": "5",
            "idBanda": "5",
            "cantidadDeMediasHoras": 5
        },
        "2025.11.03 17:00:00": {
            "id": "2025.11.03 17:00:00",
            "fecha": "2025.11.03 17:00:00",
            "idSalon": "6",
            "idBanda": "6",
            "cantidadDeMediasHoras": 2
        },
        "2025.12.25 22:00:00": {
            "id": "2025.12.25 22:00:00",
            "fecha": "2025.12.25 22:00:00",
            "idSalon": "7",
            "idBanda": "7",
            "cantidadDeMediasHoras": 3
        },
        "2025.06.18 16:00:00": {
            "id": "2025.06.18 16:00:00",
            "fecha": "2025.06.18 16:00:00",
            "idSalon": "8",
            "idBanda": "8",
            "cantidadDeMediasHoras": 4
        },
        "2025.07.22 20:30:00": {
            "id": "2025.07.22 20:30:00",
            "fecha": "2025.07.22 20:30:00",
            "idSalon": "9",
            "idBanda": "9",
            "cantidadDeMediasHoras": 2
        },
        "2025.08.30 21:15:00": {
            "id": "2025.08.30 21:15:00",
            "fecha": "2025.08.30 21:15:00",
            "idSalon": "10",
            "idBanda": "10",
            "cantidadDeMediasHoras": 3
        }
    }

def crearEntidad(entidades, campos):
    """
    Crea una nueva entidad solicitando al usuario los valores para cada campo especificado.
    Args:
        entidades (list): Lista de entidades existentes, utilizada para validaciones en la entrada de datos.
        campos (dict): Diccionario donde las claves son los nombres de los campos y los valores son los tipos de datos esperados para cada campo.
    Returns:
        dict: Un diccionario que representa la nueva entidad con los valores ingresados por el usuario para cada campo.
    """
    
    entidad = {}
    for campo, tipo in campos.items():
        entidad[campo] = inputCampo(campo, tipo, entidades)
    return entidad

def editarEntidad(entidades, campos):
    """
    Permite editar los datos de una entidad existente en un diccionario de entidades.
    Solicita al usuario el ID de la entidad a editar. Si el ID existe, permite modificar los campos de la entidad,
    dejando en blanco aquellos que no se deseen cambiar. El campo "id" no puede ser editado.
    Args:
        entidades (dict): Diccionario que contiene las entidades, donde las claves son los IDs y los valores son diccionarios con los datos de cada entidad.
        campos (dict): Diccionario que define los nombres de los campos y sus tipos asociados.
    Returns:
        dict or None: El diccionario actualizado de la entidad si el ID existe, o None si el ID no se encuentra en 'entidades'.
    """

    idEntidad = input("ID: ")
    if idEntidad not in entidades:
        print("El ID no existe.")
        return None
    print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")
    entidad = entidades[idEntidad]
    for campo, tipo in campos.items():
        if campo == "id":
            continue  # No se edita el ID
        entidad[campo] = inputCampo(campo, tipo, entidades, actual=entidad[campo])
    return entidad

def listarEntidades(entidades, campos):
    """
    Imprime en consola una lista de entidades con sus respectivos campos y valores.
    Args:
        entidades (dict): Un diccionario donde las claves son los IDs de las entidades y los valores son diccionarios con los datos de cada entidad.
        campos (dict): Un diccionario que define los nombres de los campos y sus tipos de datos correspondientes.
    Returns:
        None: Esta función no retorna ningún valor, solo imprime la información de las entidades activas en consola.
    """

    for idEntidad, datos in entidades.items():
        if "activo" in datos and not datos["activo"]:
            continue
        print(f"ID: {idEntidad}")
        for campo, tipo in campos.items():
            printCampo = printCamelCase(campo)
            if campo == "id":
                continue
            if tipo == dict:
                print(f"{printCampo}: {', '.join(datos[campo].values())}")
            elif tipo == bool:
                print(f"{printCampo}: {'Sí' if datos[campo] else 'No'}")
            else:
                print(f"{printCampo}: {datos[campo]}")
        print("---------------------------")

def eliminarEntidad(entidades, nombreEntidad="entidad"):
    """
    Elimina lógicamente una entidad del diccionario de entidades, marcándola como inactiva.
    Solicita al usuario el ID de la entidad a eliminar. Si el ID existe en el diccionario,
    cambia el valor de la clave "activo" a False para esa entidad. Si el ID no existe,
    informa al usuario.
    Parámetros:
        entidades (dict): Diccionario que contiene las entidades, donde las claves son los IDs y los valores son diccionarios con información de cada entidad.
        nombreEntidad (str, opcional): Nombre descriptivo de la entidad a eliminar, utilizado en los mensajes al usuario. Por defecto es "entidad".
    Retorna:
        dict: El diccionario de entidades actualizado, con la entidad correspondiente marcada como inactiva si el ID existe.
    """

    print(f"Ingrese el ID de {nombreEntidad} a eliminar:")
    idEntidad = input(f"ID de {nombreEntidad}: ")
    if idEntidad in entidades:
        entidades[idEntidad]["activo"] = False
        print(f"{nombreEntidad.capitalize()} con ID {idEntidad} eliminada.")
    else:
        print(f"El ID de {nombreEntidad} no existe.")
    return entidades


def printCamelCase(texto):
    """
    Convierte una cadena en formato camel case a una cadena separada por espacios, con la primera letra en mayúscula.
    Parámetros:
        texto (str): Cadena de entrada en formato camel case.
    Retorna:
        str: Cadena convertida a formato separado por espacios, con la primera letra en mayúscula.
    """

    resultado = ""
    for i, c in enumerate(texto):
        if c.isupper() and i != 0:
            resultado += " "
        resultado += c
    return resultado.capitalize()


def inputCampo(campo, tipo, entidades=None, actual=None):
    """
    Solicita y procesa la entrada de un campo según su tipo y otras opciones.
    Parámetros:
        campo (str): El nombre del campo a solicitar.
        tipo (type): El tipo de dato esperado para el campo (por ejemplo, int, float, bool, dict, str).
        entidades (list, opcional): Lista de entidades para selección, utilizada si el campo es un identificador. Por defecto es None.
        actual (any, opcional): Valor actual del campo, utilizado para mostrar o sugerir el valor existente. Por defecto es None.
    Retorna:
        any: El valor ingresado y procesado para el campo, del tipo especificado por el parámetro 'tipo'.
    """

    printCampo = printCamelCase(campo)
    if isIdCampo(campo):
        return handleIdCampo(entidades)
    if tipo == dict:
        return handleDictCampo(campo, printCampo, actual)
    elif tipo == bool:
        return handleBoolCampo(printCampo, actual)
    elif tipo == int:
        return handleIntCampo(printCampo, actual)
    elif tipo == float:
        return handleFloatCampo(printCampo, actual)
    else:  # str u otros
        return handleStrCampo(printCampo, actual)
    
def isIdCampo(campo):
    return campo.lower() == "id"

def handleIdCampo(entidades):
    """
    Solicita al usuario un ID de entidad, validando que no exista previamente en la colección de entidades y que no esté vacío.
    Parámetros:
        entidades (iterable): Colección de IDs existentes de entidades para validar unicidad.
    Retorna:
        str: Un ID de entidad válido, único y no vacío ingresado por el usuario.
    """
    
    while True:
        idEntidad = input("ID:")
        if idEntidad in entidades:
            print("El ID ya existe. Intente con otro.")
        elif not idEntidad.strip():
            print("El ID no puede estar vacío. Intente con otro.")
        else:
            return idEntidad

def handleDictCampo(campo, printCampo, actual):
    """
    Solicita al usuario que ingrese múltiples valores para un campo específico y los almacena en un diccionario.
    Args:
        campo (str): Nombre base del campo (en plural) que se utilizará como clave en el diccionario.
        printCampo (str): Nombre descriptivo del campo que se mostrará al usuario en el mensaje de entrada.
        actual (dict or None): Diccionario existente con valores previos, o None si se desea iniciar uno nuevo.
    Returns:
        dict: Diccionario con los valores ingresados por el usuario, donde las claves son generadas a partir de 'campo' y un contador incremental.
    """

    resultado = {} if actual is None else actual.copy()
    contador = len(resultado) + 1
    while True:
        valor = input(f"Ingrese un valor para {printCampo} (o 'fin' para terminar): ")
        if valor.lower() == "fin":
            break
        if not valor.strip():
            print("El valor no puede estar vacío. Intente nuevamente.")
            continue
        resultado[f"{campo[:-1]}{contador}"] = valor
        contador += 1
    return resultado

def handleBoolCampo(printCampo, actual):
    """
    Solicita al usuario que ingrese un valor booleano ('si' o 'no') para un campo específico, mostrando el valor actual si está disponible.
    Parámetros:
        printCampo (str): El nombre o descripción del campo a mostrar en el prompt.
        actual (bool or None): El valor booleano actual del campo, o None si no hay valor previo.
    Retorna:
        bool: True si el usuario ingresa 'si', False si ingresa 'no' o cualquier otro valor distinto de 'si'.
              Si el usuario presiona Enter sin ingresar nada y 'actual' no es None, retorna el valor actual.
    """

    if actual is not None:
        entrada = input(f"{printCampo} (si/no, actual: {'sí' if actual else 'no'}): ").strip().lower()
        if entrada == "":
            return actual
    else:
        entrada = input(f"{printCampo} (si/no): ").strip().lower()
    return entrada == "si"

def handleIntCampo(printCampo, actual):
    """
    Solicita al usuario que ingrese un número entero, mostrando un mensaje personalizado y el valor actual si está disponible.
    Parámetros:
        printCampo (str): Mensaje a mostrar al usuario solicitando el valor.
        actual (int or None): Valor actual del campo, que se muestra como referencia y se puede mantener presionando Enter.
    Retorna:
        int: El número entero ingresado por el usuario, o el valor actual si se presiona Enter y 'actual' no es None.
    """

    while True:
        prompt = f"{printCampo}" + (f" (actual: {actual})" if actual is not None else "") + ": "
        entrada = input(prompt)
        if entrada == "" and actual is not None:
            return actual
        try:
            return int(entrada)
        except ValueError:
            print("Debe ingresar un número entero.")

def handleFloatCampo(printCampo, actual):
    """
    Solicita al usuario que ingrese un número decimal para un campo específico, mostrando el valor actual si está disponible.
    Parámetros:
        printCampo (str): El nombre o descripción del campo a mostrar en el prompt.
        actual (float or None): El valor actual del campo, si existe. Si es None, no se muestra valor actual.
    Retorna:
        float: El valor ingresado por el usuario convertido a float, o el valor actual si el usuario no ingresa nada y actual no es None.
    """

    while True:
        prompt = f"{printCampo}" + (f" (actual: {actual})" if actual is not None else "") + ": "
        entrada = input(prompt)
        if entrada == "" and actual is not None:
            return actual
        try:
            return float(entrada)
        except ValueError:
            print("Debe ingresar un número decimal.")

def handleStrCampo(printCampo, actual):
    """
    Solicita al usuario que ingrese un valor para un campo de tipo string, mostrando el valor actual si existe.
    Parámetros:
        printCampo (str): El nombre o descripción del campo a mostrar en el prompt.
        actual (str or None): El valor actual del campo, si existe.
    Retorna:
        str: El valor ingresado por el usuario, o el valor actual si no se ingresó nada y existe un valor actual.
    """

    entrada = input(f"{printCampo}" + (f" (actual: {actual})" if actual is not None else "") + ": ")
    if entrada == "" and actual is not None:
        return actual
    return entrada


#----------------------------------------------------------------------------------------------
# SALONES
#----------------------------------------------------------------------------------------------

def camposSalon():
    return {
        "id": str,
        "nombre": str,
        "ubicacion": str,
        "capacidad": int,
        "equipamientos": dict,
        "empleados": dict,
        "accesoDiscapacitados": bool
    }

def ingresarSalon(salones):
    """
    Agrega un nuevo salón al diccionario de salones solicitando los datos necesarios al usuario.
    Parámetros:
        salones (dict): Diccionario que contiene los salones existentes, donde la clave es el ID del salón y el valor es un diccionario con los datos del salón.
    Retorna:
        dict: Diccionario actualizado de salones con el nuevo salón agregado.
    """

    print("Ingrese los datos del salón:")
    campos = camposSalon()
    salon = crearEntidad(salones, campos)
    salon["activo"] = True  # Por defecto, el salón es activo al ingresarlo
    salones[salon["id"]] = salon
    return salones

def editarSalon(salones):
    """
    Edita un salón existente en la colección de salones.
    Solicita al usuario el ID del salón a editar, permite modificar sus campos y actualiza la colección de salones con los nuevos datos.
    Parámetros:
        salones (dict): Diccionario que contiene los salones, donde la clave es el ID del salón y el valor es un diccionario con los datos del salón.
    Retorna:
        dict: El diccionario de salones actualizado con los cambios realizados. Si no se edita ningún salón, retorna el diccionario original.
    """

    print("Ingrese el ID del Salon a editar:")
    campos = camposSalon()
    salon = editarEntidad(salones, campos)
    if salon is None:
        return salones
    salones[salon["id"]] = salon
    return salones

def listarSalones(salones):
    """
    Imprime un listado de los salones activos.
    Args:
        salones (list): Lista de salones a mostrar. Cada elemento representa un salón.
    Returns:
        None
    """
    
    print("Listado de salones activos:")
    campos = camposSalon()
    listarEntidades(salones, campos)
    


def eliminarSalon(salones):
    """
    Elimina un salón de la lista de salones utilizando la función eliminarEntidad.
    Parámetros:
        salones (list): Lista de salones existentes.
    Retorna:
        list: Lista de salones actualizada después de eliminar el salón seleccionado.
    """

    return eliminarEntidad(salones, "salón")


#----------------------------------------------------------------------------------------------
# BANDAS
#----------------------------------------------------------------------------------------------

def camposBanda():
    return {
        "id": str,
        "nombre": str,
        "generoMusical": str,
        "costoMediaHora": float,
        "contacto": str,
        "integrantes": dict
    }   

def ingresarBanda(bandas):
    """
    Agrega una nueva banda al diccionario de bandas solicitando los datos necesarios al usuario.
    Args:
        bandas (dict): Diccionario que contiene las bandas existentes, donde la clave es el ID de la banda y el valor es un diccionario con los datos de la banda.
    Returns:
        dict: Diccionario actualizado de bandas con la nueva banda agregada.
    """

    print("Ingrese los datos de la banda:")
    campos = camposBanda()
    banda = crearEntidad(bandas, campos)
    banda["activo"] = True  # Por defecto, la banda es activa al ingresarla
    bandas[banda["id"]] = banda
    return bandas

def editarBanda(bandas):
    """
    Edita la información de una banda existente en el diccionario de bandas.
    Solicita al usuario el ID de la banda a editar, permite modificar sus campos y actualiza la información en el diccionario.
    Parámetros:
        bandas (dict): Diccionario que contiene las bandas, donde la clave es el ID de la banda y el valor es un diccionario con los datos de la banda.
    Retorna:
        dict: Diccionario actualizado de bandas con la banda editada, o el diccionario original si no se realizó ninguna edición.
    """

    print("Ingrese el ID de la Banda a editar:")
    campos = camposBanda()
    banda = editarEntidad(bandas, campos)
    if banda is None:
        return bandas
    bandas[banda["id"]] = banda
    return bandas

def listarBandas(bandas):
    """
    Imprime un listado de las bandas activas.
    Args:
        bandas (list): Lista de diccionarios o entidades que representan bandas musicales.
    Returns:
        None
    """

    print("Listado de bandas activas:")
    campos = camposBanda()
    listarEntidades(bandas, campos)

def eliminarBanda(bandas):
    """
    Elimina una banda de la lista de bandas utilizando la función eliminarEntidad.
    Parámetros:
        bandas (list): Lista de bandas existentes.
    Retorna:
        list: Nueva lista de bandas con la banda eliminada.
    """

    return eliminarEntidad(bandas, "banda")

#----------------------------------------------------------------------------------------------
# EVENTOS
#----------------------------------------------------------------------------------------------

def registrarEvento(eventos, salones, bandas):
    """
    Registra un nuevo evento en el diccionario de eventos.
    Args:
        eventos (dict): Diccionario que almacena los eventos existentes, donde la clave es el ID del evento y el valor es un diccionario con los datos del evento.
        salones (dict): Diccionario de salones disponibles, donde la clave es el ID del salón y el valor es un diccionario con los datos del salón.
        bandas (dict): Diccionario de bandas disponibles, donde la clave es el ID de la banda y el valor es un diccionario con los datos de la banda.
    Returns:
        dict: Diccionario de eventos actualizado con el nuevo evento registrado.
    """

    fecha = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    id = fecha
    cantidadDeMediasHoras = handleIntCampo("Cantidad de medias horas", 0)
    idSalon = obtenerIdEntidad(salones, "del salón")
    idBanda = obtenerIdEntidad(bandas, "de la banda")

    eventos[id] = {
        "id": id,
        "fecha": fecha,
        "idSalon": idSalon,
        "idBanda": idBanda
        ,"cantidadDeMediasHoras": cantidadDeMediasHoras
    }
    print("Evento registrado correctamente.")

    return eventos

def obtenerIdEntidad(entidades, tituloEntidad="de la entidad"):
    """
    Solicita al usuario que ingrese un ID de entidad válido y lo retorna.
    Parámetros:
        entidades (iterable): Colección de IDs válidos de entidades.
        tituloEntidad (str, opcional): Texto descriptivo para mostrar en el mensaje de ingreso. Por defecto es "de la entidad".
    Retorna:
        idEntidad (str): El ID de entidad ingresado por el usuario que existe en 'entidades'.
    """

    while True:
        idEntidad = input(f"Ingrese el ID {tituloEntidad}: ")
        if idEntidad in entidades:
            return idEntidad
        else:
            print("El ID no existe. Intente nuevamente.")

#----------------------------------------------------------------------------------------------
# INFORMES
#----------------------------------------------------------------------------------------------

def listarEventosMesActual(eventos, salones, bandas):
    """
    Lista e imprime los eventos del mes actual.
    Esta función filtra los eventos que ocurren en el mes actual y los imprime junto con la información de los salones y bandas asociadas.
    Parámetros:
        eventos (list): Lista de eventos disponibles.
        salones (list): Lista de salones donde se realizan los eventos.
        bandas (list): Lista de bandas que participan en los eventos.
    Retorna:
        None: Esta función no retorna ningún valor, solo imprime la información de los eventos del mes actual.
    """

    eventosMes = obtenerEventosMesActual(eventos)
    imprimirEventos(eventosMes, salones, bandas)

def obtenerEventosMesActual(eventos):
    """
    Filtra y retorna los eventos que ocurren en el mes y año actual.

    Args:
        eventos (dict): Un diccionario donde cada valor es un evento representado por otro diccionario
                        que debe contener la clave "fecha" con el formato "%Y.%m.%d %H:%M:%S".

    Returns:
        list: Una lista de eventos (diccionarios) que ocurren en el mes y año actual.
    """
    hoy = datetime.date.today()
    mesActual = hoy.month
    anioActual = hoy.year
    eventosFiltrados = []
    for evento in eventos.values():
        try:
            fechaEvento = datetime.datetime.strptime(evento["fecha"], "%Y.%m.%d %H:%M:%S").date()
        except Exception:
            continue
        if fechaEvento.month == mesActual and fechaEvento.year == anioActual:
            eventosFiltrados.append(evento)
    return eventosFiltrados

def imprimirEventos(eventos, salones, bandas):
    """
    Imprime una tabla formateada con información sobre eventos, incluyendo fecha, salón, banda, costo por 30 minutos, duración y costo total.
    Parámetros:
        eventos (list of dict): Lista de diccionarios, cada uno representando un evento con las claves 'fecha', 'idSalon', 'idBanda' y 'cantidadDeMediasHoras'.
        salones (dict): Diccionario donde las claves son IDs de salón y los valores son diccionarios con información del salón (incluyendo la clave 'nombre').
        bandas (dict): Diccionario donde las claves son IDs de banda y los valores son diccionarios con información de la banda (incluyendo las claves 'nombre' y 'costoMediaHora').
    Retorno:
        None: Esta función no retorna ningún valor. Imprime la información de los eventos en consola.
    """

    print("-" * 90)
    print(f"{'Fecha':<20} {'Salón':<18} {'Banda':<20} {'Costo 30min':>10} {'Dur.':>6} {'Total':>12}")
    print("-" * 90)
    for evento in eventos:
        salon = salones.get(evento["idSalon"], {}).get("nombre", "Desconocido")
        banda = bandas.get(evento["idBanda"], {}).get("nombre", "Desconocida")
        costoMediaHora = bandas.get(evento["idBanda"], {}).get("costoMediaHora", 0)
        duracion = evento.get("cantidadDeMediasHoras", 1)
        costoTotal = costoMediaHora * duracion
        print(f"{evento['fecha']:<12} {salon:<20} {banda:<20} {costoMediaHora:>10,.2f} {duracion:>6} {costoTotal:>12,.2f}")
    print("-" * 90)


def resumenEventosPorBandaYMes(eventos, bandas):
    """
    Genera y muestra un resumen de la cantidad total de eventos por banda y por mes para un año específico.
    Parámetros:
        eventos (list): Lista de eventos, donde cada evento contiene información relevante (por ejemplo, fecha, banda, etc.).
        bandas (list): Lista de bandas a considerar en el resumen.
    Retorno:
        None: La función imprime en pantalla la matriz resumen, no retorna ningún valor.
    """

    anio = ingresarAnio()
    matriz = obtenerMatrizBandaMes(eventos, bandas, anio, valorCantidad)
    imprimirMatrizBandaMes(matriz, anio, "CANTIDADES TOTALES POR MES", formatoCelda="{:>6}")

def resumenPesosPorBandaYMes(eventos, bandas):
    """
    Genera y muestra un resumen de los totales facturados en pesos por cada banda y por mes para un año específico.
    Parámetros:
        eventos (list): Lista de eventos, donde cada evento contiene información relevante para el cálculo de facturación.
        bandas (list): Lista de bandas a considerar en el resumen.
    Retorno:
        None: La función imprime la matriz de totales facturados por banda y mes, no retorna ningún valor.
    """

    anio = ingresarAnio()
    matriz = obtenerMatrizBandaMes(eventos, bandas, anio, valorPesos)
    imprimirMatrizBandaMes(matriz, anio, "TOTALES FACTURADOS POR MES", formatoCelda="{:<6,.2f}")


def ingresarAnio():
    while True:
        try:
            anio = int(input("Ingrese el año a consultar (ej: 2025): "))
            return anio
        except ValueError:
            print("Año inválido. Intente nuevamente.")

def valorCantidad(evento, banda):
    return 1

def valorPesos(evento, banda):
    return banda.get("costoMediaHora", 0) * evento.get("cantidadDeMediasHoras", 1)

def obtenerMatrizBandaMes(eventos, bandas, anio, funcionValor):
    """
    Genera una matriz que representa, para cada banda activa, un valor mensual calculado a partir de los eventos ocurridos en un año específico.
    Args:
        eventos (dict): Diccionario de eventos, donde cada valor es un diccionario que contiene información del evento, incluyendo la fecha y el id de la banda asociada.
        bandas (dict): Diccionario de bandas, donde cada clave es el id de la banda y el valor es un diccionario con información de la banda (incluyendo el nombre y si está activa).
        anio (int): Año para el cual se deben considerar los eventos.
        funcionValor (callable): Función que recibe un evento y una banda, y retorna el valor a acumular en la matriz para ese evento.
    Returns:
        dict: Un diccionario donde las claves son los nombres de las bandas activas y los valores son listas de 12 elementos (uno por cada mes), con los valores acumulados según la función proporcionada.
    """

    matriz = {}
    for idBanda, banda in bandas.items():
        if not banda.get("activo", True):
            continue
        matriz[banda["nombre"]] = [0] * 12

    for evento in eventos.values():
        idBanda = evento.get("idBanda")
        banda = bandas.get(idBanda)
        if not banda or not banda.get("activo", True):
            continue
        try:
            fecha = datetime.datetime.strptime(evento["fecha"], "%Y.%m.%d %H:%M:%S")
        except Exception:
            continue
        if fecha.year == anio:
            valor = funcionValor(evento, banda)
            matriz[banda["nombre"]][fecha.month - 1] += valor
    return matriz

def imprimirMatrizBandaMes(matriz, anio, titulo, formatoCelda="{:>6}"):
    """
    Imprime una matriz de valores asociados a diferentes bandas y meses, formateada como una tabla.
    Parámetros:
        matriz (dict): Diccionario donde las claves son nombres de bandas (str) y los valores son listas de 12 elementos numéricos, uno por cada mes.
        anio (int): Año que se mostrará en el encabezado de la tabla.
        titulo (str): Título que se imprimirá antes de la tabla.
        formatoCelda (str, opcional): Formato de cadena para cada celda de valor en la tabla. Por defecto es "{:>6}".
    Retorno:
        None. La función imprime la tabla en la salida estándar.
    """

    meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
    print(titulo)
    print(f"{'Banda':<25} " + " ".join([f"{mes}.{str(anio)[2:]:<2}" for mes in meses]))
    print("-" * (25 + 13 * 7))
    for banda, valores in matriz.items():
        fila = f"{banda:<25} " + " ".join([formatoCelda.format(v) for v in valores])
        print(fila)
    print("-" * (25 + 13 * 7))

def rankingCostoPorSalon(eventos, salones, bandas):
    """
    Calcula y muestra un ranking de salones basado en el costo total generado por eventos en un año específico.
    Para cada salón activo, suma el costo de todos los eventos realizados en ese salón durante el año ingresado,
    considerando la duración de cada evento y el costo por media hora de la banda correspondiente.
    El ranking se ordena de mayor a menor costo total y se imprime utilizando la función `imprimirRanking`.
    Parámetros:
        eventos (dict): Diccionario de eventos, donde cada valor es un dict con información del evento,
                        incluyendo 'idSalon', 'idBanda', 'fecha' y 'cantidadDeMediasHoras'.
        salones (dict): Diccionario de salones, donde cada clave es el ID del salón y el valor es un dict
                        con información del salón, incluyendo 'nombre' y 'activo'.
        bandas (dict): Diccionario de bandas, donde cada clave es el ID de la banda y el valor es un dict
                       con información de la banda, incluyendo 'costoMediaHora' y 'activo'.
    Retorno:
        None. La función imprime el ranking de salones por costo total generado en el año seleccionado.
    """

    anio = ingresarAnio()
    # Inicializar acumulador: {salon: total}
    ranking = {}
    for idSalon, salon in salones.items():
        if not salon.get("activo", True):
            continue
        ranking[salon["nombre"]] = 0.0

    # Sumar montos por salón
    for evento in eventos.values():
        idSalon = evento.get("idSalon")
        salon = salones.get(idSalon)
        if not salon or not salon.get("activo", True):
            continue
        try:
            fecha = datetime.datetime.strptime(evento["fecha"], "%Y.%m.%d %H:%M:%S")
        except Exception:
            continue
        if fecha.year == anio:
            idBanda = evento.get("idBanda")
            banda = bandas.get(idBanda)
            if not banda or not banda.get("activo", True):
                continue
            duracion = evento.get("cantidadDeMediasHoras", 1)
            costoMediaHora = banda.get("costoMediaHora", 0)
            ranking[salon["nombre"]] += costoMediaHora * duracion

    # Ordenar de mayor a menor
    rankingOrdenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    imprimirRanking(rankingOrdenado)

def imprimirRanking(ranking):
    """
    Imprime en consola un ranking anual de costo por salón.
    Parámetros:
        ranking (list of tuple): Una lista de tuplas, donde cada tupla contiene el nombre del salón (str)
        y el total facturado (float) correspondiente.
    Retorno:
        None: Esta función no retorna ningún valor. Solo imprime el ranking en formato tabular.
    """

    print("RANKING ANUAL DE COSTO POR SALÓN")
    print(f"{'Salón':<25} {'Total Facturado':>20}")
    print("-" * 45)
    for salon, total in ranking:
        print(f"{salon:<25} {total:>20,.2f}")
    print("-" * 45)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    salones = inicializarSalones()
    bandas = inicializarBandas()
    eventos = inicializarEventos()



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
                    salones = editarSalon(salones)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    listarSalones(salones)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    salones = eliminarSalon(salones)

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
                    bandas = editarBanda(bandas)

                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    listarBandas(bandas)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    bandas = eliminarBanda(bandas)

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
                    eventos = registrarEvento(eventos, salones, bandas)
                    

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
                    listarEventosMesActual(eventos, salones, bandas)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    resumenEventosPorBandaYMes(eventos, bandas)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    resumenPesosPorBandaYMes(eventos, bandas)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    rankingCostoPorSalon(eventos, salones, bandas)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()