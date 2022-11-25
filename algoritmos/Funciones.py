from arboles import *
import csv
from Tarea import Tarea
def crear_tarea():
    print('REGISTRO DE TAREA:')
    nombre = input('Nombre de la tarea: ')
    descripcion = input('Ingresa una descripcion de la tarea: ')
    condicion = True
    while condicion:
        try:
            urgencia = int(input('En una escala del 1 al 3 ¿Qué tan urgente es su realización? '))
            condicion = False
        except Exception as e:
            print('Error')
    condicion = True
    while condicion:
        try:
            tiempo = int(input('Ingresa un tiempo estimado para la realizacion de la tarea: '))
            condicion = False
        except Exception as e:
            print('Error')
    condicion = True
    while condicion:
        try:
            dias = int(input('¿Cuantos dias tienes para la realizacion de la actividad? '))
            condicion = False
        except Exception as e:
            print('Error')
    
    return Tarea(nombre,descripcion,urgencia,tiempo,dias)
        
def lista_de_tareas():
    lista_de_tareas = []
    condicion = True
    while condicion:
        tarea = crear_tarea()
        lista_de_tareas.append(tarea)
        c_interna = True
        while c_interna:
            try:
                res = int(input('¿Quieres ingresar otra tarea?\n1.-Si\n2.-No\n'))
                c_interna = False
            except Exception as e:
                print('Error')
        if res == 1:
            print()
        elif res == 2:
            condicion = False
    return lista_de_tareas
            
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



        
#Para ingresar el producto
def ingresar_producto():
    print('Registro del producto')
    nombre = input('Ingresa el nombre del producto: ')
    condicion = True
    while condicion:
        try:
            precio = float(input('Ingresa el precio del producto: '))
            condicion = False
        except Exception as e:
            print('Error')
    condicion = True
    while condicion:
        try:
            cantidad = int(input('¿Cuantos?:  '))
            condicion = False
        except Exception as e:
            print('Error')
    
    producto = Producto(nombre,precio,cantidad)
    return producto

#Crea la lista de productos
def lista_de_productos():
    lista_de_productos = []
    condicion = True
    while condicion:
        producto = ingresar_producto()
        lista_de_productos.append(producto)
        try:
            res = int(input('¿Quieres ingresar otro producto?\n1.-Si\n2.-No\n'))
            if res == 1:
                print()
            elif res == 2:
                condicion = False #Sale del while
                print('\nLista finalizada')                
        except Exception as e:
            print(f'Error')
    return lista_de_productos
    
#Para crear el arbol
def crear_arbol(lista_de_productos):
    arbol = Arbol('x',0,0) #Producto simbolico (necesario unicamente para la creacion del arbol)
    for producto in lista_de_productos:
        arbol.agregar_2(producto.nombre,producto.precio,producto.cantidad)
    return arbol

#Agrega un producto (al arbol y a la lista)
def agregar_producto(arbol,lista_de_productos):
    producto = ingresar_producto()
    lista_de_productos.append(producto)
    arbol.agregar_2(producto.nombre,producto.precio,producto.cantidad)
    return arbol,lista_de_productos

#Retorna el total de la compra
def total_de_compra(arbol):
    arbol.calcularTotal()
    return arbol.totalDeCompra

def escribir_productos(lista_productos,nombre_lista):
    archivo = str(nombre_lista) + '.csv'
    with open(archivo,'w',encoding='UTF-8',newline='')as file:
        writer = csv.writer(file,delimiter = '$')
        for producto in lista_productos:
            registro = [producto.nombre,producto.precio,producto.cantidad]
            writer.writerow(registro)

def leer_lista_productos(nombre_lista):
    archivo = str(nombre_lista) + '.csv'
    with open(archivo)as file:
        lista_productos = []
        reader = csv.reader(file,delimiter='$')
        for row in reader:
            lista_productos.append(Producto(row[0],row[1],row[2]))
    return lista_productos
    
def lista_para_el_usuario(arbol,lista_de_productos):
    with open('Lista_de_productos.txt','w',encoding='UTF-8') as file:
        file.write('LISTA DE PRODUCTOS:\n')
        contador = 0
        for producto in lista_de_productos:
            contador+=1
            file.write(f'{contador}.-{producto.nombre} - Precio: {producto.precio} - Cantidad a comprar: {producto.cantidad}\n')
        arbol.totalDeCompra = 0 
        arbol.calcularTotal()
        total = arbol.totalDeCompra
        file.write(f'Total de la compra: ${total}')
        
        
if __name__ == '__main__':
    lista_de_tareas = lista_de_tareas()
    for tarea in lista_de_tareas:
        print(tarea)