#conversor de unidades

def km_millas(km):
    return km * 0.621371

def millas_km (km):
    return km / 0.621371

def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_celsius(celsius):
    return (celsius - 32) * 5/9

while True:
    print("Conversor de unidades: ")
    print("1. Km a millas")
    print("2. millas a km")
    print("3. celsius a fahrenheit")
    print("4. fahrenheit a celsius")
    print("5. Salir")
    
    opcion= input("Escoja una opcion (1-5): ").strip()
    
    if opcion== "5":
        print("Gracias, hasta luego")
        break

    if opcion not in ["1","2","3","4"]:
        print("Porfavor ingrese numeros validos")
        continue

    try:
        valor=float(input("Ingrese el valor a convertir: "))
    except ValueError:
        print("Ingresa solo numeros porfavor")
    
    if opcion == '1':
        print(f"{valor} km = {km_millas(valor): .2f} millas")
    elif opcion == '2':
        print(f"{valor} millas = {millas_km(valor): .2f} km")
    elif opcion == '3':
        print(f"{valor} Celsius = {celsius_fahrenheit(valor): .2f} Fahrenheit")
    elif opcion == '4':
        print(f"{valor} Fahrenheit = {fahrenheit_celsius(valor): .2f} Celsius")
        