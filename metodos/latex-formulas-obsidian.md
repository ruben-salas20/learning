---
tags: [tipo/cheatsheet, tema/latex, tema/obsidian, tema/matematicas]
fecha: 2026-05-18
---
# LaTeX en Obsidian — Fórmulas matemáticas

> Guía práctica para escribir matemáticas en tus notas. Obsidian usa MathJax, que implementa la mayoría de LaTeX matemático. No necesitas instalar nada extra.

---

## 1. Cómo activar LaTeX en Obsidian

Por defecto ya está activado. Solo escribe:

- **Inline** (dentro de un párrafo): encierra entre `$...$`
- **Bloque** (centrado, en su propia línea): encierra entre `$$...$$`

```markdown
El teorema de Pitágoras dice que $a^2 + b^2 = c^2$.

$$
a^2 + b^2 = c^2
$$
```

Se ve así:
- Inline: el teorema dice que $a^2 + b^2 = c^2$ dentro del texto.
- Bloque: ecuación centrada y más grande, sola en su línea.

---

## 2. Operaciones básicas

| Lo que quieres         | Código LaTeX     | Resultado        |                       |                   |
| ---------------------- | ---------------- | ---------------- | --------------------- | ----------------- |
| Suma / Resta           | `a + b - c`      | $a + b - c$      |                       |                   |
| Multiplicación (punto) | `a \cdot b`      | $a \cdot b$      |                       |                   |
| Multiplicación (cruz)  | `a \times b`     | $a \times b$     |                       |                   |
| División en línea      | `a / b`          | $a / b$          |                       |                   |
| Fracción               | `\frac{a}{b}`    | $\frac{a}{b}$    |                       |                   |
| Potencia               | `x^2` o `x^{10}` | $x^2$ / $x^{10}$ |                       |                   |
| Subíndice              | `x_i` o `x_{ij}` | $x_i$ / $x_{ij}$ |                       |                   |
| Raíz cuadrada          | `\sqrt{x}`       | $\sqrt{x}$       |                       |                   |
| Raíz n-ésima           | `\sqrt[n]{x}`    | $\sqrt[n]{x}$    |                       |                   |
| Valor absoluto         | `                | x                | ` o `\lvert x \rvert` | $\lvert x \rvert$ |

> [!tip] Potencias y subíndices de más de un carácter
> Si tienen más de un carácter, usa llaves: `x^{10}` → $x^{10}$, no `x^10` → $x^10$ (solo toma el `1`).

---

## 3. Letras griegas

Las más usadas en estadística y ML:

| Nombre | Minúscula | Mayúscula |
|---|---|---|
| alpha | `\alpha` → $\alpha$ | `A` |
| beta | `\beta` → $\beta$ | `B` |
| gamma | `\gamma` → $\gamma$ | `\Gamma` → $\Gamma$ |
| delta | `\delta` → $\delta$ | `\Delta` → $\Delta$ |
| epsilon | `\epsilon` → $\epsilon$ | `E` |
| theta | `\theta` → $\theta$ | `\Theta` → $\Theta$ |
| lambda | `\lambda` → $\lambda$ | `\Lambda` → $\Lambda$ |
| mu | `\mu` → $\mu$ | `M` |
| sigma | `\sigma` → $\sigma$ | `\Sigma` → $\Sigma$ |
| pi | `\pi` → $\pi$ | `\Pi` → $\Pi$ |
| rho | `\rho` → $\rho$ | `P` |
| phi | `\phi` → $\phi$ | `\Phi` → $\Phi$ |
| omega | `\omega` → $\omega$ | `\Omega` → $\Omega$ |
| eta | `\eta` → $\eta$ | `H` |
| xi | `\xi` → $\xi$ | `\Xi` → $\Xi$ |

---

## 4. Sumatorias, productos e integrales

### Sumatoria

```latex
\sum_{i=1}^{n} x_i
```
$$\sum_{i=1}^{n} x_i$$

### Sumatoria con fracción (ejemplo: media aritmética)

```latex
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
```
$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

### Productoria

```latex
\prod_{i=1}^{n} x_i
```
$$\prod_{i=1}^{n} x_i$$

### Integral definida

