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

# Parte Rodrigo
def agregar_producto():
    nombre_producto = input("Nombre del producto: ")

precio_valido = False
while precio_valido == False:
    try:
        precio_producto = float(input("Precio del producto:"))
        if precio_producto > 0:
            precio_valido = True
        else:
            print("El precio  debe ser mayor a 0.Intenta de nuevo")
    except ValueError:
        print("Debes escribir un numero valido para el precio")

cantidad_valida = False
while cantidad_valida == False
 try:
     cantidad_producto = int(input("Cantidad en inventario:"))
     if cantidad_producto >= 0:
         cantidad_valida = True 
     else:
         print("La cantidad no puede ser negativa")
except ValueError:
    print("Debes escribir un numero entero valido para la cantidad")

inventario[nombre_producto] = [precio_producto,cantidad_producto]
 print("Producto agregado correctamente")

def consultar_inventario():
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return

    print("\n----- INVENTARIO COMPLETO -----")
    for nombre_producto in inventario:
        precio = inventario[nombre_producto][0]
        cantidad = inventario[nombre_producto][1]
        print(nombre_producto, "- Precio: $" + str(precio), "- Cantidad:", cantidad)
# Fin parte de Rodrigo
