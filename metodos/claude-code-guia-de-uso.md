---
title: Claude Code — Guía de uso
tags:
  - claude-code
  - cli
  - productividad
  - ia
created: 2026-05-30
fuente:
  - "claude --help (instalación local)"
  - "code.claude.com/docs (oficial)"
---

# 🤖 Claude Code — Guía de uso

> [!info] Sobre este documento
> Referencia personal de **Claude Code** (el CLI de Anthropic en la terminal).
> Todo está **verificado** contra `claude --help` de tu instalación y contra la documentación oficial (`code.claude.com/docs`).
> Nace de una necesidad real: dejar de guardar los comandos de "volver a la sesión" en WhatsApp.

> [!tip] Atajo mental
> - **Antes de cada comando** → escribe `/` y mira el autocompletado. Te muestra TODO lo disponible (built-ins, skills, plugins, MCP).
> - **Para ayuda** → `/help`.
> - **Para ver tus shortcuts** → en modo fullscreen, pulsa `?` en el visor de transcripción.

---

## 🧭 El concepto clave primero

> [!important] No guardes el UUID a mano
> El comando feo tipo `claude --resume f1024867-9ecf-462c-94db-cf84819484a2` **NO es algo que debas anotar tú**.
> Claude Code YA guarda todas tus sesiones y te las muestra en un selector. Anotar el UUID es como apuntar la ruta de cada archivo en una libreta teniendo un explorador de archivos.

**¿Dónde se guardan las sesiones?**

```
C:\Users\ruben\.claude\projects\<ruta-del-proyecto-codificada>\<id-sesion>.jsonl
```

Cada archivo guarda automáticamente un **título generado por IA** (`aiTitle`), la carpeta de trabajo (`cwd`), fechas y todos los mensajes. Por eso el selector muestra una lista legible sin que anotes nada.

---

## ⭐ Sesiones: empezar, nombrar, volver

> [!tip] El trío que reemplaza a WhatsApp
> `nombrar` + `selector` + `continuar`. Punto.

### Desde la terminal (al arrancar `claude`)

| Comando | Qué hace |
| --- | --- |
| `claude -r` / `--resume` | Abre el **selector interactivo** de sesiones de **esa carpeta**. Eliges de una lista. Sin UUID. |
| `claude -r "login"` | Igual, pero **filtra** por término de búsqueda. |
| `claude -c` / `--continue` | Retoma **directo** la última conversación de la carpeta. |
| `claude -n "Bug login"` / `--name` | Le pone **nombre legible** a la sesión (visible en `/resume`, en la caja del prompt y en el título de la terminal). |
| `claude --resume --fork-session` | Retoma una sesión **creando una copia nueva** sin pisar la original. |
| `claude --from-pr 123` | Retoma la sesión ligada a un **Pull Request**. |

### Dentro de la sesión (slash commands)

| Comando | Qué hace |
| --- | --- |
| `/resume [sesión]` | Cambiar de sesión por **ID o nombre**, o abrir el selector. Alias: `/continue`. |
| `/rename [nombre]` | **Renombrar la sesión actual** (aparece en la barra del prompt). Sin nombre, lo autogenera. |
| `/branch [nombre]` | **Bifurca** la conversación en este punto: te mueve a la rama y preserva la original. Alias: `/fork`. |
| `/clear [nombre]` | Empieza una conversación nueva con contexto vacío. Pasar un nombre **etiqueta la anterior** en el selector. Alias: `/new`, `/reset`. |
| `/export [archivo]` | Exporta la conversación a texto plano. |
| `/copy [N]` | Copia la última respuesta (o la N-ésima) al portapapeles. |

> [!example] Flujo recomendado para tus ~20 proyectos
> 1. Al **empezar**: `claude -n "Refactor auth Vaecos"`.
> 2. Si ya estás dentro y quieres etiquetarla: `/rename Refactor auth Vaecos`.
> 3. Al **volver**: entra a la carpeta y `claude -r` → eliges por nombre.
> 4. Para seguir lo último de ese proyecto sin elegir: `claude -c`.

