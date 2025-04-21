#Programa que simula una calculadora con operaciones basicas como suma, resta, multiplicacion, division

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "Error no se puede dividir por 0"
    return a/b

while True:
    print("Calculadora de Python ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
    opcion= input("Elige una opcion (1-5): ").strip()
    
    if opcion == '5':
        print("Hasta Luego!")
    
    if opcion not in["1","2","3","4"]:
        print("Porfavor ingrese un numero valido")
    
    try:
        num1= float(input("Ingrese el primer numero para operar"))
        num2= float(input("Ingrese el segundo numero para operar"))
    except ValueError:
        print("Error, ingresa solo numeros!")
        continue
    
    if opcion == "1":
        print(f"Resultado de la operacion {suma(num1,num2)}")
    if opcion == "2":
        print(f"Resultado de la operacion {resta(num1,num2)}")
    if opcion == "3":
        print(f"Resultado de la operacion {multiplicacion(num1,num2)}")
    if opcion == "4":
        print(f"Resultado de la operacion {division(num1,num2)}")


    