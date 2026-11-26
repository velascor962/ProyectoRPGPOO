class inventario:
    def __init__(self):
        self.items = []

    def agregar (self, item):
        self.items.append(item)
        print (f" items en el inventario: {self.items}")

    def listar(self):
        if not self.items:
            print("El inventario está vacío.")
        for i, items in enumerate(self.items, start=1):
            print(f"{i}. {items.nombre}")

    def esta_vacio(self):
        return len(self.items) == 0

    def sacar(self, numero):
        return self.items.pop(numero - 1)
    