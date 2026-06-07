---
tags: [tipo/apunte, tema/bd, tema/sql, tema/programacion]
fecha: 2026-05-10
---
# Bases de Datos Relacionales — Conceptos

> Apunte de conceptos fundamentales de bases de datos relacionales en español. Pensado para entender la BD de vaecos-tracking y cualquier otra que veas en proyectos reales.

---

## 1. Qué es una base de datos relacional

Una **base de datos** es un sistema que guarda información de forma **organizada**, **persistente** y **consultable**.

**Relacional** significa que los datos se guardan en **tablas** que se pueden **relacionar entre sí**. Es el modelo dominante desde los años 70.

**Analogía:** una BD relacional es como un **archivo de Excel ultra-disciplinado**:
- Cada hoja de Excel = una tabla
- Cada columna tiene un tipo de dato definido (no puedes mezclar texto en una columna de números)
- Las hojas se pueden conectar entre sí con códigos compartidos

Ejemplos de motores relacionales: **SQLite, PostgreSQL, MySQL, MariaDB, SQL Server, Oracle**.

---

## 2. Tabla, columna, fila

| Término técnico | Equivalente Excel | Qué es |
|---|---|---|
| **Tabla** | Hoja | Conjunto de datos del mismo tipo (ej: `guides`, `users`) |
| **Columna** o **campo** | Columna | Una característica que se guarda (ej: `nombre`, `email`) |
| **Fila** o **registro** | Fila | Una instancia concreta de la tabla (ej: el usuario "Ruben") |
| **Celda** | Celda | El dato específico (ej: el email de Ruben) |

```
tabla: users
┌────┬────────┬──────────────────┐
│ id │ nombre │ email            │  ← columnas
├────┼────────┼──────────────────┤
│ 1  │ Ruben  │ ruben@vaecos.com │  ← fila / registro
│ 2  │ Ana    │ ana@vaecos.com   │  ← otra fila
└────┴────────┴──────────────────┘
```

---

## 3. Tipos de datos

Cada columna tiene un **tipo** que define qué se puede guardar ahí. Tipos comunes:

| Tipo | Para qué | Ejemplo |
|---|---|---|
| `INTEGER` / `INT` | Números enteros | `42` |
| `REAL` / `FLOAT` | Decimales | `3.14` |
| `TEXT` / `VARCHAR(n)` | Cadenas de texto | `"hola"` |
| `BOOLEAN` | Sí/No | `true` |
| `DATE` / `DATETIME` / `TIMESTAMP` | Fechas y horas | `2026-05-10 14:30:00` |
| `BLOB` | Datos binarios | imágenes, archivos |
| `JSON` | Datos estructurados | `{"key": "value"}` (no todos los motores) |

> En SQLite (que usa vaecos), los tipos son más laxos que en Postgres — pero la disciplina de respetarlos hace que tu código no se rompa.

---

## 4. Primary Key (PK) — clave primaria

La **PK** es la columna (o combinación de columnas) que **identifica de forma única** cada fila.

**Reglas:**
- Una sola PK por tabla
- No puede ser nula
- No puede repetirse

**Analogía:** es el **número de cédula**. Hay millones de personas, pero cada cédula es única. Si te dan una cédula, encuentras a UNA sola persona.

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,     -- ← PK
    nombre TEXT,
    email TEXT
);
```

**Patrón común:** una columna `id` autoincrementable que no significa nada del negocio, solo sirve como identificador interno.

**PK natural vs sintética:**
- **Natural** = un dato del negocio (ej: número de DNI, código de producto)
- **Sintética** = un número autogenerado sin significado (ej: `id INTEGER AUTOINCREMENT`)

La industria prefiere PKs sintéticas porque el negocio puede cambiar (el DNI puede emitir un duplicado, el código de producto puede repetirse en otra región, etc.), pero un id interno nunca cambia.

---

## 5. Foreign Key (FK) — clave foránea

La **FK** es una columna que **apunta a la PK de otra tabla**. Así se conectan tablas.

**Analogía:** si la PK es el DNI de una persona, una FK es un papel que dice "este contrato pertenece al DNI 123456".

```sql
CREATE TABLE guides (
    guide_id TEXT PRIMARY KEY,
    cliente TEXT
);

CREATE TABLE guide_edits (
    id INTEGER PRIMARY KEY,
    guide_id TEXT,                          -- ← FK
    field TEXT,
    old_value TEXT,
    new_value TEXT,
    FOREIGN KEY (guide_id) REFERENCES guides(guide_id)
);
```

Cada `guide_edits.guide_id` apunta a un `guides.guide_id`. Si en `guides` no existe ese id, la FK puede prevenir que insertes esa edición (depende de la configuración del motor).

**Para qué sirve:**
1. **Integridad referencial** — no puedes apuntar a algo que no existe
2. **Conexión semántica** — sabes qué pertenece a qué
3. **JOINs** — puedes combinar info de varias tablas (más abajo)

---

## 6. Cardinalidad — "cuántos se relacionan con cuántos"

Define cuántas filas de una tabla se relacionan con cuántas de la otra.

### Uno a uno (1:1)

Una fila de A se relaciona con UNA SOLA fila de B, y viceversa.

**Ejemplo:** un usuario tiene un perfil. Cada usuario tiene UN solo perfil, y cada perfil pertenece a UN solo usuario.

```
users  ──── profiles
  1   ───   1
