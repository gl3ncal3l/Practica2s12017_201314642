import Estructuras.Lista
import Estructuras.Cola
import Estructuras.Pila


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
