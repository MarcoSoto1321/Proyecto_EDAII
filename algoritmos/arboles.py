class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.izquierda = None
        self.derecha = None
    def __str__(self):
        return f'Producto: {self.nombre}'
        
            


class Arbol:
    def __init__(self,nombre,precio,cantidad):
        self.raiz = Producto(nombre, precio, cantidad)
    
    def agregar(self,producto,nombre,precio,cantidad):
        if precio < producto.precio:
            if producto.izquierda == None:
                producto.izquierda = Producto(nombre,precio,cantidad)
            else:
                self.agregar(producto.izquierda, nombre, precio, cantidad)
        else:
            if producto.derecha is None:
                producto.derecha = Producto(nombre, precio, cantidad)
            else:
                self.agregar(producto.derecha, nombre, precio, cantidad)
    def inorder(self,producto):
        if producto is not None:
            self.inorder(producto.izquierda)
            print(producto.nombre,end=', ')
            self.inorder(producto.derecha)
        

    def inorder_2(self):
        print('imprimiendo inorder')
        self.inorder(self.raiz)
        print("")
    def agregar_2(self,nombre,precio,cantidad):
        self.agregar(self.raiz, nombre,precio,cantidad)

arbol = Arbol('x',0,0)
arbol.agregar_2('Producto 1',50,1)
arbol.agregar_2('Producto 2',150,6)
arbol.agregar_2('Producto 3',500,5)
arbol.inorder_2()