---
tags: [tipo/clase, tema/gpu, tema/cuda, tema/deep-learning, proyecto/ai-engineering-from-scratch, estado/en-curso]
fecha: 2026-06-08
fase: 0 - Setup & Tooling
leccion: 03 - GPU Setup & Cloud
fuente: phases/00-setup-and-tooling/03-gpu-setup-and-cloud
tipo-doc: clase traducida y explicada (lectura). El apunte destilado va en notas/.
---
# Fase 0 · Lección 3 — GPU Setup & Cloud (clase)

> Lección tipo **Build** (~45 min), lenguaje Python. Material NUEVO de verdad:
> primeros conceptos de Deep Learning que se usan en serio. Se aprende haciendo.
> El *Build It* se corre en la **RTX 3050** real.

---

## El problema

> Frase de apertura: *"Training on CPU is fine for learning. Training for real needs a GPU."*
> (Entrenar en CPU está bien para aprender. Entrenar en serio necesita una GPU.)

Las Phases 1-3 corren bien en CPU. Pero al llegar a entrenar **CNNs, transformers o LLMs**
(Phase 4+), se necesita aceleración por GPU. *"A training run that takes 8 hours on CPU
takes 10 minutes on GPU"* — un entrenamiento de 8 horas en CPU = 10 minutos en GPU.

### Las tres opciones

| Opción | Costo | Para qué sirve |
|---|---|---|
| **1. GPU local** (mi RTX 3050) | $0 (ya la tengo) | Uso regular, datasets grandes |
| **2. Google Colab** (*free tier* = capa gratis) | $0 | Experimentos rápidos, o si no hay GPU |
| **3. Cloud GPU** (Lambda, RunPod, Vast.ai) | $0.20-2.00/hora | Entrenamiento serio, modelos grandes |

---

## Los 4 conceptos clave

### 1. ¿Por qué la GPU es más rápida que la CPU?

No es potencia bruta, es **arquitectura**.

> 🏗️ **Analogía de obra**: una **CPU** son 8 ingenieros expertos — pocos, brillantes, tareas
> complejas en secuencia. Una **GPU** son 5.000 obreros — cada uno hace algo simple, pero los
> 5.000 trabajan **AL MISMO TIEMPO** (en paralelo).

Entrenar redes neuronales es, en el fondo, **multiplicar matrices gigantes**: millones de
operaciones simples e independientes. Eso es justo lo que les gusta a los 5.000 obreros.
*"Thousands of parallel matrix operations simultaneously"* = miles de operaciones de matriz
en paralelo, simultáneas.

### 2. VRAM — el límite real de la GPU

**VRAM** = *Video RAM*, la memoria **propia de la GPU**, SEPARADA de la RAM del sistema
(los 16 GB del PC). La RTX 3050 tiene **6 GB de VRAM**.

> CRÍTICO: la VRAM **limita el tamaño del modelo** que se puede cargar. Aunque haya 16 GB de
> RAM del sistema, si el modelo no entra en los 6 GB de VRAM, no corre en la GPU.
> RAM del sistema y VRAM son dos cajas distintas.

### 3. fp16 y la regla del pulgar (cuánto modelo entra)

Cada **parámetro** de un modelo es un número. ¿Cuánto pesa?

| Precisión | Bytes por parámetro |
|---|---|
| **fp32** (*full precision*, 32 bits) | 4 bytes |
| **fp16** (*half precision*, 16 bits) | 2 bytes |

> **fp16** = "media precisión": la MITAD de memoria que fp32, con pérdida mínima de exactitud.
> Por eso en IA se usa muchísimo.

**Regla del pulgar** (*rule of thumb*): `parámetros que entran ≈ VRAM en bytes / 2` (en fp16).

Ejemplo: 24 GB → 24/2 = **12 mil millones (12B) de parámetros**. (Estimación optimista: solo
cuenta los pesos; entrenar de verdad necesita más memoria para activaciones, gradientes y
estados del optimizador.)

### 4. Tensor Cores y el truco de `synchronize()`

- **Tensor Cores**: núcleos especializados SOLO en multiplicar matrices, 4-8x más rápidos que
  los normales. La 3050 (arquitectura Ampere) los tiene. Es el "hardware mágico" de la IA moderna.
- **`torch.cuda.synchronize()`**: las operaciones en GPU son **asíncronas** — Python lanza la
  orden y sigue SIN esperar a que la GPU termine. Si se mide el tiempo sin sincronizar, se mide
  "lo que tardó Python en dar la orden", no lo que tardó la GPU. `synchronize()` dice "esperá a
  que la GPU termine de verdad" antes de parar el cronómetro. Sin eso, **el benchmark miente**.

---

## Build It — benchmark en la RTX 3050

El curso trae `gpu_check.py` (script oficial) que detecta la GPU, mide CPU vs GPU y estima el
modelo máximo en VRAM. Seguimos el curso paso a paso.

**1. Ritual de arranque** (el venv tiene PyTorch):
```bash
cd ~/ai-eng && source .venv/bin/activate
```

**2. Correr el script oficial** (comillas por los espacios en la ruta):
```bash
python "/mnt/d/Mis Archivos/Documentos/Cursos/ai-engineering-from-scratch/phases/00-setup-and-tooling/03-gpu-setup-and-cloud/code/gpu_check.py"
```

Imprime: versión de PyTorch/CUDA, GPU, memoria, **benchmark CPU vs GPU + speedup**, y la
**estimación de modelo máximo en fp16**.

**Dos cosas a observar:**
1. **`Speedup`** — cuántas veces más rápida fue la GPU. (La PRIMERA op en GPU incluye un
   "calentamiento"/inicialización; el número puede salir más bajo de lo real.)
2. **`Estimated max model size`** — cuánto modelo banca la 3050. Pregunta: ¿un Llama de 7B
   entra en 6 GB? (Pista: 6/2 = 3 → ~3B. Un 7B NO entra en fp16; por eso existe la
   cuantización a 4 bits, que se verá más adelante.)

---

## Key Terms (glosario de la lección)

| Término | Lo que la gente dice | Lo que de verdad es |
|---|---|---|
| **CUDA** | "programar la GPU" | Plataforma de NVIDIA para correr código en la GPU |
| **VRAM** | "memoria de la GPU" | Video RAM de la GPU, separada de la RAM del sistema. Limita el tamaño del modelo |
| **fp16** | "media precisión" | Coma flotante de 16 bits; la mitad de memoria que fp32, pérdida mínima |
| **Tensor Core** | "hardware rápido de matrices" | Núcleos GPU especializados en multiplicar matrices, 4-8x más rápidos |

## Vocabulario inglés nuevo
free tier = capa gratis · rule of thumb = regla del pulgar · speedup = aceleración (factor) ·
half/full precision = media/precisión completa · benchmark = medición comparativa de rendimiento.
