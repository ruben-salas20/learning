---
tags: [tipo/apunte, tema/ai, tema/machine-learning, tema/fundamentos, estado/en-progreso]
fecha: 2026-05-20
fuente: examples/01-hello-ai-world.py del repo microsoft/AI-For-Beginners
---
# Cómo aprende una AI — anatomía del Hello AI World

> Este apunte parte del código que ya corriste (`01-hello-ai-world.py`). Responde a cuatro preguntas tuyas:
> 1. ¿Cómo "guarda" la AI lo que aprende? ¿Dónde está su memoria?
> 2. ¿Cómo se "educa" la predicción?
> 3. ¿Qué son las **épocas** (`epochs`)?
> 4. ¿Qué son el **peso** (`weight`) y el **learning rate**?
>
> Vamos a usar el código real como ancla. NO vas a salir de acá sabiendo "qué es una red neuronal" — vas a salir sabiendo qué hace UNA neurona, que es la base de TODO lo demás.

---

## Mapa del archivo

| # | Tema | Pregunta que responde |
|---|---|---|
| 1 | El código que corriste, repasado | ¿Qué hace cada parte? |
| 2 | La "memoria" de esta AI | ¿Dónde se guarda lo aprendido? |
| 3 | El ciclo de aprendizaje | ¿Cómo se educa la predicción? |
| 4 | El `weight` (peso) | ¿Qué es lo que realmente aprende? |
| 5 | El `learning_rate` | ¿Por qué `0.01` y no `1`? |
| 6 | Las `epochs` (épocas) | ¿Por qué hay que repetir? |
| 7 | La fórmula mágica desarmada | `weight += learning_rate * error * x` |
| 8 | Analogía del arquero | Para que se te quede |
| 9 | Conexión con lo que viene | De UN peso a millones |

---

## 1. El código que corriste, repasado

```python
class SimpleAILearner:
    def __init__(self):
        self.weight = random.uniform(0, 5)   # arranca con un número AL AZAR
        self.learning_rate = 0.01            # cuánto se mueve por paso

    def predict(self, x):
        return self.weight * x               # toda la "inteligencia" está acá

    def train(self, training_data, epochs=100):
        for epoch in range(epochs):
            for x, y_actual in training_data:
                y_predicted = self.weight * x
                error = y_actual - y_predicted
                self.weight += self.learning_rate * error * x
```

Lo que vamos a desarmar es esa última línea: `self.weight += self.learning_rate * error * x`. **Esa línea es el corazón de todo el machine learning moderno**. Si la entendés, entendés el 80% del concepto.

---

## 2. La "memoria" de esta AI — y por qué te va a sorprender

### La pregunta intuitiva (mal planteada)

Cuando vos pensás "memoria de una AI", probablemente imaginás algo así:

```
Vio que x=1 → y=2
Vio que x=2 → y=4
Vio que x=3 → y=6
...
```

Una especie de **base de datos** donde la AI "anota" los ejemplos y los consulta después. **NO. Eso NO es lo que pasa.**

### Lo que realmente está pasando

Fijate qué atributos tiene `SimpleAILearner`:

```python
self.weight = random.uniform(0, 5)
self.learning_rate = 0.01
```

**DOS números. Solo dos.** Y de esos dos, solo UNO (`weight`) cambia durante el entrenamiento. El otro (`learning_rate`) es una constante que vos elegís.

> [!important] La memoria de esta AI es UN número
> Toda la "experiencia" de haber visto los 5 ejemplos de entrenamiento se **comprime** en el valor final de `self.weight` (~2.0). No guarda los ejemplos. No los "recuerda" en el sentido humano. Los **destila** en un parámetro.

Esto es PROFUNDAMENTE distinto a una base de datos. La AI no busca el ejemplo más parecido cuando le preguntas algo nuevo — **aplica un cálculo** usando el número que aprendió.

### ¿Y en una AI grande?

GPT-4 tiene ~1.7 **billones** (trillions en inglés) de pesos. ChatGPT no "guarda" todos los textos de internet — los **comprime** en esos pesos. Es la misma idea que viste hoy en el Hello World, escalada brutalmente.

