class Item:
    def __init__(self, nombre, peso, rareza):
        self.nombre = nombre
        self.peso = peso
        self.rareza = rareza

class Inventario:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.items = {}
        self.orden_ingreso = []

    def peso_actual(self):

        total = 0
        for data in self.items.values():
            total += data['item'].peso * data['cantidad']
        return total

    def espacio_disponible(self):
        return self.capacidad_maxima - self.peso_actual()

    def agregar_item(self, item):

        print(f"\nEspacio disponible antes de agregar: {self.espacio_disponible()}")

        if item.peso > self.espacio_disponible():
            print(f"No se puede agregar {item.nombre}, pesa {item.peso} y solo queda {self.espacio_disponible()} de espacio")
            return False
        if item.nombre in self.items:
            self.items[item.nombre]['cantidad'] += 1
        else:
            self.items[item.nombre] = {'item': item, 'cantidad': 1}
        self.orden_ingreso.append(item)
        print(f"Agregado: {item.nombre} | Peso total: {self.peso_actual()}")
        return True

    def organizar_por_rareza(self):
        def obtener_rareza(item):
            return item.rareza
        self.orden_ingreso.sort(key=obtener_rareza, reverse=True)

if __name__ == "__main__":
    inventario = Inventario(capacidad_maxima=10)

    print(f"Espacio total de la mochila: {inventario.capacidad_maxima}")

    espada = Item("Espada", 3, 2)
    pocion = Item("Poción", 1, 1)
    armadura = Item("Armadura", 5, 3)
    anillo = Item("Anillo", 3, 4)
    puas = Item("Puas", 5, 5)

    inventario.agregar_item(espada)
    inventario.agregar_item(pocion)
    inventario.agregar_item(espada)
    inventario.agregar_item(puas)
    inventario.agregar_item(armadura)
    inventario.agregar_item(anillo)
    
    print("\nInventario actual:")
    for nombre, data in inventario.items.items():
        item = data['item']
        cantidad = data['cantidad']
        print(f"{item.nombre}  Peso:{item.peso}  Rareza:{item.rareza}  x{cantidad}")

    inventario.organizar_por_rareza()
    print("\nOrden de ingreso por rareza (mayor a menor):")
    for item in inventario.orden_ingreso:
        print(f"{item.nombre}  Peso:{item.peso}  Rareza:{item.rareza}")

    print("\nPeso total:", inventario.peso_actual())
    print("Espacio disponible:", inventario.espacio_disponible())
