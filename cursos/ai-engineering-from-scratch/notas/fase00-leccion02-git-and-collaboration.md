---
tags: [tipo/apunte, tema/git, tema/colaboracion, proyecto/ai-engineering-from-scratch, estado/completo]
fecha: 2026-06-08
fase: 0 - Setup & Tooling
leccion: 02 - Git & Collaboration
fuente: phases/00-setup-and-tooling/02-git-and-collaboration
---
# Fase 0 · Lección 2 — Git & Collaboration

> **Lema de la lección**: *"Version control is not optional."*
> (El control de versiones NO es opcional.) Cada experimento, cada modelo, cada lección se trackea.
>
> Esta lección la pasé por **evaluación (5/6)**: ya manejaba el flujo. Acá quedan los conceptos
> + las dos correcciones que valieron la pena.

---

## 1. El concepto que más se confunde: repo LOCAL vs REMOTO

Un repositorio **NO vive (solo) en GitHub**. Un repo es **tu carpeta de proyecto + TODO su historial de cambios**, y existe **primero en tu máquina** (la carpeta oculta `.git/`).

> GitHub/GitLab/BitBucket solo guardan una **COPIA REMOTA** de ese repo.

```
Repo LOCAL (tu PC, carpeta .git)  ⇄  Repo REMOTO (GitHub)
```

La pista de que esto es así: cuando hago `git push` subo los commits **pendientes**. Si están "pendientes de subir" es porque YA existen en mi repo local. El commit es local; el push lo replica al remoto.

---

## 2. El flujo diario (las 3 zonas)

```
Working Directory  → (git add)    → Staging Area      # carpeta de trabajo → área de preparación
Staging Area       → (git commit) → Local Repo        # preparación → repo LOCAL (nueva versión/snapshot)
Local Repo         → (git push)   → Remote (GitHub)   # repo local → remoto
Remote             → (git fetch)  → Local Repo         # bajar cambios sin fusionar
Local Repo         → (git pull)   → Working Directory  # traer + fusionar cambios
```

- **`git add`**: pone los cambios en el *staging area* (como un pre-commit; eligís QUÉ entra en la próxima versión).
- **`git commit -m "..."`**: crea una **snapshot** (foto del proyecto entero en ese momento). A un commit se puede volver.
- **`git push origin main`**: sube la rama `main` al remoto apodado `origin`.
  - 📌 **`origin` es solo un ALIAS** de la URL del remoto (para no escribir `https://github.com/...` cada vez). Por convención se llama `origin`, pero el nombre lo definís vos.

---

## 3. Ramas (branches)

Una **branch** es un **puntero** a un commit que avanza a medida que trabajás (NO una copia literal).

```bash
git checkout -b experiment/new-optimizer   # crea la rama Y te cambia a ella
# ...trabajás y comiteás aislado de main...
git checkout main
git merge experiment/new-optimizer          # trae los cambios de la rama a main
```

> **Nota moderna (Git 2.23+)**: el viejo `checkout` hacía demasiado (cambiar de rama Y restaurar archivos), confuso. Hoy se recomienda separarlo:
> - `git switch <rama>` → moverse entre ramas
> - `git switch -c <rama>` → crear y cambiar (equivale a `checkout -b`)
> - `git restore <archivo>` → descartar cambios de un archivo

---

## 4. `.gitignore` y los archivos de modelos (mi gap, ya cubierto)

El `.gitignore` lista lo que Git debe IGNORAR (no trackear). En IA, lo crítico son los **pesos de modelos**:

| Extensión | Qué es |
|---|---|
| `.pt` / `.pth` | **PyTorch** — modelo/pesos guardados con `torch.save()`. ("p**t**" = py**t**orch) |
| `.safetensors` | **Hugging Face** — formato seguro para pesos (sin código ejecutable, a diferencia del pickle de `.pt`) |

**Por qué se excluyen**: son **binarios enormes** (GB), Git maneja pésimo lo binario/pesado (infla y ralentiza el repo), y **se pueden regenerar** (re-entrenando o re-descargando).

> **Regla de oro**: si es pesado y se puede volver a generar → NO va al repo (va al `.gitignore`).
> Otros típicos: `__pycache__/`, `.venv/`, `*.log`, datasets grandes, `node_modules/`.

Ejemplo mínimo de `.gitignore` para IA:
```gitignore
.venv/
__pycache__/
*.pt
*.pth
*.safetensors
data/raw/
```

---

## 5. Leer el historial

```bash
git log --oneline   # historial compacto, un commit por línea (hash + mensaje)
```
Sirve para entender la evolución del proyecto. Para este curso NO se necesitan `rebase`, `cherry-pick` ni `submodules`.

---

## 6. Git vs GitHub (no confundir)

| | Qué es |
|---|---|
| **Git** | La **herramienta** de control de versiones (corre en tu máquina). Funciona con cualquier remoto. |
| **GitHub** | Una **plataforma en internet** que aloja repos remotos (alternativas: GitLab, BitBucket). |

---

## 7. Comandos esenciales para el curso

| Comando | Cuándo |
|---|---|
| `git clone <url>` | Traer un repo |
| `git add` + `git commit -m "..."` | Guardar trabajo (local) |
| `git push` | Respaldar en el remoto |
| `git checkout -b` / `git switch -c` | Probar algo sin romper `main` |
| `git log --oneline` | Ver qué se hizo |
| `git status` | Ver qué cambió / qué está en staging |

---

## 8. Glosario inglés → español

| Inglés | Español |
|---|---|
| version control | control de versiones |
| repository (repo) | repositorio |
| commit | snapshot/versión guardada |
| staging area | área de preparación |
| branch | rama |
| merge | fusionar |
| remote | remoto |
| to push / pull / fetch | subir / traer+fusionar / traer |
| pointer | puntero |
| working directory | directorio de trabajo |
| checkpoint files | archivos de pesos de modelos |

---

## Estado
✅ **Entendida por evaluación (5/6).** Dominaba el flujo diario, ramas y git vs GitHub.
Correcciones aplicadas: concepto repo local↔remoto, `origin` como alias. Gap cubierto: extensiones de modelos en `.gitignore`. Conocimiento extra propio: `switch`/`restore`.

## Links
- [[fase00-leccion01-dev-environment]] (anterior)
- [[fase00-leccion03-gpu-setup-and-cloud]] (próxima)
- Relacionado: futuros proyectos a subir a GitHub (ver `CV/certificaciones-y-proyectos.md`)
