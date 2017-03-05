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
	valor=str(request.form['palabra'])
	instanciaLista.insertarInicio(valor)
	return "se ha insertado el valor en la lista: "+str(valor)

@app.route('/eliminarLista', methods=['POST'])
def eliminarLista():
	valor=int(request.form['numero'])
	instanciaLista.eliminarPorIndice(valor)
	return "se ha eliminado el valor: "+str(valor)
	
@app.route('/buscarLista', methods=['POST'])
def buscarLista():
	valor=str(request.form['palabra'])
	valo1=str(instanciaLista.obtenerPosicion(valor))
	return str(valo1)

@app.route('/graficarLista', methods=['POST'])
def graficarLista():
	valor=str(request.form['numero'])
	instanciaLista.graficarLista()
	return "se ha creado el reporte!"
	
#------------------PILA----------------------
@app.route('/insertarPila', methods=['POST'])
def insertarPila():
	valor=str(request.form['numero'])
	instanciaPila.insertarPila(valor)
	return "se ha insertado el valor en la pila: "+str(valor)

@app.route('/eliminarPila', methods=['POST'])
def eliminarPila():
	valor1=str(request.form['numero'])
	valor = instanciaPila.eliminar()
	return "se ha insertado el valor en la pila: "+str(valor)

@app.route('/graficarPila', methods=['POST'])
def graficarPila():
	valor=str(request.form['numero'])
	instanciaPila.graficarPila()
	return "se ha creado el reporte!"
	
#------------------COLA----------------------
@app.route('/insertarCola', methods=['POST'])
def insertarCola():
	valor=str(request.form['numero'])
	instanciaCola.insertarCola(valor)
	return "se ha insertado el valor en la cola: "+str(valor)
	
@app.route('/eliminarCola', methods=['POST'])
def eliminarColaCola():
	valor1=str(request.form['numero'])
	valor = instanciaCola.eliminar()
	return "se ha eliminado el elemento de la cola: "+str(valor)

@app.route('/graficarColaCola', methods=['POST'])
def graficarCola():
	valor1=str(request.form['numero'])
	valor = instanciaCola.graficarCola()
	return "Se ha creado el reporte!"

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
valor = prueba.eliminar()
print(valor)
#prueba2.graficarCola()

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
