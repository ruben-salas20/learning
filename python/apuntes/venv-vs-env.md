---
tags: [tipo/apunte, tema/python, tema/herramientas]
fecha: 2026-05-11
estado: en-progreso
---

# `venv` vs `.env` — NO son lo mismo

## Qué es

> Dos cosas completamente distintas que se confunden mucho porque suenan parecido y aparecen juntas en proyectos generados por IA.
>
> - **`venv`** → un **entorno virtual** de Python. Aísla las dependencias de un proyecto.
> - **`.env`** → un **archivo de texto** con variables de entorno (típicamente secretos: API keys, contraseñas).

## Por qué importa

Si no usás `venv`, todas las librerías que instalás se mezclan en tu Python global. Eso significa:
- Proyecto A necesita `pandas==1.5`, proyecto B necesita `pandas==2.1` → conflicto, uno se rompe.
- Cuando alguien clone tu repo, NO puede reproducir tu entorno.
- Tu Python global termina con 200 librerías chocando entre sí, imposible de mantener.

Si no usás `.env` para secretos, los hardcodés en el código y los subís a GitHub. **Resultado clásico:** tu API key de OpenAI queda pública, alguien la encuentra con un scraper en 2 horas, te gastan USD 5.000 antes del lunes.

---

## `venv` — entorno virtual

### Qué hace

Crea una carpeta (típicamente llamada `.venv/`) que contiene:
- Una copia de Python.
- Un directorio donde se instalan las librerías SOLO de ese proyecto.

Cuando lo "activás", el `python` y `pip` que se ejecutan apuntan a esa copia local, no a la global.

### Cómo se usa

```bash
# 1. Crear el venv (una vez por proyecto)
python -m venv .venv

# 2. Activarlo
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

# 3. Ahora todo lo que instales con pip queda DENTRO del proyecto
pip install pandas

# 4. Guardar las dependencias para que otros las repliquen
pip freeze > requirements.txt

# 5. Desactivarlo cuando termines
deactivate
```

### Cómo sabés que está activo

El prompt te lo muestra:

```
(.venv) PS D:\Mis Archivos\proyecto> _
```

Ese `(.venv)` al principio = activado.

### Regla de oro

`.venv/` **nunca** va a Git. Agregalo siempre al `.gitignore`:

```
.venv/
```

Lo que SÍ subís es `requirements.txt` — la lista de dependencias. El que clone tu repo recrea el venv:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## `.env` — variables de entorno

### Qué hace

Es un **archivo de texto plano** donde guardás valores que NO deben ir en el código:

```
# .env
OPENAI_API_KEY=sk-proj-abc123...
DATABASE_URL=postgres://user:pass@host:5432/mydb
DEBUG=True
```

### Cómo se usa en Python

Necesitás una librería para leerlo, típicamente `python-dotenv`:

```bash
pip install python-dotenv
```

```python
import os
from dotenv import load_dotenv

load_dotenv()  # lee el .env y carga las variables al entorno

api_key = os.getenv("OPENAI_API_KEY")
db_url = os.getenv("DATABASE_URL")
```

### Regla de oro

`.env` **nunca** va a Git. Agregalo al `.gitignore`:

```
.env
```

Lo que SÍ subís es un `.env.example` con las claves vacías o falsas, para que otro sepa qué variables necesita configurar:

```
# .env.example
OPENAI_API_KEY=
DATABASE_URL=
DEBUG=
```

---

## Comparación rápida

| | `venv` | `.env` |
|---|---|---|
| ¿Qué es? | Carpeta con Python aislado | Archivo de texto con variables |
| ¿Para qué? | Aislar dependencias del proyecto | Guardar secretos / config |
| ¿Va a Git? | ❌ No (`.venv/` en `.gitignore`) | ❌ No (`.env` en `.gitignore`) |
| ¿Qué SÍ va a Git? | `requirements.txt` | `.env.example` |
| ¿Lo activás? | ✅ Sí, con `Activate.ps1` o `source` | ❌ No, lo lee tu código |

## Errores comunes / gotchas

- **Subir `.venv/` a GitHub.** Pesa cientos de MB y no sirve a nadie. Si te pasó, agregalo al `.gitignore` y borralo del repo.
- **Subir `.env` a GitHub.** Si te pasó, considerá las claves COMPROMETIDAS — rotalas inmediatamente, no solo borres el commit.
- **No activar el venv y pensar que sí.** Mirá el prompt: si no aparece `(.venv)`, no está activo.
- **En Windows PowerShell, error de "no se puede ejecutar scripts":** ejecutás una vez `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` y listo.

## Notas relacionadas

- [[../README]] — índice de Python
- [[../../metodos/conceptos-git]] — `.gitignore` y por qué importa

## Fuentes

- Python docs — venv: https://docs.python.org/3/library/venv.html
- python-dotenv: https://pypi.org/project/python-dotenv/
