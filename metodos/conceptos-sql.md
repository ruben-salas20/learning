---
tags: [tipo/apunte, tema/sql, tema/bases-de-datos]
fecha: 2026-05-11
estado: en-progreso
---

# SQL — Lectura y escritura básica

> Este apunte es la parte **práctica** del trabajo con bases de datos. La parte teórica (qué es una BD, PK, FK, normalización, ACID) está en [[conceptos-bd]].

## Por qué importa

SQL es el lenguaje universal de bases de datos relacionales. Lo vas a usar en:
- Análisis de datos (toda la información de empresa vive en bases SQL).
- Backend (toda app real consulta una BD).
- ML/Data Science (extraer datos de tu warehouse para entrenar modelos).

**Si no sabés SQL, no podés trabajar con datos reales.** Punto.

---

## Anatomía de una query SELECT

Toma esta query como ejemplo y leamosla por dentro:

```sql
SELECT nombre, COUNT(*) AS total
FROM ventas
WHERE fecha >= '2026-01-01'
GROUP BY nombre
ORDER BY total DESC;
```

Vamos cláusula por cláusula:

| Cláusula | Qué hace |
|---|---|
| `SELECT nombre, COUNT(*) AS total` | **Qué columnas traer.** Aquí pide la columna `nombre` y un conteo de filas (que renombra como `total` con `AS`). |
| `FROM ventas` | **De qué tabla.** |
| `WHERE fecha >= '2026-01-01'` | **Filtro de filas.** Solo las filas cuya `fecha` sea **mayor o igual** al 1 de enero de 2026 (es decir, desde esa fecha en adelante). |
| `GROUP BY nombre` | **Agrupar.** Consolidá las filas por valor único de `nombre`. Esto habilita usar funciones de agregación como `COUNT`, `SUM`, `AVG`. |
| `ORDER BY total DESC` | **Ordenar.** Por la columna `total` de mayor a menor (`DESC` = descendente). |

> ⚠️ **Trampa común:** `>=` significa **"desde, en adelante"**. NO significa "ese día". Para "ese día exacto" se usa `=`. Confundirlas te hace traer datos de más o de menos.

> ⚠️ **`SELECT nombre, COUNT(*)` ≠ "todos los datos de nombre".** SQL trae **exactamente las columnas que pediste**, ni una más. No existe el "trae todo automágicamente". Si querés todas las columnas, `SELECT *` (pero en producción se evita por performance).

### Orden de ejecución real (importante)

Aunque la query la escribís así:

```
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

La base de datos la ejecuta en otro orden:

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

**Por qué importa:** podés usar `WHERE` con cualquier columna de la tabla, pero NO podés usar `WHERE` con un alias de `SELECT` (porque `SELECT` aún no se ejecutó). Para filtrar después de agrupar, usás `HAVING`.

```sql
-- ❌ Esto NO funciona
SELECT nombre, COUNT(*) AS total
FROM ventas
WHERE total > 10              -- alias 'total' no existe todavía
GROUP BY nombre;

