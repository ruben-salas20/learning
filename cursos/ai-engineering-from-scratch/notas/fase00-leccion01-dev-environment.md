---
tags: [tipo/apunte, tema/wsl, tema/terminal, tema/setup, proyecto/ai-engineering-from-scratch, estado/completo]
fecha: 2026-05-29
fase: 0 - Setup & Tooling
leccion: 01 - Dev Environment
fuente: phases/00-setup-and-tooling/01-dev-environment
---
# Fase 0 · Lección 1 — Dev Environment (Entorno de desarrollo)

> **Lema de la lección**: *"Your tools shape your thinking. Set them up once, set them up right."*
> (Tus herramientas moldean tu forma de pensar. Configuralas una vez, configuralas bien.)
>
> Destilado en español de todo lo que monté e investigué. Términos clave en inglés a propósito (vocabulario que se repite en todo el mundo de la IA).

---

## 1. El concepto madre: el stack de 4 capas

Un entorno de AI engineering se construye **de abajo hacia arriba**. Cada capa se apoya en la de abajo.

```
┌─────────────────────────────────────────────┐
│ 4. AI/ML Libraries  → PyTorch, NumPy, etc.    │
├─────────────────────────────────────────────┤
│ 3. Language Runtimes → Python, Node, Rust...  │
├─────────────────────────────────────────────┤
│ 2. Package Managers  → uv, pnpm, cargo        │
├─────────────────────────────────────────────┤
│ 1. System Foundation → SO, shell, git, GPU    │
└─────────────────────────────────────────────┘
```

**Analogía de obra**: es una casa. Cimientos (sistema) → paredes (runtimes) → muebles (librerías). No podés poner muebles sin paredes. Si los cimientos están mal, todo se cae.

---

## 2. WSL2 — Linux real dentro de Windows

Elegí **WSL2 + Ubuntu 24.04** sobre Windows nativo. Razón: es el estándar de la industria IA (el 95% de tutoriales/herramientas asumen Linux) y de paso practico Linux/Terminal, que es objetivo mío.

> WSL2 NO es un emulador ni una VM pesada. Es un **kernel de Linux real** integrado a Windows, liviano. Como un apartamento independiente dentro de tu casa.

### 2.1 El concepto que más confunde: WSL tiene DOS sistemas de archivos

| Ruta | Qué es | Velocidad |
|---|---|---|
| `~` = `/home/ruben` | disco "de Ubuntu" (Linux nativo) | **RÁPIDO** |
| `/mnt/d`, `/mnt/c` | mis discos de Windows vistos desde Linux | **LENTO desde WSL** |

Mi carpeta `D:\...\Learning` se ve desde Ubuntu como `/mnt/d/Mis Archivos/Documentos/Learning`.

**Gotcha #1 de WSL**: los entornos virtuales (miles de archivos chicos) y el código pesado deben vivir en Linux nativo (`~`), NO en `/mnt/d`, porque cada archivo cruza la frontera Windows↔Linux y eso es lento.

**Mi flujo decidido** (3 lugares):
- Código activo → `~/ai-eng/` (rápido)
- Ejercicios terminados que valen → copiar a `.../Learning/.../ejercicios-mios/` (queda en git)
- Apuntes en español → `.../Learning/.../notas/`

### 2.2 Gotcha #2: WSL2 se come media RAM

WSL2 por defecto reserva **el 50% de la RAM física** (en mi equipo de 16GB → 8GB). El proceso `vmmem` en Windows lo retiene, y deja Windows lento.

**Diagnóstico real**: dentro de WSL, `free -h` mostraba `used: 551Mi` (Linux usaba casi nada) pero `total: 7.7Gi` (WSL solo ve la mitad). El problema NO era adentro, era la reserva del lado Windows.

**Solución**: archivo `C:\Users\ruben\.wslconfig` (en el home de WINDOWS, no en WSL):
```ini
[wsl2]
memory=6GB
swap=4GB
[experimental]
autoMemoryReclaim=gradual
```
Aplicar con `wsl --shutdown` en PowerShell + reabrir Ubuntu. Resultado: WSL domado a 6GB, Windows fluido.

> **Concepto clave de RAM en Linux**: "used" real ≠ lo que Windows ve ocupado. `buff/cache` es caché reclaimable (liberable al instante). Hay que mirar la columna `available`, no el % de Windows.

---

## 3. Entornos virtuales (venv) y la separación de capas

### El problema que resuelven
Proyecto A necesita NumPy 1.24, Proyecto B necesita NumPy 2.0. Globalmente NO podés tener las dos. Eso es el *dependency hell* (infierno de dependencias).

### La solución
Un **virtual environment (venv)** es una caja aislada de Python con SUS propias librerías. Cada proyecto, su caja.
> Analogía: un taller separado por obra. Las herramientas del baño no se mezclan con las de la cocina.

### Regla de oro: ¿dónde instalo cada cosa?
| Tipo | Dónde | Con qué |
|---|---|---|
| Programa del sistema (node, git, rust, unzip) | **fuera** del venv (global) | `apt` o su instalador |
| Librería de Python (numpy, torch, pandas) | **dentro** del venv | `uv pip` |

El venv aísla SOLO paquetes de Python. Por eso instalé Node/Rust/Julia fuera del venv (son globales) y PyTorch dentro (es Python).

---

