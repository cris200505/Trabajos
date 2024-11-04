import json
import os

productos = []

def cargar_datos():
    global productos
    if os.path.exists('productos.txt'):
        with open('productos.txt', 'r') as f:
            productos = json.load(f)

def guardar_datos():
    with open('productos.txt', 'w') as f:
        json.dump(productos, f)

def añadir_producto():
    nombre = input("Nombre del producto: ")
    while True:
        try:
            precio = float(input("Precio del producto: "))
            break
        except ValueError:
            print("Error: Por favor ingresa un número válido para el precio.")
    
    while True:
        try:
            cantidad = int(input("Cantidad del producto: "))
            break
        except ValueError:
            print("Error: Por favor ingresa un número entero válido para la cantidad.")
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    print("Producto añadido exitosamente.")

def ver_productos():
    """Muestra la lista de todos los productos."""
    if not productos:
        print("No hay productos en el inventario.")
        return
    for p in productos:
        print(f"Nombre: {p['nombre']}, Precio: {p['precio']}, Cantidad: {p['cantidad']}")

def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ")
    for p in productos:
        if p['nombre'] == nombre:
            nuevo_nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ") or p['nombre']
            nuevo_precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            if nuevo_precio:
                while True:
                    try:
                        nuevo_precio = float(nuevo_precio)
                        break
                    except ValueError:
                        print("Error: Por favor ingresa un número válido para el precio.")
                        nuevo_precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
                p['precio'] = nuevo_precio
            
            nueva_cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            if nueva_cantidad:
                while True:
                    try:
                        nueva_cantidad = int(nueva_cantidad)
                        break
                    except ValueError:
                        print("Error: Por favor ingresa un número entero válido para la cantidad.")
                        nueva_cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
                p['cantidad'] = nueva_cantidad
            
            p['nombre'] = nuevo_nombre
            print("Producto actualizado exitosamente.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    global productos
    cantidad_inicial = len(productos)
    productos = [p for p in productos if p['nombre'] != nombre]
    if len(productos) < cantidad_inicial:
        print(f"Producto eliminado: {nombre}")
    else:
        print("Producto no encontrado.")

def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
