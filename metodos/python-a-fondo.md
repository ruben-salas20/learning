---
tags: [tipo/apunte, tema/python, tema/python-profesional, estado/en-progreso]
fecha: 2026-05-19
---
# Python a fondo — del "sé sintaxis" al "leo y escribo código real"

> Este apunte NO es Python básico. Asume que ya manejas variables, funciones, clases, listas, diccionarios y excepciones (lo tienes en `python/apuntes/`).
>
> El objetivo es cerrar el **gap de lectura**: cuando abras el motor de reglas de `vaecos-tracking`, los patrones de este archivo deben sentirse familiares, no mágicos. Cada sección responde a una pregunta: *"¿qué es esto que veo en el código y por qué está ahí?"*

---

## Mapa del archivo

| # | Tema | Qué desbloquea al leer código |
|---|---|---|
| 1 | Type hints | Entender la "forma" de los datos sin ejecutar nada |
| 2 | `*args` / `**kwargs` | Funciones que aceptan "cualquier cosa" |
| 3 | Comprehensions a fondo | Bucles condensados en una línea |
| 4 | Generadores y `yield` | Por qué algo "recorre" sin guardar todo en memoria |
| 5 | Iteradores e iterables | Qué hace funcionar a un `for` por dentro |
| 6 | Context managers (`with`) | Por qué los archivos y conexiones se abren así |
| 7 | Dataclasses | Clases que son "solo datos" sin `__init__` a mano |
| 8 | Módulos y paquetes | Qué significan los `import` y los `__init__.py` |
| 9 | Gotchas que muerden | Errores sutiles que verás en código vibecoded |

---

## 1. Type hints — la documentación que el código se da a sí mismo

### El problema

Python NO obliga a declarar tipos. Esto funciona:

```python
def procesar(dato):
    return dato * 2
```

Pero al leer esa función no sabes: ¿`dato` es un número? ¿una lista? ¿un string? Tienes que adivinar leyendo cómo se usa. En un motor de reglas con decenas de funciones, eso es agotador.

### La solución

Los **type hints** (anotaciones de tipo) declaran la forma esperada de los datos:

```python
def procesar(dato: int) -> int:
    return dato * 2
```

Esto se lee: "`dato` debería ser un `int`, y la función devuelve un `int`".

> [!important] Los type hints NO se verifican en ejecución
> Python los ignora al correr. `procesar("hola")` NO da error por el tipo — daría `"holahola"`. Los hints son para: (1) que TÚ los leas, (2) que tu editor te avise, (3) que herramientas como `mypy` los chequeen aparte. Son **documentación ejecutable**, no una garantía.

### Sintaxis que verás en código real

```python
nombre: str = "Rubén"
edad: int = 30
activo: bool = True
precio: float = 19.99

# Colecciones (Python 3.9+)
nombres: list[str] = ["a", "b"]
config: dict[str, int] = {"reintentos": 3}
coordenadas: tuple[float, float] = (4.6, -74.0)

# "Puede ser un str o None" — patrón omnipresente
def buscar_regla(id: int) -> str | None:
    ...
```

| Anotación | Significado |
|---|---|
| `x: int` | `x` es un entero |
| `-> bool` | la función devuelve un booleano |
| `list[str]` | una lista de strings |
| `dict[str, int]` | dict con claves string y valores int |
| `str \| None` | un string **o** `None` (el `\|` se lee "o") |
| `-> None` | la función no devuelve nada útil |

> En código más viejo verás `Optional[str]` y `List[str]` (con mayúscula, importados de `typing`). Es la sintaxis antigua de lo mismo: `Optional[str]` == `str | None`.

**Por qué importa para el rules engine:** una regla normalmente recibe datos de entrada y devuelve una decisión. Los hints te dicen, de un vistazo, qué entra y qué sale — sin tener que rastrear toda la lógica.

---

## 2. `*args` y `**kwargs` — funciones que aceptan cantidad variable de argumentos

Ya los viste en el apunte de decoradores. Aquí van a fondo, porque NO son exclusivos de decoradores.

### `*args` — argumentos posicionales variables

El `*` recoge "todos los argumentos sueltos que sobren" en una **tupla**:

```python
def sumar(*numeros):
    print(type(numeros))   # <class 'tuple'>
    return sum(numeros)

sumar(1, 2)          # numeros = (1, 2)        -> 3
sumar(1, 2, 3, 4)    # numeros = (1, 2, 3, 4)  -> 10
sumar()              # numeros = ()            -> 0
```

El nombre `args` es pura convención. Lo que importa es el `*`.

### `**kwargs` — argumentos nombrados variables

El `**` recoge "todos los argumentos con nombre que sobren" en un **diccionario**:

