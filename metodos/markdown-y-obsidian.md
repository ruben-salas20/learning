---
tags: [tipo/cheatsheet, tema/markdown, tema/obsidian]
fecha: 2026-05-10
---
# Markdown y Obsidian — Guía rápida para tomar notas

> Cheat sheet de lo que vas a usar en serio. Markdown estándar + extras de Obsidian.

---

## 1. Encabezados (jerarquía de la nota)

```markdown
# Título principal (H1) — uno solo por nota
## Sección (H2)
### Sub-sección (H3)
#### Detalle (H4)
```

**Regla práctica:** una nota = un H1. Resto son H2/H3.

---

## 2. Énfasis

```markdown
*cursiva* o _cursiva_
**negrita** o __negrita__
***negrita y cursiva***
~~tachado~~
==resaltado==          ← solo Obsidian
```

---

## 3. Listas

**Con viñetas:**
```markdown
- Item 1
- Item 2
  - Sub-item (2 espacios o tab)
  - Otro sub-item
```

**Numeradas:**
```markdown
1. Primer paso
2. Segundo paso
3. Tercero
```

**Checkboxes (clave para tareas):**
```markdown
- [ ] Pendiente
- [x] Hecho
```

---

## 4. Enlaces

**Markdown estándar:**
```markdown
[Texto visible](https://url.com)
[Enlace a archivo local](./otro-archivo.md)
```

**Wikilinks de Obsidian (la joya):**
```markdown
[[Nombre de la nota]]              ← enlaza a otra nota
[[Nombre de la nota|Texto alias]]  ← con texto distinto al nombre
[[Nota#Sección]]                   ← enlaza a una sección específica
[[Nota#^bloque]]                   ← enlaza a un bloque específico
```

Los wikilinks son la **superpotencia de Obsidian**. Crean la red de conocimiento. Úsalos siempre que menciones otra nota.

---

## 5. Imágenes

```markdown
![Texto alternativo](ruta/imagen.png)
![[imagen.png]]                    ← Obsidian, más simple
![[imagen.png|300]]                ← con ancho en px
```

---

## 6. Código

**Inline:** rodea con backticks → \`código\` → se ve como `código`

**Bloques con sintaxis:**

````markdown
```python
def hola():
    print("hola")
```

```bash
git checkout -b nueva-rama
```

```sql
SELECT * FROM users WHERE active = 1;
```
````

Lenguajes útiles: `python`, `bash`, `powershell`, `sql`, `javascript`, `typescript`, `java`, `json`, `yaml`, `markdown`.

---

## 7. Citas / blockquotes

```markdown
> Esto es una cita o nota destacada.
> Sigue en la línea siguiente.
>
> Otro párrafo de la cita.
```

---

## 8. Tablas

```markdown
| Columna 1 | Columna 2 | Columna 3 |
|---|---|---|
| dato | dato | dato |
| dato | dato | dato |
```

**Alineación:**
```markdown
| Izquierda | Centrado | Derecha |
|:---|:---:|---:|
| a | b | c |
```

---

## 9. Líneas horizontales (separadores)

```markdown
---
```

Tres guiones en línea propia. Útil para separar secciones grandes.

---

## 10. Callouts (Obsidian) — muy útiles

```markdown
> [!note] Título opcional
> Contenido de la nota

> [!tip] Tip rápido
> Algo que vale la pena resaltar.

> [!warning] Cuidado
> Esto puede salir mal si no...

> [!info]
> Información general.

> [!success] Hecho
> Funcionó.

> [!example]
> Mira este ejemplo concreto.

> [!quote]
> "Cita textual aquí."
```

Tipos disponibles: `note`, `tip`, `info`, `warning`, `danger`, `success`, `example`, `quote`, `abstract`, `todo`, `question`, `bug`.

**Plegable:**
```markdown
> [!info]- Plegado por defecto
> Aparece cerrado.