```

Raro en la práctica. Si fuera 1:1 estricto, suele ser mejor poner todo en una sola tabla.

### Uno a muchos (1:N)

Una fila de A se relaciona con MUCHAS de B, pero cada fila de B pertenece a UNA sola de A.

**Ejemplo:** una guía tiene muchas ediciones, pero cada edición pertenece a UNA sola guía.

```
guides  ──── guide_edits
   1   ───   N
```

**Este es el caso más común en la práctica.** La FK vive en el lado "N" (`guide_edits.guide_id` apunta a `guides`).

### Muchos a muchos (N:N)

Una fila de A se relaciona con MUCHAS de B, y una fila de B con MUCHAS de A.

**Ejemplo:** un estudiante toma muchos cursos, y un curso tiene muchos estudiantes.

```
students  ──── ?  ──── courses
   N     ───  ───   ───   N
```

En BDs relacionales esto **NO se puede modelar directo**. Se resuelve con una **tabla intermedia** (también llamada *junction table* o *tabla de unión*):

```sql
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

Cada fila en `enrollments` es UNA inscripción de UN estudiante en UN curso.

---

## 7. JOIN — combinar info de varias tablas

Cuando los datos están repartidos entre tablas, JOIN te los combina en una sola consulta.

**Ejemplo:** "dame todas las ediciones con el nombre del cliente"

```sql
SELECT g.cliente, e.field, e.new_value
FROM guides g
JOIN guide_edits e ON g.guide_id = e.guide_id;
```

**Tipos de JOIN:**

| JOIN | Qué devuelve |
|---|---|
| `INNER JOIN` | Solo filas que existen en AMBAS tablas |
| `LEFT JOIN` | Todas las filas de la tabla izquierda, NULL si no hay match en la derecha |
| `RIGHT JOIN` | Todas las de la derecha, NULL en la izquierda si no hay match |
| `FULL OUTER JOIN` | Todas las filas de ambas, NULL donde no hay match |

**Analogía:**
- `INNER JOIN` = "solo los que están en las dos listas"
- `LEFT JOIN` = "todos los de la lista izquierda, da igual si están en la derecha"

> **SQLite NO soporta RIGHT JOIN ni FULL OUTER JOIN** directamente. Suficiente con INNER y LEFT — cubren el 95% de los casos.

---

## 8. Índices — la "memoria de búsqueda"

Un **índice** es una estructura que el motor mantiene aparte para acelerar búsquedas en una columna.

**Analogía:** es como el **índice alfabético al final de un libro**. Sin él, para encontrar la palabra "transistor" tienes que leer el libro entero. Con él, vas directo a la página.

```sql
CREATE INDEX idx_guides_cliente ON guides(cliente);
```

Ahora `SELECT * FROM guides WHERE cliente = 'Ruben'` es mucho más rápido.

**Reglas prácticas:**
- ✅ Índices en columnas que usas mucho en `WHERE`, `JOIN` o `ORDER BY`
- ✅ La PK ya tiene índice automático (siempre)
- ❌ NO crees índice en columnas que casi no consultas (ocupa espacio y ralentiza inserts)
- ❌ NO crees índice si la tabla tiene pocas filas (no vale la pena)

---

## 9. Normalización — evitar duplicar datos

**Normalizar** = organizar las tablas de forma que cada dato viva en UN solo lugar.

**Ejemplo malo (sin normalizar):**

```
tabla: pedidos
┌────┬──────────┬──────────────┬───────────────┐
│ id │ cliente  │ email        │ producto      │
├────┼──────────┼──────────────┼───────────────┤
│ 1  │ Ruben    │ ruben@x.com  │ camiseta      │
│ 2  │ Ruben    │ ruben@x.com  │ pantalón      │
│ 3  │ Ruben    │ ruben@x.com  │ zapatos       │
└────┴──────────┴──────────────┴───────────────┘
```

Problemas: si Ruben cambia su email, hay que actualizarlo en 3 filas. Si te olvidas de uno, la BD queda inconsistente.

**Ejemplo bueno (normalizado):**

```
tabla: clientes
┌────┬────────┬──────────────┐
│ id │ nombre │ email        │
├────┼────────┼──────────────┤
│ 1  │ Ruben  │ ruben@x.com  │  ← email en UN solo lugar
└────┴────────┴──────────────┘

tabla: pedidos
┌────┬─────────────┬───────────┐
│ id │ cliente_id  │ producto  │
├────┼─────────────┼───────────┤
│ 1  │ 1           │ camiseta  │
│ 2  │ 1           │ pantalón  │
│ 3  │ 1           │ zapatos   │
└────┴─────────────┴───────────┘
```

Si Ruben cambia su email, lo cambias en `clientes` una sola vez, y todos los pedidos quedan correctos.

