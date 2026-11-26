from inventario import inventario

class personaje:
    def __init__(self, nombre, salud, arma):
        self.nombre = nombre
        self.salud = salud
        self.arma = arma    
        self.inventario = inventario()

    def atacar(self):
        daño = self.arma.usar()
        print(f"{self.nombre} causa {daño} de daño.")

    def recibir_daño(self, cantidad):
        self.salud -= cantidad
        if self.salud < 0:
            self.salud = 0
        print(f"{self.nombre} recibe {cantidad} de daño. Salud : {self.salud}")

    def curar(self, cantidad):
        self.salud += cantidad
        print(f"{self.nombre} recupera {cantidad} de vida. salud: {self.salud}")

    def esta_vivo(self):
        return self.salud > 0 