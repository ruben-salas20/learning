class Estudiante:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.__notas = []
    
    def agregar_nota(self, nota):
        if not (0 <= nota <= 10):
            raise ValueError(f"La nota {nota} no es válida. Debe estar entre 0 y 10.")
        self.__notas.append(nota)

    @property
    def promedio(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    @property
    def estado(self):
        return "Aprobado" if self.promedio >= 6 else "Reprobado"

    def reporte(self):
        print(f"{self.nombre} | promedio: {self.promedio} | {self.estado}")

class Salon:
    def __init__(self):
        self.__estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    def mejor_estudiante(self):
        if not self.__estudiantes:
            return None
        mejor = max(self.__estudiantes, key=lambda e: e.promedio)
        print(f"Mejor estudiante: {mejor.nombre}")
        return mejor

    def reporte_salon(self):
        for estudiante in self.__estudiantes:
            estudiante.reporte()

e1 = Estudiante("Ruben")
e1.agregar_nota(9)
e1.agregar_nota(8)
e1.agregar_nota(10)
e1.reporte()
# Ruben | promedio: 9.0 | aprobado

e2 = Estudiante("Ana")
e2.agregar_nota(4)
e2.agregar_nota(5)
e2.reporte()
# Ana | promedio: 4.5 | reprobado

salon = Salon()
salon.agregar_estudiante(e1)
salon.agregar_estudiante(e2)
salon.mejor_estudiante()
# Ruben

salon.reporte_salon()
# Ruben | promedio: 9.0 | aprobado
# Ana | promedio: 4.5 | reprobado