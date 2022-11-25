def modificar_tarea(lista_tareas,nombre):
    tarea = busqueda_nombre(lista_tareas, nombre)
    if tarea != None:
        c = True
        indice = lista_tareas.index(tarea)
        entrada = int(input('¿Que quieres modificar?\n1.-Descripcion\n2.-Urgencia\n3.-Tiempo de realizacion\n4.-Dias de entrega\n'))
        if entrada == 1:
            cambio = input('Ingresa la nueva descripcion: \n')
            tarea.descripcion = cambio
            c = False
        elif entrada == 2:
            condicion = True
            while condicion:
                cambio = int(input('Ingresa la nueva urgencia'))
                if cambio >= 1 and cambio<=3:
                    tarea.urgencia = cambio
                    condicion = False
                else:
                    print('Ingresa un valor entre 1 y 3\n')
            c = False
        elif entrada == 3:
            cambio = int(input('Ingresa el tiempo de realizacion: '))
            tarea.tiempo = cambio
            c = False
        elif entrada == 4:
            cambio = int(input('Ingresa cuantos dias tienes para finalizar la tarea: '))
            tarea.diasParaEntregar = cambio
            c = False
        else:
            print('Ingresa un valor que se encuentre en el menu')
    else:
        print('La tarea que ingresaste no existe')
        

def crear_grafo(lista): #Recibe la lista ya filtrada
    g = Grafica()
    #Ingresa todas las tareas al grafo
    for tarea in lista:
        g.agregarVertice(tarea)
    #Crear aristas
    aristas = []
    i=0
    relaciones = len(lista)
    while i<len(lista): 
        for k in range(relaciones):
            aristas.append(lista[i])
            aristas.append(lista[i+k])
        relaciones -= 1
        i+=1
    #Agrega las aristas
    for i in range(0,len(aristas)-1,2):
        g.agregarArista(aristas[i],aristas[i+1])
    
    return g

#Para crear las prioridades
def prioridad_alta(lista_tareas):
    alta_prioridad = []
    for tarea in lista_tareas:
        if tarea.urgencia == 1 and tarea.diasParaEntregar <= 1:
            alta_prioridad.append(tarea)
    return alta_prioridad

def prioridad_media(lista_tareas):
    prioridad_media = []
    for tarea in lista_tareas:
        if tarea.urgencia == 2 and (tarea.diasParaEntregar>=2 and tarea.diasParaEntregar<=4):
            prioridad_media.append(tarea)

def prioridad_baja(lista_tareas):
    prioridad_baja = []
    for tarea in lista_tareas:
        if tarea.urgencia == 3 and tarea.diasParaEntregar>4:
            prioridad_baja.append(tarea)
    return prioridad_baja