> [!tip] La frase para que se te quede
> **Una AI no recuerda ejemplos. Aprende parámetros que resumen los ejemplos.**

---

## 3. El ciclo de aprendizaje — cómo se "educa" la predicción

Mirá este bloque del código:

```python
for x, y_actual in training_data:
    y_predicted = self.predict(x)        # 1. Adivina
    error = y_actual - y_predicted       # 2. Mide qué tan mal adivinó
    self.weight += self.learning_rate * error * x   # 3. Corrige
```

**Ese es TODO el ciclo de aprendizaje**. Tres pasos:

1. **Adivinar**: con el conocimiento actual (`self.weight`), predice un valor.
2. **Medir el error**: compara la predicción con la respuesta correcta.
3. **Corregir**: ajusta `self.weight` para que la próxima vez se equivoque menos.

Repetí esto miles, millones, billones de veces — y eso es machine learning. Literalmente. No hay magia adicional. Las redes neuronales modernas hacen exactamente esto, solo que con millones de pesos en lugar de uno.

### Visualizalo

```
Inicio:       weight = 3.47 (random)
              predict(1) = 3.47, pero debería ser 2.0  → error = -1.47
              ajusta weight ↓ un poquito

Iter 1:       weight = 3.46
              predict(2) = 6.92, pero debería ser 4.0  → error = -2.92
              ajusta weight ↓ un poquito más

...
Iter 500:     weight ≈ 2.0
              predict(x) ≈ 2x para cualquier x  ✓
```

El error EMPUJA al peso hacia su valor correcto, una y otra vez.

---

## 4. El `weight` (peso) — qué es lo que realmente aprende

### Definición concreta

En este código, `weight` es **un número**. Empieza al azar (`random.uniform(0, 5)`) y termina cerca de 2.0 (porque el patrón era `y = 2x`).

```python
def predict(self, x):
    return self.weight * x
```

La predicción es `weight * x`. Si `weight = 2`, entonces `predict(7) = 14`. Eso es. Esa es toda la "inteligencia".

### ¿Por qué se llama "peso"?

Porque en redes más grandes, cada entrada tiene **un peso distinto** que dice **cuánto importa esa entrada** para la decisión final. Imaginá una AI que decide si te dan un préstamo:

```
salario       → peso_1 = 0.8   (importa mucho)
edad          → peso_2 = 0.1   (importa poco)
deudas        → peso_3 = -0.9  (importa mucho, en contra)
```

Cada peso "pesa" la influencia de su entrada. Por eso se llama `weight`. En el Hello World hay solo una entrada (`x`), entonces hay solo un peso.

### Conexión con neurona biológica

En una neurona biológica, cada conexión sináptica tiene una **fuerza** distinta. Aprender = ajustar esas fuerzas. Es **exactamente** la misma idea. Por eso este algoritmo es el ancestro directo de las redes neuronales artificiales.

> [!info] Ya tienes un apunte previo
> Esto conecta con `apuntes/neurocomputacion-y-ai-engineer.md` que armaste el 2026-05-18. Acá viste la versión computacional minimalista de lo que ahí planteaste biológicamente.

---

## 5. El `learning_rate` — el tamaño del paso

```python
self.learning_rate = 0.01
```

### El problema que resuelve

Cuando la AI detecta que se equivocó, ¿cuánto debería corregir el `weight`? Hay dos extremos malos:

| Si corrige... | Qué pasa |
|---|---|
| **Demasiado poco** (`learning_rate = 0.0001`) | Tarda eternidades en aprender. Como aprender a manejar moviendo el volante un milímetro por curva. |
| **Demasiado** (`learning_rate = 1.0`) | "Sobre-corrige" y nunca encuentra el valor correcto. Como manejar dando volantazos enteros. |

`learning_rate = 0.01` es el **compromiso**: pasos chiquitos pero no microscópicos.

### Analogía: bajando una montaña en la niebla