> [!warning] La limitación real del selector nativo
> `claude -r` solo muestra las sesiones de **la carpeta actual** (`cwd`). No hay vista global que cruce todos los proyectos ni etiquetas propias. Si lo necesitas, se construye un visor que lea todos los `.jsonl` de `~/.claude/projects/`.

---

## 🚀 Formas de arrancar Claude

```bash
claude                      # Sesión interactiva normal
claude "arregla el test X"  # Arranca con un prompt inicial
claude -p "explica esto"    # Modo "print": responde y SALE (ideal para pipes/scripts)
git diff | claude -p "resume estos cambios"   # Encadenado con pipes
```

> [!note] Modo `-p` / `--print`
> Para automatización. **Omite el diálogo de confianza del workspace** → úsalo solo en carpetas en las que confías.

---

## 🧠 Modelo, esfuerzo y modo rápido

| Flag / Comando | Para qué | Valores |
| --- | --- | --- |
| `--model` / `/model` | Elegir modelo | `opus`, `sonnet`, `haiku` o nombre completo (`claude-opus-4-8`) |
| `--effort` / `/effort` | Cuánto razona | `low`, `medium`, `high`, `xhigh`, `max`, `ultracode` |
| `--fallback-model` | Modelo de respaldo si el principal está saturado | (solo con `--print`) |
| `/fast [on\|off]` | **Modo rápido**: Opus con salida más veloz | — |

> [!tip] Regla práctica de modelo/esfuerzo
> - **Mecánico / rápido** → `sonnet` o `haiku`, `effort low/medium`.
> - **Arquitectura, debugging duro** → `opus`, `effort high/max`.
> - `ultracode` = `xhigh` + orquestación automática de workflows (para tareas grandes).

---

## 🔐 Modos de permiso

Controlan cuánto te pregunta Claude antes de actuar. Se ciclan en vivo con `Shift+Tab`.

| Modo (`--permission-mode` o `/permissions`) | Comportamiento |
| --- | --- |
| `default` | Pregunta ante acciones sensibles (lo normal). |
| `plan` | **Planifica y propone**, no ejecuta cambios. Entra directo con `/plan`. |
| `acceptEdits` | Acepta ediciones de archivos sin preguntar cada una. |
| `auto` / `dontAsk` | Reducen las confirmaciones. |
| `bypassPermissions` | **Salta TODAS las confirmaciones.** |

> [!danger] Cuidado con `bypassPermissions` / `--dangerously-skip-permissions`
> Solo en entornos aislados (sandbox sin internet). En tu equipo normal, evítalo.

```bash
claude --permission-mode plan      # Primero planifica, luego decides
```

---

## ⌨️ Slash commands por propósito

> [!note] Se escriben dentro de Claude. `<arg>` = obligatorio · `[arg]` = opcional.
> No todos aparecen para todos (dependen de plan/plataforma). Escribe `/` para ver los tuyos.

### 🗂️ Contexto y memoria

| Comando | Para qué |
| --- | --- |
| `/context [all]` | **Visualiza el uso del contexto** como una grilla de colores, con sugerencias de optimización. |
| `/compact [instrucciones]` | **Resume la conversación** para liberar contexto sin perder el hilo. |
| `/clear` | Conversación nueva con contexto vacío (la anterior queda en `/resume`). |
| `/memory` | Editar los `CLAUDE.md`, activar/ver auto-memoria. |
| `/btw <pregunta>` | **Pregunta al margen**: respuesta rápida que NO entra en el historial. Ve todo el contexto pero no tiene herramientas. |
| `/recap` | Resumen de una línea de la sesión actual. |

### ⚙️ Configuración

