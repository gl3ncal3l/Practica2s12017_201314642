class NodoCola(object):
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None
    def getNumero(self):
        return self.numero