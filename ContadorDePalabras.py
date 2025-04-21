#contador de palabras, en este contaremos la cantidad de palabras en un texto

def contadorpalabras(texto):
    """Cuenta la cantidad de palabras en un texto."""
    palabras = texto.strip().split()
    return len(palabras)


texto= input("Ingrese el texto que desees: ")
cantidad= contadorpalabras(texto)
print(f"El texto tiene {cantidad} palabras")
