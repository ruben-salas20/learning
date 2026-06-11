---
tags: [tipo/clase, tema/apis, tema/llm, tema/seguridad, proyecto/ai-engineering-from-scratch, estado/en-curso]
fecha: 2026-06-09
fase: 0 - Setup & Tooling
leccion: 04 - APIs & Keys
fuente: phases/00-setup-and-tooling/04-apis-and-keys
tipo-doc: clase traducida y explicada (lectura). El apunte destilado va en notas/.
---
# Fase 0 · Lección 4 — APIs & Keys (clase)

> **Lema**: *"Every AI API works the same way: send a request, get a response.
> The details change, the pattern doesn't."*
> (Toda API de IA funciona igual: mandás una petición, recibís una respuesta.
> Los detalles cambian; el patrón, no.)
>
> Lección tipo **Build** (~30 min), Python + TypeScript. Para leer antes de la próxima sesión.

---

## El problema

A partir de la **Phase 11** vas a llamar APIs de LLMs (Anthropic, OpenAI, Google). En las
**Phases 13-16** vas a construir **agentes** que usan esas APIs en bucle. Necesitás saber tres cosas:
cómo funcionan las **API keys**, cómo guardarlas de forma SEGURA, y cómo hacer tu primera llamada.

> 🔗 **Conexión con tu vida real (Vaecos)**: vos ya tenés una app en producción. El manejo seguro de claves NO es teoría para vos — es lo que separa una app profesional de una que filtra secretos en GitHub.

---

## El concepto: anatomía de una llamada a API

```
Tu código  ──(HTTP Request + API key)──▶  Servidor de la API
Tu código  ◀──(HTTP Response en JSON)───  Servidor de la API
```

Toda llamada a una API tiene 4 partes:
1. **Endpoint** (la URL a la que pegás, ej. `https://api.anthropic.com/v1/messages`)
2. **API key** (autenticación: dice QUIÉN sos y que tenés permiso)
3. **Request body** (lo que pedís: el modelo, el mensaje, etc.)
4. **Response body** (lo que te devuelven, en JSON)

---

## 1. Guardar las API keys de forma SEGURA (lo más importante)

> ⛔ **REGLA DE ORO: NUNCA pongas una API key escrita en el código.**

¿Por qué? Porque si la hardcodeás (la escribís fija en el `.py`) y subís ese archivo a GitHub,
**queda expuesta públicamente** — hay bots que escanean GitHub buscando claves y las explotan en segundos (te vacían el crédito o peor). Esto conecta DIRECTO con la Lección 2: las keys van al
`.gitignore`.

**La forma correcta: variables de entorno (environment variables).**

```bash
# Opción A: exportar en la terminal (se borra al cerrarla)
export ANTHROPIC_API_KEY="sk-ant-..."

# Opción B (mejor): un archivo .env que NUNCA se sube a git
# archivo .env:
ANTHROPIC_API_KEY=sk-ant-...
```

Y en el `.gitignore` (¡como en la Lección 2!):
```gitignore
.env
```

> El SDK lee la key **sola** desde la variable de entorno. Tu código nunca la ve escrita.

---

## 2. Primera llamada en Python (con el SDK oficial)

El **SDK** (*Software Development Kit*) es la librería oficial que te ahorra escribir el HTTP a mano.

```python
import anthropic

client = anthropic.Anthropic()   # lee ANTHROPIC_API_KEY del entorno, sola

response = client.messages.create(
    model="claude-opus-4-8",      # ← ver NOTA DEL TUTOR abajo
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
)

print(response.content[0].text)
```

> 🧑‍🏫 **NOTA DEL TUTOR (corrección importante)**: el curso usa `model="claude-sonnet-4-20250514"`, que es un id **desactualizado** (queda retirado el 2026-06-15). Verifiqué contra la referencia oficial de Anthropic. Los ids ACTUALES (2026) son:
> - **`claude-opus-4-8`** → el más capaz.
> - **`claude-sonnet-4-6`** → mejor balance velocidad/inteligencia.
> - **`claude-haiku-4-5`** → el más rápido y barato.
>
> Importante: NO se le agregan sufijos de fecha a estos alias (es `claude-sonnet-4-6`, no
> `claude-sonnet-4-6-20251114`). Lección de fondo: **las APIs evolucionan**; siempre verificá el
> model id en la doc oficial, no copies a ciegas de un tutorial.