```python
def crear_regla(**opciones):
    print(type(opciones))   # <class 'dict'>
    return opciones

crear_regla(activa=True, prioridad=5)
# opciones = {'activa': True, 'prioridad': 5}
```

### El orden obligatorio

Cuando los combinas, el orden NO es negociable:

```python
def f(normal, *args, kw_normal=None, **kwargs):
    ...
#     ↑          ↑          ↑              ↑
#   posicional  resto    nombrado       resto de
#   fijo      posicional  con default    nombrados
```

### El otro uso del `*`: desempaquetar (unpacking)

El MISMO símbolo, al **llamar** a una función, hace lo contrario: reparte una colección.

```python
numeros = [1, 2, 3]
sumar(*numeros)        # equivale a sumar(1, 2, 3)

config = {"activa": True, "prioridad": 5}
crear_regla(**config)  # equivale a crear_regla(activa=True, prioridad=5)
```

> Regla mental: en la **definición** de la función, `*`/`**` *empaquetan* (recogen). En la **llamada**, `*`/`**` *desempaquetan* (reparten).

---

## 3. Comprehensions a fondo

Ya usaste list comprehensions básicas. Aquí, los cuatro tipos y el filtrado.

### Los cuatro tipos

```python
# List comprehension  ->  produce una lista
cuadrados = [x**2 for x in range(5)]            # [0, 1, 4, 9, 16]

# Dict comprehension  ->  produce un diccionario
indice = {x: x**2 for x in range(5)}            # {0:0, 1:1, 2:4, ...}

# Set comprehension   ->  produce un set (sin duplicados)
unicos = {x % 3 for x in range(10)}             # {0, 1, 2}

# Generator expression -> produce un generador (ver sección 4)
perezoso = (x**2 for x in range(5))             # NO es una lista
```

> Detalle clave: `[...]` lista, `{...}` set o dict, `(...)` generador. El delimitador decide el tipo.

### Filtrado: el `if` al final

```python
pares = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]
```

Se lee de izquierda a derecha como una frase: *"x, por cada x en el rango, si x es par"*.

### `if/else` al PRINCIPIO — es distinto

```python
etiquetas = ["par" if x % 2 == 0 else "impar" for x in range(4)]
# ['par', 'impar', 'par', 'impar']
```

> [!tip] Cómo distinguirlos
> - `if` **al final** = filtro (decide si el elemento entra o no).
> - `if/else` **al principio** = transformación (decide QUÉ valor poner).
> Si ves un `else` dentro de una comprehension, está al principio: es transformación, no filtro.

### Cuándo NO usar una comprehension

Si la comprehension necesita lógica de varias líneas, ifs anidados, o efectos secundarios (`print`, escribir en BD) → usa un `for` normal. La comprehension es para **construir una colección**, no para reemplazar todo bucle. Una comprehension ilegible es peor que tres líneas claras.

---

## 4. Generadores y `yield` — recorrer sin guardar todo

### El problema que resuelven

```python
def primeros_cuadrados(n):
    resultado = []
    for x in range(n):
        resultado.append(x**2)
    return resultado

primeros_cuadrados(1_000_000)   # construye UN MILLÓN de números en RAM
```

Si solo vas a recorrerlos uno por uno, tener el millón entero en memoria es desperdicio.

### La solución: `yield`

Una función con `yield` en vez de `return` es un **generador**. Produce valores **uno a uno, bajo demanda**:

```python
def primeros_cuadrados(n):
    for x in range(n):
        yield x**2          # "entrega" un valor y se PAUSA aquí

for c in primeros_cuadrados(1_000_000):
    print(c)
    if c > 100:
        break               # nunca calculó más allá de lo necesario
```

### Cómo funciona mentalmente

- `return` termina la función y la abandona.
- `yield` **entrega un valor y congela la función** en ese punto. La próxima vez que se le pide un valor, **descongela** y sigue justo después del `yield`.
- El generador recuerda su estado entre llamadas. Es como pausar y reanudar un video.

```python
def contador():
    print("arranco")
    yield 1
    print("sigo")
    yield 2
    print("termino")

g = contador()        # NO imprime nada todavía — está perezoso
next(g)               # imprime "arranco", devuelve 1
next(g)               # imprime "sigo", devuelve 2
next(g)               # imprime "termino", luego lanza StopIteration
```

> [!important] Un generador se consume UNA sola vez
> Cuando recorres un generador hasta el final, queda agotado. Volver a hacer `for` sobre él no produce nada. Si necesitas los valores dos veces, conviértelo a lista (`list(g)`) o regenéralo. Este es un gotcha clásico.

