import Estructuras.NodoCola
nodo = Estructuras.NodoCola

class Cola(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esVacia(self):
        if self.primero == None:
            return True

    def insertarCola(self,numero):
        nuevo = nodo.NodoCola(numero)
        if self.esVacia()==True:
            self.primero = nuevo
        else:
            self.ultimo.siguiente = nuevo
        self.ultimo = nuevo

    def obtenerDato(self):
        aux = self.primero
        return aux.getNumero()

    def eliminar(self):
        valor = self.primero.getNumero()
        if self.esVacia() != True:
            if self.primero == self.ultimo:
                self.primero = self.ultimo = None
            else:
                self.primero = self.primero.siguiente
            return valor
        return valor

    def imprimirCola(self):
        aux = self.primero
        while aux != None:
            print(aux.getNumero())
            aux = aux.siguiente
