import Estructuras.Lista
import Estructuras.Cola
import Estructuras.Pila

"""
# LISTA ENLAZADA
prueba = Estructuras.Lista.ListaSimple()
prueba.insertarInicio("hola")
prueba.insertarInicio("mundo")
prueba.insertarInicio("11:50")
prueba.insertarInicio("01:00")
prueba.insertarInicio("ultimo")
prueba.imprimirLista()
print(prueba.obtenerTamanio())
print(prueba.obtenerPosicion("hola"))
print("---------------------------------")
prueba.eliminarPorIndice(3)
prueba.imprimirLista()
print(prueba.obtenerTamanio())
"""
"""
# COLA
prueba2 = Estructuras.Cola.Cola()
prueba2.insertarCola(2)
prueba2.insertarCola(19)
prueba2.insertarCola(39)
prueba2.insertarCola(45)
prueba2.insertarCola(12)
prueba2.insertarCola(18)

prueba2.imprimirCola()
print("----------------------------------")
prueba2.eliminar()
prueba2.eliminar()
prueba2.imprimirCola()
"""

#Pila
prueba3 = Estructuras.Pila.Pila()
prueba3.insertarPila(2)
prueba3.insertarPila(5)
prueba3.insertarPila(6)
prueba3.insertarPila(19)
prueba3.insertarPila(8)
prueba3.insertarPila(9)
prueba3.imprimirPila()
print("----------------------------------")
prueba3.eliminar()
prueba3.eliminar()
prueba3.eliminar()
prueba3.imprimirPila()