**Por qué lo verás en el rules engine:** procesar registros de tracking (corridas, eventos) a menudo se hace en streaming. Un generador permite ir aplicando reglas registro por registro sin cargar toda la BD en memoria.

---

## 5. Iteradores e iterables — qué hace funcionar al `for`

Esto es el concepto debajo de los generadores. Vale la pena entenderlo porque explica MUCHO comportamiento de Python.

- **Iterable**: algo sobre lo que puedes hacer `for`. Listas, tuplas, strings, dicts, sets, archivos, generadores.
- **Iterador**: el objeto que lleva la cuenta de "por dónde voy". Sabe dar el `siguiente` elemento.

Cuando escribes `for x in lista:`, Python por dentro hace:

```python
it = iter(lista)        # pide un iterador al iterable
while True:
    try:
        x = next(it)    # pide el siguiente elemento
    except StopIteration:
        break           # el iterador avisó "ya no hay más"
```

No necesitas escribir esto nunca — pero saber que `for` ES esto explica por qué:
- Un generador se agota (su iterador llegó al final).
- `StopIteration` es la señal interna de "se acabó", no un error real.
- Puedes hacer `for` sobre un archivo (cada línea es un elemento).

---

## 6. Context managers — el `with` y por qué los archivos se abren así

Habrás visto siempre:

```python
with open("datos.txt") as archivo:
    contenido = archivo.read()
# aquí el archivo YA está cerrado, automáticamente
```

### Qué problema resuelve

Sin `with`, tendrías que acordarte de cerrar todo a mano:

```python
archivo = open("datos.txt")
contenido = archivo.read()
archivo.close()            # ¿y si read() lanza una excepción antes? -> nunca se cierra
```

El `with` **garantiza** la limpieza (cerrar archivo, soltar conexión, liberar candado) **aunque haya una excepción** en medio. Es el patrón "abrir → usar → cerrar pase lo que pase".

### Qué es un context manager

Cualquier objeto que defina dos métodos especiales:
- `__enter__` — se ejecuta al **entrar** al `with` (abre el recurso).
- `__exit__` — se ejecuta al **salir** del `with`, ocurra lo que ocurra (cierra el recurso).

Los verás en: archivos (`open`), conexiones a base de datos (`sqlite3.connect`), candados de hilos, transacciones. En el rules engine, una transacción contra la BD SQLite muy probablemente se maneja con un `with`.

> No necesitas escribir tus propios context managers todavía. Sí necesitas reconocer que `with` significa "esto se limpia solo al salir del bloque".

---

## 7. Dataclasses — clases que son "solo datos"

### El problema

Una clase que solo guarda datos te obliga a escribir mucho ruido:

```python
class Regla:
    def __init__(self, nombre, prioridad, activa):
        self.nombre = nombre
        self.prioridad = prioridad
        self.activa = activa

    def __repr__(self):
        return f"Regla({self.nombre}, {self.prioridad}, {self.activa})"

    def __eq__(self, otra):
        return (self.nombre, self.prioridad, self.activa) == \
               (otra.nombre, otra.prioridad, otra.activa)
```

Tres atributos, ~12 líneas mecánicas. Y los nombres se repiten tres veces cada uno.

### La solución: `@dataclass`

```python
from dataclasses import dataclass

@dataclass
class Regla:
    nombre: str
    prioridad: int
    activa: bool = True      # valor por defecto
```

El decorador `@dataclass` **genera automáticamente** el `__init__`, el `__repr__` y el `__eq__`. Lo de arriba ahora son 4 líneas y hacen lo mismo (y más):

```python
r = Regla("descuento", 5)
print(r)              # Regla(nombre='descuento', prioridad=5, activa=True)
r == Regla("descuento", 5)   # True  -> compara por valor, no por identidad
```

> Conecta con tu apunte `igualdad-vs-identidad`: por defecto dos objetos distintos nunca son `==`. `@dataclass` genera un `__eq__` que compara **campo por campo**. Por eso `r == Regla(...)` da `True`.

Las anotaciones de tipo aquí **no son opcionales**: `@dataclass` las usa para saber cuáles son los campos. Es un caso donde los type hints sí cambian el comportamiento.

---

## 8. Módulos y paquetes — qué significan los `import`

Para leer `vaecos-tracking` necesitas entender cómo está organizado el código en archivos.

### Módulo

Un **módulo** es simplemente un archivo `.py`. Su nombre es el nombre del archivo sin extensión.

```python
# archivo: reglas.py  ->  módulo "reglas"

import reglas                      # importa todo el módulo
reglas.evaluar(...)                # se usa con prefijo

from reglas import evaluar         # importa solo una cosa
evaluar(...)                       # se usa directo

from reglas import evaluar as ev   # importa con otro nombre
```

### Paquete