---

## ⚙️ Qué API usamos NOSOTROS (decisión 2026-06-09, corregida)

No tengo key nativa de Anthropic/Claude. Tengo dos: **MiniMax** y **OpenCode GO**. Verificado (jun-2026): **ambas ofrecen endpoint Anthropic-compatible**, así que el código del curso (SDK `anthropic` + `messages.create()`) funciona **casi sin cambios**, solo seteando `base_url`. Esto es lo MÁS acorde al curso.

| Proveedor                     | base_url (Anthropic-compatible)       | Modelos                                                                                                                    | Notas                                                                                           |
| ----------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **MiniMax** (principal)       | `https://api.minimax.io/anthropic/v1` | MiniMax-M2.5 / M3, etc.                                                                                                    | MiniMax **recomienda** este endpoint sobre el OpenAI. Funciona con el SDK de Anthropic directo. |
| **OpenCode GO** (alternativa) | `https://opencode.ai/zen/go/v1`       | open-source: MiniMax y Qwen (via `/messages`, Anthropic-compat); GLM/Kimi/DeepSeek (via`/chat/completions`, OpenAI-compat) | Tarifa plana mensual. **NO incluye Claude.**                                                    |

> ⚠️ **Corrección importante**: ninguna sirve modelos **Claude** (son modelos open-source / MiniMax). Da exactamente igual para el curso — el curso solo necesita *un* LLM detrás, no Claude específicamente.

> 🔑 **El punto clave (mejor de lo que pensaba)**: el curso usa el **SDK de Anthropic**
> (`anthropic.Anthropic()` + `client.messages.create()`). Como mis dos proveedores tienen endpoint **Anthropic-compatible**, NO necesito el SDK de OpenAI ni cambiar de método: uso el **mismo SDK del curso**, solo apunto el `base_url`.

**Adaptación del código del curso → lo que corremos nosotros (mínima):**

```python
import os, anthropic

# CURSO:  client = anthropic.Anthropic()   ← lee key de Anthropic del entorno
# NOSOTROS: solo agregamos base_url + nuestra key
client = anthropic.Anthropic(
    base_url="https://api.minimax.io/anthropic/v1",   # MiniMax (o https://opencode.ai/zen/go/v1)
    api_key=os.environ["MINIMAX_API_KEY"],            # (o OPENCODE_API_KEY)
)

r = client.messages.create(          # ← IGUAL que el curso
    model="MiniMax-M2.5",            # (verificar el nombre exacto en el dashboard del proveedor)
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}],
)
print(r.content[0].text)             # ← IGUAL que el curso
```

**Lo único que cambia** (el patrón de los 4 elementos es idéntico):
1. `base_url` → apunta al endpoint Anthropic del proveedor.
2. `api_key` → mi key (MiniMax u OpenCode GO), guardada en variable de entorno.
3. `model` → el nombre del modelo del proveedor (ej. `MiniMax-M2.5`).

El SDK (`anthropic`), el método (`messages.create`) y el parseo (`r.content[0].text`) **NO cambian**.

> 🎓 **Esto ES la lección, demostrada aún mejor**: *"the details change, the pattern doesn't"*.
> Endpoint + key + request + response son los mismos 4 elementos; acá solo cambia el endpoint y el modelo. Aprendo el patrón provider-agnóstico, que es lo que de verdad importa.

**Seguridad (igual que con cualquier key)**: las guardo en variables de entorno / `.env`, y `.env`
va al `.gitignore`. Mismo principio de la Lección 2, da igual el proveedor.

