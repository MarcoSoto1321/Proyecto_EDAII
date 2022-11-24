from Tarea import Tarea

class Grafica:
    paso_anterior = 0
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
        if origen in self.vertices: #Verifica si esta en los vertices
            self.vertices[origen].visitado = True #Lo marca como visitado
            for nodo in self.vertices[origen].vecinos:
                #Escoge a cual vecino ir 
                mas_corto = 100
                destino = None
                for n in self.vertices[origen].vecinos:
                    if n.tiempo < mas_corto and n.tiempo>self.paso_anterior:
                        mas_corto = n.tiempo
                        destino = n
                        self.paso_anterior = mas_corto
                # print(destino)
                # print(mas_corto)
                
                if self.vertices[destino].visitado == False:
                    self.vertices[destino].padre = origen
                    print('(' + str(destino) + ', ' + str(origen) + ')')
                    self.dfs(destino)
    
            
            # for nodo in self.vertices[r].vecinos: #Recorre los vecinos
            #     if self.vertices[destino].visitado == False:
            #         self.vertices[destino].padre = r
            #         print('(' + str(destino) + ', ' + str(r) + ')')
            #         self.dfs(destino)
    
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
    # for vertice in g.vertices[tarea_1].vecinos:
    #     print(vertice)

main()