| Comando | Para qué |
| --- | --- |
| `/config` | Abre Settings (tema, modelo, output style…). Alias: `/settings`. |
| `/model` · `/effort` · `/fast` | Modelo, esfuerzo, modo rápido. |
| `/permissions` | Gestionar reglas allow/ask/deny. Alias: `/allowed-tools`. |
| `/theme` · `/statusline` · `/color` | Apariencia: tema, barra de estado, color del prompt. |
| `/keybindings` | Editar tus atajos de teclado. |
| `/hooks` | Ver/configurar hooks de eventos de herramientas. |

### 🔍 Revisión y calidad

| Comando | Para qué |
| --- | --- |
| `/diff` | Visor interactivo de cambios sin commitear y por turno. |
| `/code-review [nivel] [--fix] [--comment]` | Revisa el diff: bugs + mejoras. `--fix` aplica, `ultra` = revisión cloud multi-agente. |
| `/review [PR]` | Revisa un PR localmente. |
| `/security-review` | Analiza cambios buscando vulnerabilidades (inyección, auth, fugas). |
| `/simplify [target]` | Limpieza (reuso, simplificación, eficiencia) y aplica fixes. |
| `/verify` | **Confirma que un cambio funciona** ejecutando la app de verdad, no solo tests. |
| `/run` | Lanza y maneja tu app para verla funcionando. |

### 🧩 Trabajo en paralelo y agentes

| Comando | Para qué |
| --- | --- |
| `/agents` | Gestionar configuraciones de subagentes. |
| `/tasks` | Listar/gestionar tareas en background. Alias: `/bashes`. |
| `/background [prompt]` | Desacopla la sesión para que corra en background y libera la terminal. Alias: `/bg`. |
| `/batch <instrucción>` | Cambios a gran escala: descompone en 5–30 unidades y lanza un subagente por cada una en su worktree (requiere git). |
| `/loop [intervalo] [prompt]` | Repite un prompt en un intervalo (ej. `/loop 5m revisa el deploy`). |
| `/goal [condición]` | Claude **sigue trabajando entre turnos** hasta cumplir la condición. |
| `/workflows` | Vista de progreso de workflows en curso. |
| `/plan [descripción]` | Entra en modo plan directo. |

### 🔌 MCP, skills y plugins

| Comando | Para qué |
| --- | --- |
| `/mcp` | Gestionar servidores MCP y OAuth. |
| `/skills` | Listar skills (pulsa `t` para ordenar por tokens). |
| `/plugin` | Gestionar plugins. |
| `/reload-skills` · `/reload-plugins` | Recargar sin reiniciar la sesión. |

### 🩺 Diagnóstico y cuenta

| Comando | Para qué |
| --- | --- |
| `/doctor` | Diagnostica instalación y settings (pulsa `f` para que arregle). |
| `/debug [descripción]` | Activa logs de debug y los analiza. |
| `/usage` | Costo de sesión, límites del plan, stats. Alias: `/cost`, `/stats`. |
| `/insights` | Reporte de tus sesiones: áreas, patrones, fricciones. |
| `/feedback [reporte]` | Reportar bug con contexto de sesión. Alias: `/bug`, `/share`. |
| `/release-notes` | Ver el changelog por versión. |

### 🏁 Inicio de proyecto

| Comando | Para qué |
| --- | --- |
| `/init` | Genera un `CLAUDE.md` inicial del proyecto. |
| `/add-dir <ruta>` | Añade una carpeta de trabajo para acceso a archivos. |

### 🌐 Remoto y multiplataforma

| Comando | Para qué |
| --- | --- |
| `/remote-control` | Hace la sesión controlable desde claude.ai. Alias: `/rc`. |
| `/teleport` | Trae una sesión de Claude Code web a esta terminal. Alias: `/tp`. |
| `/desktop` · `/mobile` | Continuar en la app de escritorio / móvil. |
| `/schedule [descripción]` | Crear/gestionar **routines** que corren en cloud por cron. Alias: `/routines`. |

---

## 🎹 Atajos de teclado (modo interactivo)

