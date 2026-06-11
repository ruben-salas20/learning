---
tags: [tipo/apunte, tema/gpu, tema/cuda, tema/deep-learning, proyecto/ai-engineering-from-scratch, estado/completo]
fecha: 2026-06-08
fase: 0 - Setup & Tooling
leccion: 03 - GPU Setup & Cloud
fuente: phases/00-setup-and-tooling/03-gpu-setup-and-cloud
tipo-doc: apunte destilado (repaso). La clase completa está en docs/.
---
# Fase 0 · Lección 3 — GPU Setup & Cloud (apunte)

> **Lema**: *"Training on CPU is fine for learning. Training for real needs a GPU."*
> Destilado de lo que entendí + el benchmark en mi RTX 3050. (Clase completa: `docs/fase00-leccion03...`)

---

## Lo esencial

1. **GPU > CPU por arquitectura, no por potencia bruta.** CPU = pocos núcleos expertos (en serie);
   GPU = miles de núcleos simples **en paralelo**. Entrenar = multiplicar matrices gigantes
   (millones de ops independientes) → la GPU lo hace de un golpe.

2. **VRAM** = memoria propia de la GPU, SEPARADA de la RAM del sistema. **Limita el tamaño del
   modelo.** Mi 3050: **6.4 GB**. (Aunque tenga 16 GB de RAM, si el modelo no entra en VRAM, no corre en GPU.)

3. **Regla del pulgar (fp16)**: `params que entran ≈ VRAM_bytes / 2`. fp16 = 2 bytes/param,
   fp32 = 4 bytes/param. Mi 3050 → ~3B params en fp16.

4. **Cuantización** = bajar precisión para que el modelo pese menos. Trade-off: ahorro memoria,
   pierdo un poco de exactitud. Un 7B en fp16 = 14 GB (NO entra), pero a 4 bits = 3.5 GB (SÍ entra).

5. **`torch.cuda.synchronize()`**: las ops de GPU son **asíncronas** (Python no espera). Para medir
   tiempo real hay que sincronizar, si no medís solo "lo que tardó la orden", no el cómputo.

---

## Mi benchmark (RTX 3050, 6.4 GB)

| Métrica | Valor |
|---|---|
| CPU matmul 4000x4000 | 0.324 s |
| GPU matmul 4000x4000 | 0.198 s |
| **Speedup** | **2x** |
| Max modelo fp16 | ~3B params |

**¿Por qué solo 2x y no 50x?** (lección de fondo, NO es que la GPU sea mala):
- **Warmup**: la 1ª op en GPU paga el costo único de inicializar CUDA/kernels, metido en ese tiempo.
- **Una sola op = poco trabajo**: el overhead fijo (mover datos + lanzar) pesa mucho con una sola op.
- **El CPU de PyTorch ya es rápido** (BLAS multinúcleo) → el rival no era lento.
- El speedup real (50-100x) aparece en loops de entrenamiento con miles de ops + Tensor Cores + fp16.

> Moraleja: un benchmark mal diseñado SUBESTIMA a la GPU. Hay que saber QUÉ se está midiendo.

---

## Las 3 opciones de GPU
1. **Local** (mi 3050): $0, uso regular. Buena para aprender (modelos ≤3B fp16 o ~7B a 4 bits).
2. **Google Colab** (T4 gratis): $0, cero setup, experimentos rápidos.
3. **Cloud GPU** (Lambda/RunPod/Vast.ai): $0.20-2/h, entrenamiento serio.

## Comprensión (evaluación): 3/3 ✅
Explicó las 3 razones del speedup bajo, el porqué de synchronize (asíncrono), y la cuantización
a 4 bits con su trade-off precisión↔memoria.

## Links
- [[fase00-leccion02-git-and-collaboration]] (anterior)
- Clase completa: `docs/fase00-leccion03-gpu-setup-and-cloud.md`
- Relacionado: `notas/fase00-leccion01-dev-environment.md` (sección GPU/CUDA)
