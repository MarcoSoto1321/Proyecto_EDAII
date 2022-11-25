
def selecccionTareas(select):
    if select == 1:
        print("")
    elif select == 2:
        print("")
    elif select == 3:
        print("")
    elif select == 4:
        print("")
    elif select == 5:
        print("")
    elif select == 6:
        print("")
    else:
        print("")

def selecccionCompras(select):
    if select == 1:
        print("")
    elif select == 2:
        print("")
    elif select == 3:
        print("")
    else:
        print("")

if __name__ == "__main__":
    select = 0
    print("1. Tareas")
    print("2. Compras")
    select = input("Ingresa la opcion")
    if select == 1:

        print("(^o^)/==================(^o^)/\n")
        print("1. ingresar tarea\n")
        print("2. Modificar tarea\n")
        print("3. Imprimir tareas\n")
        print("4. ordenar tareas\n")
        print("5. buscar tareas\n")
        print("6. Crear ruta de tareas\n")

        select = input("Ingresa la opcion")
        selecccionTareas(select)
        
    if select == 2:

        print("(^o^)/==================(^o^)/\n")
        print("1. ingresar productos\n")
        print("2. Imprimir productos\n")
        print("3. Precio productos\n")

        select = input("Ingresa la opcion")
        selecccionCompras(select)
