---
tags: [tipo/apunte, tema/python, tema/funciones-avanzadas]
fecha: 2026-05-11
estado: en-progreso
---
# Decoradores — Introducción

## Qué es

> Un **decorador** es una función que **envuelve** a otra función para agregarle comportamiento, SIN modificar el código original.
>
> Sintácticamente lo reconocés por la `@` arriba de una función:
>
> ```python
> @mi_decorador
> def saludar():
>     print("hola")
> ```

## Por qué importa

- En frameworks reales (Flask, FastAPI, Django, pytest) los decoradores están **en todas partes**: `@app.route(...)`, `@pytest.fixture`, `@property`, `@staticmethod`, `@classmethod`.
- No entender qué es `@algo` te deja viendo código como si fuera magia. Y "no entender" es exactamente el vibecoded gap que estamos cerrando.
- Es uno de los conceptos que separa "sé sintaxis básica" de "entiendo Python".

## Cómo funciona — la idea base

En Python, **las funciones son objetos de primera clase**. Esto significa que:

```python
def saludar():
    print("hola")

# Las funciones se pueden asignar a variables
otra = saludar
otra()                  # imprime "hola"

# Se pueden pasar como argumentos
def ejecutar(funcion):
    funcion()

ejecutar(saludar)       # imprime "hola"

# Se pueden retornar desde otras funciones
def crear_funcion():
    def interna():
        print("soy interna")
    return interna

f = crear_funcion()
f()                     # imprime "soy interna"
```

Sobre esto se construyen los decoradores.

## Ejemplo concreto — paso a paso

### Versión sin azúcar sintáctico

```python
def loguear(funcion):
    def envoltura():
        print(f"-> Ejecutando {funcion.__name__}")
        funcion()
        print(f"<- Terminó {funcion.__name__}")
    return envoltura

def saludar():
    print("hola")

# Decoramos manualmente
saludar = loguear(saludar)
saludar()
```

Salida:
```
-> Ejecutando saludar
hola
<- Terminó saludar
```

### Versión con `@` (azúcar sintáctico)

Esto:

```python
@loguear
def saludar():
    print("hola")
```

Es **exactamente lo mismo** que:

```python
def saludar():
    print("hola")
saludar = loguear(saludar)
```

`@loguear` arriba de `saludar` significa "asigná `saludar` al resultado de `loguear(saludar)`".

## Decorador con argumentos en la función decorada

Cuando la función decorada recibe argumentos, la envoltura debe pasarlos:

```python
def loguear(funcion):
    def envoltura(*args, **kwargs):
        print(f"-> {funcion.__name__}({args}, {kwargs})")
        resultado = funcion(*args, **kwargs)
        print(f"<- retornó {resultado}")
        return resultado
    return envoltura

@loguear
def sumar(a, b):
    return a + b

sumar(3, 4)
```

Salida:
```
-> sumar((3, 4), {})
<- retornó 7
```

> `*args` y `**kwargs` significan "aceptá cualquier cantidad de argumentos posicionales y nombrados". Es OTRO tema importante de Python intermedio que voy a profundizar después.

## Decoradores que verás en código real

| Decorador | Para qué |
|---|---|
| `@property` | Convierte un método en un atributo de solo lectura |
| `@staticmethod` | Método de clase que no necesita `self` ni `cls` |
| `@classmethod` | Método de clase que recibe `cls` en vez de `self` |
| `@app.route("/")` | Flask — registra una URL |
| `@app.get("/")` | FastAPI — registra un endpoint GET |
| `@pytest.fixture` | pytest — declara una fixture de testing |
| `@dataclass` | Auto-genera `__init__`, `__repr__`, etc. en una clase |
| `@functools.cache` | Cachea resultados de la función |

## Errores comunes / gotchas

- **No retornar la envoltura.** Si el decorador no retorna `envoltura`, la función decorada queda como `None` y rompe.
- **Olvidar `*args, **kwargs`.** Si tu envoltura no los acepta, cualquier función con argumentos rompe.
- **Perder el nombre original.** Por defecto, `saludar.__name__` después de decorar es `"envoltura"`, no `"saludar"`. Para preservarlo se usa `functools.wraps`:
  ```python
  from functools import wraps

  def loguear(funcion):
      @wraps(funcion)
      def envoltura(*args, **kwargs):
          ...
      return envoltura
  ```
  Esto importa para debugging y para frameworks que inspeccionan los nombres.

## Cuándo NO crear tu propio decorador

- Para una sola función. Si solo querés agregar logging a una función, agregalo dentro de la función. Los decoradores brillan cuando aplicás el MISMO comportamiento a MUCHAS funciones (autenticación, logging, caching, validación de permisos).

## Notas relacionadas

- [[../README]] — índice de Python
- POO en Python: [[../../metodos/conceptos-poo]] — `@property`, `@staticmethod`, `@classmethod`

## Fuentes

- Real Python — Primer on Decorators: https://realpython.com/primer-on-python-decorators/
- Python docs — functools.wraps: https://docs.python.org/3/library/functools.html#functools.wraps
