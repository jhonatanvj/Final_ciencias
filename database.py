import json
from avl_tree import AVLTree
from node import Node

class JSONDatabase:
    def __init__(self, file_path='storage.json'):
        self.tree = AVLTree()
        self.root = None
        self.file_path = file_path
        self.load()

    def insert(self, key, obj):
        self.root = self.tree.insert(self.root, key, obj)
        self.save()

    def get(self, key):
        return self.tree.search(self.root, key)

    def update(self, key, new_obj):
        if self.get(key):
            self.delete(key)
            self.insert(key, new_obj)
        else:
            raise KeyError("Objeto no encontrado")

    def delete(self, key):
        self.root = self._delete_node(self.root, key)
        self.save()

    def _delete_node(self, root, key):
        # Implementación opcional de borrado en AVL
        pass  # Se puede implementar después

    def list_all(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append({node.key: node.data})
            self._inorder(node.right, result)

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.list_all(), f, indent=4)

    def load(self):
        try:
            with open(self.file_path, 'r') as f:
                items = json.load(f)
                for pair in items:
                    for key, data in pair.items():
                        self.root = self.tree.insert(self.root, key, data)
        except FileNotFoundError:
            pass
