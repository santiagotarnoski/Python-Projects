#calculadora de imc(indice de masa corporal)
def calculoimc(estatura,peso):
    return peso / (estatura**2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Tiene obesidad"

print("Bienvenido a la calculadora de Indice de Masa Corporal. ")

try:
        
    estatura=float(input("A continuacion, ingrese su altura: "))
    peso=float(input("Ingrese su peso en kg ahora: "))
    
    imc= calculoimc(estatura,peso)
    categoria= clasificar_imc(imc)
    
    print(f"Tu imc es: {imc:.2f}")
    print(f"Categoria: {categoria}")

except ValueError:
    print("Ingresa valores numericos porfavor, gracias.")
          



