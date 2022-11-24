from Tarea import Tarea

class Grafica:
    mas_corto_anterior = 1000
    def __init__(self):
        self.vertices = {}
    def agregarVertice(self,tarea):
        if tarea not in self.vertices:
            self.vertices[tarea] = tarea
    def agregarArista(self,a,b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b)
            self.vertices[b].agregarVecino(a)
            
                    
    def dfs(self,origen):
        if origen in self.vertices:
            self.vertices[origen].yaRecorrido = True #Marca el origen como visitado
            destino,mas_corto = origen.escogerMasCorto() #Elige el mas corto
            self.vertices[destino].yaRecorrido = True
            # print(f'Destino: {destino}')
            print('(' + str(origen) + ', ' + str(destino) + ')')
            if destino.revisar_vecinos() > 0:                
                self.dfs(destino)
            
            



def main():
    g = Grafica()
    tarea_1 = Tarea('Tarea 1','Descripcion 1',3,1,2)
    tarea_2 = Tarea('Tarea 2','Descripcion 2',2,4,2)
    tarea_3 = Tarea('Tarea 3','Descripcion 3',1,7,2)
    tarea_4 = Tarea('Tarea 4','Descripcion 4',2,9,2)
    tarea_5 = Tarea('Tarea 5','Descripcion 5',1,2,2)
    tarea_6 = Tarea('Tarea 6','Descripcion 6',3,3,2)

    l = [tarea_1,tarea_2,tarea_3,tarea_4,tarea_5,tarea_6]
    for tarea in l:
        g.agregarVertice(tarea)

    lista_aristas = [tarea_1,tarea_2,tarea_1,tarea_3,tarea_1,tarea_4,tarea_1,tarea_5,tarea_1,tarea_6,
                    tarea_2,tarea_3,tarea_2,tarea_4,tarea_2,tarea_5,tarea_2,tarea_6,
                    tarea_3,tarea_4,tarea_3,tarea_5,tarea_3,tarea_6,
                    tarea_4,tarea_5,tarea_4,tarea_6,
                    tarea_5,tarea_6]

    for i in range(0,len(lista_aristas)-1,2):
        g.agregarArista(lista_aristas[i], lista_aristas[i+1])

    g.dfs(tarea_1)


main()
