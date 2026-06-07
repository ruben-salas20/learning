---
tags: [tipo/apunte, tema/poo, tema/programacion, tema/python]
fecha: 2026-05-10
---
# Programación Orientada a Objetos (POO) — Conceptos

> Apunte de conceptos POO en español, con analogías y ejemplos en Python. Pensado para entender código que ya escribiste (o que escribió la IA) sin tener que tragar un libro entero.

---

## 1. Clase vs Objeto

**Clase** = el **molde**, el **plano**.
**Objeto** = la **cosa real construida** a partir del molde.

**Analogía:** la clase es el **plano de una casa**. El objeto es la **casa construida**. Con el mismo plano puedes construir mil casas; cada una es un objeto distinto pero comparten el plano.

```python
class Perro:          # ← clase (el plano)
    def __init__(self, nombre):
        self.nombre = nombre

firulais = Perro("Firulais")   # ← objeto (una instancia construida)
rocky = Perro("Rocky")         # ← otro objeto, mismo plano
```

`firulais` y `rocky` son **instancias** de la clase `Perro`. Cada uno tiene su propio nombre, pero ambos comparten lo que el plano `Perro` define.

---

## 2. Atributos vs Métodos

- **Atributos** → los **datos** que tiene la clase. Sustantivos. Variables.
- **Métodos** → las **acciones** que la clase puede hacer. Verbos. Funciones dentro de la clase.

**Analogía:** en una casa:
- Atributos: color de pared, número de habitaciones, tiene piscina (sí/no)
- Métodos: encender luces, abrir puerta, calentar agua

```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre   # atributo
        self.edad = edad       # atributo

    def ladrar(self):          # método
        print("¡Guau!")

    def cumplir_anios(self):   # método
        self.edad += 1
```

---

## 3. El `self` en Python

`self` significa "este objeto específico". Cuando un método se ejecuta, `self` apunta al objeto que lo llamó.

```python
firulais.cumplir_anios()
# Por dentro Python hace: Perro.cumplir_anios(firulais)
# Entonces dentro del método, self ES firulais
```

No es magia, es solo Python diciendo "el primer parámetro de cualquier método siempre es el objeto sobre el que se llama".

---

## 4. Encapsulación (visibilidad)

Idea: **proteger lo interno** de la clase para que desde fuera solo puedan tocar lo que tú quieres exponer.

**Analogía:** en tu casa hay cosas públicas (la puerta de entrada, el timbre) y cosas privadas (tu cajón de ropa interior). No quieres que cualquier visitante entre directo al cajón.

**En Python (convención, no se aplica por la fuerza):**

| Notación | Significado | Visualmente |
|---|---|---|
| `nombre` | Público — accesible desde cualquier lugar | `+` en diagramas UML |
| `_nombre` | "Casi-privado" — convención: no toques esto desde fuera | `#` (protegido) |
| `__nombre` | Privado — Python lo "esconde" con name mangling | `-` (privado) |

```python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular        # público
        self._tipo = "ahorros"        # protegido (por convención)
        self.__saldo = saldo          # privado real

    def consultar_saldo(self):        # método público
        return self.__saldo
```

Desde fuera puedes hacer `cuenta.titular` libremente, pero `cuenta.__saldo` te lo va a esconder Python. La única forma de leerlo es a través del método público `consultar_saldo()`.

**Por qué importa:** si mañana cambias cómo se guarda internamente el saldo (en otra moneda, en otra estructura), el código que usa `consultar_saldo()` no se rompe. Solo cambias lo de adentro.

---

## 5. Constructor `__init__` y propiedades

El método especial `__init__` es el **constructor**: se ejecuta automáticamente cuando creas un objeto.

```python
firulais = Perro("Firulais")
# Python ejecuta Perro.__init__(firulais, "Firulais") por debajo
```

**Properties** = atributos que se calculan en vivo en vez de estar guardados.

