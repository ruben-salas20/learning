---
tags: [tipo/apunte, tema/python, tema/estructuras-de-datos]
fecha: 2026-05-11
estado: en-progreso
---

# Mutabilidad — Lista vs Tupla

## Qué es

> En Python, los objetos son **mutables** (se pueden modificar después de crearlos) o **inmutables** (no se tocan una vez creados). Lista y tupla NO se diferencian por el orden — ambas son ordenadas. Se diferencian por la **mutabilidad**.

## Por qué importa

Confundir esto te hace elegir mal la estructura de datos. Y elegir mal:
- Te puede romper código sin que entiendas por qué (modificás una "tupla" pensando que es lista).
- Te puede hacer pasar por novato en cualquier entrevista técnica.
- Te impide entender por qué Python permite usar tuplas como **claves de diccionario** y listas no.

## Cómo funciona

| Estructura | Sintaxis | Mutable | Ordenada | Permite duplicados |
|---|---|---|---|---|
| **list** | `[1, 2, 3]` | ✅ Sí | ✅ Sí | ✅ Sí |
| **tuple** | `(1, 2, 3)` | ❌ No | ✅ Sí | ✅ Sí |
| **set** | `{1, 2, 3}` | ✅ Sí | ❌ No | ❌ No |
| **dict** | `{"a": 1}` | ✅ Sí | ✅ Sí (Python 3.7+) | Claves no |

> Lo que confundiste — "ordenados vs sin orden" — es la diferencia entre **list/tuple** (ordenadas) y **set/dict** (no garantizan orden de inserción en el sentido clásico, aunque dict lo preserva desde 3.7).

## Ejemplo concreto

```python
# LISTA — mutable
mi_lista = [1, 2, 3]
mi_lista.append(4)          # OK
mi_lista[0] = 99            # OK
print(mi_lista)             # [99, 2, 3, 4]

# TUPLA — inmutable
mi_tupla = (1, 2, 3)
mi_tupla[0] = 99            # ❌ TypeError: 'tuple' object does not support item assignment
mi_tupla.append(4)          # ❌ AttributeError: 'tuple' object has no attribute 'append'
```

### ¿Para qué sirve la inmutabilidad?

```python
# Tupla como clave de diccionario (válido porque es inmutable y hasheable)
ubicaciones = {
    (4.7110, -74.0721): "Bogotá",
    (6.2442, -75.5812): "Medellín",
}
print(ubicaciones[(4.7110, -74.0721)])  # "Bogotá"

# Con lista esto NO funciona
ubicaciones_mal = {[4.7110, -74.0721]: "Bogotá"}
# ❌ TypeError: unhashable type: 'list'
```

### Retornos múltiples = tupla implícita

```python
def coordenadas():
    return 4.71, -74.07   # esto es una tupla, los paréntesis son opcionales

lat, lon = coordenadas()   # unpacking
```

## Cuándo usar cada una

- **Lista** → colecciones que van a cambiar (carrito de compras, lista de tareas, resultados de una API que filtrás).
- **Tupla** → datos que NO deben cambiar (coordenadas, fecha-hora, configuración fija, retornos de función).
- **Set** → necesitás unicidad (¿qué usuarios distintos visitaron hoy?).
- **Dict** → necesitás mapear clave → valor (id → usuario).

## Errores comunes / gotchas

- **Tupla de un solo elemento:** `(5)` NO es tupla, es un entero entre paréntesis. La forma correcta es `(5,)` con coma final.
- **"Las tuplas son inmutables, ergo todo dentro es inmutable" → falso.** Si una tupla contiene una lista, esa lista interna SÍ se puede modificar:
  ```python
  t = ([1, 2], "fijo")
  t[0].append(3)   # OK — modificás la lista DENTRO de la tupla
  print(t)         # ([1, 2, 3], "fijo")
  ```
  Lo que es inmutable es la REFERENCIA, no el contenido referenciado.
- **Performance:** las tuplas son ligeramente más rápidas que las listas porque Python las optimiza al ser inmutables. Diferencia despreciable salvo en código de altísimo rendimiento.

## Notas relacionadas

- [[igualdad-vs-identidad]] — la inmutabilidad afecta cómo se compara con `is`
- [[../README]] — índice de Python

## Fuentes

- Python docs — Data Structures: https://docs.python.org/3/tutorial/datastructures.html
