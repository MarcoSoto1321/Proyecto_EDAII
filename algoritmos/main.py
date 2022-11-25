from Tarea import Tarea
from arboles import *
from Funciones import *
from Funciones import lista_de_tareas
import csv
from Busqueda import *
from heapsort import *
from Archivo import *
from Grafos import *

def main():
    print('MENÚ')
    condicion = True
    while condicion:
        try:
            entrada = int(input('¿Que quieres hacer?\n1.-Tareas\n2.-Lista de compras\n'))
            condicion = False
        except Exception as e:
            print('Error')
    if entrada == 1:
        # lista_tareas = None
        print('BIENVENIDO AL MENÚ DE TAREAS')
        nombre_usuario = input('En primer lugar, ¿Cual es tu nombre?\n')
        print(f'Hola,{nombre_usuario}')
        print('Ingresa una de las siguientes opciones: ')
        print('1.-Registrar tareas')
        print('2.-Agregar tarea')
        print('3.-Modificar tarea')
        print('4.-Obtener un plan de trabajo')
        print('5.-Mostrar tareas')
        print('6.-Salir')
        opcion = int(input(': '))
        if opcion == 1:
            print('Has elegido la opcion de registrar tareas\n')
            lista_t = lista_de_tareas()
            escribirTareas(lista_t, nombre_usuario)
        if opcion == 2:
            print('Has elegido la opcion de agregar una tarea')
            if lista_t is None:
                print('Parece que no tienes donde agregar tareas, empecemos creando algunas\n')
                lista_t = lista_de_tareas()
            else:
                tarea = crear_tarea()
                lista_t.append(tarea)
            escribirTareas(lista_t, nombre_usuario)
        if opcion == 3:
            print('Has elegido la opcion de modificar una tarea\n')
            if lista_t is None:
                print('Parece que no tienes tareas registradas, comencemos por ahi')
                lista_t = lista_de_tareas()
            else:
                nombre_tarea = input('ingresa el nombre de la tarea a modificar: ')
                modificar_tarea(lista_t, nombre_tarea)
                escribirTareas(lista_t, nombre_usuario)
        if opcion == 4:
            print('Has elegido la opcion de crear un plan de trabajo')
            if lista_t is None:
                print('Parece que no tienes tareas registradas, comencemos por ahi')
                lista_t = lista_de_tareas()
                escribirTareas(lista_t, nombre_usuario)
                prioridad_alta = prioridad_alta(lista_de_t)
                prioridad_media = prioridad_media(lista_de_t)
                prioridad_baja = prioridad_baja(lista_de_t)
                #Grafos
                alta = crear_grafo(prioridad_alta)
                media = crear_grafo(prioridad_media)
                baja = crear_grafo(prioridad_baja)
                if len(prioridad_alta) > 0:
                    alta.dfs(prioridad_alta[0])
                    escribir_ruta(alta, nombre_usuario)
                if len(prioridad_media)> 0:
                    media.dfs(prioridad_media[0])
                    escribir_ruta(media, nombre_usuario)
                if len(prioridad_baja)>0:
                    baja.dfs(prioridad_baja[0])
                    escribir_ruta(baja, nombre_usuario)
            else:
                prioridad_alta = prioridad_alta(lista_t)
                prioridad_media = prioridad_media(lista_t)
                prioridad_baja = prioridad_baja(lista_t)
                #Grafos
                alta = crear_grafo(prioridad_alta)
                media = crear_grafo(prioridad_media)
                baja = crear_grafo(prioridad_baja)
                if len(prioridad_alta) > 0:
                    alta.dfs(prioridad_alta[0])
                    escribir_ruta(alta, nombre_usuario)
                if len(prioridad_media)> 0:
                    media.dfs(prioridad_media[0])
                    escribir_ruta(media, nombre_usuario)
                if len(prioridad_baja)>0:
                    baja.dfs(prioridad_baja[0])
                    escribir_ruta(baja, nombre_usuario)
                    
                    
        if opcion == 5:
            print('Has elegido la opcion de mostrar tareas: \n')
            print('Elige que tareas quieres ver')
            print('1.-Mostrar las mas urgentes')
            print('2.-Mostrar las de fecha de entrega más próxima')
            condicion = True
            while condicion:
                try:
                    a = int(input('Ingresa la opcion: '))
                    condicion = False
                except Exception  as e:
                    print('Error')
            if a == 1:
                print('Tareas mas urgentes: ')
                mas_urgentes = busqueda_importancia(lista_t)
                for tarea in mas_urgentes:
                    print(tarea)
            elif a == 2:
                print('Mas proximas a entregar: ')
                mas_cercanas = busqueda_fecha(lista_t)
                for tarea in mas_cercanas:
                    print(tarea)
            else:
                print('Opcion invalida')
        if opcion == 6:
            print('Hasta luego')            
    #Lista de compras        
    elif entrada == 2:
        print('BIENVENIDO AL MENU DE LISTA DE COMPRAS')
        print('''Aqui podras escribir que cosas requieres comprar incluyendo su precio y cantidad
            y al final podrás tener la opcion de conseguir un preticked para conocer el valor aproximado
            de tu compra''')
        print('En primer lugar, registremos los articulos que comprarás')
        lista_de_p = lista_de_productos()
        arbol = crear_arbol(lista_de_p)
        condicion = True
        while condicion:
            print('¿Que quieres hacer?')
            print('1.-Ingresar otro producto\n2.-Obtener preticked\n3.-Salir')
            c_interna = True
            while c_interna:
                try:
                    opcion = int(input('Ingresa tu opcion: '))
                    c_interna = False
                except Exception as e:
                    print('Error')
            if opcion == 1:
                arbol,lista_de_p = agregar_producto(arbol, lista_de_p)
            elif opcion == 2:
                lista_para_el_usuario(arbol, lista_de_p)
                print('Revisa tus archivos, ahi esta el preticked')
                condicion = False
            elif opcion == 3:
                print(f'Adios,{nombre_usuario}')
                condicion = False
            else:
                print('Opcion invalida')
                
                
                
if __name__ == '__main__':
    main()