```python
class Estudiante:
    def __init__(self, notas):
        self.__notas = notas

    @property
    def promedio(self):
        return sum(self.__notas) / len(self.__notas)

ruben = Estudiante([9, 8, 10])
ruben.promedio   # ← se ve como atributo, pero se calcula al acceder
```

Útil cuando un valor depende de otros y no quieres tener que actualizarlo manualmente.

---

## 6. Herencia — "es un tipo de"

**Una clase HEREDA DE otra cuando ES UN TIPO DE ella.**

- `Perro` HEREDA DE `Animal` → un perro ES UN animal
- `Gato` HEREDA DE `Animal` → un gato ES UN animal
- `EffiCarrier` HEREDA DE `Carrier` → effi ES UN carrier

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def respirar(self):
        print(f"{self.nombre} respira")

class Perro(Animal):           # ← Perro hereda de Animal
    def ladrar(self):
        print(f"{self.nombre} dice guau")

firulais = Perro("Firulais")
firulais.respirar()   # ← funciona, lo heredó de Animal
firulais.ladrar()     # ← funciona, es propio de Perro
```

**Cuándo SÍ usar herencia:** cuando la relación es genuinamente "es un tipo de".

**Cuándo NO usar herencia (error clásico):** cuando solo quieres reusar código sin que haya relación conceptual. En esos casos, usa **composición** (más abajo).

---

## 7. Polimorfismo — "se comportan distinto, pero hablan el mismo idioma"

Misma llamada, distinta acción según el objeto.

```python
class Animal:
    def hablar(self):
        raise NotImplementedError

class Perro(Animal):
    def hablar(self):
        print("Guau")

class Gato(Animal):
    def hablar(self):
        print("Miau")

for animal in [Perro(), Gato()]:
    animal.hablar()   # cada uno dice algo distinto
```

Todos los animales tienen el método `hablar()` (mismo idioma), pero cada uno lo implementa a su manera (distinta acción). Tu código no necesita saber qué tipo es: solo llama `hablar()` y cada objeto sabe qué hacer.

**Por qué importa:** te permite escribir código genérico que funcione con cualquier tipo de objeto que cumpla cierta interfaz. Es la base del patrón Strategy y del Protocol pattern de vaecos.

---

## 8. Composición — "tiene un"

**Una clase TIENE OTRA CLASE adentro como parte de sí.**

- Un `Coche` **tiene un** `Motor`
- Un `Estudiante` **tiene** una lista de `Curso`s
- Una `Web` **tiene** un `Database`

```python
class Motor:
    def encender(self):
        print("Brrr")

class Coche:
    def __init__(self):
        self.motor = Motor()    # ← Coche TIENE UN Motor

    def arrancar(self):
        self.motor.encender()
```

**Composición vs Herencia — regla práctica:**
- ¿"Es un tipo de"? → Herencia
- ¿"Tiene un"? → Composición

La industria de software dice: **"prefiere composición sobre herencia"**. La herencia es rígida (no puedes cambiar de padre fácil), la composición es flexible (cambias el motor sin tirar el coche).

---

## 9. Agregación — "usa, pero no es dueño"

Variante suave de composición. La diferencia es **el ciclo de vida**.

- **Composición:** si destruyes el objeto padre, el hijo también muere. Ejemplo: si demueles la casa, los muros se van con ella.
- **Agregación:** si destruyes el padre, el hijo sigue existiendo independiente. Ejemplo: si cierras el equipo de fútbol, los jugadores siguen vivos y se van a otros equipos.

```python
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Equipo:
    def __init__(self, jugadores):
        self.jugadores = jugadores   # ← agregación: vienen de fuera, viven fuera
