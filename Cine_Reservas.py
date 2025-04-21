import os

FILAS = 5
COLUMNAS = 5

peliculas = {
    "1": {"nombre": "Avengers", "horarios": ["15:00", "18:00", "21:00"]},
    "2": {"nombre": "Matrix", "horarios": ["16:00", "19:00"]},
    "3": {"nombre": "Shrek", "horarios": ["14:00", "17:00", "20:00"]}
}

reservas = {}  # clave = pelicula-horario, valor = matriz de 5x5


def inicializar_asientos():
    for p in peliculas:
        for h in peliculas[p]["horarios"]:
            clave = f"{peliculas[p]['nombre']}-{h}"
            reservas[clave] = [["O" for _ in range(COLUMNAS)] for _ in range(FILAS)]


def mostrar_asientos(asientos):
    print("   " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(asientos):
        print(chr(65 + i), " ".join(fila))


def seleccionar_pelicula():
    print("Películas disponibles:")
    for k, p in peliculas.items():
        print(f"{k}. {p['nombre']}")
    return peliculas[input("Elegí la película (número): ")]


def seleccionar_horario(pelicula):
    print(f"Horarios para {pelicula['nombre']}:")
    for i, h in enumerate(pelicula['horarios']):
        print(f"{i + 1}. {h}")
    return pelicula['horarios'][int(input("Elegí el horario (número): ")) - 1]


def reservar_asiento(matriz):
    mostrar_asientos(matriz)
    fila = input("Elegí la fila (A-E): ").upper()
    col = int(input("Elegí el número de asiento (1-5): ")) - 1
    f_idx = ord(fila) - 65

    if matriz[f_idx][col] == "X":
        print("Asiento ocupado.")
    else:
        matriz[f_idx][col] = "X"
        print("Reserva realizada con éxito.")


def guardar_reservas():
    with open("reservas.txt", "w") as f:
        for funcion, matriz in reservas.items():
            f.write(f"{funcion}\n")
            for fila in matriz:
                f.write("".join(fila) + "\n")


def main():
    inicializar_asientos()
    while True:
        print("\n=== Sistema de Reservas ===")
        peli = seleccionar_pelicula()
        hora = seleccionar_horario(peli)
        clave = f"{peli['nombre']}-{hora}"
        reservar_asiento(reservas[clave])
        guardar_reservas()

        cont = input("¿Querés hacer otra reserva? (s/n): ").lower()
        if cont != "s":
            break


if __name__ == "__main__":
    main()
