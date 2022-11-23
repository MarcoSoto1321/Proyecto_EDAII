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
    totalDeCompra = 0
    def __init__(self,nombre,precio,cantidad):
        self.raiz = Producto(nombre, precio, cantidad)
    
    def agregar_recursivo(self,producto,nombre,precio,cantidad):
        if precio < producto.precio:
            if producto.izquierda == None:
                producto.izquierda = Producto(nombre,precio,cantidad)
            else:
                self.agregar_recursivo(producto.izquierda, nombre, precio, cantidad)
        else:
            if producto.derecha is None:
                producto.derecha = Producto(nombre, precio, cantidad)
            else:
                self.agregar_recursivo(producto.derecha, nombre, precio, cantidad)
                
    def inorder_recursivo(self,producto):
        if producto is not None:
            self.inorder_recursivo(producto.izquierda)
            self.totalDeCompra += producto.precio * producto.cantidad
            print(producto.nombre,end=', ')
            self.inorder_recursivo(producto.derecha)     

    def calcularTotal(self):  #Esto es inorder 
        print('Lista de compras')
        self.inorder_recursivo(self.raiz)
        print("")
    def agregar_2(self,nombre,precio,cantidad):
        self.agregar_recursivo(self.raiz, nombre,precio,cantidad)

arbol = Arbol('Producto 0',1000,5)
arbol.agregar_2('Producto 1',50,1)
arbol.agregar_2('Producto 2',300,6)
arbol.agregar_2('Producto 3',500,5)
arbol.agregar_2('Producto 5',100,15)
arbol.agregar_2('Producto 7',100,2)
arbol.agregar_2('Producto 8',10, 100)
arbol.calcularTotal()
print(arbol.totalDeCompra) #Para obtener el precio total de la compra