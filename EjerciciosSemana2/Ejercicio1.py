class Habilidad:
    def __init__(self, nombre, costo, danio):
        self.nombre = nombre
        self.costo = costo
        self.danio = danio

class Objeto:
    def __init__(self, nombre, tipo, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad

class Mago:
    def __init__(self, nombre, vida, mana):
        self.nombre = nombre
        self.vida = vida
        self.mana = mana
        self.grimorio = []
        self.inventario = []

    def aprender_hechizo(self, habilidad):
        self.grimorio.append(habilidad)
        print(f"{self.nombre} ha aprendido el hechizo {habilidad.nombre}")

    def agregar_objeto(self, objeto):
        self.inventario.append(objeto)
        print(f"{self.nombre} ha conseguido {objeto.nombre} ")

    def usar_objeto(self, objeto):
        if objeto not in self.inventario:
            print(f"{objeto.nombre} no está en el inventario de {self.nombre}")
            return

        if objeto.tipo == "vida":
            self.vida += objeto.cantidad
            print(f"{self.nombre} usa {objeto.nombre} y ahora tiene {self.vida} de vida")
        elif objeto.tipo == "mana":
            self.mana += objeto.cantidad
            print(f"{self.nombre} usa {objeto.nombre} y ahora tiene {self.mana} de maná")

        self.inventario.remove(objeto)
        print("-" * 40)

    def lanzar_hechizo(self, habilidad, oponente):
        if habilidad not in self.grimorio:
            print(f"{self.nombre} intenta usar {habilidad.nombre} pero no lo ha aprendido")
            return
        if self.mana < habilidad.costo:
            print(f"{self.nombre} intenta lanzar {habilidad.nombre} pero no tiene suficiente maná")
            return

        self.mana -= habilidad.costo
        oponente.vida -= habilidad.danio
        oponente.vida = max(oponente.vida, 0)  
        
        print(f"{self.nombre} lanza {habilidad.nombre} contra {oponente.nombre}!")
        print(f"{oponente.nombre} recibe {habilidad.danio} de daño")
        print(f"{oponente.nombre} ahora tiene {oponente.vida} y {oponente.mana} de maná")
        print(f"{self.nombre} tiene {self.vida} y {self.mana} de maná restante")
        print("-" * 40)

mago1 = Mago("Gandalf", vida=100, mana=50)
mago2 = Mago("Saruman", vida=120, mana=40)

bola_de_fuego = Habilidad("Bola de Fuego", costo=20, danio=30)
rayo = Habilidad("Rayo", costo=15, danio=25)

pocion_vida = Objeto("Poción de Vida", tipo="vida", cantidad=40)
pocion_mana = Objeto("Poción de Maná", tipo="mana", cantidad=30)

mago1.aprender_hechizo(bola_de_fuego)
mago2.aprender_hechizo(rayo)

mago1.agregar_objeto(pocion_vida)
mago2.agregar_objeto(pocion_mana)

mago1.lanzar_hechizo(bola_de_fuego, mago2)
mago2.lanzar_hechizo(rayo, mago1)
mago1.usar_objeto(pocion_vida)
mago2.usar_objeto(pocion_mana)
mago1.lanzar_hechizo(bola_de_fuego, mago2)
