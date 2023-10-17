import os
import re
from data_stark import *


def extraer_iniciales(personaje:str):
    iniciales_unidas = []
    if personaje:
        if re.findall("-", personaje):
            personaje = personaje.replace("-", " ")

        for item in personaje:
            algo = re.split(" ", personaje)

        for item in algo:
            if re.findall("the", item.lower()):
                pass
            else:
                iniciales = re.findall(r"\w", item)
                iniciales_unidas.append(iniciales[0])
        iniciales_unidas = '.'.join(iniciales_unidas)
        return iniciales_unidas
    else:
        return "N/A"

iniciales = extraer_iniciales("Howard The Duck")


Howard = {'nombre': 'Howard the Duck', 'identidad': 'Howard (Last name unrevealed)', 'empresa': 'Marvel Comics', 'altura': '79.349999999999994', 'peso': '18.449999999999999', 'genero': 'M', 'color_ojos': 'Brown', 'color_pelo': 'Yellow', 'fuerza': '2', 'inteligencia': ''}
def definir_iniciales_nombre(heroe:dict, key:str):
    if type(heroe) == dict and heroe["nombre"]:
        valor = extraer_iniciales(heroe["nombre"])
        heroe.update({key:valor})
        return heroe
    else:
        return False


def agregar_iniciales_nombre(lista:list):
    personaje = []
    if type(lista) == list and lista:
        for item in lista:
            personaje.append(definir_iniciales_nombre(item, "iniciales"))
            if personaje == False:
                print("El origen de datos no contiene el formato correcto")
                return False
        if personaje:
            return personaje



def stark_imprimir_nombres_con_iniciales(lista:list):
    if type(lista) == list and lista:
        personajes_con_iniciales = agregar_iniciales_nombre(lista)
        for item in personajes_con_iniciales:
            print(f"{item['nombre']} ({item['iniciales']})")

def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    if type(id_heroe) == int and (genero_heroe == "F" or genero_heroe =="M" or genero_heroe == "NB") and genero_heroe:
        id_heroe = str(id_heroe)
        id_largo = len(id_heroe)
        tamaño = 8
        
        if genero_heroe == "NB":
            tamaño = 7

        if id_largo <= tamaño:
            ceros_agregar = tamaño - id_largo
            id_completo = "0" * ceros_agregar + id_heroe
        elif id_largo > tamaño:
            return "La id está mal"
        else:  
            id_completo = id
        
        id_completo = f"{genero_heroe}-{id_completo}"
        return id_completo
    else:
        return "Algo está mal"

def agergar_codigo_heroe(heroe:dict,id_heroe:int):
    if type(heroe) == dict and heroe:
        codigo = generar_codigo_heroe(id_heroe, heroe["genero"])
        if re.match('[A-Z-0-9]{10}$', codigo):
            heroe.update({"codigo_heroe":codigo})
            return True
        else:
            return False


def stark_generar_codigos_heroes(lista:list):
    contador = 0
    if lista:
        for item in lista:
            if type(item) == dict and item["genero"]:
                contador += 1
            else:
                print("‘El origen de datos no contiene el formato correcto’")
                break
            agergar_codigo_heroe(item, contador)
        print(f"""Se asignaron {contador} códigos:
    El código del primer heroe es: {lista[0]["codigo_heroe"]}  
    El código del ultimo heroe es: {lista[-1]["codigo_heroe"]}""")

def sanitizar_entero(numero_str:str):
    numero_str = numero_str.strip()
    if numero_str.isdigit():
        numero_str = int(numero_str)
        return numero_str
    elif numero_str.isalpha():
        return "-1"
    elif numero_str < "0":
        return "-2"
    else:
        return "-3"


def sanitizar_flotante(numero_str:str):
    if type(numero_str) == str:
        numero_str = numero_str.strip()
    try:
        numero_str = float(numero_str)
        if numero_str > 0:
            return numero_str
        else:
            return "-2"
    except ValueError:
        return "-1"
    except:
        return "-3"


def sanitizar_string(valor_str:str, valor_por_defecto:str):
    valor_str = valor_str.strip()
    if re.findall('[A-Z-a-z]', valor_str):
        if re.findall('[0-9]', valor_str):
            return "N/A"
        if re.findall("/", valor_str):
            valor_str = valor_str.replace("/", " ")
        valor_str.lower()
        return valor_str
    elif valor_str.isalnum():
        return "N/A"
    elif valor_str == "":
        return valor_por_defecto.lower()


def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
    if clave not in heroe:
        print("La clave especificada no existe en el héroe")
        return False
    else:
        match tipo_dato.lower():
            case "flotante":
                dato = sanitizar_flotante(heroe[clave])
            case "entero":
                dato = sanitizar_entero(heroe[clave])
            case "string":
                dato = sanitizar_string(heroe[clave], "-")
            case _:
                print("Tipo de dato no reconocido")
                return False
        return dato

