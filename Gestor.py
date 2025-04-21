# Gestor de Contactos
def mostrar_menu():
    print("\nGestor de Contactos")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Ver contactos")
    print("4. Salir")

def agregar_contacto(contactos):
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    contactos.append({"nombre": nombre, "telefono": telefono})
    print(f"Contacto {nombre} agregado.")

def eliminar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            contactos.remove(contacto)
            print(f"Contacto {nombre} eliminado.")
            return
    print("Contacto no encontrado.")

def ver_contactos(contactos):
    if not contactos:
        print("No hay contactos para mostrar.")
    else:
        print("\nLista de Contactos:")
        for idx, contacto in enumerate(contactos, start=1):
            print(f"{idx}. {contacto['nombre']} - {contacto['telefono']}")

def main():
    contactos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            eliminar_contacto(contactos)
        elif opcion == "3":
            ver_contactos(contactos)
        elif opcion == "4":
            print("Saliendo del gestor de contactos. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