## 4. El PATH y el orden de carga (el bug que resolví)

El **PATH** es la lista de carpetas donde el sistema busca los programas. Si la carpeta de `node` no está en el PATH, "no existe" aunque esté instalado.
> Analogía: el PATH es la agenda de contactos. Si "node" no está en la agenda, el sistema no lo conoce.

**El bug**: el verify daba 5/7 (no veía node/cargo) aunque estaban instalados. Causa: en la shell donde corrí el verify, node/cargo no estaban en el PATH.

**Las dos causas y el fix**:
1. `fnm use 22` activa node solo por sesión → fix: `fnm default 22` (lo fija para toda terminal nueva).
2. `source ~/.cargo/env` solo afecta esa shell → fix: recargar la shell con `exec bash`.

**El orden correcto** (mi ritual): abrir terminal (carga node/cargo vía `~/.bashrc`) → DESPUÉS activar el venv (se monta encima, conserva todo). Si activo el venv en una shell sin node/cargo cargados, quedan afuera.

---

## 5. GPU en WSL2 (mi RTX 3050)

> **Concepto crítico**: en WSL2 el driver de la GPU vive en **WINDOWS**, NO en Linux. WSL2 toma la GPU prestada automáticamente. **NUNCA instalar el driver NVIDIA dentro de Ubuntu** (eso rompe todo).

`nvidia-smi` confirmó: RTX 3050, 6GB VRAM, driver 596.21, **CUDA Version: 13.2**.

> **Trampa de versiones**: "CUDA Version: 13.2" en nvidia-smi = el MÁXIMO que soporta el driver, NO lo que hay que instalar. PyTorch trae su propio CUDA por dentro; solo necesita un driver igual o superior. Instalé PyTorch con CUDA 12.4 (cu124) → 12.4 ≤ 13.2 → funciona (retrocompatible).

Instalación (dentro del venv): `uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`
Verificación: `torch.cuda.is_available()` → **True** ✅

Realidad de la 3050 (6GB): perfecta para APRENDER (modelos chicos, LoRA, inferencia, redes de Phases 3-5). NO para entrenar modelos grandes (para eso, Colab/cloud).

---

## 6. `uv` — el gestor de Python del curso

`uv` (escrito en Rust, ultrarrápido) hace varios trabajos: instala Python (runtime), instala paquetes, y maneja venvs. El curso lo usa en vez de `pip` por velocidad (10-100x).

```bash
uv venv                          # crea el venv (.venv)
source .venv/bin/activate        # entra al venv → aparece (ai-eng) en el prompt
uv pip install numpy matplotlib jupyter
deactivate                       # sale del venv
```

---

## 7. Comandos y reflejos que aprendí

| Comando | Qué hace |
|---|---|
| `<programa> --version` / `--help` | **reflejo #1**: qué tengo y en qué versión |
| `pwd` | *print working directory* — dónde estoy parado |
| `ls` | listar archivos de la carpeta actual |
| `cd <carpeta>` | entrar a una carpeta |
| `mkdir <nombre>` | crear carpeta |
| `which <programa>` | **diagnóstico**: ¿está en el PATH? ¿dónde? |
| `free -h` | uso de RAM (mirar `available`) |
| `nvidia-smi` | estado de la GPU |
| `sudo apt install -y <paquete>` | instalar programa del sistema |
| `source <archivo>` | recargar config sin cerrar la terminal |
| `exec bash` | reiniciar la shell (relee `~/.bashrc`) |
| `python -c "..."` | correr una línea de Python sin entrar al REPL |

**Patrón ante un error "missing dependency"**: leer QUÉ falta → instalarlo → reintentar. (Ej: fnm falló por `unzip` faltante → `sudo apt install unzip` → reintentar.)

**Manejo de espacios en rutas**: ruta con espacios → encerrarla en comillas `"..."`. (Mejor aún: evitar espacios en nombres de carpetas nuevas.)

---

## 8. Mi ritual de arranque diario del curso

```bash
# 1. Abrir terminal de Ubuntu (carga node/cargo sola)
# 2. Entrar al proyecto y activar el venv:
cd ~/ai-eng && source .venv/bin/activate
# 3. A trabajar (ya tengo Python, GPU, todo listo)
```

---

## 9. Glosario inglés → español

| Inglés | Español |
|---|---|
| dev environment | entorno de desarrollo |
| runtime | entorno de ejecución |
| package manager | gestor de paquetes |
| virtual environment (venv) | entorno virtual |
| dependency | dependencia |
| toolchain | cadena de herramientas |
| build / compiler | compilar / compilador |
| array | arreglo (lista de números) |
| GPU / VRAM | unidad gráfica / memoria de video |
| CUDA | plataforma de NVIDIA para cálculo en GPU |
| driver | controlador |
| PATH | lista de búsqueda de programas |
| cache (reclaimable) | caché (liberable) |

---

## Estado final del entorno

✅ WSL2 + Ubuntu 24.04 · Python 3.12.3 + uv · Node 22 (fnm) · Rust 1.96 · Julia 1.12.6 · PyTorch cu124 + GPU RTX 3050 (`True`) · verify.py **7/7 core** · RAM domada (`.wslconfig` 6GB)

## Links
- [[fase00-leccion02-git-and-collaboration]] (próxima)
- Relacionado: `metodos/como-aprende-una-ai.md`, `metodos/python-a-fondo.md`