def stark_normalizar_datos(lista:list):
    if lista:
        for item in lista:
            sanitizar_dato(item, "altura", "flotante")
            sanitizar_dato(item, "peso", "flotante")
            sanitizar_dato(item, "color_ojos", "string")
            sanitizar_dato(item, "color_pelo", "string")
            sanitizar_dato(item, "fuerza", "entero")
            sanitizar_dato(item, "inteligencia", "string")
        print("Datos normalizados")
    else:
        print("Error: Lista de heroes vacía")

def generar_indices_nombres(lista:list):
    lista_nombres = []
    if lista:
        for item in lista:
            if type(item) == dict:
                nombre = item["nombre"]
                nombre = re.split(" ", nombre)
                for i in nombre:
                    lista_nombres.append(i)
            else:
                return "El origen de datos no contiene el formato correcto"
        
        return lista_nombres
    else:
        return "El origen de datos no contiene el formato correcto"

def stark_imprimir_indice_nombre(lista:list):
    nombres = generar_indices_nombres(lista)
    nombres = "-".join(nombres)
    print(nombres)


def convertir_cm_a_mtrs(valor_cm:float):
    cm = sanitizar_flotante(valor_cm)
    metros = cm / 100
    return metros

def generar_separador(patron:str, largo:int, imprimir:bool == False):
    if largo < 236 and patron:
        separador = patron * largo
        if imprimir:
            print(separador)
        return separador
    else:
        return "N/A"


def generar_encabezado(titulo:str):
    encabezado = f"{generar_separador('*', 80, False)}\n{titulo.upper()}\n{generar_separador('*', 80, False)}"
    return encabezado



def imprimir_ficha_heroe(heroe:dict):
    datos = f"{generar_encabezado('principal')}\nNOMBRE DEL HEROE: {heroe['nombre']}\nIDENTIDAD SECRETA: {heroe['identidad']}\nCONSULTORA: {heroe['empresa']}\nCODIGO DE HEROE: {heroe['codigo_heroe']}\n{generar_encabezado('fisico')}\nALTURA: {heroe['altura']}\nPESO: {heroe['peso']}\nFUERZA: {heroe['fuerza']}\n{generar_encabezado('señas particulares')}\nCOLOR DE OJOS: {heroe['color_ojos']}\nCOLOR DE PELO: {heroe['color_pelo']}"
    print(datos)


def stark_navegar_fichas(lista:list):
    contador = 0
    while True:
        imprimir_ficha_heroe(lista[contador])
        opcion = input("[1] Ir a la izquiera [2] Ir a la derecha [s] Salir: ").lower()
        match opcion:
            case "1":
                contador += 1
                if contador > 23:
                    contador = 0
                imprimir_ficha_heroe(lista[contador])
            case "2":
                contador -= 1
                if contador < -24:
                    contador = 0
                imprimir_ficha_heroe(lista[contador])
            case "s":
                return opcion
            case _:
                print("ERROR, reintente")
                os.system("pause")
        continue

def imprimir_menu():
    os.system("cls")
    print("""***Bienvenidos a las Industrias Stark***
************Menu de Opciones************
1-Imprimir la lista de nombres junto con sus iniciales
2-Generar códigos de héroes
3-Normalizar datos
4-Imprimir índice de nombres
5-Navegar fichas
S-Salir""")
#--------------------------------------------------------------------------------------------------------------------------------------      
def validar_entero(num):
    try:
        int(num)
        entero = True
    except ValueError:
        entero = False
    
    return entero

def stark_menu_principal():
    imprimir_menu()
    
    opcion =(input("Ingrese una opcion: ")).lower()

    if validar_entero(opcion):
        return int(opcion)
    elif opcion == "s":
        return opcion
    else:
        return -1

def stark_marvel_app_3(lista:list):
    opcion = stark_menu_principal()
    match opcion:
        case 1:
            stark_imprimir_nombres_con_iniciales(lista)
        case 2:
            stark_generar_codigos_heroes(lista)
        case 3:
            stark_normalizar_datos(lista)
        case 4:
            stark_imprimir_indice_nombre(lista)
        case 5:
            lista_heroes_iniciales = (agregar_iniciales_nombre(lista))
            lista_heroes_iniciales.append(stark_generar_codigos_heroes(lista))
            lista_heroes_iniciales.pop(-1)
            opcion = stark_navegar_fichas(lista_heroes_iniciales)
            if opcion == "s":
                return stark_menu_principal()
        case "s":
            opcion = input("Seguro que desea salir? s/n: ")
            return opcion
        case _:
            print("ERROR. Opción inválida. Reintente")
    
flag_seguir = True
while flag_seguir:
    os.system("cls") #se limpia la consola
    print("-------------------------------------")
    y = stark_marvel_app_3(lista_personajes)
    if y == "s":
        flag_seguir = False
                
    os.system("Pause")
        