```latex
\int_a^b f(x)\, dx
```
$$\int_a^b f(x)\, dx$$

### Integral doble / triple

```latex
\iint_D f(x,y)\, dx\, dy \qquad \iiint_V f\, dV
```
$$\iint_D f(x,y)\, dx\, dy \qquad \iiint_V f\, dV$$

### Límite

```latex
\lim_{x \to \infty} \frac{1}{x} = 0
```
$$\lim_{x \to \infty} \frac{1}{x} = 0$$

---

## 5. Estadística y probabilidad

### Media y varianza

```latex
\mu = \frac{1}{n}\sum_{i=1}^n x_i
\qquad
\sigma^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \mu)^2
```
$$\mu = \frac{1}{n}\sum_{i=1}^n x_i \qquad \sigma^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \mu)^2$$

### Distribución normal

```latex
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(x-\mu)^2}{2\sigma^2}}
```
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

### Probabilidad condicional

```latex
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
```
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

### Teorema de Bayes

```latex
P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}
```
$$P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}$$

### Valor esperado

```latex
\mathbb{E}[X] = \sum_{x} x\, P(X = x)
```
$$\mathbb{E}[X] = \sum_{x} x\, P(X = x)$$

---

## 6. Álgebra lineal (vectores y matrices)

### Vector columna

```latex
\mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}
```
$$\mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}$$

### Matriz genérica

```latex
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
```
$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$$

### Producto punto y norma

```latex
\mathbf{u} \cdot \mathbf{v} = \sum_{i} u_i v_i
\qquad
\|\mathbf{v}\| = \sqrt{\sum_i v_i^2}
```
$$\mathbf{u} \cdot \mathbf{v} = \sum_{i} u_i v_i \qquad \|\mathbf{v}\| = \sqrt{\sum_i v_i^2}$$

### Transpuesta e inversa

```latex
A^\top \qquad A^{-1} \qquad (AB)^\top = B^\top A^\top
```
$$A^\top \qquad A^{-1} \qquad (AB)^\top = B^\top A^\top$$

---

## 7. Machine Learning / Deep Learning

### Función de costo MSE

```latex
\mathcal{L} = \frac{1}{n}\sum_{i=1}^n \left(\hat{y}_i - y_i\right)^2
```
$$\mathcal{L} = \frac{1}{n}\sum_{i=1}^n \left(\hat{y}_i - y_i\right)^2$$

### Cross-entropy (clasificación binaria)

```latex
\mathcal{L} = -\frac{1}{n}\sum_{i=1}^n \left[y_i \log(\hat{y}_i) + (1 - y_i)\log(1 - \hat{y}_i)\right]
```
$$\mathcal{L} = -\frac{1}{n}\sum_{i=1}^n \left[y_i \log(\hat{y}_i) + (1 - y_i)\log(1 - \hat{y}_i)\right]$$

### Softmax

```latex
\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}
```
$$\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}$$

### Sigmoid

```latex
\sigma(z) = \frac{1}{1 + e^{-z}}
```
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

### ReLU

```latex
\text{ReLU}(x) = \max(0, x)
```
$$\text{ReLU}(x) = \max(0, x)$$

### Gradiente descendente

```latex
\theta \leftarrow \theta - \alpha \nabla_\theta \mathcal{L}(\theta)
```
$$\theta \leftarrow \theta - \alpha \nabla_\theta \mathcal{L}(\theta)$$

### Atención (Attention) — Transformer

```latex
\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
```
$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

---

## 8. Símbolos y operadores frecuentes