> [!tip] Los que más se usan
> Pulsa `?` en el visor de transcripción (fullscreen) para ver todos.

### Control general

| Atajo | Acción |
| --- | --- |
| `Ctrl+C` | Interrumpe la operación; si no hay nada, limpia el input (2ª vez sale). |
| `Esc` | Interrumpe a Claude a mitad de turno (conserva lo hecho). |
| `Esc` `Esc` | Limpia el borrador, o abre el menú **rewind** si el input está vacío. |
| `Ctrl+D` | Salir de la sesión. |
| `Ctrl+O` | Mostrar/ocultar el **visor de transcripción** (detalle de tools). |
| `Ctrl+R` | **Búsqueda inversa** en el historial de comandos. |
| `Ctrl+B` | Mandar a **background** la tarea/bash actual (tmux: dos veces). |
| `Ctrl+T` | Mostrar/ocultar la **lista de tareas**. |
| `Ctrl+G` / `Ctrl+X Ctrl+E` | Editar el prompt en tu **editor de texto** por defecto. |
| `Ctrl+L` | Redibujar la pantalla (si se ve corrupta). |
| `Shift+Tab` | **Ciclar modos de permiso** (default → acceptEdits → plan → …). |
| `Alt+P` | Cambiar de modelo sin borrar el prompt. |
| `Alt+T` | Activar/desactivar **extended thinking**. |
| `Alt+O` | Activar/desactivar **fast mode**. |
| `Ctrl+V` (`Alt+V` en Windows/WSL) | Pegar imagen del portapapeles. |

### Edición de texto (estilo readline)

| Atajo | Acción |
| --- | --- |
| `Ctrl+A` / `Ctrl+E` | Inicio / fin de línea. |
| `Ctrl+K` / `Ctrl+U` | Borrar hasta el fin / inicio de línea. |
| `Ctrl+W` | Borrar palabra anterior. |
| `Ctrl+Y` | Pegar lo borrado (`Alt+Y` cicla el historial). |
| `Alt+B` / `Alt+F` | Mover una palabra atrás / adelante. |

### Input multilínea

