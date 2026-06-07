---
tags: [tipo/bitacora, tema/ai, proyecto/ai-engineering-from-scratch, estado/en-progreso]
fecha-inicio: 2026-05-27
curso: github.com/rohitg00/ai-engineering-from-scratch
ubicacion-curso: D:\Mis Archivos\Documentos\Cursos\ai-engineering-from-scratch
---
# Progreso — AI Engineering from Scratch

> Bitácora HUMANA de mi avance. Engram es la memoria de Claude; este archivo es la mía.
> Lo puedo abrir y leer sin Claude para saber dónde voy.

## Entorno (WSL2)

- **SO de trabajo**: WSL2 + Ubuntu 24.04 (dentro de Windows 11). Decisión 2026-05-27.
- **Gestor Python**: `uv` (no pip). Más rápido, junta runtime + paquetes + venvs.
- **Workspace de trabajo activo**: `~/ai-eng/` en **Linux nativo** (RÁPIDO, sin gotchas de venv). Decisión 2026-05-27.
- **Flujo de archivos** (3 lugares):
  - Código en curso → `~/ai-eng/` (WSL nativo)
  - Ejercicios terminados que valen → copiar a `/mnt/d/Mis Archivos/Documentos/Learning/cursos/ai-engineering-from-scratch/ejercicios-mios/` (git/Obsidian)
  - Apuntes en español → Claude los escribe directo en `.../Learning/cursos/ai-engineering-from-scratch/notas/`
- **Dato WSL clave**: `/mnt/d` (disco Windows) es LENTO desde WSL; `~` (Linux nativo) es rápido. Por eso el venv vive en `~`.

## Cómo trabajamos (reglas acordadas)

- **Tutor**: Claude (el repo aporta contenido, Claude aporta la guía adaptativa).
- **Inglés**: día 1, con glosado progresivo (leo término en inglés → Claude explica → construyo vocabulario).
- **Lenguajes**: Python primario SIEMPRE. Rust y Julia cuando el curso los pida, en secuencia (NO las 4 versiones de cada lección).
- **Continuidad**: trabajo SIEMPRE desde la carpeta `Learning` (nunca desde la del curso) para que Engram mantenga el proyecto `learning`.
- **Loop por lección**: (1) traducir docs/en.md marcando términos EN → (2) Claude explica a mi nivel con analogías → (3) Build It guiado sin código masticado → (4) evaluar comprensión → (5) destilar apunte en español.
- **Evaluación por fase**: usar el skill `check-understanding` al cerrar cada fase antes de avanzar.

## Línea base — Placement quiz (find-your-level)

**Fecha**: 2026-05-27 · **Puntaje: 2/10**

| Área | Puntaje |
|---|---|
| Math & Statistics | 0/2 |
| Classical ML | 1/2 (Q4 por deducción) |
| Deep Learning | 0/2 |
| NLP & Transformers | 0/2 |
| Applied AI | 1/2 (Q10 correcta) |

**Punto de entrada asignado: Phase 1 — Math Foundations.** Coincide con el Bloque 2 (Mate+Datos) del roadmap previo → plan bien calibrado.

## Ruta (resumen)

- **DECISIÓN (2026-05-27)**: hago **Phase 0 COMPLETO** (no skip), por elección propia — quiero profundizar Git, Terminal, Jupyter y tooling. Si una lección ya la domino, la verifico rápido y avanzo.
- **Track paralelo de Python-lenguaje**: Phase 0 NO enseña Python el lenguaje (solo el ecosistema: envs/uv/conda). La profundidad de Python la trabajo con `metodos/python-a-fondo.md` + ejercitando en cada Build It desde Phase 1.
- **Phase 1 → 19: Do.** Phase 1 (Math) coincide con mi Bloque 2 del roadmap.
- Total núcleo ~460h (sin capstone), capstone ~500h = proyectos de carrera. Una lección a la vez.

## Registro de lecciones

| Fecha | Fase | Lección | Estado | Notas / qué quedó flojo |
|---|---|---|---|---|
| 2026-05-27 | — | Placement quiz | ✅ | 2/10 → entrada Phase 1 (pero elijo empezar en Phase 0) |
| 2026-05-27 | 0 | 01-dev-environment | ✅ entendida | Entorno completo (7/7 + GPU). Apunte ES en notas/. Evaluación de comprensión: 3/3 con sus palabras (venv, CUDA techo, PATH). Ejercicio 3: hello world en Python/JS/Julia/Rust ✅ (sintió interpretado vs compilado). Ejercicios → ejercicios-mios/fase00-leccion01. |
| 2026-05-29 | 0 | 02-git-and-collaboration | ⬜ pendiente | (próxima) |

> Estados: ⬜ pendiente · 🔄 en curso · ✅ entendida · ⚠️ revisar
