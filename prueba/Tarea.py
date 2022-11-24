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
        self.nivel = -1
        self.padre = None
        self.vecinos = []
        self.yaRecorrido = False
    def agregarVecino(self,v):
        if v not in self.vecinos:
            self.vecinos.append(v)
        
        
        
    
    def __str__(self):
        return f'{self.nombre}'
    
    
    