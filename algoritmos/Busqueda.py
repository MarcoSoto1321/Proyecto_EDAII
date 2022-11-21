from Tarea import Tarea

def busqueda(lista_tareas,nombre):
    i = 0
    coincidencias = []
    while i<len(lista_tareas):
        if lista_tareas[i].nombre.lower() == nombre.lower():
            coincidencias.append(lista_tareas[i])
        i+=1
    return coincidencias

# tarea1 = Tarea('Ecuaciones','Hacer la serie',3,2,False,1)
# tarea2 = Tarea('EDA','Hacer el proyecto',2,2,True,2)

# lista_tareas = [tarea1,tarea2]

# encontrados = busqueda(lista_tareas,'ecuaciones')
# for i in encontrados:
#     print(i)