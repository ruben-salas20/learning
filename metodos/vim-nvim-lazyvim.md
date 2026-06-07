---
tags: [tipo/apunte, tema/vim, tema/neovim, tema/lazyvim, tema/editor, tema/terminal, estado/en-progreso]
fecha: 2026-05-29
---
# Vim, Neovim y LazyVim — del "estoy atrapado" al "fluyo con el teclado"

> Instalé LazyVim para acostumbrarme al teclado, pero muchos comandos me enredan.
> Este apunte NO busca que memorices todo (imposible y contraproducente). Busca que entiendas **el concepto modal** —que lo explica casi todo— y te da un núcleo mínimo de supervivencia + un plan por capas.
>
> Regla mental: **no se aprende vim memorizando, se aprende usándolo un poco cada día.** La velocidad llega sola.

---

## 0. Primero la confusión #1: ¿Vim, Neovim o LazyVim?

Son tres cosas en capas, una encima de la otra:

| Capa | Qué es | Analogía |
|---|---|---|
| **Vim** | el editor modal clásico de terminal | el motor |
| **Neovim (nvim)** | una versión moderna de Vim (mejor, extensible con Lua, plugins modernos) | el motor mejorado |
| **LazyVim** | una **configuración lista para usar** de Neovim (plugins, atajos, UI ya armados) | el auto completo con el motor adentro |

> **Clave**: LazyVim ES Neovim, solo que pre-configurado para que no tengas que armar todo a mano. Y Neovim entiende casi todos los comandos de Vim. Entonces: **lo que aprendas de Vim te sirve en los tres.** Por eso este apunte empieza por Vim (el núcleo universal) y al final agrega lo específico de LazyVim.

---

## 1. EL concepto que lo explica todo: editor MODAL

En un editor normal (Word, VS Code), el teclado siempre escribe texto. En Vim, el teclado **cambia de función según el MODO en el que estés**.

> **Analogía**: es como la tecla `Shift`. Sola, `a` escribe "a"; con Shift, escribe "A". La misma tecla, distinta función según el "modo". Vim lleva esa idea al extremo: tiene varios modos, y en cada uno las teclas hacen cosas distintas.

Esto explica el meme de "no puedo salir de Vim": la gente entra, empieza a escribir, y las teclas hacen cosas raras porque **no están en el modo de escribir** — están en modo Normal, donde las letras son COMANDOS, no texto.

### Por qué esto es PODEROSO (no una molestia)
Como en modo Normal las teclas son comandos, editás "hablándole" al editor con un lenguaje, sin mouse y sin combos imposibles tipo `Ctrl+Shift+Alt+K`. Una vez que hace click, editás más rápido que con mouse.

---

## 2. Los 4 modos (memorizá ESTO, no los comandos)

| Modo | Para qué | Cómo entrar | Cómo salir |
|---|---|---|---|
| **Normal** | navegar y ejecutar comandos (el modo "base") | `Esc` (vuelve acá desde cualquier lado) | — |
| **Insert** | escribir texto (como un editor normal) | `i`, `a`, `o` (entre otros) | `Esc` |
| **Visual** | seleccionar texto | `v`, `V`, `Ctrl+v` | `Esc` |
| **Command** | ejecutar comandos largos (guardar, salir, buscar/reemplazar) | `:` (desde Normal) | `Enter` o `Esc` |

> **Regla de oro del principiante**: cuando estés perdido o algo raro pasa → apretá **`Esc`**. Te devuelve a modo Normal, terreno seguro. `Esc` es tu botón de pánico.

---

## 3. SUPERVIVENCIA MÍNIMA (lo único que necesitás el día 1)

Con esto NO quedás atrapado nunca más:

```
i        → entrar a modo Insert (escribir) ANTES del cursor
Esc      → volver a Normal (dejar de escribir)
:w       → guardar (write)
:q       → salir (quit)
:wq      → guardar Y salir
:q!      → salir SIN guardar (descartar cambios) ← el salvavidas
```

**Flujo típico**: abrís archivo → `i` (escribís) → `Esc` → `:wq` (guardás y salís). Eso es todo para empezar.

> En LazyVim, además, `Ctrl+s` guarda directo (más cómodo que `:w`).

---

## 4. Movimiento en modo Normal (las manos quietas en el teclado)

La idea central de vim: **moverte sin flechas ni mouse**, con la mano en la fila central.

### Básico — las teclas sagradas `h j k l`
```
        k  (arriba)
   h  ←   → l        j = abajo, k = arriba
        j  (abajo)    h = izquierda, l = derecha
```
> Cuesta al principio, pero te mantiene las manos en la posición de tipeo. Truco para recordar: `j` parece una flecha hacia abajo.

