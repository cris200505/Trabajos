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
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto: "))
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
            nuevo_precio = float(nuevo_precio) if nuevo_precio else p['precio']
            nueva_cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else p['cantidad']
            
            p['nombre'] = nuevo_nombre
            p['precio'] = nuevo_precio
            p['cantidad'] = nueva_cantidad
            print("Producto actualizado exitosamente.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    global productos
    productos = [p for p in productos if p['nombre'] != nombre]
    print("Producto eliminado exitosamente." if len(productos) < len(productos) else "Producto no encontrado.")

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
