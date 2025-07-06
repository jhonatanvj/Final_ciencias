class Node:
    def __init__(self, clave, datos):
        self.clave = clave
        self.datos = datos
        self.altura = 1
        self.izquierda = None
        self.derecha = None
