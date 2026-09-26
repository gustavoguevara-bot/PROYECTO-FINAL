# Parte Gustavo
import os

inventario = {}
ventas_del_dia = []
Nombre_Archivo = "inventario.txt"


def cargar_inventario():
    if not os.path.exists(Nombre_Archivo):
        print("No se encontro un inventario")
        return

    try:
        archivo = open(Nombre_Archivo, "r")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes      = linea.split(",")
            nombre      = partes [0]
            precio      = float(partes[1])
            cantidad    = int(partes[2])
            inventario[nombre] = [precio,cantidad]
        archivo.close()
        print("inventario cargado")
    except Exception as error:
        print("Error al cargar el inventario:", error)


def guardar_inventario():
    try:
        archivo = open(Nombre_Archivo, "w")
        for nombre_producto in inventario:
            precio   = inventario[nombre_producto][0]
            cantidad = inventario[nombre_producto][1]
            linea = f"{nombre_producto},{precio},{cantidad}\n"
            archivo.write(linea)
        archivo.close()
        print("Inventario guardado")
    except Exception as error:
        print("Hubo un error al guardar",error)


def mostrar_menu():
    print("\n=== Menu Ferreteria ===")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Vender producto")
    print("4. Buscar producto")
    print("5. Reporte de stock")
    print("6. Ver ventas del dia")
    print("7. Total ventas del dia")
    print("8. Salir")
# Fin Parte Gustavo