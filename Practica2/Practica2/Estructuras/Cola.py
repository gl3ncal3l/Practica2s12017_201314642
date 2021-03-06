import NodoCola
import os
nodo = NodoCola

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

    def graficarCola(self):
        aux = self.primero
        aux2 = self.primero.siguiente
        file_path = "Graficas"
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
                print("se ha creado el directorio")
            archivo = open("Graficas/cola.dot", "w")
            archivo.write("digraph Lista{\n")
            archivo.write("\t node[shape=record];\n")
            archivo.write("\t subgraph clusterQueue {\n")
            archivo.write("\t label = \"Cola \";\n")
            archivo.write("\t fontsize = 16;\n")
            while aux != None and aux2 != None:
                archivo.write("\t" + str(aux.getNumero()) + "->" + str(aux2.getNumero()) + "\n")
                aux = aux.siguiente
                aux2 = aux2.siguiente
            archivo.write("\t}\n")
            archivo.write("}")
            archivo.close()
            cmd = '"C:\\Program Files (x86)\\Graphviz 2.28\\bin\\dot.exe" -Tjpg Graficas\\cola.dot -o Graficas\\cola.jpg'
            #a2 = '"C:\\Users\\Glen\\Desktop\\EDD LAB\\Practica2\\Practica2\\Estructuras\\Graficas\\cola.jpg"'
            os.system(cmd)
			#os.system(a2)

        except ValueError:
            print("Error!")