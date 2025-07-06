import json
from avl_tree import AVLTree

class JSONDatabase:
    def __init__(self, archivo='storage.json'):
        self.arbol = AVLTree()
        self.raiz = None
        self.archivo = archivo
        self.cargar()

    def insertar(self, clave, objeto):
        self.raiz = self.arbol.insertar(self.raiz, clave, objeto)
        self.guardar()

    def obtener(self, clave):
        return self.arbol.buscar(self.raiz, clave)

    def actualizar(self, clave, nuevo_objeto):
        self.eliminar(clave)
        self.insertar(clave, nuevo_objeto)

    def eliminar(self, clave):
        self.raiz = self.arbol.eliminar(self.raiz, clave)
        self.guardar()

    def listar(self):
        resultados = []
        self._inorden(self.raiz, resultados)
        return resultados

    def _inorden(self, nodo, resultados):
        if nodo:
            self._inorden(nodo.izquierda, resultados)
            resultados.append({nodo.clave: nodo.datos})
            self._inorden(nodo.derecha, resultados)

    def guardar(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.listar(), f, indent=4)

    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                contenido = f.read()
                if not contenido.strip():
                    return
                elementos = json.loads(contenido)
                for par in elementos:
                    for clave, datos in par.items():
                        self.raiz = self.arbol.insertar(self.raiz, clave, datos)
        except FileNotFoundError:
            pass
