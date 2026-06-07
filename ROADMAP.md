---
tags: [tipo/plan, tema/aprendizaje, tema/datacamp]
fecha: 2026-05-10
estado: activo
---

# Roadmap de aprendizaje — 6 meses (Mayo–Octubre 2026)

> Plan de uso del beneficio de Datacamp (6 meses gratis vía GitHub Student) combinado con Anthropic Academy y trabajo sobre repos existentes (especialmente `vaecos-tracking`).

---

## 🎯 Objetivo general

Construir las **bases comunes** para los 3 caminos posibles (AI Engineer, Data Scientist, ML Researcher) Y, en paralelo, **convertir los proyectos vibecoded existentes en código entendido y propio**.

> **Insight clave:** ya tienes proyectos serios en GitHub. No hay que pensar nuevos. Hay que cerrar el gap entre "lo que está publicado" y "lo que sé explicar/modificar yo mismo".

---

## 📌 Reglas del juego

1. **Datacamp ≠ aprendizaje real.** Por cada hora de curso → al menos 30min de aplicación sobre `vaecos-tracking` u otro repo propio.
2. **Máximo 1-2 cursos activos a la vez.** Saltar dispersa.
3. **Documentar es parte del trabajo.** Cada bloque cierra con apuntes en `tema/apuntes/`.
4. **Si un mes se cae**, se corre el siguiente. La presión rompe el sistema.
5. **Cursos NO necesarios para ti** (los marcamos para saltar): "Introduction to Python", "Intermediate Python", "Introduction to Functions" → ya manejas POO, clases, excepciones. Estos te aburrirían.

---

## 🗓️ Plan mensual con cursos específicos

### **Mes 1 — Mayo 2026** · Python profesional (~14h Datacamp)

Lo que te falta NO es Python básico — es Python "de producción".

