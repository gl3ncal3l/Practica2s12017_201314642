import Estructuras.NodoPila
nodo = Estructuras.NodoPila

class Pila(object):
    def __init__(self):
        self.primero = None

    def esVacio(self):
        if self.primero == None:
            return True

    def insertarPila(self,numero):
        nuevo = nodo.NodoPila(numero)
        if self.esVacio() == True:
            self.primero = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo

    def eliminar(self):
        if self.esVacio() == True:
            print("Pila vacia")

        var = self.primero.getNumero()
        self.primero = self.primero.siguiente
        return var

    def imprimirPila(self):
        aux = self.primero
        while aux != None:
            print(aux.getNumero())
            aux = aux.siguiente
