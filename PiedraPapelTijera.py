#piedra papel tijera en python
import random

def jugar():
    opciones= ["piedra", "papel", "tijera"]
    puntos_jugador = 0
    puntos_computadora = 0
    
    while True:
        #hacemos que el usuario elija las opciones
        jugador= input("Elige piedra,papel,tijera, o salir: ").lower()
        if jugador == 'salir'.lower():
            break
        while jugador not in opciones: #si no elije piedra,papel,tijera, que pruebe de nuevo
            print("Elija una opcion correcta. Intentalo de nuevo")
            jugador=input("Elige nuevamente. ").lower()
    
    
    # se establece lo que la maquina eligira
        computadora= random.choice(opciones)
        print(f"La computadora eligio: {computadora}")
    
    #establecemos las condiciones para saber quien gana en el juego
        if jugador == computadora:
            print(f"Hubo un empate, ambos eligieron {jugador}")
        elif(jugador == 'piedra' and computadora == 'tijera') or \
            (jugador == 'papel' and computadora == 'piedra') or \
            (jugador == 'tijera' and computadora == 'papel'):
            print("Felicidades, has ganado!")
            puntos_jugador+=1
        else:
            print("Lo siento, has perdido")
            puntos_computadora+=1
        
        #muestra las puntuaciones
        print(f"Puntuacion: Usuario: {puntos_jugador}, Computadora: {puntos_computadora}")
        print("-" * 30)
    
    print("Juego terminado")
    if puntos_jugador > puntos_computadora:
        print(f"Felicidades, ganaste el juego, tu puntuacion es de: {puntos_jugador}")
    elif puntos_jugador < puntos_computadora:
        print(f"Lo siento has perdido el juego, tu has hecho {puntos_jugador} puntos, y la computadora {puntos_computadora} puntos")
    else:
        print(f"Es un empate! Ambos obtuvieron {puntos_computadora} puntos")    
jugar()   
