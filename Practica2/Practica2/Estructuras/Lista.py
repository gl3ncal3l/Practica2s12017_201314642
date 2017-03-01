import Estructuras.NodoLista
nodo = Estructuras.NodoLista


class ListaSimple(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def esVacio(self):
        if self.primero == None:
            return True

    def insertarInicio(self,palabra):
        nuevo = nodo.NodoLista(palabra)
        if self.esVacio()==True:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo
        self.tamanio +=1


    def obtenerTamanio(self):
        return self.tamanio

    def buscar(self, valor):
        aux = self.primero
        encontrado = False
        while(aux!=None and encontrado!=True):
            if valor == aux.getPalabra():
                encontrado = True
            else:
                aux = aux.siguiente
        return encontrado

    def obtenerPosicion(self, valor):
        if self.buscar(valor):
            aux = self.primero
            contador = 0
            while valor != aux.getPalabra():
                contador = contador +1
                aux = aux.siguiente
            return contador
        else:
            print("NO SE ENCONTRÓ EL DATO")



    def eliminarPorIndice(self,indice):
        if indice >=0 and indice<self.tamanio:
            if indice ==0:
                self.primero = self.primero.siguiente
            else:
                aux = self.primero
                contador = 0
                while contador<indice-1:
                    aux = aux.siguiente
                    contador+=1
                siguientenodo = aux.siguiente
                aux.siguiente = siguientenodo.siguiente
                self.ultimo = aux
        self.tamanio -=1


    def insertarFinal(self,palabra):
        nuevo = nodo.NodoLista(palabra)
        if self.esVacio()==True:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.tamanio += 1

    def imprimirLista(self):
        if self.esVacio()==True:
            print("Lista Vacia")
        else:
            validar = True
            temp = self.primero
            while(validar):
                print(temp.getPalabra())
                if temp == self.ultimo:
                    validar = False
                else:
                    temp = temp.siguiente