-- ✅ Esto SÍ
SELECT nombre, COUNT(*) AS total
FROM ventas
GROUP BY nombre
HAVING COUNT(*) > 10;
```

---

## Las cláusulas básicas que tenés que dominar

### `WHERE` — filtros

```sql
SELECT * FROM productos WHERE precio > 100;
SELECT * FROM productos WHERE categoria = 'electrónica';
SELECT * FROM productos WHERE precio BETWEEN 50 AND 200;
SELECT * FROM productos WHERE nombre LIKE 'cable%';   -- empieza con 'cable'
SELECT * FROM productos WHERE categoria IN ('electrónica', 'hogar');
SELECT * FROM productos WHERE descripcion IS NULL;     -- ⚠️ NUNCA `= NULL`
```

> NULL es especial: no se compara con `=`, se compara con `IS NULL` o `IS NOT NULL`.

### Funciones de agregación

| Función | Qué hace |
|---|---|
| `COUNT(*)` | Cuenta filas |
| `SUM(columna)` | Suma valores |
| `AVG(columna)` | Promedio |
| `MIN(columna)` | Mínimo |
| `MAX(columna)` | Máximo |

Casi siempre se usan junto con `GROUP BY`.

```sql
-- Total vendido por categoría
SELECT categoria, SUM(precio * cantidad) AS ingresos
FROM ventas
GROUP BY categoria;
```

### `LIMIT` y `OFFSET`

```sql
SELECT * FROM productos ORDER BY precio DESC LIMIT 10;          -- top 10
SELECT * FROM productos ORDER BY precio DESC LIMIT 10 OFFSET 10; -- siguientes 10 (paginación)
```

---

## JOINs — combinar tablas

El concepto que más confunde al inicio. Es lo que hace que SQL sea poderoso.

### Setup de ejemplo

Imaginá dos tablas:

**`clientes`**
| id | nombre |
|---|---|
| 1 | Ana |
| 2 | Bruno |
| 3 | Carla |

**`pedidos`**
| id | cliente_id | total |
|---|---|---|
| 100 | 1 | 50 |
| 101 | 1 | 30 |
| 102 | 2 | 80 |

Bruno tiene 1 pedido. Ana tiene 2. Carla no tiene ninguno.

### `INNER JOIN` — solo las coincidencias

Trae filas que tienen match en AMBAS tablas.

```sql
SELECT clientes.nombre, pedidos.total
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;
```

Resultado:
| nombre | total |
|---|---|
| Ana | 50 |
| Ana | 30 |
| Bruno | 80 |

> Carla no aparece. No tiene pedidos.

### `LEFT JOIN` — todo lo de la izquierda + lo que matchee de la derecha

Trae TODAS las filas de la tabla izquierda. Si no hay match en la derecha, las columnas de la derecha quedan en `NULL`.

```sql
SELECT clientes.nombre, pedidos.total
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;
```

Resultado:
| nombre | total |
|---|---|
| Ana | 50 |
| Ana | 30 |
| Bruno | 80 |
| Carla | NULL |

> Carla aparece con NULL. Útil para preguntas como "¿qué clientes NUNCA compraron?":
> ```sql
> SELECT c.nombre
> FROM clientes c
> LEFT JOIN pedidos p ON c.id = p.cliente_id
> WHERE p.id IS NULL;
> ```

### `RIGHT JOIN` y `FULL OUTER JOIN`

- **`RIGHT JOIN`** = espejo del LEFT. Casi nadie lo usa, se prefiere reescribir como LEFT cambiando el orden de las tablas.
- **`FULL OUTER JOIN`** = todo de ambas tablas, NULL donde no hay match. Útil para auditorías.

### Diagrama mental

```
INNER:   solo intersección                A ∩ B
LEFT:    todo A + intersección con B     A
RIGHT:   todo B + intersección con A      B
FULL:    todo A + todo B                 A ∪ B
```

---

## Errores comunes / gotchas

- **`SELECT *` en producción.** Trae todas las columnas, gasta red, gasta memoria, y se rompe si la tabla cambia. Pedí siempre lo que vas a usar.
- **Comparar con NULL usando `=`.** No funciona. NULL no es igual a NULL. Usá `IS NULL`/`IS NOT NULL`.
- **Olvidar `GROUP BY`.** Si en `SELECT` mezclás columnas con funciones de agregación, casi siempre te falta `GROUP BY` con esas columnas. Algunos motores te dan error, otros (como MySQL viejo) te dejan pasar y devuelven datos incorrectos.
- **JOIN sin `ON`.** Sin condición de unión, hacés un **producto cartesiano** (cada fila de A × cada fila de B). Si A tiene 1000 y B tiene 1000, te trae 1.000.000 de filas. Cuidado.
- **No usar alias.** En queries con muchos JOINs, los alias (`FROM clientes c`, `FROM pedidos p`) hacen el SQL legible.

## Notas relacionadas

- [[conceptos-bd]] — teoría de BD relacionales (PK, FK, normalización)
- [[../python/apuntes/venv-vs-env]] — para conectar Python a una BD necesitás librería + secretos en `.env`

## Fuentes

- SQLZoo (gratis, con ejercicios): https://sqlzoo.net
- Mode Analytics SQL Tutorial: https://mode.com/sql-tutorial
