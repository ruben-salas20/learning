---
tags: [tipo/tarea, proyecto/vaecos-tracking, tema/lectura-codigo, estado/pendiente]
fecha-asignada: 2026-05-10
estado: pendiente
---
# Tarea — Pasada 2: Trazar `/attention` en vaecos-tracking v0.4

> **Fecha asignada:** 2026-05-10
> **Método:** [[leer-codigo-vibecoded]] — Pasada 2
> **Estado:** 🟡 Pendiente

---

## 🎯 Objetivo

Entender end-to-end qué pasa cuando un usuario abre la ruta `/attention` en la web v0.4. Pasar de "esto lo hizo la IA" a "yo puedo explicar este flujo línea por línea".

## 🧭 Por qué esta tarea

Es la primera pasada práctica del método de lectura. Cierra el gap entre tener el código y entender el código. Sin esto, eres rehén de la IA en tu propio proyecto.

---

## 📚 Pre-requisitos — leer ANTES de tocar código

Estos 3 documentos te dan el mapa mental. Sin ellos, leer código es navegar sin GPS.

- [ ] `CLAUDE.md` (raíz del repo) — guía técnica completa
- [ ] `docs/ARCHITECTURE.md` — arquitectura por capas y patrones
- [ ] `docs/PRD.md` — el "por qué" del producto

**Tiempo estimado:** 1–2 horas. Anota dudas que surjan, no las resuelvas todavía.

---

## 🛠️ Setup técnico

- [ ] `cd "D:\Mis Archivos\Documentos\Vaecos\Proyectos\Automatización novedades"`
- [ ] Verificar que la carpeta es repo git: `Test-Path .git` → debe devolver `True`
- [ ] `git status` para confirmar que no hay cambios sin commitear
- [ ] `git checkout main` y `git pull` para tener el código más reciente
- [ ] Crear branch de experimento: `git checkout -b lectura/entender-attention`
- [ ] Confirmar que estás en la branch nueva: `git branch` → debe mostrar `* lectura/entender-attention`

---

## 🚶 Pasada 2 — Trazar el flujo

Hacer en este orden, sin saltarse pasos.

### Paso 1 — Encontrar el punto de entrada de la ruta

- [ ] Identificar el archivo `server.py` o equivalente que arranca v0.4
- [ ] Encontrar cómo se registran las rutas (probablemente blueprints de Flask)
- [ ] Localizar el archivo específico donde vive la ruta `/attention`
- [ ] Anotar la ruta del archivo y el número de línea donde se define la ruta

### Paso 2 — Trazar la función handler

- [ ] Leer la función que maneja `GET /attention` línea por línea
- [ ] Identificar qué hace: ¿consulta la BD? ¿filtra datos? ¿llama a otros módulos?
- [ ] Anotar cada llamada externa con el formato: `handler → llama a X.y() → que está en archivo/path.py`

### Paso 3 — Bajar por la pila de llamadas

- [ ] Para cada función que llamó el handler, repetir Paso 2
- [ ] Llevar un diagrama tipo árbol o bullet points anidados de la cadena de llamadas
- [ ] Detenerse cuando llegues a:
  - Una query SQL directa
  - Una llamada a librería externa (Notion, Flask, etc.)
  - Un retorno de datos simple

### Paso 4 — Identificar la respuesta

- [ ] ¿Qué template HTML se renderiza? Localizarlo en `templates/`
- [ ] ¿Qué variables se le pasan al template?
- [ ] Abrir el template y entender qué muestra al usuario

### Paso 5 — Cuestionar (esto es lo más valioso)

Anotar dudas honestas para discutir en la próxima sesión:

- [ ] ¿Hay alguna decisión que me parece extraña o complicada?
- [ ] ¿Alguna abstracción que me parece innecesaria?
- [ ] ¿Hay código que no entiendo qué hace, incluso después de leerlo varias veces?
- [ ] ¿Hay nombres confusos o que podrían ser más claros?

---

## 📦 Qué entregar

Un archivo markdown propio dentro de `Learning/vaecos/apuntes/` (crear la carpeta si no existe) con:

- [ ] **Diagrama del flujo** — texto/bullets anidados o un mermaid simple
- [ ] **Listado de archivos involucrados** con rutas exactas
- [ ] **Resumen en lenguaje natural** — explicar el flujo en 5-10 frases como si se lo contaras a otro humano
- [ ] **Mis dudas** — lista honesta de lo que no entendiste o te pareció raro
- [ ] **Patrones de diseño identificados** — nombres formales si pudiste reconocerlos (Protocol pattern, Factory, etc.)

Nombre sugerido del archivo: `pasada-2-attention.md`

---

## ✅ Criterios de "hecho"

La tarea está completa cuando:

- [ ] Puedes explicar el flujo de `/attention` en voz alta sin mirar el código
- [ ] Tienes un archivo markdown en `vaecos/apuntes/` con el flujo documentado
- [ ] Tienes al menos 3 dudas o cuestionamientos honestos para llevar a la próxima sesión
- [ ] El branch `lectura/entender-attention` existe localmente (puede no tener commits — solo lectura es válido)

---

## ⚠️ Reglas de oro

- **No le pidas a la IA que te explique el código aún.** Si lo haces, te ahorras tiempo pero pierdes el aprendizaje. La IA viene en la siguiente sesión cuando comparemos lo que tú entendiste vs lo que es.
- **No leas linealmente.** El código no se lee como un libro, se lee siguiendo llamadas.
- **Anota TODO lo que no entiendas.** No te juzgues por no entender — esa es la materia prima de la próxima sesión.
- **Si algo te toma más de 30 minutos sin avanzar**, paras y lo dejas anotado como duda. No insistas.

---

## ⏱️ Tiempo estimado total

- Pre-lectura: 1–2h
- Setup git: 5 min
- Pasada 2: 1–2h
- Documentar entrega: 30 min

**Total realista:** 3–5 horas distribuidas en 1–2 sesiones de trabajo personal.

---

*Vuelve con esto listo y arrancamos la próxima sesión con sustancia real.*
