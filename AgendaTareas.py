#To do list en python, donde el usuario pueda agregar eliminar y ver tareas 
import json

tareas= []

#Funcion para agregar una tarea
def agregar_tareas(tarea):
    tareas.append(tarea)
    print(f"Tarea {tarea} agregada con exito")

#Funcion para eliminar una tarea
def eliminar_tarea(tarea):
    if tarea in tareas:
        tareas.remove(tarea)
        print(f"Tarea {tarea} fue eliminada de su lista")
    else:
        print(f"Tarea {tarea} no existe en la lista")

#ver tareas
def ver_tareas():
    if tareas:
        print("Lista de Tareas")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")
    else:
        print("No hay ninguna tarea")

def ordenar_tareas():
    tareas.sort()
    print("Tareas ordenadas alfabeticamente.")

def guardar_tareas():
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)
    print("Tareas guardadas con exito.")

def cargar_tareas():
    global tareas
    try:
        with open("tareas.json", "r") as archivo:
            tareas= json.load(archivo)
    except FileNotFoundError:
        tareas= []
        

#Menu para anadir, eliminar y ver tareas

def menu():
    while True:
        print("Menu de lista de tareas: ")
        print("1. Agregar tarea.")
        print("2. Eliminar tarea.")
        print("3. Ver tareas.")
        print("4. Ordenar tareas.")
        print("5. Salir.")
        
        option= input("Seleccione la opcion: ")
        
        if option== "1":
            tarea=input("Ingrese la tarea: ")
            agregar_tareas(tarea)
        elif option== "2":
            tarea= input("Ingrese que tarea quiere eliminar")
            eliminar_tarea(tarea)
        elif option== "3":
            ver_tareas()
        elif option== "4":
            ordenar_tareas()
        elif option== "5":
            print("Hasta Luego! ")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            
#Ejecutor del programa
if __name__ == "__main__":
    cargar_tareas()
    menu()
    