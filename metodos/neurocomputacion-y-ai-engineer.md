---
tags: [tema/neurocomputacion, tema/ai-engineer, tipo/apunte, estado/exploratorio]
fecha: 2026-05-18
---
# Neurocomputación y su conexión con AI Engineering

> Vista superficial del campo. El objetivo no es ser experto en neurociencia, sino entender *de dónde vienen* las ideas que usamos en AI.

---

## ¿Qué es la Neurocomputación?

Campo que estudia **cómo el cerebro procesa información** y usa ese entendimiento para diseñar sistemas computacionales. Se sienta entre neurociencia, matemáticas y computación.

Preguntas centrales:
- ¿Cómo aprenden las neuronas biológicas?
- ¿Cómo puede una red de elementos simples producir comportamiento inteligente?
- ¿Podemos replicar eso artificialmente?

---

## El puente: de neurona biológica a neurona artificial

Una neurona biológica tiene tres partes clave:
1. **Dendritas** — reciben señales de otras neuronas
2. **Cuerpo celular (soma)** — suma las señales recibidas
3. **Axón** — si la suma supera un umbral, dispara una señal de salida

Una neurona artificial hace exactamente lo mismo en matemáticas:

$$
\text{salida} = f\!\left(\sum_{i} w_i x_i + b\right)
$$

Donde:
- $x_i$ = entradas (como las dendritas)
- $w_i$ = pesos (importancia de cada entrada)
- $b$ = bias (umbral de activación)
- $f$ = función de activación (¿dispara o no?)

```html-embed
file: interactivos/neurona-interactiva.html
```

---

## Tabla de correspondencias: Neurocomputación → AI

| Concepto biológico | Lo que produjo en AI |
|---|---|
| Neurona biológica (disparo) | Perceptrón → neurona artificial |
| Red de neuronas | Redes neuronales profundas (Deep Learning) |
| Regla de Hebb (1949) | Backpropagation, aprendizaje por refuerzo |
| Capas del córtex visual | CNNs (visión por computadora) |
| Memoria y atención selectiva | Mecanismo de Attention → Transformers |
| Plasticidad sináptica | Gradient descent (ajuste de pesos) |
| Umbral de activación | ReLU, sigmoide, tanh |

---

## Los 3 conceptos clave (para no perderse en la literatura)

### 1. Regla de Hebb (1949)
> *"Las neuronas que disparan juntas, se conectan."*

Si dos neuronas se activan al mismo tiempo repetidamente, la conexión entre ellas se fortalece. Es la intuición detrás de **cómo aprende** una red neuronal: los pesos que generan resultados correctos se refuerzan.

### 2. Redes de Hopfield
Memoria asociativa: dada una entrada incompleta o ruidosa, la red puede recuperar el patrón completo original. Inspiraron directamente el **mecanismo de Attention** moderno (los Transformers hacen algo análogo con Q, K, V).

### 3. Spiking Neural Networks (SNNs)
La "siguiente generación" de redes neuronales — imitan el cerebro con mucha más fidelidad (las neuronas disparan en pulsos discretos, no valores continuos). Aún en investigación, pero Intel (Loihi) y IBM (TrueNorth) ya tienen chips neuromorphic.

---

## ¿Por qué importa esto para un AI Engineer?

No para ser neurocientífico. Sí para entender el **"por qué"** detrás de decisiones de diseño:

| Decisión de diseño | Raíz en neurocomputación |
|---|---|
| ¿Por qué capas en una red? | El córtex visual tiene capas jerárquicas de procesamiento |
| ¿Por qué ReLU y no sigmoide? | Las neuronas tienen umbral discreto, no activación continua |
| ¿Por qué funciona Attention? | Hay mecanismos de atención selectiva en el cerebro |
| ¿Por qué regularización / dropout? | Simula la muerte aleatoria de neuronas — evita memorizar |

---

## Estado del campo hoy (2026)

- **Deep Learning clásico** — bien establecido, en producción masiva
- **Neuromorphic computing** — hardware que imita el cerebro, bajo consumo energético, en crecimiento
- **Brain-Computer Interfaces** — Neuralink y similares; cruzan la línea hacia hardware real
- **Computational neuroscience** — modela el cerebro para entenderlo, no para replicarlo

---

## Nivel de relevancia para tu camino

```
Neurocomputación superficial  ████████░░  Muy útil — contexto e intuición
Neurocomputación profunda     ████░░░░░░  Opcional — solo si quieres investigación
Neuromorphic computing        ██░░░░░░░░  Futuro — worth watching
```

**Prioridad real:** entender bien las redes neuronales artificiales primero. La neurocomputación es el "por qué" que enriquece ese entendimiento.

---

## Notas relacionadas

- [[markdown-y-obsidian]]
- [[latex-formulas-obsidian]]

---

*Tema explorado superficialmente el 2026-05-18. Si se profundiza, empezar por Regla de Hebb y luego Redes de Hopfield.*
