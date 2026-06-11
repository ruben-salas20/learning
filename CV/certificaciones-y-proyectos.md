---
tags: [tipo/cv, tema/python, estado/activo]
fecha-creacion: 2026-06-08
proposito: Insumo para armar hoja de vida y portfolio. Logros + proyectos con evidencia.
---
# CV — Certificaciones y Proyectos

> Banco de material para mi hoja de vida y portfolio. Cada entrada describe QUÉ hice,
> QUÉ demuestra (habilidades), y DÓNDE está la evidencia. Pensado para copiar/adaptar
> a LinkedIn, CV y portfolio cuando los rearme.

---

## 🎓 Certificaciones

### Associate Python Developer — DataCamp
- **Fecha**: 2026-06 · **Evidencia**: `python/ruta-associate-python-developer/certificate.pdf`
- **Qué valida**: dominio práctico de Python para desarrollo y manejo de datos. Incluye
  examen práctico cronometrado (resolver un problema con código propio, no teoría).
- **Temas cubiertos en la ruta**: manipulación de cadenas (strings), expresiones regulares
  (regex), funciones y docstrings, manejo de errores (try/except, excepciones), módulo
  `datetime`, estructuras de datos, control de flujo.
- **Apuntes propios de la ruta**: `python/ruta-associate-python-developer/cursos/`
  (ej. `regular-expresions-in-python.md`).

---

## 🛠️ Proyectos

### 1. User Registration System — Validación y manejo de errores
- **Carpeta**: `python/ruta-associate-python-developer/practicas/Project Creating Functions to Register App Users/`
- **Contexto**: sistema de registro de usuarios para una app móvil; valida nombre, email y
  contraseña antes de crear la cuenta.
- **Qué construí**: las funciones `validate_user()` y `register_user()`, integrando funciones
  auxiliares de validación (`validate_name`, `validate_email`, `validate_password`).
- **Habilidades demostradas**:
  - Diseño de funciones que componen otras funciones.
  - Manejo de errores con `raise ValueError` + `try/except`.
  - Validación de entrada (longitud, formato de email, fortaleza de contraseña).
  - Lectura y uso de docstrings de código ajeno (entender antes de usar).
- **Bullet para CV (ES)**: "Desarrollé un sistema de validación y registro de usuarios en
  Python aplicando composición de funciones y manejo de excepciones."
- **Bullet for resume (EN)**: "Built a Python user-registration system with input validation
  and exception handling, composing helper functions for name/email/password checks."

### 2. Interstellar Delivery — Mastering Datetime in Python
- **Carpeta**: `python/ruta-associate-python-developer/practicas/Project Interstellar Delivery Mastering Datetime in Python/`
- **Contexto**: software de logística para una empresa ficticia de entregas con cohetes;
  funciones reutilizables para fechas, horas y duraciones.
- **Qué construí**: `format_date()`, `calculate_landing_time()` y `days_until_delivery()`
  usando el módulo `datetime` (`datetime`, `timedelta`, `fromtimestamp`, `strftime`).
- **Habilidades demostradas**:
  - Manejo de fechas/horas: timestamps, formateo, aritmética de fechas con `timedelta`.
  - Diseño de funciones puras y reutilizables.
- **Bullet para CV (ES)**: "Implementé funciones reutilizables de manejo de fechas y duraciones
  en Python con el módulo datetime (timestamps, formateo y aritmética de fechas)."
- **Bullet for resume (EN)**: "Implemented reusable date/time utilities in Python with the
  datetime module — timestamp formatting, landing-time computation, and deadline countdowns."

---

## 🧰 Inventario de habilidades demostradas (Python)
Strings · regex · funciones & docstrings · manejo de errores (try/except, raise) ·
módulo datetime · control de flujo · validación de entrada · composición de funciones.

---

## Pendientes para fortalecer el portfolio
- [ ] Refactor del Proyecto 1 (guard clauses / quitar `== True`) como ejercicio de calidad de código.
- [ ] Subir proyectos a GitHub con README propio cada uno.
- [ ] Conectar estos fundamentos con los Build It del curso AI Engineering from Scratch.

## Links
- Bitácora del curso de IA: `cursos/ai-engineering-from-scratch/progreso.md`
- Métodos de aprendizaje: `metodos/`
