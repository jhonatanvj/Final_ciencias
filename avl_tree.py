from node import Node

class AVLTree:
    def insertar(self, raiz, clave, datos):
        if not raiz:
            return Node(clave, datos)
        elif clave <= raiz.clave:
            raiz.izquierda = self.insertar(raiz.izquierda, clave, datos)
        else:
            raiz.derecha = self.insertar(raiz.derecha, clave, datos)

        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha))
        balance = self.obtener_balance(raiz)

        if balance > 1 and clave <= raiz.izquierda.clave:
            return self.rotar_derecha(raiz)
        if balance < -1 and clave > raiz.derecha.clave:
            return self.rotar_izquierda(raiz)
        if balance > 1 and clave > raiz.izquierda.clave:
            raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)
        if balance < -1 and clave <= raiz.derecha.clave:
            raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)

        return raiz

    def buscar(self, raiz, clave):
        if not raiz:
            return None
        if clave == raiz.clave:
            return raiz.datos
        elif clave < raiz.clave:
            return self.buscar(raiz.izquierda, clave)
        else:
            return self.buscar(raiz.derecha, clave)

    def eliminar(self, raiz, clave):
        if not raiz:
            return raiz

        if clave < raiz.clave:
            raiz.izquierda = self.eliminar(raiz.izquierda, clave)
        elif clave > raiz.clave:
            raiz.derecha = self.eliminar(raiz.derecha, clave)
        else:
            if not raiz.izquierda:
                return raiz.derecha
            elif not raiz.derecha:
                return raiz.izquierda

            temp = self.obtener_maximo(raiz.izquierda)
            raiz.clave = temp.clave
            raiz.datos = temp.datos
            raiz.izquierda = self.eliminar(raiz.izquierda, temp.clave)

        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha))
        balance = self.obtener_balance(raiz)

        if balance > 1 and self.obtener_balance(raiz.izquierda) >= 0:
            return self.rotar_derecha(raiz)
        if balance < -1 and self.obtener_balance(raiz.derecha) <= 0:
            return self.rotar_izquierda(raiz)
        if balance > 1 and self.obtener_balance(raiz.izquierda) < 0:
            raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)
        if balance < -1 and self.obtener_balance(raiz.derecha) > 0:
            raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)

        return raiz

    def obtener_maximo(self, nodo):
        actual = nodo
        while actual.derecha:
            actual = actual.derecha
        return actual

    def obtener_altura(self, nodo):
        return nodo.altura if nodo else 0

    def obtener_balance(self, nodo):
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha) if nodo else 0

    def rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.derecha = T2
        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))
        return y

    def rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha
        y.derecha = z
        z.izquierda = T3
        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))
        return y
