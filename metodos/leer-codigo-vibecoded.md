---
tags: [tipo/metodo, tema/lectura-codigo, tema/git]
fecha: 2026-05-10
---
# Cómo leer código vibecoded (o de otra persona) para entenderlo

> Método de las 5 pasadas. Funciona igual con código humano y con código IA, pero el código IA suele tener más sobre-ingeniería, así que la pasada 3 (cuestionar) es más crítica.

## Filosofía base

Leer un repo es como inspeccionar una casa que otro construyó. **No empiezas mirando los enchufes** — empiezas con la fachada, los planos, las habitaciones principales. Las pasadas van de lo general a lo específico.

## Antes de empezar: protección con Git

No necesitas copia separada del repo. Necesitas **branches**.

```bash
git checkout -b experimento/lo-que-vas-a-explorar
# trabajas, commits atómicos, sin miedo
git checkout main  # vuelves a lo bueno
git branch -d experimento/lo-que-vas-a-explorar  # tiras el experimento si no sirve
```

Combinado con tests existentes (`python -m unittest` o `pytest`), puedes experimentar libremente sin romper producción.

---

## Las 5 pasadas

### 🛩️ Pasada 1 — Vista aérea

Mapeas el territorio. **Sin leer código aún.**

Qué mirar:
- `README.md` — qué hace el proyecto, cómo se arranca
- Estructura de carpetas — qué módulos hay
- Archivos de entrada (`main.py`, `cli.py`, `server.py`, `index.js`)
- Archivos de configuración (`package.json`, `requirements.txt`, `.env.example`)
- Carpeta `docs/` si existe — PRD, Architecture, Design
- Carpeta `tests/` — los tests son documentación viva

Output: deberías poder explicar en voz alta "este proyecto tiene X capas, entra por Y, persiste en Z".

### 🚶 Pasada 2 — Trazar UN camino feliz

Eliges UN flujo (ej: "usuario abre /attention") y lo sigues end-to-end.

Cómo:
1. Desde el entry point, buscas dónde se maneja ese flujo
2. Entras a la función → ves qué llama → entras → etc.
3. Vas anotando: "A llamó B, B leyó C, C devolvió a B, B respondió A"

**Regla clave:** NO leas archivos sueltos. Lee FLUJOS. Un archivo aislado pierde sentido.

### ❓ Pasada 3 — Cuestionar el "por qué"

Por cada decisión rara que veas:
- ¿Esto era necesario o la IA agregó complejidad?
- ¿Qué se rompería si esto no existiera?
- ¿Hay una forma más simple?

Acá detectas sobre-ingeniería típica de IAs: abstracciones prematuras, patrones aplicados sin necesidad, fallbacks para escenarios imposibles.

### 🔧 Pasada 4 — Identificar abstracciones repetidas

Patrones que aparecen 2+ veces. Aprende a nombrarlos:
- **Protocol pattern** (Python typing.Protocol)
- **Registry pattern** (dict de implementaciones)
- **Factory pattern** (función que devuelve la instancia correcta)
- **Strategy pattern** (varias clases con misma interfaz, eliges en runtime)

Cuando los nombras, los entiendes. Cuando los entiendes, los USAS conscientemente en código propio.

### 🔨 Pasada 5 — Modificar deliberadamente

La prueba final: cambias UNA cosa, **predices** qué va a pasar, verificas.
- Acierto → entendiste
- Falla → vuelve a las pasadas 1-4

Vives en una branch con tests. Sin miedo a romper.

---

## Errores comunes al leer código IA

1. **Asumir que todo lo que está ahí es necesario.** Las IAs agregan código defensivo y abstracciones por inercia. Cuestiona.
2. **Leer linealmente top-to-bottom.** Un archivo no se lee como un libro — se lee siguiendo llamadas.
3. **Saltarse los tests.** Los tests son la documentación más honesta del comportamiento esperado.
4. **No mirar `docs/` ni RFCs.** Si la IA documentó sus decisiones, leerlas te ahorra horas.

---

## Herramientas útiles

- `grep -r "función"` (o ripgrep `rg "función"`) — busca dónde se usa algo
- `git log -p archivo.py` — ver historia de cambios de UN archivo
- `git blame archivo.py` — quién (cuándo) escribió cada línea
- Tests como puntos de entrada para entender: corres un test, lees lo que hace, sigues el flujo
- Print debugging selectivo: agregas `print(f"DEBUG: {variable}")` en puntos clave para ver el flujo de datos en vivo

---

## Cuándo aplicar este método

- Heredas un proyecto que no escribiste
- Vuelves a tu propio código vibecoded después de meses
- Vas a entrevista técnica y te dan un repo para revisar
- Te toca contribuir a un open source que no conoces

---

*Apunte vivo — se actualiza con la experiencia.*
