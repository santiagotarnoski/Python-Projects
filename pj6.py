# Programa el cual deberemos adivinar un numero random que nos da el mismo. Si es mas bajo el numero del que nos dio para adivinar, nos dira que es muy bajo, y asi viceversa si es muy grande

import random

num_secreto= random.randint(1,100)
intento = 0

print("Bienvenido, tendras que adivinar un numero entre el 1 al 100")

while True:
    try:
        num= int(input("Ingresa el numero: "))
        intento += 1
        
        if num < num_secreto:
            print("Numero muy bajo, intentalo de nuevo")
        elif num > num_secreto:
            print("Numero muy alto, intentalo de nuevo")
        else:
            print("Felicidades, adivinaste el numero")
            break
    except ValueError:
        print("Ingresa un numero valido, gracias")
