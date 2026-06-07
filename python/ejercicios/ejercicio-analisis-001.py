class Biblioteca:

    def __init__(self):
        self.catalogo = [] 
        self.prestados = {}

    def agregar_libro(self, titulo, autor):
        libro = {"titulo": titulo, "autor": autor} 
        self.catalogo.append(libro)

    def prestar_libro(self, titulo, usuario): 
        for libro in self.catalogo:
            if libro["titulo"] == titulo:
                if titulo in self.prestados:
                    raise ValueError(f"El libro '{titulo}' ya esta prestado.")
                self.prestados[titulo] = usuario
                return f"{titulo} prestado a {usuario}"
        return f"{titulo} no encontrado"

    def devolver_libro(self, titulo):
        if titulo in self.prestados:
            del self.prestados[titulo]
            return f"{titulo} devuelto"
        return f"{titulo} no estaba prestado"

    def mostrar_catalogo(self):
        for libro in self.catalogo:
            estado = "prestado" if libro["titulo"] in self.prestados else "disponible"
            print(f"{libro['titulo']} - {libro['autor']} [{estado}]")


bib = Biblioteca()
bib.agregar_libro("El principito", "Saint-Exupéry")
bib.agregar_libro("1984", "Orwell")
bib.agregar_libro("Dune", "Herbert")

bib.prestar_libro("1984", "Ruben")
bib.prestar_libro("Dune", "Ruben") 
bib.prestar_libro("Dune", "Ana") 

bib.mostrar_catalogo()