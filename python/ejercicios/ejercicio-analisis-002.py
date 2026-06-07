class Estudiante:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cursos = []

    def inscribir(self, curso):
        self.cursos.append(curso)

    @property
    def promedio(self):
        if not self.cursos:
            return 0
        notas = [curso["nota"] for curso in self.cursos]
        return sum(notas) / len(notas)

    def reporte(self):
        print(f"Estudiante: {self.nombre}")
        print(f"Edad: {self.edad}")
        if not self.cursos:
            print("No hay cursos inscritos.")
            return
        print(f"Promedio: {self.promedio}")
        for curso in self.cursos:
            print(curso["nombre"] + " - " + str(curso["nota"]))


e = Estudiante("Ruben", 19)
e.inscribir({"nombre": "Matemáticas", "nota": 9})
e.inscribir({"nombre": "Física", "nota": 8})
e.inscribir({"nombre": "Programación", "nota": 10})

e.reporte()

print("-" * 20)

e2 = Estudiante("Ana", 20)
e2.reporte()