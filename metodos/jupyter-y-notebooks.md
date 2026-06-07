---
tags: [tipo/apunte, tema/jupyter, tema/herramientas, tema/data-science]
fecha: 2026-05-11
estado: en-progreso
---

# Jupyter y Notebooks — la herramienta del oficio

## Qué es

> Un **notebook** es un documento interactivo que mezcla, en celdas, **código ejecutable + texto explicativo en Markdown + visualizaciones + resultados**. Se ejecuta celda por celda, no de arriba a abajo como un script.
>
> **Jupyter Notebook** y **Jupyter Lab** son las apps que te dejan abrir y editar archivos `.ipynb` localmente. **Google Colab** es la versión en la nube de Google (gratis, con GPU disponible).

## Por qué importa

Esto NO es "un editor para escribir código en web". Es la herramienta de trabajo cotidiana de cualquier Data Scientist, ML Engineer o investigador. Y por una razón muy concreta:

**El trabajo con datos es exploratorio, no lineal.** No sabés qué vas a encontrar hasta que lo mirás. Necesitás:
- Cargar un dataset → mirarlo → "uy, hay nulls" → limpiarlos → mirar otra vez → graficar → "uy, hay un outlier" → entenderlo → reentrenar.

Cada uno de esos pasos es una celda. Modificás UNA celda y la re-ejecutás sin reiniciar todo. En un script `.py` clásico tendrías que correr todo desde cero cada vez.

Pero ojo: los notebooks NO son para escribir software de producción. Son para **explorar, prototipar y comunicar**.

---

## Diferencia conceptual: notebook vs script

| | Script `.py` | Notebook `.ipynb` |
|---|---|---|
| Forma de correr | De arriba a abajo, todo de una | Celda por celda, en cualquier orden |
| Estado | Se pierde al terminar | Persiste mientras el kernel viva |
| Output | En consola | Inline, debajo de cada celda (incluye gráficos, tablas, imágenes) |
| Texto explicativo | Comentarios `#` | Celdas Markdown formateadas |
| Para qué | Software, scripts, APIs | Exploración, análisis, enseñanza, reporting |
| Versionado en Git | Limpio | Sucio (los outputs se guardan como JSON, hace diffs ilegibles) |

---

## Anatomía de un notebook

### Tipos de celda

1. **Celda de código** — código Python (o R, Julia, según el kernel) que se ejecuta con `Shift+Enter`. El resultado aparece debajo.
2. **Celda Markdown** — texto formateado: títulos, listas, links, ecuaciones LaTeX, imágenes. No se "ejecuta", se "renderiza" con `Shift+Enter`.

### El kernel

El **kernel** es el proceso de Python (o el lenguaje que sea) que mantiene el estado: variables, imports, funciones definidas. Si reiniciás el kernel, perdés todo.

> **El gotcha más típico de notebook:** ejecutás celdas en desorden, redefinís variables, y terminás con un estado que es imposible de reproducir desde cero. Regla de oro: antes de terminar una sesión, "Restart Kernel & Run All". Si no corre limpio de arriba a abajo, el notebook está roto.

---

## Cuándo usar Jupyter Local vs Google Colab

### Jupyter local
- ✅ Trabajás con datos privados / sensibles.
- ✅ Querés guardar el notebook en tu repo Git local.
- ✅ Ya tenés Python y el setup configurado.
- ❌ No tenés GPU.
- ❌ Setup inicial (instalar, lanzar el server).

### Google Colab
- ✅ Cero setup, abrís y funciona.
- ✅ GPU/TPU gratis (con límites) para entrenar modelos.
- ✅ Compartir es trivial (link).
- ✅ Excelente para enseñar / aprender.
- ❌ No es ideal para datos sensibles (suben a Google).
- ❌ Sesiones se cortan después de inactividad.

**Para empezar a aprender ML, Colab es perfecto.** Cuando ya tengas proyecto serio, Jupyter local + venv.

---

## Setup local mínimo

```bash
# Dentro de un venv activado
pip install jupyter

# Lanzar Jupyter (abre el navegador)
jupyter notebook

# o la versión moderna:
pip install jupyterlab
jupyter lab
```

Abrí, creá nuevo notebook, elegí kernel Python 3.

---

## Atajos imprescindibles

| Atajo | Qué hace |
|---|---|
| `Shift + Enter` | Ejecutar celda actual y pasar a la siguiente |
| `Ctrl + Enter` | Ejecutar celda actual y quedarse |
| `Alt + Enter` | Ejecutar y crear celda nueva debajo |
| `Esc` | Salir del modo edición de la celda |
| `A` (en modo comando) | Insertar celda **A**rriba |
| `B` (en modo comando) | Insertar celda a**B**ajo |
| `M` (en modo comando) | Convertir celda a **M**arkdown |
| `Y` (en modo comando) | Convertir celda a código (P**Y**thon) |
| `D, D` (en modo comando) | Borrar celda |

> "Modo comando" = celda seleccionada pero NO en edición (presionás `Esc` para salir).

---

## Qué viste vos vs qué es realmente

> Tu respuesta en la autoevaluación fue: *"Colab para escribir código en web"*. Esa es la respuesta de alguien que abrió Colab para ejecutar un fragmento que le pasaron, sin entender la herramienta.
>
> En realidad Colab es donde se hace casi todo el aprendizaje y prototipado de ML hoy. Si entrás a Data Science o ML Engineering, vas a vivir adentro de notebooks. Por eso esto NO es opcional en tu plan.

---

## Estructura típica de un notebook bien hecho

```
1. Celda Markdown — Título y descripción del análisis
2. Celda código — Imports
3. Celda código — Carga del dataset
4. Celda Markdown — "Exploración inicial"
5. Celda código — head(), info(), describe()
6. Celda Markdown — "Limpieza"
7. Celda código — manejo de nulls, tipos
8. Celda Markdown — "Visualización"
9. Celda código — gráficos
10. Celda Markdown — "Conclusiones"
```

Un notebook leíble cuenta una historia. Si solo son celdas de código sin contexto, es código suelto, no un análisis.

---

## Errores comunes / gotchas

- **Ejecutar celdas en desorden.** Genera estado irreproducible. Antes de cerrar: Restart & Run All.
- **Subir notebooks con outputs grandes a Git.** Los outputs (especialmente imágenes) inflan el archivo y hacen diffs ilegibles. Configurá tu IDE para limpiar outputs antes de commitear, o usá `nbstripout`.
- **Notebooks como "software de producción".** No. Si tu modelo va a correr en producción, sale del notebook y se vuelve script o paquete.
- **Pensar que Jupyter es Python.** Jupyter es un editor. Python es el lenguaje. Podés tener kernels de R, Julia, Scala. Lo común es Python.

## Notas relacionadas

- [[../python/apuntes/venv-vs-env]] — instalá Jupyter dentro de un venv del proyecto, NO global
- [[conceptos-git]] — los `.ipynb_checkpoints/` van al `.gitignore`
- [[markdown-y-obsidian]] — Markdown que aprendiste para Obsidian funciona en celdas Markdown de Jupyter

## Fuentes

- Project Jupyter: https://jupyter.org
- Google Colab: https://colab.research.google.com
- Real Python — Jupyter Notebook: https://realpython.com/jupyter-notebook-introduction/
