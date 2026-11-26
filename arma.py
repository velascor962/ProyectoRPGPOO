class arma:
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.daño = daño

    def usar(self):
        print(f"ataque con {self.nombre}")
        return self.daño
