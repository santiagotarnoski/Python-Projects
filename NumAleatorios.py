#Este programa ingresa numeros aleatorios en base a la cantidad de numeros que nosotros le pidamos
import random

num= int(input("Ingrese la cantidad de numeros aleatorios que quieres que se generen: "))

def numaleatorio(cantidad):
    return [random.randint(1,100) for _ in range(cantidad)]

numero= numaleatorio(num)

print(f"Los numeros son: {numero}")

