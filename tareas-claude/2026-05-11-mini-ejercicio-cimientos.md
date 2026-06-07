---
tags: [tipo/tarea, tema/python, tema/git, tema/jupyter]
fecha-asignada: 2026-05-11
estado: pendiente
---
# Tarea — Mini-ejercicio Cimientos (Bloque 1)

> **Estado:** 🟡 Pendiente

---

## 🎯 Objetivo

Solidificar las 5 correcciones del Bloque 1 con **práctica real**, no solo lectura. Al final tenés que tener un repo público en GitHub que demuestre que entendiste:

1. Mutabilidad (lista vs tupla)
2. `venv` vs `.env`
3. `==` vs `is`
4. Git con branches reales y un PR
5. Jupyter como herramienta de exploración

## 🧭 Por qué esta tarea

Leer las notas no garantiza que entendiste. Lo único que lo demuestra es **hacer las cosas con tus manos** y darte cuenta dónde te trabás. Esta tarea es chica deliberadamente — todo en 3-4 horas. Lo importante no es el código, es el **proceso completo**: crear repo, venv, branch, commit, PR, merge.

## 📚 Pre-requisitos

- [ ] Leer [[../python/apuntes/mutabilidad-listas-tuplas]]
- [ ] Leer [[../python/apuntes/venv-vs-env]]
- [ ] Leer [[../python/apuntes/igualdad-vs-identidad]]
- [ ] Leer [[../python/apuntes/decoradores-intro]]
- [ ] Leer [[../metodos/conceptos-git]]
- [ ] Leer [[../metodos/jupyter-y-notebooks]]

## 🛠️ Pasos

### Parte 1 — Setup del repo (≈ 30 min)