| Método | Atajo |
| --- | --- |
| Universal | `\` + `Enter`  ·  o  `Ctrl+J` |
| Nativo (iTerm2, WezTerm, Ghostty, Kitty, Warp, Windows Terminal…) | `Shift+Enter` |
| Otros (VS Code, Cursor, Zed, Alacritty) | correr `/terminal-setup` una vez |

### Prefijos rápidos (al inicio del prompt)

| Prefijo | Acción |
| --- | --- |
| `/` | Comando o skill. |
| `!` | **Shell mode**: ejecuta el comando directo y su salida entra al contexto (sin que Claude lo apruebe). |
| `@` | Autocompletar **ruta de archivo**. |

---

## ⌨️ Modo Vim (para los que venimos de LazyVim)

> [!note] Activación
> `/config` → **Editor mode** → Vim. (El antiguo `/vim` fue removido en v2.1.92.)

**Cambio de modo:** `Esc` (NORMAL), `i`/`I`/`a`/`A`/`o`/`O` (INSERT), `v`/`V` (VISUAL).

**Navegación:** `h j k l`, `w`/`e`/`b`, `0`/`$`/`^`, `gg`/`G`, `f{c}`/`F{c}`/`t{c}`/`T{c}`, `;`/`,`.

**Edición:** `x`, `dd`, `D`, `dw`/`de`/`db`, `cc`/`C`/`cw`, `yy`/`yw`, `p`/`P`, `>>`/`<<`, `J`, `u`, `.`.

**Text objects** (con `d`/`c`/`y`): `iw`/`aw`, `i"`/`a"`, `i(`/`a(`, `i[`/`a[`, `i{`/`a{`.

> [!info] Detalle útil
> En NORMAL, si el cursor está en el borde del input, `j`/`k` navegan el **historial de comandos** en vez de moverse.

---

## 📄 Contexto del proyecto: `CLAUDE.md`

> [!important] El archivo más importante para resultados consistentes
> Un `CLAUDE.md` en la raíz del proyecto (o `~/.claude/CLAUDE.md` global) le da a Claude tus reglas y convenciones **en cada sesión**.

- Genéralo con `/init`; refínalo con `/memory`.
- Pon ahí: stack, convenciones de commits, arquitectura, estilo, qué NO hacer.
- Es la diferencia entre que Claude **adivine** tu forma de trabajar y que la **conozca**.

---

## 🛠️ Subcomandos del CLI (desde la terminal)

| Comando | Para qué |
| --- | --- |
| `claude doctor` | Salud de la instalación y el auto-updater. |
| `claude update` / `upgrade` | Buscar e instalar actualizaciones. |
| `claude mcp` | Configurar servidores MCP. |
| `claude plugin` / `plugins` | Gestionar plugins. |
| `claude agents` | Gestionar agentes en background. |
| `claude auth` · `claude setup-token` | Autenticación / token de larga duración. |
| `claude install [stable\|latest\|versión]` | Instalar el build nativo. |
| `claude -v` / `--version` | Ver versión. |

---

## 🌿 Sesiones en paralelo con git worktrees

> [!example] Varias tareas/ramas sin pisarte
> ```bash
> claude -w "feature-x"     # Crea un git worktree nuevo para la sesión
> claude -w --tmux          # Worktree + tmux (requiere -w)
> ```
> Útil cuando tienes varias tareas abiertas y no quieres mezclar cambios. Combínalo con `/batch` para cambios masivos.

---

## 📌 Flags de arranque (referencia rápida)

| Flag | Uso |
| --- | --- |
| `-r`, `--resume [valor]` | Retomar sesión / abrir selector |
| `-c`, `--continue` | Retomar la última de la carpeta |
| `-n`, `--name <nombre>` | Nombrar la sesión |
| `--fork-session` | Al retomar, crear copia nueva |
| `--from-pr [valor]` | Retomar sesión ligada a un PR |
| `-w`, `--worktree [nombre]` | Crear git worktree |
| `-p`, `--print` | Responder y salir (pipes/scripts) |
| `--model` · `--effort` | Modelo · nivel de razonamiento |
| `--permission-mode <modo>` | Modo de permisos |
| `--add-dir <dirs...>` | Carpetas adicionales accesibles |
| `--agents <json>` | Definir agentes personalizados |
| `--mcp-config <archivos...>` | Cargar servidores MCP desde JSON |
| `--settings <archivo-o-json>` | Cargar settings extra |
| `--max-budget-usd <monto>` | Tope de gasto en API (solo `--print`) |
| `--verbose` | Modo detallado |

---

## ✅ Buenas prácticas (checklist)

> [!success] Para trabajar mejor
> - [ ] **Nombra** las sesiones importantes con `-n` o `/rename`. Nunca anotes el UUID a mano.
> - [ ] Vuelve con `claude -r`; sigue lo último con `claude -c`.
> - [ ] Mantén un `CLAUDE.md` por proyecto.
> - [ ] Tareas grandes → modo `plan` primero, revisa, luego ejecuta.
> - [ ] Vigila el contexto con `/context`; cuando crezca, `/compact`.
> - [ ] Ajusta `--model`/`--effort` a la dificultad real (no todo necesita `opus`/`max`).
> - [ ] Evita `bypassPermissions` salvo en sandbox.
> - [ ] Antes de mergear: `/code-review`, `/security-review` o `claude ultrareview`.
> - [ ] Usa `/btw` para dudas rápidas sin ensuciar el historial.

---

## 🔗 Notas relacionadas

- Idea pendiente: visor **global** de sesiones que cruce todos los proyectos (leyendo `~/.claude/projects/**/*.jsonl`).
- `/insights` y `/team-onboarding` analizan tu historial de uso — útiles para detectar patrones.
- Ver también: configuración de `~/.claude/CLAUDE.md` global.