> [!info]+ Abierto por defecto
> Aparece expandido.
```

---

## 11. Tags (Obsidian)

```markdown
#tema/python
#nivel/intermedio
#vaecos
```

Los tags con `/` crean jerarquías. Aparecen en el panel de tags.

---

## 12. Frontmatter / Metadatos (Obsidian)

Al inicio del archivo, entre `---`:

```markdown
---
titulo: Pasada 2 — Trazar attention
fecha: 2026-05-10
tags: [vaecos, lectura-codigo, pendiente]
estado: en-progreso
---

# Contenido normal aquí
```

Muy útil para filtrar y organizar.

---

## 13. Notas al pie

```markdown
Algo importante[^1].

[^1]: La explicación de la nota al pie.
```

---

## 14. Matemáticas (LaTeX) — Obsidian

```markdown
Inline: $a^2 + b^2 = c^2$

Bloque:
$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$
```

Útil para apuntes de estadística o ML.

---

## 15. Diagramas Mermaid (Obsidian)

````markdown
```mermaid
graph LR
    A[Usuario] --> B[/attention]
    B --> C[Handler]
    C --> D[(SQLite)]
    D --> C
    C --> E[Template]
```
````

Tipos: `graph`, `flowchart`, `sequenceDiagram`, `classDiagram`, `gantt`, `pie`.

Muy útil para diagramas de flujo cuando documentes lo que aprendiste leyendo código.

---

## 16. Atajos de teclado en Obsidian (los que valen)

| Acción | Atajo |
|---|---|
| Negrita | `Ctrl + B` |
| Cursiva | `Ctrl + I` |
| Enlace | `Ctrl + K` |
| Nueva nota | `Ctrl + N` |
| Cambiar entre vista edición/preview | `Ctrl + E` |
| Buscar en todo el vault | `Ctrl + Shift + F` |
| Abrir comando rápido | `Ctrl + P` |
| Insertar wikilink | `[[` |
| Insertar tag | `#` |

---

## 17. Convenciones que te recomiendo adoptar

1. **Una nota = una idea o un tema.** No mezcles. Mejor 10 notas chiquitas conectadas que 1 nota gigante.
2. **Nombra archivos en kebab-case**: `pasada-2-attention.md`, no `Pasada 2 Attention.md`. Funciona mejor con git.
3. **Empieza siempre con un H1** que diga qué es la nota.
4. **Usa frontmatter para tareas:** `estado: pendiente | en-progreso | hecho`.
5. **Wikilinks > enlaces relativos** dentro del vault. Más resistentes a renombres.
6. **Si una nota crece mucho, divídela** y conéctala con wikilinks.
7. **Tags por dimensión, no por nota:** `#tema/python`, `#tipo/apunte`, `#estado/pendiente`.

---

## 18. Templates recomendados (para tu vault)

### Plantilla — apunte conceptual
```markdown
---
tags: [tema/X, tipo/apunte]
fecha: YYYY-MM-DD
---

# Título del concepto

## Qué es
...

## Por qué importa
...

## Ejemplo concreto
...

## Notas relacionadas
- [[...]]
- [[...]]
```

### Plantilla — bitácora de ejercicio
```markdown
---
tags: [tema/X, tipo/ejercicio]
fecha: YYYY-MM-DD
estado: hecho
---

# Ejercicio: ...

## Enunciado
...

## Mi solución
```python
...


## Qué aprendí
- ...
- ...

## Dudas que quedaron
- ...


---

## 19. Errores comunes

- ❌ Olvidar la línea en blanco antes de un bloque de código → se rompe el formato.
- ❌ Indentar listas con un solo espacio → necesita 2 o tab.
- ❌ Confundir `*` con `-` en listas (ambos funcionan, pero sé consistente).
- ❌ Usar negrita en TODO → pierde fuerza.
- ❌ Notas gigantes sin H2/H3 → imposibles de escanear.

---

*Esta guía es viva. Cuando descubras algo útil en Obsidian, agrégalo aquí.*
