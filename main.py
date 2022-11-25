from algoritmos import Funciones
from algoritmos import heapSort
from algoritmos import Busqueda


ordenar =  heapSort()
if __name__ == "__main__":
    print("1. Tareas")
    print("2. Compras")
    select = int(input("Ingresa la opcion\n"))

    if select == 1:

        print("(^o^)/==================(^o^)/\n")
        print("1. ingresar tarea\n")
        print("2. Modificar tarea\n")
        print("3. Imprimir tareas\n")
        print("4. ordenar tareas\n")
        print("5. buscar tareas\n")
        print("6. Crear ruta de tareas\n")

        select = input("Ingresa la opcion\n")
        if select == 1:#agregar tareas
            print("")
        elif select == 2:#modificar tareas
            lista = []
            nombre = ""
            Funciones.modificar_tarea(lista, nombre)

        elif select == 3:#imprimir tareas
            print("")

        elif select == 4:#ordenar tareas
            lista = []
            print("ordenar por: \n 1. dias para entregar \n 2. Prioridad")
            opcion = int(input("Ingresa la opcion\n"))
            if opcion == 1:
                ordenar.heapSort_diasParaEntregar(lista)
            elif opcion == 2:
                ordenar.heapSort(lista)
            else:
                print("Ingresa una opcion valida")

        elif select == 5:#buscar tareas
            print("")
        elif select == 6:#ruta de tareas
            lista = []
            Funciones.crear_grafo(lista)
        else:
            print("")
        
    if select == 2:

        print("(^o^)/==================(^o^)/\n")
        print("1. ingresar productos\n")
        print("2. Imprimir productos\n")
        print("3. Precio productos\n")

        select = input("Ingresa la opcion")
        if select == 1:#ingresar productos
            print("")
        elif select == 2:#imprimir productos
            print("")
        elif select == 3:#precioproductos
            print("")
        else:
            print("")