**Recomendación**: **MiniMax** como principal (su endpoint Anthropic da máxima fidelidad al código del curso); **OpenCode GO** como alternativa (también expone `/messages` Anthropic-compat para MiniMax/Qwen).

---

## 3. La misma llamada en TypeScript (para las Phases 13-16)

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const response = await client.messages.create({
  model: "claude-opus-4-8",
  max_tokens: 256,
  messages: [{ role: "user", content: "What is a neural network in one sentence?" }],
});

console.log(response.content[0].text);
```

Es el MISMO patrón (cliente → `messages.create` → leer respuesta). Cambia la sintaxis del lenguaje, no la idea. Eso es justo el lema de la lección.

---

## 4. HTTP crudo (sin SDK) — para entender qué hay debajo

Esto es lo que el SDK hace por dentro. Entenderlo te salva cuando algo falla:

```python
import os, urllib.request, json

url = "https://api.anthropic.com/v1/messages"
headers = {
    "Content-Type": "application/json",
    "x-api-key": os.environ["ANTHROPIC_API_KEY"],   # ← clave en el header
    "anthropic-version": "2023-06-01",
}
body = json.dumps({
    "model": "claude-opus-4-8",
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    print(result["content"][0]["text"])
```

> 📌 **Detalle clave que confirmé en la doc oficial**: Anthropic autentica con el header
> **`x-api-key`**, NO con el típico `Authorization: Bearer ...` que usan otras APIs. Cada API tiene su propia forma; por eso conviene leer SU documentación.

---

## Errores comunes (los vas a ver, así que reconocelos)

| Código HTTP | Qué significa | Qué hacer |
|---|---|---|
| **401** Unauthorized | API key inválida o ausente | revisar la key / la variable de entorno |
| **429** Too Many Requests | pasaste el **rate limit** (límite de peticiones) | esperar y reintentar (con *exponential backoff*) |
| **400** Bad Request | el body está mal armado | revisar modelo, formato de `messages` |

> **Buena noticia**: los SDK oficiales **reintentan solos** los 429 y los errores 5xx con backoff
> exponencial. No tenés que programarlo a mano.

---

## Key Terms (glosario de la lección)

| Término | Lo que la gente dice | Lo que de verdad es |
|---|---|---|
| **API key** | "contraseña de la API" | Cadena única que identifica tu cuenta y autoriza tus peticiones |
| **Rate limit** | "me están frenando" | Máximo de peticiones por minuto/hora, para evitar abusos |
| **Token** | "una palabra" | Unidad de **facturación**: tokens de entrada y de salida se cuentan y cobran por separado |
| **Streaming** | "respuestas en tiempo real" | Recibir la respuesta palabra por palabra, sin esperar a que termine toda |

## Vocabulario inglés nuevo
endpoint = punto de acceso (URL) · request/response = petición/respuesta · header = cabecera ·
environment variable = variable de entorno · to hardcode = escribir fijo en el código ·
authentication = autenticación · rate limit = límite de tasa · exponential backoff = reintento con espera creciente.

---

## Ejercicios (para cuando consigas una API key — opcional, tiene costo)
1. Conseguir una API key de Anthropic y hacer la primera llamada (hay $5 de crédito al registrarse).
2. Probar la versión HTTP cruda y comparar el formato de respuesta con el del SDK.
3. Usar a propósito una key equivocada y LEER el mensaje de error (aprender a leer errores).

> ⚠️ Estos ejercicios consumen crédito real. Los podemos posponer hasta que de verdad los necesites (recién en Phase 11). Por ahora, con ENTENDER el patrón y la seguridad de las keys es suficiente.

## Próximo paso (próxima sesión)
Charlamos dudas de esta clase + evaluación de comprensión, y decidimos si cerramos o avanzamos a la Lección 5 (Jupyter Notebooks).

## Links
- [[fase00-leccion03-gpu-setup-and-cloud]] (anterior)
- Relacionado: Lección 2 (`.gitignore` para no filtrar `.env`), tu app Vaecos (manejo de secretos).
