class Tarea:
    def __init__(self,nombre,descripcion,urgencia,tiempo,diasParaEntregar):
        self.nombre = nombre
        self.descripcion =descripcion 
        self.urgencia = urgencia
        self.tiempo = tiempo
        self.diasParaEntregar = diasParaEntregar
        self.padre = None
        #Para grafos
        self.visitado = False
        self.padre = None
        self.vecinos = []
        self.yaRecorrido = False
    def agregarVecino(self,v):
        if v not in self.vecinos:
            self.vecinos.append(v)
    def escogerMasCorto(self):
        mas_corto = 100
        destino = None
        for nodo in self.vecinos:
            if nodo.tiempo < mas_corto and nodo.yaRecorrido == False:
                mas_corto = nodo.tiempo
                destino = nodo
        return destino,mas_corto
        
    def revisar_vecinos(self):
        vecinos_sin_visitar = 0
        for nodo in self.vecinos:
            if nodo.yaRecorrido == False:
                vecinos_sin_visitar +=1
        return vecinos_sin_visitar

    def __str__(self):
        return f'{self.nombre}'
    
    
    