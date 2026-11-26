from arma import arma
from objeto import objeto   
from personaje import personaje

espada = arma ("Espada de hierro", 12)
heroe = personaje("Link", 100, espada)

heroe.inventario.agregar(objeto("pocion pequeña", 20))
heroe.inventario.listar()
heroe.atacar()