```

En diagramas UML: composición es `*--` (rombo lleno), agregación es `o--` (rombo vacío). En la práctica del día a día, no te obsesiones con la diferencia — saber que existe es suficiente.

---

## 10. Interfaces / Protocols — "el contrato"

Una **interfaz** (en Java, C#) o **protocolo** (en Python) es un **contrato**: define qué métodos debe tener una clase, sin decir cómo se implementan.

**Analogía:** un protocolo es como **la regulación de tomas eléctricas**. La regulación dice "todo enchufe debe tener dos clavijas redondas separadas X mm". No te dice cómo fabricar el enchufe. Cualquiera puede fabricar un enchufe que cumpla la regulación, y todos van a funcionar en la pared.

```python
from typing import Protocol

class Carrier(Protocol):
    name: str

    def fetch_tracking(self, guide_id: str) -> dict:
        ...

class EffiCarrier:
    name = "effi"
    def fetch_tracking(self, guide_id: str) -> dict:
        # implementación específica de Effi
        ...

class GuatexCarrier:
    name = "guatex"
    def fetch_tracking(self, guide_id: str) -> dict:
        # implementación específica de Guatex
        ...
```

`EffiCarrier` y `GuatexCarrier` **NO heredan** de `Carrier`. Solo **cumplen el contrato**. Python verifica con duck typing: "si camina como pato y suena como pato, es pato". Si tiene `.name` y `.fetch_tracking()`, es Carrier.

**Diferencia con herencia:**
- Herencia: recibes código del padre
- Protocol: solo cumples una promesa, no recibes nada

**Es justo el patrón que usa vaecos-tracking.** Por eso lo vas a ver constantemente.

---

## 11. Clases abstractas

Una **clase abstracta** es un punto intermedio: tiene algo de código heredable, pero también define métodos abstractos que las clases hijas DEBEN implementar.

**Analogía:** es como un plano de casa con las habitaciones definidas, pero donde dice "aquí va una puerta, tú decides de qué material". No puedes vivir en el plano (no puedes instanciar la clase abstracta), pero las casas concretas (clases hijas) sí se pueden habitar.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre    # esto sí lo heredan todos

    @abstractmethod
    def hablar(self):           # cada hijo DEBE implementarlo
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

# Animal("X")  → ERROR: no se puede instanciar abstracta
# Perro("Firulais")  → OK
```

---

## 12. Métodos de clase vs estáticos vs de instancia

| Tipo | Decorador | `self`? | Cuándo usarlo |
|---|---|---|---|
| Instancia (normal) | ninguno | sí | El método necesita los datos del objeto |
| De clase | `@classmethod` | recibe `cls` (la clase) | El método actúa sobre la clase entera, no sobre un objeto |
| Estático | `@staticmethod` | no | Función utilitaria que conceptualmente pertenece a la clase pero no necesita ni objeto ni clase |

```python
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):                  # de instancia
        return f"Hola, soy {self.nombre}"

    @classmethod
    def desde_csv(cls, fila):           # de clase: crea un Estudiante desde un CSV
        nombre = fila.split(",")[0]
        return cls(nombre)              # usa cls para crear un objeto

    @staticmethod
    def es_nombre_valido(nombre):       # estático: solo lógica utilitaria
        return len(nombre) >= 2
```

---

## 13. Reglas de oro de POO

1. **Encapsula lo que cambia.** Si crees que algo va a cambiar, ponlo privado y expón métodos.
2. **Prefiere composición sobre herencia.** Más flexible.
3. **Una clase, una responsabilidad.** Si una clase hace 10 cosas, divídela. (Principio SRP — Single Responsibility)
4. **Programa contra interfaces, no implementaciones.** Tu código de alto nivel debe depender del `Carrier` Protocol, no de `EffiCarrier` directo. Eso te permite cambiar carriers sin tocar nada más.
5. **No hereses solo para reusar código.** Si no hay relación "es un tipo de", usa composición.

---

## Apuntes relacionados

- [[mermaid-diagramas]] — cómo dibujar class diagrams
- [[leer-codigo-vibecoded]] — método para entender clases que escribió la IA

---

*Apunte vivo. Cuando entiendas un nuevo patrón POO, agrégalo aquí.*
