#En este se realiza un simulador de dados, para probar la suerte 
import random

def tirar_dados():
    return random.randint(1,6)

print("Bienvenido al simulador de dados")
while True:
    input("Presiona enter para tirar el dado")
    resultado= tirar_dados()
    print(f"🎲 Salió un {resultado}!")
    
    otravez= input("Quieres tirar de vuelta? (s/n)").strip().lower()
    if otravez != 's':
        print("Gracias por jugar")
        break
    