- [ ] Crear repo nuevo en GitHub: `cimientos-python`. Público. Sin README, sin .gitignore (los hacés vos).
- [ ] Clonarlo en tu máquina dentro de `D:\Mis Archivos\Documentos\Learning\` o donde tengas los proyectos.
- [ ] Crear y activar `venv`:
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
  Verificá: el prompt debe mostrar `(.venv)` al inicio.
- [ ] Crear `.gitignore` que ignore al menos: `.venv/`, `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/`, `.env`.
- [ ] Crear `README.md` inicial con: título del repo + descripción de 2 líneas (qué es y por qué lo creaste).
- [ ] **Primer commit en `main`**:
  ```powershell
  git add .gitignore README.md
  git commit -m "chore: setup inicial del repo"
  git push origin main
  ```

> ✅ Checkpoint: andá a GitHub. Verificá que NO está la carpeta `.venv/`. Si está, fallaste el `.gitignore`.

### Parte 2 — Branch + ejercicios de Python (≈ 60 min)

- [ ] Crear branch:
  ```powershell
  git switch -c feat/ejercicios-cimientos
  ```
- [ ] Crear archivo `ejercicios/mutabilidad.py` con:
  - Una lista que modificás (`append`, `pop`, asignación por índice).
  - Una tupla con la que intentás hacer `append` y atrapás el error con `try/except`.
  - Una tupla usada como clave de diccionario (mostrá que funciona).
  - Una lista usada como clave de diccionario (mostrá el `TypeError`, atrapado).
- [ ] Crear archivo `ejercicios/identidad.py` con:
  - Comparación de dos listas con `==` y con `is` (resultados distintos).
  - Asignación `c = a` y mostrar que `a is c`.
  - Comparación con `None` usando `is` (forma idiomática).
  - El gotcha de enteros chicos (100 vs 1000).
- [ ] Cada archivo debe correr con `python ejercicios/mutabilidad.py` y mostrar prints claros.
- [ ] Commitear:
  ```powershell
  git add ejercicios/
  git commit -m "feat: ejercicios de mutabilidad e identidad"
  git push -u origin feat/ejercicios-cimientos
  ```

### Parte 3 — Pull Request y merge (≈ 15 min)

- [ ] En GitHub, abrir Pull Request desde `feat/ejercicios-cimientos` hacia `main`.
- [ ] Título: `feat: ejercicios de cimientos (mutabilidad + identidad)`.
- [ ] Body: 3-5 líneas explicando qué hicieron los ejercicios y qué aprendiste vos al hacerlos.
- [ ] Mergear el PR.
- [ ] Volver a tu local:
  ```powershell
  git switch main
  git pull
  git branch -d feat/ejercicios-cimientos
  ```

### Parte 4 — Notebook Jupyter (≈ 60 min)

- [ ] Instalar Jupyter en el venv:
  ```powershell
  pip install jupyter
  pip freeze > requirements.txt
  ```
- [ ] Crear nueva branch: `git switch -c feat/notebook-exploracion`
- [ ] Lanzar Jupyter: `jupyter notebook` (se abre en navegador).
- [ ] Crear `notebooks/exploracion.ipynb` con la siguiente estructura mínima:
  - **Celda Markdown**: título "Exploración Cimientos" + qué vas a mostrar.
  - **Celda código**: definir una lista, una tupla, mostrar `id()` de cada una.
  - **Celda Markdown**: explicación de qué muestra la celda anterior (con tus palabras).
  - **Celda código**: ejemplo de `==` vs `is`.
  - **Celda Markdown**: tu interpretación.
  - **Celda código**: definir un decorador simple (`@loguear`) y aplicarlo a una función `sumar`.
  - **Celda Markdown**: cierre con qué te quedó claro y qué todavía no.
- [ ] Antes de guardar: **Restart Kernel & Run All**. Si no corre limpio de cabo a rabo, arreglá las dependencias entre celdas.
- [ ] Commitear:
  ```powershell
  git add notebooks/ requirements.txt
  git commit -m "feat: notebook de exploración con conceptos del bloque 1"
  git push -u origin feat/notebook-exploracion
  ```
- [ ] PR + merge igual que antes.

### Parte 5 — Cierre

- [ ] Actualizar el `README.md` del repo con:
  - Estructura del repo (árbol de carpetas).
  - Cómo correrlo (crear venv, instalar requirements, etc.).
  - Sección "Lo que aprendí" con tus reflexiones (escrita por vos, NO con IA).
- [ ] Commit final directo en main: `docs: README completo`.

## 📦 Qué entregar

- [ ] Link al repo público en GitHub.
- [ ] Confirmación de que `.venv/` NO está en el repo.
- [ ] Lista de cosas con las que te trabaste y cómo las resolviste (1 mensaje en nuestra próxima conversación).

## ✅ Criterios de "hecho"

- [ ] Repo público accesible.
- [ ] `.venv/` y `.env` NO subidos al repo.
- [ ] `requirements.txt` presente con `jupyter`.
- [ ] Al menos **2 PRs creados y mergeados** desde branches feature (no commits directos a main, salvo el setup inicial y el README final).
- [ ] Notebook abre y corre limpio con Restart & Run All.
- [ ] Sección "Lo que aprendí" en el README escrita por vos, sin IA. Mínimo 5 frases.

## ⏱️ Tiempo estimado

- 3 a 4 horas en total, distribuido como vos quieras (puede ser 1 sesión o varias).

## ⚠️ Reglas

1. **Cero código generado por IA en esta tarea.** Buscar en Google y en docs SÍ. Copiar código de IA NO. Esta tarea es para que TUS manos escriban cada línea.
2. Si te trabás más de 30 min en algo, **anotá** el problema (qué intentaste, qué pasó) y traelo a la próxima conversación. No abandones, no copies — anotá.
3. Si necesitás explicación adicional sobre alguno de los conceptos, releé las notas en `python/apuntes/` y `metodos/`. La respuesta probablemente está ahí.

---

## Notas durante la ejecución

(este espacio es tuyo — anotá errores, dudas, descubrimientos a medida que vas haciéndolo)