| Curso | Horas | Por qué |
|---|---|---|
| Writing Functions in Python | 3h | Cierres, decoradores, *args/**kwargs — lo verás en TODO el código vibecoded |
| Writing Efficient Python Code | 4h | List comprehensions avanzadas, generadores, profiling |
| Software Engineering Principles in Python | 3h | Estructura de proyectos, packaging — clave para entender vaecos-tracking |
| Unit Testing for Data Science in Python | 3h | `pytest`, fixtures — saltó al producto real |
| Object-Oriented Programming in Python | 4h (opcional) | Si quieres reforzar lo que ya haces, herencia, ABC |

**Aplicación:** abrir `vaecos-tracking/v0.2/` y leer el código del rules engine. Identificar 3 funciones y reescribir UNA tú mismo desde cero, sin IA, comparando después.

**Conflicto Mayo:** Anthropic Academy Etapa 1 (cierre antes de junio). Distribuir tiempo.

---

### **Mes 2 — Junio 2026** · SQL + Pandas (~14h Datacamp)

| Curso | Horas | Por qué |
|---|---|---|
| Introduction to SQL | 2h | Sintaxis base |
| Intermediate SQL | 4h | JOIN, subqueries, agregaciones |
| Data Manipulation with pandas | 4h | DataFrames, filtros, groupby |
| Joining Data with pandas | 4h | Merge, concat, reshape |

**Aplicación:** la base SQLite de `vaecos-tracking` tiene tablas `rules`, `rule_history`, corridas, tracking. Escribir queries en SQL puro contra ella y luego replicar las mismas en pandas leyendo el `.db`. Análisis real, sin IA.

**Anthropic Academy:** Etapa 2 (MCP, Agent Skills) arranca aquí.

---

### **Mes 3 — Julio 2026** · LLMs aplicados (~17h Datacamp)

| Curso | Horas | Por qué |
|---|---|---|
| Working with the OpenAI API | 3h | API básica (sirve igual para Claude API mentalmente) |
| Prompt Engineering with the OpenAI API | 3h | Estructurado, no hacks |
| Introduction to Embeddings with the OpenAI API | 3h | Concepto matemático + uso |
| Developing LLM Applications with LangChain | 4h | Chains, agents, parsers |
| Retrieval Augmented Generation (RAG) with LangChain | 3h | RAG end-to-end |

**Aplicación:** mini-RAG sobre los datos de `vaecos-tracking` — "preguntale al historial de corridas cosas en lenguaje natural". Esto se convierte en un feature real de la plataforma, no un ejercicio aislado.

**Anthropic Academy:** Etapa 2 continúa. Sinergia altísima — lo de Datacamp aterriza acá.

---

### **Mes 4 — Agosto 2026** · Estadística práctica (~10h Datacamp)

Tu ventaja: ya pasaste por esto en Economía. Esto es REPASO, no aprendizaje. Velocidad alta esperada.

| Curso | Horas | Por qué |
|---|---|---|
| Introduction to Statistics in Python | 4h | Refrescar con sintaxis Python (scipy.stats) |
| Hypothesis Testing in Python | 3h | Tests, p-values aplicados |
| Sampling in Python | 3h | Bootstrap, intervalos, métodos modernos |

**Aplicación:** análisis estadístico real sobre `vaecos-tracking` — ¿hay diferencia significativa de tiempos de entrega entre transportistas? ¿Qué clientes son outliers reales vs ruido?

---

### **Mes 5 — Septiembre 2026** · Machine Learning fundamentals (~15h Datacamp)

| Curso | Horas | Por qué |
|---|---|---|
| Supervised Learning with scikit-learn | 4h | Base de todo ML clásico |
| Unsupervised Learning in Python | 4h | Clustering, PCA |
| Machine Learning with Tree-Based Models in Python | 4h | Random Forest, Gradient Boosting (top en producción) |
| LLMOps Concepts | 3h | Cierra el ciclo entre ML clásico y LLM |

**Punto de decisión:** a fin de este mes deberías sentir si te llama más el lado *modelos clásicos* (DS/ML) o el lado *sistemas con LLMs* (AI Eng) o el lado *teoría profunda* (Research). La intuición ya debería estar formada.

**Aplicación:** modelo predictivo sobre `vaecos-tracking` — predecir qué corridas requerirán intervención manual basándose en datos históricos. Output medible.

---

### **Mes 6 — Octubre 2026** · Proyecto integrador (CERO cursos nuevos)

Construir. Elegir UN proyecto a profundidad — el camino se elige en este mes.

- 🧱 **Si te encendió AI Eng**: agente con MCP que opere sobre `vaecos-tracking` y permita conversación natural con el sistema.
- 🔬 **Si te encendió Research**: replicar un paper sencillo (sugerencia: algo de Papers with Code, nivel "implementación didáctica") y publicar un notebook explicativo.
- 📊 **Si te encendió Data Science**: análisis profundo de datos de VAECOS con modelo predictivo, dashboard, e informe ejecutivo para tu familia.

**Cursos extra opcionales solo si el proyecto los pide:**
- *Designing Agentic Systems with LangChain* (camino AI Eng)
- *Vector Databases for Embeddings with Pinecone* (camino AI Eng)

---

## 📊 Resumen total

| Mes | Cursos | Horas Datacamp | Aplicación principal |
|---|---|---|---|
| Mayo | 4-5 | ~14-18h | Entender código de vaecos-tracking |
| Junio | 4 | ~14h | Queries reales sobre BD de vaecos-tracking |
| Julio | 5 | ~16h | Mini-RAG sobre vaecos-tracking |
| Agosto | 3 | ~10h | Análisis estadístico sobre vaecos-tracking |
| Septiembre | 4 | ~15h | Modelo predictivo sobre vaecos-tracking |
| Octubre | 0 | 0h | Proyecto integrador |
| **Total** | **~20-21** | **~70-75h** | — |

> **70-75h en 6 meses = ~3h/semana de curso puro.** Con aplicación práctica (2x) son ~6h/semana. Cabe en tu disponibilidad realista.

---

## 🛠️ Repos como laboratorio (no construir desde cero)

Tu GitHub ya tiene material — úsalo:

| Repo | Para qué sirve en el plan |
|---|---|
| **vaecos-tracking** | Laboratorio principal. SQL, pandas, RAG, estadística, ML — todo se aplica acá. |
| **traductor-pantalla** | Material para entender OCR, multiprocessing en Python. Tema avanzado para más adelante. |
| **agents-ai** | Material para entender estructura de un paquete npm + TypeScript, cuando llegue el momento. |
| **educagent** | Tu visión pedagógica está documentada. Cuando llegues a AI Eng + RAG, este es el siguiente proyecto natural. |
| **study-timer** | Si te interesa el stack web moderno (React/TS), acá ya tienes uno. |

---

## ✋ Cuándo replanear

- Si en mes 2 SQL te aburre profundamente → revisar ruta DS.
- Si en mes 3 los LLMs te encienden mucho más que cualquier otra cosa → considerar dedicar más al camino AI Eng en los meses 4-5.
- Si en mes 4-5 la matemática te apasiona en serio → la ruta ML Researcher se vuelve más realista.

---

*Plan vivo. Se revisa al cierre de cada mes en sesión corta de retro.*
