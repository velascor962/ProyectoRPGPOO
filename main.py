from arma import arma
from objeto import objeto   
from personaje import personaje
from combate import Combate

espada = arma ("Espada de hierro", 12)
arco = arma ("arco de madera", 8)
navaja = arma ("navaja", 6)

heroe = personaje("Link", 100, espada)
heroe.inventario.agregar(objeto("pocion pequeña", 20))
heroe.inventario.agregar(objeto("pocion mediana", 30))

goblin =personaje("Goblin", 50, navaja)
combate = Combate(heroe, goblin)
combate.iniciar()