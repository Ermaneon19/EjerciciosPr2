class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Particula:
    def __init__(self, masa, posicion, velocidad):
        self.masa = masa
        self.posicion = posicion
        self.velocidad = velocidad

    def actualizar_paso(self):
        self.posicion.x += self.velocidad.x
        self.posicion.y += self.velocidad.y
        self.posicion.z += self.velocidad.z

pos = Punto3D(0, 0, 0)
vel = Punto3D(1, -2, 0.5)

p = Particula(2.0, pos, vel)
p.actualizar_paso()

print(p.posicion.x, p.posicion.y, p.posicion.z)

