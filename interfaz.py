import tkinter as tk
from tkinter import messagebox
from database import JSONDatabase

class InterfazAVL:
    def __init__(self, root):
        self.db = JSONDatabase()
        self.root = root
        self.root.title("Gestor AVL")

        # Entrada de clave y datos
        tk.Label(root, text="Clave (número):").grid(row=0, column=0)
        self.entry_clave = tk.Entry(root)
        self.entry_clave.grid(row=0, column=1)

        tk.Label(root, text="Nombre:").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(root, text="Edad:").grid(row=2, column=0)
        self.entry_edad = tk.Entry(root)
        self.entry_edad.grid(row=2, column=1)

        # Botones
        tk.Button(root, text="Añadir", command=self.añadir).grid(row=3, column=0)
        tk.Button(root, text="Eliminar", command=self.eliminar).grid(row=3, column=1)
        tk.Button(root, text="Buscar", command=self.buscar).grid(row=4, column=0)
        tk.Button(root, text="Actualizar", command=self.actualizar).grid(row=4, column=1)
        tk.Button(root, text="Listar / Mostrar árbol", command=self.mostrar_arbol).grid(row=5, column=0, columnspan=2)

        # Área para mostrar el árbol
        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.grid(row=6, column=0, columnspan=2, pady=10)

    def añadir(self):
        try:
            clave = int(self.entry_clave.get())
            datos = {"nombre": self.entry_nombre.get(), "edad": self.entry_edad.get()}
            self.db.insertar(clave, datos)
            messagebox.showinfo("Éxito", f"Elemento {clave} añadido.")
        except ValueError:
            messagebox.showerror("Error", "Clave debe ser numérica.")

    def eliminar(self):
        try:
            clave = int(self.entry_clave.get())
            self.db.eliminar(clave)
            messagebox.showinfo("Éxito", f"Elemento {clave} eliminado.")
        except ValueError:
            messagebox.showerror("Error", "Clave debe ser numérica.")

    def buscar(self):
        try:
            clave = int(self.entry_clave.get())
            resultado = self.db.obtener(clave)
            if resultado:
                messagebox.showinfo("Encontrado", str(resultado))
            else:
                messagebox.showinfo("No encontrado", "No hay datos con esa clave.")
        except ValueError:
            messagebox.showerror("Error", "Clave debe ser numérica.")

    def actualizar(self):
        try:
            clave = int(self.entry_clave.get())
            nuevo = {"nombre": self.entry_nombre.get(), "edad": self.entry_edad.get()}
            self.db.actualizar(clave, nuevo)
            messagebox.showinfo("Éxito", f"Elemento {clave} actualizado.")
        except ValueError:
            messagebox.showerror("Error", "Clave debe ser numérica.")

    def mostrar_arbol(self):
        self.canvas.delete("all")
        self._dibujar_nodo(self.db.raiz, 400, 30, 180)

    def _dibujar_nodo(self, nodo, x, y, offset):
        if nodo is None:
            return
        # Dibuja el nodo actual
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
        self.canvas.create_text(x, y, text=str(nodo.clave))

        # Línea y subárbol izquierdo
        if nodo.izquierda:
            self.canvas.create_line(x, y, x-offset, y+70)
            self._dibujar_nodo(nodo.izquierda, x-offset, y+70, offset//2)

        # Línea y subárbol derecho
        if nodo.derecha:
            self.canvas.create_line(x, y, x+offset, y+70)
            self._dibujar_nodo(nodo.derecha, x+offset, y+70, offset//2)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazAVL(root)
    root.mainloop()