Imaginá que querés llegar al valle (mínimo error) y estás en una ladera, con niebla densa (no ves el valle). Solo podés sentir la pendiente bajo tus pies. ¿Cuánto avanzás en cada paso?

- Pasos gigantes → te pasás del valle y subís por el otro lado.
- Pasos minúsculos → llegás dentro de un mes.
- Pasos medianos → en una hora estás en el valle.

`learning_rate` es **el tamaño de cada paso**. Es un **hiperparámetro**: NO se aprende, lo elegís vos. Encontrar el `learning_rate` correcto es uno de los artes oscuros del ML.

### Probá vos mismo

El propio script te invita:
```
- Experiment with the learning_rate (line 29)
```

Cambialo a `0.001` y a `0.5`. Mirá qué pasa con el error promedio en cada época. Esa es la mejor forma de internalizar el concepto: **rompelo a propósito**.

---

## 6. Las `epochs` (épocas) — cuántas pasadas

```python
def train(self, training_data, epochs=100):
    for epoch in range(epochs):
        for x, y_actual in training_data:
            ...
```

### Definición concreta

Una **época** = una pasada completa por TODOS los datos de entrenamiento.

En el Hello World hay 5 ejemplos. Con `epochs=100`, el AI ve los 5 ejemplos... **100 veces**. Total: 500 actualizaciones del `weight`.

### ¿Por qué hay que repetir?

Porque cada actualización del `weight` es **chiquita** (por el `learning_rate` bajo). Con una sola pasada, el `weight` apenas se mueve. Necesita repetir para que las correcciones se acumulen y converja al valor correcto.

### Analogía: estudiar para un examen

| Iteración | Equivalente |
|---|---|
| 1 ejemplo de training | Leer un ejercicio del libro |
| 1 epoch (todos los ejemplos) | Leer el libro entero una vez |
| 100 epochs | Leer el libro 100 veces |

¿Sirve leer un libro 100 veces? Depende. Si cada lectura cambia poquito tu entendimiento, sí, sumás. Si ya entendiste a la primera, las otras 99 no aportan nada (eso se llama **overfitting**, pero ese es tema de otro apunte).

### El balance

| Pocas epochs | Muchas epochs |
|---|---|
| AI mal entrenada (**underfitting**) | AI memoriza ejemplos pero falla en datos nuevos (**overfitting**) |
| Predicciones malas | Predicciones perfectas en training, malas en producción |

Es OTRO hiperparámetro que elegís vos.

---

## 7. La fórmula mágica desarmada

```python
self.weight += self.learning_rate * error * x
```

Esta es la línea que merece detenerse. Vamos pieza por pieza.

### Pieza 1: `error`

```python
error = y_actual - y_predicted
```

Si predijo MENOS de lo correcto → `error` es **positivo** → hay que **subir** el weight.
Si predijo MÁS de lo correcto → `error` es **negativo** → hay que **bajar** el weight.

El signo del error te dice **la dirección** del ajuste.

### Pieza 2: `x` (el input)

¿Por qué multiplicar por `x`? Acá está lo bonito. Mirá:

```
predict(x) = weight * x
```

Si `x` es grande, un cambio chico en `weight` produce un cambio GRANDE en la predicción.
Si `x` es chico, el mismo cambio en `weight` casi no afecta la predicción.

Entonces para corregir el mismo error, **necesitás ajustar más el weight cuando `x` es grande**. Multiplicar por `x` ajusta el tamaño de la corrección a la magnitud del input. Es **proporcional**.

### Pieza 3: `learning_rate`

Ya lo viste: amortigua el tamaño del paso para que no sobre-corrija.

### Junto

```python
ajuste = learning_rate * error * x
self.weight += ajuste
```

Se lee así: **"Ajustá el weight, en la dirección del error, proporcional al input, con un tamaño de paso controlado."**

> [!important] Esta fórmula tiene nombre
> Lo que acabas de leer es una versión simplificada del **descenso del gradiente** (*gradient descent*), el algoritmo que entrena casi todas las AIs del mundo, incluyendo GPT-4. Cuando llegues al Bloque 3, esto va a volver — pero ya lo viste.

