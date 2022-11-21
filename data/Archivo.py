import csv
from Tarea import Tarea

def escribirTareas(lista_tareas):
    with open('prueba.csv','w',encoding='UTF-8',newline='')as file:
        writer = csv.writer(file,delimiter = ',')
        for tarea in lista_tareas:
            registro = [tarea.nombre,tarea.descripcion,tarea.urgencia,tarea.tiempo,tarea.enCasa,
                        tarea.diasParaEntregar]
            writer.writerow(registro)

def leerTareas():
    with open('prueba.csv')as file:
        lista_tareas = []
        reader = csv.reader(file)
        for row in reader:
            lista_tareas.append(Tarea(row[0],row[1],row[2],row[3],row[4],row[5]))
    return lista_tareas
    
    

# tarea1 = Tarea('Ecuaciones','Hacer la serie',3,2,False,1)
# tarea2 = Tarea('EDA','Hacer el proyecto',2,2,True,2)

# lista_tareas = [tarea1,tarea2]

# escribirTareas(lista_tareas)
# lista_tareas = leerTareas()
# for i in lista_tareas:
#     print(i)