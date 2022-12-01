##2. Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
##clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
##tener un método para agregar productos y otra para mostrar toda la lista de productos.
class Producto:

    def __init__(self,autoparte,precio):
        self.autoparte=autoparte
        self.precio=precio

    def __str__(self):
        return "la autoparte {}, esta costando: {} soles ".format(self.autoparte,self.precio)


class Catalogo:
    listaProductos = []

    def __init__(self,productos):
        self.listaProductos.append(productos)

    def agregar(self,p):
        self.listaProductos.append(p)
    def mostrar(self):
        for p in self.listaProductos:
            print(p)

p1=Producto("Batería",250)
c1=Catalogo(p1)
c1.mostrar()