| Símbolo | Código | Uso |
|---|---|---|
| $\infty$ | `\infty` | Infinito |
| $\partial$ | `\partial` | Derivada parcial |
| $\nabla$ | `\nabla` | Gradiente |
| $\approx$ | `\approx` | Aproximado |
| $\neq$ | `\neq` | Diferente |
| $\leq$ | `\leq` | Menor o igual |
| $\geq$ | `\geq` | Mayor o igual |
| $\in$ | `\in` | Pertenece |
| $\notin$ | `\notin` | No pertenece |
| $\subset$ | `\subset` | Subconjunto |
| $\cup$ | `\cup` | Unión |
| $\cap$ | `\cap$ | Intersección |
| $\forall$ | `\forall` | Para todo |
| $\exists$ | `\exists` | Existe |
| $\Rightarrow$ | `\Rightarrow` | Implica |
| $\Leftrightarrow$ | `\Leftrightarrow` | Si y solo si |
| $\mathbb{R}$ | `\mathbb{R}` | Reales |
| $\mathbb{N}$ | `\mathbb{N}` | Naturales |
| $\mathbb{Z}$ | `\mathbb{Z}` | Enteros |
| $\hat{y}$ | `\hat{y}` | Estimado / predicción |
| $\bar{x}$ | `\bar{x}` | Media muestral |
| $\tilde{x}$ | `\tilde{x}` | Aproximación |

---

## 9. Formato avanzado de ecuaciones

### Ecuaciones alineadas (con `&` como punto de alineación)

```latex
\begin{align}
f(x) &= x^2 + 3x + 2 \\
     &= (x+1)(x+2)
\end{align}
```
$$\begin{align} f(x) &= x^2 + 3x + 2 \\ &= (x+1)(x+2) \end{align}$$

### Sistema de ecuaciones

```latex
\begin{cases}
2x + y = 5 \\
x - y = 1
\end{cases}
```
$$\begin{cases} 2x + y = 5 \\ x - y = 1 \end{cases}$$

### Definición por partes

```latex
f(x) = \begin{cases}
x^2 & \text{si } x \geq 0 \\
-x  & \text{si } x < 0
\end{cases}
```
$$f(x) = \begin{cases} x^2 & \text{si } x \geq 0 \\ -x & \text{si } x < 0 \end{cases}$$

### Paréntesis que se ajustan al tamaño

```latex
\left( \frac{a}{b} \right) \quad \left[ \frac{a}{b} \right] \quad \left\{ \frac{a}{b} \right\}
```
$$\left( \frac{a}{b} \right) \quad \left[ \frac{a}{b} \right] \quad \left\{ \frac{a}{b} \right\}$$

> [!tip] Regla de oro
> Usa siempre `\left(` y `\right)` cuando el contenido lleva fracciones o sumatorias. Los paréntesis se escalan solos.

---

## 10. Texto dentro de fórmulas

Para mezclar texto normal dentro de una ecuación:

```latex
f(x) = x^2 \quad \text{para todo } x \in \mathbb{R}
```
$$f(x) = x^2 \quad \text{para todo } x \in \mathbb{R}$$

Espacios útiles:

| Código | Espacio |
|---|---|
| `\,` | Pequeño |
| `\;` | Mediano |
| `\quad` | Grande |
| `\qquad` | Muy grande |

---

## 11. Errores comunes

- ❌ `$\frac{a}{b$` — olvidar cerrar el `$`. Siempre en par.
- ❌ `x^10` → toma solo el `1`. Correcto: `x^{10}`.
- ❌ `x_ij` → toma solo la `i`. Correcto: `x_{ij}`.
- ❌ Usar `*` para multiplicar → en LaTeX no es símbolo matemático estándar. Usa `\cdot` o `\times`.
- ❌ Poner `\\` sin entorno `align` o `cases` para saltar línea → no funciona en bloque `$$`.
- ❌ Texto plano dentro de fórmula sin `\text{}` → se pone en cursiva y sin espacios.

---

## 12. Plantilla rápida — nota con fórmulas

```markdown
---
tags: [tema/estadistica, tipo/apunte]
fecha: YYYY-MM-DD
---

# Concepto: nombre

## Definición

Descripción en prosa. La fórmula central es:

$$
\text{fórmula principal aquí}
$$

## Desglose de variables

| Variable | Significado |
|---|---|
| $x$ | ... |
| $\mu$ | ... |

## Ejemplo numérico

Dado $n = 5$ y valores $x_i = \{2, 4, 4, 4, 5, 5, 7, 9\}$:

$$
\bar{x} = \frac{1}{8}(2+4+4+4+5+5+7+9) = 5
$$

## Notas relacionadas
- [[...]]
```

---

## Notas relacionadas

- [[markdown-y-obsidian]]
- [[mermaid-diagramas]]

---

*Cuando encuentres una fórmula nueva que uses seguido, agrégala aquí con su código.*
