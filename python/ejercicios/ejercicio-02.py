class Inventario:

    def __init__(self):
        self.__producto = {}

    def agregar(self, nombre, cantidad):
        if nombre in self.__producto:
            self.__producto[nombre] += cantidad
        else:
            self.__producto[nombre] = cantidad

    def retirar(self, nombre, cantidad):
        if nombre not in self.__producto:
            raise KeyError(f"El producto '{nombre}' no existe")
        if cantidad > self.__producto[nombre]:
            raise ValueError(f"No hay suficiente cantidad de '{nombre}'")
        self.__producto[nombre] -= cantidad

    def mostrar(self):
        for nombre, cantidad in self.__producto.items():
            print(f"{nombre}: {cantidad}")
        
inv = Inventario()
inv.agregar("manzanas", 10)
inv.agregar("peras", 5)
inv.agregar("manzanas", 3)
inv.mostrar()

inv.retirar("peras", 2)
inv.mostrar()


# inv.retirar("uvas", 1)      
# inv.retirar("manzanas", 99) 