**Regla práctica:** un dato, un lugar. Si lo repites en varias filas, probablemente necesitas otra tabla.

> **Trade-off:** normalizar más significa más JOINs en las consultas, lo cual puede ser más lento. En sistemas muy grandes a veces se **desnormaliza** a propósito para ganar velocidad. Pero ese es un problema avanzado — empieza siempre normalizando.

---

## 10. Transacciones y ACID

Una **transacción** es un grupo de operaciones que se ejecutan **todas juntas o ninguna**. No hay estados intermedios.

**Ejemplo clásico — transferir dinero:**
1. Restar $100 de la cuenta A
2. Sumar $100 a la cuenta B

Si solo se ejecuta el paso 1 y falla el 2, hay $100 perdidos. Una transacción **garantiza que ambos pasos suceden o ninguno**.

```sql
BEGIN TRANSACTION;
    UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1;
    UPDATE cuentas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;
```

Si algo falla, haces `ROLLBACK` y se deshace todo.

**ACID** son las 4 garantías de una transacción:

| Letra | Nombre | Qué garantiza |
|---|---|---|
| **A** | Atomicity (Atomicidad) | Todo o nada |
| **C** | Consistency (Consistencia) | La BD nunca queda en estado inválido |
| **I** | Isolation (Aislamiento) | Las transacciones concurrentes no se pisan |
| **D** | Durability (Durabilidad) | Una vez commit, los datos sobreviven a caídas |

> En vaecos-tracking, el patrón "Notion FIRST → local + audit" es una forma de transacción manual entre dos sistemas distintos. Si Notion falla, no se modifica local. Es ACID aplicado a un escenario distribuido.

---

## 11. Diferencias entre motores

| Motor | Cuándo usar | Notas |
|---|---|---|
| **SQLite** | Apps pequeñas, locales, móvil, embebido | Un solo archivo `.db`, sin servidor. Lo usa vaecos. |
| **PostgreSQL** | Apps de producción serias | El "estándar de oro" de open-source. Robusto, muchas features. |
| **MySQL** / **MariaDB** | Apps web tradicionales | Muy común en WordPress, sitios PHP |
| **SQL Server** | Empresas con stack Microsoft | Pago, robusto |
| **Oracle** | Bancos, gobiernos | Caro, robusto, complejo |

**SQL básico es portable entre los 5.** Las diferencias salen cuando usas features avanzadas (procedimientos almacenados, triggers, tipos específicos).

---

## 12. NoSQL — el "otro mundo"

Existen bases NO relacionales que organizan los datos de otra forma:

| Tipo | Ejemplos | Para qué |
|---|---|---|
| **Documental** | MongoDB, CouchDB | Datos tipo JSON, esquema flexible |
| **Clave-valor** | Redis, DynamoDB | Cache, sesiones, contadores |
| **Grafos** | Neo4j | Redes sociales, recomendaciones |
| **Columnar** | Cassandra, BigQuery | Analytics, big data |
| **Vectorial** | Pinecone, Chroma, Qdrant | Embeddings para IA/RAG |

> **Para tu camino AI Engineer**, las vectoriales son las que más vas a usar (mes 3 del roadmap).

**Regla práctica:** no elijas NoSQL para escapar de SQL. Elige SQL por defecto, y NoSQL solo si tienes un problema que SQL no resuelve bien (escala extrema, datos sin estructura fija, embeddings, etc.).

---

## 13. SQL en 5 minutos — los comandos que vas a usar

```sql
-- Crear tabla
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE
);

-- Insertar
INSERT INTO users (nombre, email) VALUES ('Ruben', 'ruben@x.com');

-- Consultar
SELECT * FROM users;
SELECT nombre FROM users WHERE id = 1;
SELECT * FROM users WHERE email LIKE '%@vaecos.com';
SELECT COUNT(*) FROM users;

-- Actualizar
UPDATE users SET email = 'nuevo@x.com' WHERE id = 1;

-- Borrar
DELETE FROM users WHERE id = 1;

-- Combinar tablas
SELECT u.nombre, o.producto
FROM users u
JOIN orders o ON u.id = o.user_id;

-- Agrupar
SELECT cliente, COUNT(*) AS total
FROM pedidos
GROUP BY cliente
ORDER BY total DESC;
```

---

## 14. Errores comunes en BDs

1. **No usar índices en columnas que consultas mucho** → queries lentos
2. **Crear índices en TODO** → inserts lentos, espacio desperdiciado
3. **No usar transacciones** cuando varias operaciones deben ir juntas
4. **Permitir `NULL` donde no debería** → bugs raros después
5. **Tipos de datos imprecisos** → guardar fechas como TEXT en vez de DATETIME
6. **No tener PKs** → no puedes referenciar filas de forma estable
7. **Desnormalizar prematuramente** → datos inconsistentes, dolor mantenerlo

---

## Apuntes relacionados

- [[mermaid-diagramas]] — cómo dibujar ER diagrams
- [[leer-codigo-vibecoded]] — método para entender esquemas que escribió la IA

---

*Apunte vivo. Cuando descubras una nueva característica del motor que uses, agrégala aquí.*
