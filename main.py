from algoritmos import Funciones
from algoritmos import heapSort
from algoritmos import Busqueda
ordenar =  heapSort()

if __name__ == "__main__":
    flag =  True
    while flag == True:
        condicion = False
        print("1. Tareas")
        print("2. Compras")
        print("3. Salir")
        select = int(input("Ingresa la opcion\n"))


        if select == 1:
            flag2 = True
            while flag2 == True:
                print("(^o^)/==================(^o^)/\n")
                print("1. ingresar tarea\n")
                print("2. Modificar tarea\n")
                print("3. Imprimir tareas\n")
                print("4. ordenar tareas\n")
                print("5. buscar tareas\n")
                print("6. Crear ruta de tareas\n")
                print("7. Regresar")

                select = int(input("Ingresa la opcion\n"))
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
                    flag3 = True
                    while flag3 == True:
                        print("ordenar por: \n 1. dias para entregar \n 2. Prioridad\n 3. Regresar")
                        opcion = int(input("Ingresa la opcion\n"))
                        if opcion == 1:
                            ordenar.heapSort_diasParaEntregar(lista)
                        elif opcion == 2:
                            ordenar.heapSort(lista)
                        elif opcion == 3:
                            flag3 = False
                        else:
                            print("\nError\n")
                            flag3 = True

                elif select == 5:#buscar tareas3
                    print("")
                elif select == 6:#ruta de tareas
                    lista = []
                    Funciones.crear_grafo(lista)
                elif select == 7:
                    flag2 = False
                else:
                    print("\nError\n")
                    flag2 = True
            
        elif select == 2:
            flag4 = True
            while flag4 == True:
                print("(^o^)/==================(^o^)/\n")
                print("1. ingresar productos\n")
                print("2. Imprimir productos\n")
                print("3. Precio productos\n")
                print("4. Regresar")

                select = input("Ingresa la opcion")
                if select == 1:#ingresar productos
                    print("")
                elif select == 2:#imprimir productos
                    print("")
                elif select == 3:#precioproductos
                    print("")
                elif select == 4:
                    flag4 = False
                else:
                    print("\nError\n")
                    flag4 = True
        elif select == 3:
            flag = False

        else:
            print("\nError\n")
            flag = True
