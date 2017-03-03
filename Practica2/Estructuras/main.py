import Lista
import Cola
import Pila
from flask import Flask, request
instanciaCola = Cola.Cola()
instanciaLista = Lista.ListaSimple()
instanciaPila = Pila.Pila()
app = Flask("Practica")

#------------------LISTA ENLAZADA----------------------
@app.route('/insertarLista', methods=['POST'])
def insertarLista():
	valor=str(request.form['numero'])
	instanciaLista.insertarInicio(valor)
	return "se ha insertado el valor en lalista "+str(valor)
	
#------------------PILA----------------------
@app.route('/insertarPila', methods=['POST'])
def insertarPila():
	valor=str(request.form['numero'])
	instanciaPila.insertarPila(valor)
	return "se ha insertado el valor en lalista "+str(valor)
#------------------COLA----------------------
@app.route('/insertarCola', methods=['POST'])
def insertarCola():
	valor=str(request.form['numero'])
	instanciaCola.insertarCola(valor)
	return "se ha insertado el valor en la cola "+str(valor)
	
@app.route('/eliminarCola', methods=['POST'])
def eliminarCola():
	valor = str(instanciaCola.eliminar())
	return "Se ha eliminado el valor: "+str(valor)

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')


"""
# LISTA ENLAZADA
prueba = Estructuras.Lista.ListaSimple()
prueba.insertarInicio("a")
prueba.insertarInicio("b")
prueba.insertarInicio("c")

#prueba.imprimirLista()
#print(prueba.obtenerPosicion("hola"))
print(prueba.obtenerTamanio())
print("---------------------------------")
#prueba.graficarLista()
prueba.imprimirLista()
print(prueba.obtenerTamanio())
prueba.graficarLista()
#print(prueba.obtenerTamanio())


# COLA
prueba2 = Estructuras.Cola.Cola()
prueba2.insertarCola("2")
prueba2.insertarCola("19")
prueba2.insertarCola("39")
prueba2.insertarCola("45")
prueba2.insertarCola("12")
prueba2.insertarCola("18")

prueba2.imprimirCola()
print("----------------------------------")
prueba2.graficarCola()

#Pila
prueba3 = Estructuras.Pila.Pila()
prueba3.insertarPila("2")
prueba3.insertarPila("5")
prueba3.insertarPila("6")
prueba3.insertarPila("19")
prueba3.insertarPila("8")
prueba3.insertarPila("9")
prueba3.imprimirPila()
print("----------------------------------")
prueba3.graficarPila()
"""