### Por palabras y líneas
| Tecla | Movimiento |
|---|---|
| `w` | al inicio de la siguiente palabra (*word*) |
| `b` | atrás, al inicio de la palabra (*back*) |
| `e` | al final de la palabra (*end*) |
| `0` | inicio de la línea |
| `$` | final de la línea |
| `^` | primer carácter no-vacío de la línea |

### Por el archivo
| Tecla | Movimiento |
|---|---|
| `gg` | al inicio del archivo |
| `G` | al final del archivo |
| `42G` o `:42` | a la línea 42 |
| `Ctrl+d` / `Ctrl+u` | media pantalla abajo / arriba (*down*/*up*) |
| `{` / `}` | párrafo anterior / siguiente |

---

## 5. Variantes para entrar a Insert (importan más de lo que parece)

No todo es `i`. Elegir bien te ahorra movimientos:

| Tecla | Qué hace |
|---|---|
| `i` | insertar ANTES del cursor (*insert*) |
| `a` | insertar DESPUÉS del cursor (*append*) |
| `I` | insertar al inicio de la línea |
| `A` | insertar al final de la línea |
| `o` | abre una línea NUEVA debajo y entra a Insert |
| `O` | abre una línea nueva ARRIBA y entra a Insert |

---

## 6. Edición básica

| Tecla | Acción |
|---|---|
| `x` | borrar el carácter bajo el cursor |
| `dd` | borrar (cortar) la línea entera |
| `yy` | copiar (*yank*) la línea entera |
| `p` / `P` | pegar después / antes (*paste*) |
| `u` | deshacer (*undo*) |
| `Ctrl+r` | rehacer (*redo*) |
| `.` | **repetir** el último comando (¡poderosísimo!) |
| `r<letra>` | reemplazar un solo carácter |

---

## 7. LA GRAMÁTICA DE VIM (acá hace CLICK de verdad)

Este es el concepto que separa "sufro vim" de "amo vim". Los comandos de edición se **combinan como un lenguaje**:

```
OPERADOR + MOVIMIENTO/OBJETO
```

**Operadores** (verbos): `d` borrar · `c` cambiar (borra + entra a Insert) · `y` copiar

**Se combinan con movimientos o "text objects":**

| Comando | Se lee | Hace |
|---|---|---|
| `dw` | *delete word* | borra hasta el fin de la palabra |
| `d$` | *delete to end* | borra hasta el final de la línea |
| `dd` | *delete line* | borra la línea (operador duplicado = línea) |
| `cw` | *change word* | borra la palabra y te deja escribiendo |
| `yy` | *yank line* | copia la línea |

### Text objects (lo más elegante)
Describen "objetos" de texto: `iw` (inner word), `i"` (inside quotes), `i(` (inside parens), `ip` (inner paragraph)...

| Comando | Hace |
|---|---|
| `ciw` | *change inner word* → reemplaza la palabra donde está el cursor (¡no importa dónde de la palabra estés!) |
| `di"` | *delete inside quotes* → borra lo que hay dentro de las comillas |
| `ci(` | cambia lo que hay dentro de los paréntesis |
| `yi{` | copia lo que hay dentro de las llaves |

> **El "click"**: no memorizás `ciw`, `di"`, `ca(`... Aprendés los **verbos** (`d`/`c`/`y`) y los **objetos** (`iw`/`i"`/`i(`) por separado, y los **combinás**. Como armar frases. Eso es vim.

---

## 8. Buscar y reemplazar

| Comando | Acción |
|---|---|
| `/texto` + `Enter` | buscar "texto" hacia adelante |
| `?texto` + `Enter` | buscar hacia atrás |
| `n` / `N` | siguiente / anterior coincidencia |
| `*` | buscar la palabra bajo el cursor |
| `:%s/viejo/nuevo/g` | reemplazar TODO "viejo" por "nuevo" en el archivo |
| `:%s/viejo/nuevo/gc` | igual pero pidiendo **c**onfirmación en cada uno |

---

## 9. LazyVim — lo específico (y tu MAYOR salvavidas)

LazyVim agrega encima de Neovim un montón de comodidades. Lo más importante que tenés que saber:

### 9.1 La tecla LÍDER (`leader`) = `Espacio`
LazyVim usa la **barra espaciadora** como "tecla líder": el prefijo de casi todos sus atajos. Presionás `Espacio` y después una secuencia.

### 9.2 which-key: NO TENÉS QUE MEMORIZAR NADA
Este es el punto que resuelve tu problema de "no me sé los comandos":

> Presioná `Espacio` (leader) y **esperá medio segundo**. Aparece un menú (**which-key**) que te muestra TODOS los atajos disponibles y qué hacen. Vas eligiendo letra por letra y el menú te guía.

Esto es **recognition over recall**: no recordás de memoria, RECONOCés de una lista. Usá which-key sin culpa — es la forma correcta de aprender los atajos de LazyVim.

### 9.3 Atajos más usados de LazyVim
*(Si dudás, igual: `Espacio` y mirá which-key.)*

| Atajo | Acción |
|---|---|
| `Espacio` `f` `f` | buscar archivos por nombre (*find files*) |
| `Espacio` `f` `g` | buscar TEXTO dentro de los archivos (*grep*) |
| `Espacio` `e` | abrir/cerrar el explorador de archivos (árbol lateral) |
| `Espacio` `Espacio` | buscar archivos (rápido) |
| `Shift+h` / `Shift+l` | cambiar entre archivos abiertos (buffers) anterior/siguiente |
| `Espacio` `b` `d` | cerrar el archivo actual (*buffer delete*) |
| `Ctrl+s` | guardar |
| `Espacio` `q` `q` | salir de todo |
| `Espacio` `l` | abrir Lazy (gestor de plugins) |
| `Espacio` `g` `g` | abrir LazyGit (git visual) si está instalado |

### 9.4 Navegación de código (LSP — cuando edites código real)
| Atajo | Acción |
|---|---|
| `g` `d` | ir a la definición (*go to definition*) |
| `g` `r` | ver referencias |
| `K` | mostrar documentación de lo que está bajo el cursor (*hover*) |
| `Espacio` `c` `a` | acciones de código (*code action*) |
| `Espacio` `c` `r` | renombrar símbolo en todo el proyecto |

---

## 10. PLAN DE APRENDIZAJE POR CAPAS (no quieras todo de una)

El error #1 es intentar usar todo desde el día 1. Subí de nivel por etapas:

**Semana 1 — Supervivencia.** Solo: `i`, `Esc`, `:wq`, `:q!`, y moverte con `h j k l`. Nada más. Usá vim para archivos chicos a propósito.

**Semana 2 — Movimiento.** Sumá `w`/`b`/`e`, `0`/`$`, `gg`/`G`. Dejá las flechas por completo.

**Semana 3 — Edición.** Sumá `x`, `dd`, `yy`, `p`, `u`, `Ctrl+r`, `.` y las variantes de Insert (`a`/`A`/`o`/`O`).

**Semana 4 — La gramática.** `d`/`c`/`y` + movimientos y text objects (`ciw`, `di"`...). Acá empieza la magia.

**En paralelo — LazyVim.** Desde el día 1, usá `Espacio` + which-key para descubrir atajos. No los memorices: dejá que el menú te enseñe.

> **Recurso clásico**: en la terminal corré `vimtutor` — un tutorial interactivo de ~30 min, el mejor punto de partida oficial. (Para Neovim: `nvim +Tutor`.)

---

## 11. Cheatsheet de bolsillo (lo mínimo imprescindible)

```
PÁNICO:        Esc  (volver a Normal)
ESCRIBIR:      i (insert) · a (append) · o (línea nueva)
GUARDAR/SALIR: :w  ·  :q  ·  :wq  ·  :q! (descartar)
MOVER:         h j k l · w b e · 0 $ · gg G
EDITAR:        x · dd · yy · p · u · Ctrl+r · . (repetir)
GRAMÁTICA:     d/c/y + w/$/iw/i"  (ej: ciw, dd, di")
BUSCAR:        /texto · n/N · :%s/viejo/nuevo/g
LAZYVIM:       Espacio (leader) + esperar → which-key te guía
               Ctrl+s guardar · Espacio ff buscar archivo · Espacio e árbol
```

---

## 12. Mentalidad final

- **Esc es tu amigo.** Ante la duda, Esc.
- **which-key es tu copiloto.** No memorices atajos de LazyVim, reconocelos.
- **`vimtutor` una vez.** 30 minutos que valen oro.
- **Un comando nuevo por día.** No más. La fluidez es acumulativa, no de golpe.
- **Vas a ser MÁS lento la primera semana.** Es normal y temporal. Después no querés volver al mouse.

## Links relacionados
- `metodos/jupyter-y-notebooks.md` (otro entorno de edición)
- Conecta con el curso AI: el editor es la herramienta diaria para escribir el código de cada Build It.
