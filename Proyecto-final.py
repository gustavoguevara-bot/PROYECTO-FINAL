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

# Victor parte 
def vender_producto():
 nombre_producto = input("Nombre del producto a vender: ")

if nombre_producto not in inventario:
 print("Ese producto no existe")
    return

try:
    cantidad_vendida = int(input("Cantodad a vender: "))
except ValueError
print("Debes escribir un numero entero")
return

cantidad_disponible = iventario[nombre_producto][1]

if cantidad_vendida <= 0:
    print("La Cantidad a Vender debe ser mayor 0.")
elif cantidad_vendida > cantidad_disponible:
print("No hay Suficiente Inventario. Solo quedan", cantidad_disponible, "unidades.")
else:
precio_unitario = inventario[nombre_producto][0]
total_venta = precio_unitario * cantidad_vendida

inventario[nombre_producto][1] = cantidad_disponible - cantidad_vendida

venta = [nombre_producto, cantidad_vendida, precio_unitario,total_venta]
ventas_del_dia.append(venta)

print("Venta realizada.Total a cobrar: $" + str(total_venta))

def buscar_producto():
    nombre_producto = input("Nombre del Producto para buscar: ")

if nombre_producto in inventario:
           precio = inventario[nombre_producto][0]
        cantidad = inventario[nombre_producto][1]
        print("Producto encontrado -> Precio: $" + str(precio), "- Cantidad:", cantidad)
    else:
        print("El producto no se encuentra en el inventario.")


def reporte_stock_bajo():
    print("\n----- PRODUCTOS CON STOCK BAJO (5 o menos) -----")
    hay_stock_bajo = False

    for nombre_producto in inventario:
        cantidad = inventario[nombre_producto][1]
        if cantidad <= 5:
            print(nombre_producto, "- Cantidad restante:", cantidad)
            hay_stock_bajo = True

    if hay_stock_bajo == False:
        print("No hay productos con stock bajo por el momento.")


def ver_ventas_del_dia():
    if len(ventas_del_dia) == 0:
        print("Todavia no se ha registrado ninguna venta hoy.")
        return

    print("\n----- VENTAS DEL DIA -----")
    for venta in ventas_del_dia:
        nombre_producto = venta[0]
        cantidad_vendida = venta[1]
        precio_unitario = venta[2]
        total_venta = venta[3]
        print(nombre_producto, "| Cantidad:", cantidad_vendida, "| Precio unitario: $" + str(precio_unitario), "| Total: $" + str(total_venta))


def total_vendido_del_dia():
    total = 0
    for venta in ventas_del_dia:
        total = total + venta[3]
    print("El total vendido hoy es: $" + str(total))


def main():
    cargar_inventario()

    programa_activo = True
    while programa_activo == True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_inventario()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            buscar_producto()
        elif opcion == "5":
            reporte_stock_bajo()
        elif opcion == "6":
            ver_ventas_del_dia()
        elif opcion == "7":
            total_vendido_del_dia()
        elif opcion == "8":
            guardar_inventario()
            print("Gracias por usar el sistema. Hasta luego.")
            programa_activo = False
        else:
            print("Opcion no valida, intenta de nuevo.")


main()
# Fin parte Victor
