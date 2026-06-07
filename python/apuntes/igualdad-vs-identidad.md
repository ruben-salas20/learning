---
tags: [tipo/apunte, tema/python, tema/fundamentos]
fecha: 2026-05-11
estado: en-progreso
---

# Igualdad (`==`) vs Identidad (`is`)

## Qué es

> En Python hay DOS formas de comparar objetos:
> - **`==`** → ¿tienen el mismo **valor**?
> - **`is`** → ¿son literalmente el **mismo objeto** en memoria?
>
> Son cosas distintas. Confundirlas te lleva a bugs sutiles que tardás horas en encontrar.

## Por qué importa

- En el 99% de los casos querés `==`. Si usás `is` por costumbre, vas a tener falsos negativos.
- La excepción canónica es la comparación con `None`, donde `is None` es la forma idiomática.
- Entender la diferencia te obliga a entender cómo Python maneja **objetos en memoria** — concepto base para entender mutabilidad, paso por referencia, copias, etc.

## Cómo funciona

Cada objeto en Python tiene 3 cosas:
1. Un **valor** (lo que contiene)
2. Un **tipo** (`int`, `list`, `str`, etc.)
3. Una **identidad** (una dirección de memoria, accesible con `id(obj)`)

- `a == b` → llama al método `__eq__` de los objetos. Compara valores.
- `a is b` → compara `id(a) == id(b)`. ¿Apuntan al mismo objeto?

## Ejemplo concreto

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a               # c apunta al MISMO objeto que a

print(a == b)       # True  → mismo contenido
print(a is b)       # False → objetos distintos en memoria
print(a is c)       # True  → c y a son el mismo objeto

print(id(a))        # ej: 140234567891200
print(id(b))        # ej: 140234567891456  (distinto)
print(id(c))        # ej: 140234567891200  (igual a a)
```

### Por qué con `None` se usa `is`

`None` es un **singleton**: existe UNA sola instancia en todo el programa. Por eso comparar con `is` es:
1. Más rápido (es una comparación de punteros, no llama a `__eq__`).
2. Más correcto (no podés tener "otro None" con el mismo valor pero distinta identidad).

```python
# ✅ Forma idiomática
if x is None:
    ...

# ❌ Funciona pero NO es Pythonico
if x == None:
    ...
```

Lo mismo aplica para `True`, `False` y los tipos singleton.

## El gotcha de los enteros chicos

Python cachea los enteros pequeños (-5 a 256) por optimización. Esto puede confundirte:

```python
a = 100
b = 100
print(a is b)       # True  ← engañoso, son el mismo objeto cacheado

a = 1000
b = 1000
print(a is b)       # False ← son distintos objetos
```

**Conclusión:** NUNCA uses `is` para comparar valores. Usá `==`. Reservá `is` para `None`, `True`, `False`.

## Cuándo usar cada uno

| Caso | Operador correcto |
|---|---|
| Comparar valores (números, strings, listas, etc.) | `==` |
| Comparar contra `None` | `is` |
| Comparar contra `True` o `False` (raro) | `is` |
| Saber si dos variables apuntan al mismo objeto | `is` |
| Saber si dos objetos tienen el mismo contenido | `==` |

## Errores comunes / gotchas

- **`x == None`** funciona pero NO es idiomático. Linters como `flake8` te lo marcan.
- **`if x is True:`** rara vez es lo que querés. Casi siempre lo correcto es `if x:` (truthy check).
- **Confiar en `is` para enteros/strings.** Funciona "por accidente" en algunos casos por caching, falla en otros. Nunca dependas de eso.

## Notas relacionadas

- [[mutabilidad-listas-tuplas]] — la identidad importa más cuando los objetos son mutables
- [[../README]] — índice de Python

## Fuentes

- Python docs — `is` operator: https://docs.python.org/3/reference/expressions.html#is
- PEP 8 (estilo): comparar con None usando `is`