---

## 8. Analogía del arquero (para que se quede)

Imagina un arquero novato aprendiendo a dar al blanco:

| Concepto del código | Equivalente del arquero |
|---|---|
| `weight` | El ángulo al que apunta su arco |
| `predict(x)` | Disparar una flecha |
| `y_actual` | Dónde está realmente el blanco |
| `error` | Cuánto se desvió la flecha |
| `learning_rate` | Cuánto corrige el ángulo después de cada tiro |
| `epoch` | Una ronda completa de prácticas |

**Sin `learning_rate`**: tira una flecha al norte del blanco, corrige el ángulo 90° al sur, tira otra al sur del blanco, vuelve a corregir 90° al norte. Nunca acierta.

**Con `learning_rate = 0.01`**: tira al norte, corrige 1°, tira un poco mejor, corrige 0.5°, tira casi perfecto, corrige 0.1°... converge al blanco.

La AI es **un arquero que ajusta su ángulo después de cada tiro**. Eso es. Eso es TODO.

---

## 9. Conexión con lo que viene

Lo que viste hoy es **una neurona** con **un peso**. Lo mínimo posible.

```
                            ┌─────────┐
              x ─────────→  │ weight  │ ─────────→  predict(x)
                            └─────────┘
                              ↑ se ajusta con el error
```

Una **red neuronal** es esto mismo, repetido miles o millones de veces:

```
                 ┌─→ neurona_1 (weight_1)
                 ├─→ neurona_2 (weight_2)
        x ───────┼─→ neurona_3 (weight_3)  ──→ combinar ──→ predict(x)
                 ├─→ neurona_4 (weight_4)
                 └─→ neurona_5 (weight_5)
```

Y una **red profunda** (deep neural network) tiene MUCHAS capas como esa, una atrás de la otra.

Pero la **lógica de aprendizaje** —el ciclo predict → error → ajuste— es la misma que viste hoy. Esa es la mejor noticia: **ya viste el núcleo conceptual**. Lo que viene es escala y complejidad de combinación, no nuevos conceptos fundamentales.

---

## TL;DR — lo que tenés que recordar

1. **La memoria de una AI son sus pesos**, no una base de datos de ejemplos. Comprime experiencia en parámetros.
2. **El ciclo de aprendizaje son 3 pasos**: predecir → medir error → ajustar pesos. Repetir.
3. **`weight`** es lo que la AI APRENDE. Empieza al azar, termina ajustado al patrón.
4. **`learning_rate`** es el tamaño del paso de ajuste. Vos lo elegís. Es un hiperparámetro.
5. **`epoch`** es una pasada completa por los datos. Más epochs = más oportunidades de ajustar, pero podés sobre-entrenar.
6. La fórmula clave: `weight += learning_rate * error * x` es **descenso del gradiente** simplificado — el algoritmo que entrena CASI TODA la AI moderna.

---

## Ejercicios para fijar (rompé el código a propósito)

1. Cambiá `learning_rate` a `0.0001`. ¿Cuántas epochs tarda en converger?
2. Cambiá `learning_rate` a `0.5`. ¿Qué pasa? ¿Converge o se rompe?
3. Cambiá el patrón de los datos a `y = 5x + 3`. ¿Aprende? ¿Por qué NO aprende exactamente eso? (pista: el modelo solo tiene UN peso, no tiene "constante")
4. Imprimí `self.weight` después de CADA actualización (no solo cada 20 epochs). Mirá cómo se mueve.
5. Inicializá `self.weight = 100`. ¿Aprende igual? ¿Tarda más?

---

## Links relacionados

- `apuntes/neurocomputacion-y-ai-engineer.md` — puente neurona biológica → artificial (2026-05-18)
- `python/apuntes/` — fundamentos de clases y métodos (lo que hace que entiendas la sintaxis del Hello World)
- Próximo apunte (cuando llegues al Bloque 3): **funciones de pérdida y descenso del gradiente formal**