Un **paquete** es una carpeta que agrupa módulos. Históricamente se marcaba con un archivo `__init__.py` dentro (puede estar vacío; su sola presencia decía "esta carpeta es un paquete"). En Python moderno no siempre es obligatorio, pero lo verás en casi todos los proyectos.

```
vaecos_tracking/
├── __init__.py
├── reglas/
│   ├── __init__.py
│   ├── motor.py
│   └── condiciones.py
└── db.py
```

```python
from vaecos_tracking.reglas.motor import evaluar
#         paquete      subpaquete  módulo  función
```

El `.` en un import recorre carpetas/archivos como el `/` recorre directorios.

### El patrón `if __name__ == "__main__":`

Verás esto al final de muchos archivos:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

Significa: *"ejecuta `main()` SOLO si este archivo se corre directamente (`python archivo.py`), NO si alguien lo importa"*. Permite que un archivo sirva a la vez como programa ejecutable y como módulo importable. La variable `__name__` vale `"__main__"` cuando el archivo es el que arrancó, y vale el nombre del módulo cuando fue importado.

---

## 9. Gotchas que muerden — los verás en código vibecoded

### Argumento por defecto mutable

```python
def agregar(item, lista=[]):     # ❌ TRAMPA
    lista.append(item)
    return lista

agregar(1)    # [1]
agregar(2)    # [1, 2]  <- ¿¿??  esperabas [2]
```

El `[]` del default se crea **UNA sola vez**, cuando se define la función — no en cada llamada. Todas las llamadas comparten la MISMA lista. La forma correcta:

```python
def agregar(item, lista=None):   # ✅
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

> Conecta con `mutabilidad-listas-tuplas`: el default mutable es el caso más famoso de "no entender mutabilidad te explota en la cara".

### Variable de bucle capturada tarde

```python
funciones = [lambda: i for i in range(3)]
[f() for f in funciones]         # [2, 2, 2]  <- no [0, 1, 2]
```

Las `lambda` no capturan el **valor** de `i`, capturan la **variable** `i`. Cuando se ejecutan, el bucle ya terminó e `i` vale 2. (Si esto te confunde ahora, está bien — solo recuerda que pasó, para reconocerlo.)

### `is` para comparar valores

```python
if resultado is 0:    # ❌ no garantizado
if resultado == 0:    # ✅
```

Tu apunte `igualdad-vs-identidad` ya lo cubre: `is` es para identidad (y `None`), `==` es para valores.

### Mutar una lista mientras la recorres

```python
for x in lista:
    if condicion(x):
        lista.remove(x)    # ❌ saltea elementos, comportamiento impredecible
```

Recorre una copia (`for x in lista[:]:`) o construye una lista nueva con una comprehension.

---

## Cómo usar este apunte para leer el rules engine

Cuando abras el motor de reglas de `vaecos-tracking`, ve marcando lo que reconozcas:

1. **Mira las firmas de las funciones primero.** Los type hints te dicen qué entra y sale sin leer el cuerpo.
2. **Cada `import` arriba** te dice qué piezas usa este archivo y de dónde vienen.
3. **Un `@algo`** sobre una función o clase: es un decorador (`decoradores-intro`) o un `@dataclass`.
4. **Un `yield`**: la función es un generador, procesa de a uno.
5. **Un `with`**: hay un recurso (archivo, BD) que se abre y cierra solo.
6. **Lo que NO reconozcas, anótalo** — esa lista es el material de tu próxima sesión de estudio.

El objetivo no es entender cada línea de inmediato. Es que el código deje de verse como un idioma extranjero y empiece a verse como un idioma que estás aprendiendo.

---

## Notas relacionadas

- [[../python/apuntes/decoradores-intro]] — decoradores y funciones de primera clase
- [[../python/apuntes/mutabilidad-listas-tuplas]] — base del gotcha de default mutable
- [[../python/apuntes/igualdad-vs-identidad]] — `==` vs `is`, usado en dataclasses
- [[conceptos-poo]] — clases, `@property`, `@staticmethod`
- [[leer-codigo-vibecoded]] — método para abordar código que no escribiste
- [[../ROADMAP]] — este apunte cubre el gap del Mes 1 (Python profesional)

## Fuentes

- Python docs — typing: https://docs.python.org/3/library/typing.html
- Real Python — Generators: https://realpython.com/introduction-to-python-generators/
- Real Python — Context Managers: https://realpython.com/python-with-statement/
- Python docs — dataclasses: https://docs.python.org/3/library/dataclasses.html

---

*Apunte de Python intermedio/profesional, 2026-05-19. Próximo paso natural: aplicar la sección "Cómo usar este apunte" sobre el rules engine real de vaecos-tracking.*
