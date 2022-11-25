from Tarea import Tarea

def busqueda_nombre(lista_tareas,nombre):
    i = 0

    while i<len(lista_tareas):
        if lista_tareas[i].nombre.lower() == nombre.lower():
            return lista_tareas[i]
        i+=1

def busqueda_fecha(lista_tareas):
    menor = lista_tareas[0].diasParaEntregar
    mas_proximas = []
    for tarea in lista_tareas:
        if tarea.diasParaEntregar < menor:
            menor = tarea.diasParaEntregar
            
    for tarea in lista_tareas:
        if tarea.diasParaEntregar == menor:
            mas_proximas.append(tarea)
            
    return mas_proximas

def busqueda_importancia(lista_tareas):
    mayor_urgencia = lista_tareas[0].urgencia
    mas_urgentes = []
    for tarea in lista_tareas:
        if tarea.urgencia > mayor_urgencia:
            mayor_urgencia = tarea.urgencia            
    for tarea in lista_tareas:
        if tarea.urgencia == mayor_urgencia:
            mas_urgentes.append(tarea)
    return mas_urgentes

# tarea1 = Tarea('Ecuaciones','Hacer la serie',3,2,False,2)
# tarea2 = Tarea('EDA','Hacer el proyecto',2,2,True,3)
# tarea3 = Tarea('POO','Hacer el examen',5,1,False,4)

# lista_tareas = [tarea1,tarea2,tarea3]

# retorno = busqueda_importancia(lista_tareas)

# for i in retorno:
#     print(i)