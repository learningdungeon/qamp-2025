## **Resumen y Puente: De Vectores Simples a Notación de Dirac**

Recuerda que el estado de un solo qubit se introdujo usando notación de vector simple, muy similar a lo que se ve en álgebra lineal básica.

En computación cuántica, el estado de un solo qubit, a menudo denotado como $|\psi\rangle$, se representa como un vector columna de dos componentes (estado base computacional):

$$
|\psi\rangle =
\begin{pmatrix} a \\ b \end{pmatrix}
=
a \begin{pmatrix} 1 \\ 0 \end{pmatrix}
+
b \begin{pmatrix} 0 \\ 1 \end{pmatrix}
=
a|0\rangle + b|1\rangle
$$

Aquí, $a$ y $b$ son números complejos que representan las amplitudes de probabilidad de encontrar el qubit en:
- el estado base $|0\rangle$
- o el estado base $|1\rangle$

La regla fundamental de probabilidad asegura que este es un estado cuántico válido y requiere que:

$$
|a|^2 + |b|^2 = 1
$$

Nota: $|a|^2 = a\,a^*$, donde $a^*$ es el conjugado complejo de $a$.

---

### ¿Qué pasa con más qubits?

Para dos qubits:

$$
|\phi\rangle =
\begin{pmatrix}
a \\ b \\ c \\ d
\end{pmatrix}
$$

donde $a$, $b$, $c$, $d$ son las amplitudes de probabilidad asociadas a los estados
$|00\rangle$, $|01\rangle$, $|10\rangle$ y $|11\rangle$, respectivamente.

La condición de normalización es:

$$
|a|^2 + |b|^2 + |c|^2 + |d|^2 = 1
$$

---

## **Notación de Dirac**

La notación de Dirac, o notación Bra–Ket, es el lenguaje estándar en mecánica cuántica para describir estados y operaciones en espacios de Hilbert.

El producto interno entre dos estados se escribe como:

$$
\langle \phi | \psi \rangle
$$

---

### **Punto de Control**
¿Cuáles son las combinaciones posibles de un sistema de 4 qubits usando $|0\rangle$ y $|1\rangle$ como estados base computacionales?

---

## **Producto Tensorial en Sistemas de Múltiples Qubits**

Por ejemplo, usando la base ordenada
$\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$:

$$
|1\rangle \otimes |0\rangle =
\begin{pmatrix} 0 \\ 1 \end{pmatrix}
\otimes
\begin{pmatrix} 1 \\ 0 \end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 1 \\ 0
\end{pmatrix}
$$

Así, un sistema de $N$ qubits vive en un espacio vectorial de dimensión $2^N$.

---

### **Punto de Control**
Calcula $|0\rangle \otimes |1\rangle$ y escríbelo como vector columna.  
¿Cuál es la dimensión del espacio de estados para 3 qubits?

---

## **El Vector Ket: $|\Psi\rangle$**

Para un sistema con $n$ estados base:

$$
|\Psi\rangle =
\begin{pmatrix}
a_1 \\ \vdots \\ a_n
\end{pmatrix}
=
\sum_{k=1}^n a_k |\psi_k\rangle
$$

Por ejemplo, para dos qubits:

$$
|\Phi\rangle =
a|00\rangle + b|01\rangle + c|10\rangle + d|11\rangle
$$

---

## **El Vector Bra: $\langle\Psi|$**

El bra asociado es el conjugado transpuesto del ket:

$$
\langle\Psi| =
(a_1^*, \ldots, a_n^*)
=
\sum_{k=1}^n a_k^* \langle\psi_k|
$$

---

### **Punto de Control**
Para el vector
$$
|P\rangle =
\begin{pmatrix}
2i \\ 5 \\ 7 + 2i
\end{pmatrix},
$$
determina $\langle P|$.

---

## **Producto Interno: $\langle\Psi|\Psi\rangle$**

Dados dos estados

$$
|\Phi\rangle = \sum_k \phi_k |k\rangle,
\qquad
|\Psi\rangle = \sum_k \psi_k |k\rangle,
$$

su producto interno es:

$$
\langle\Phi|\Psi\rangle =
\sum_{k=1}^n \phi_k^* \psi_k
$$

---

### **Punto de Control**
Para el vector $|P\rangle$, calcula $\langle P|P\rangle$.  
¿Está normalizado?  
Luego, evalúa $\langle 1|0\rangle$ y explica su significado físico.

---

## **Regla de Born**

La probabilidad de medir un estado $|\phi\rangle$ cuando el sistema está en $|\psi\rangle$ es:

$$
P = |\langle \phi | \psi \rangle|^2
$$

---

## **Normalización de Estados**

Para un estado no normalizado:

$$
|\gamma\rangle =
\begin{pmatrix}
c_1 \\ \vdots \\ c_n
\end{pmatrix},
$$

el estado normalizado es:

$$
|\gamma\rangle_{\text{norm}} =
\frac{1}{\sqrt{\sum_{k=1}^n |c_k|^2}}
\begin{pmatrix}
c_1 \\ \vdots \\ c_n
\end{pmatrix}
$$

---

## **Producto Externo**

El producto externo se define como:

$$
|\psi\rangle\langle\phi| =
\begin{pmatrix}
a_1 \\ \vdots \\ a_n
\end{pmatrix}
(b_1^*, \ldots, b_n^*)
=
\begin{pmatrix}
a_1 b_1^* & \cdots & a_1 b_n^* \\
\vdots & \ddots & \vdots \\
a_n b_1^* & \cdots & a_n b_n^*
\end{pmatrix}
$$

Si $|\psi\rangle = |\phi\rangle$, el operador resultante es un **operador de proyección**.

---

## **Operador de Proyección**

$$
P = |\psi\rangle\langle\psi|
$$

Propiedad de idempotencia:

$$
P^2 = P
$$

---

## **Modelando la Medición**

La medición respecto al estado base $|k\rangle$ se describe mediante:

$$
P_k = |k\rangle\langle k|
$$

y su acción sobre un estado es:

$$
P_k|\psi\rangle = |k\rangle\langle k|\psi\rangle
$$

---

## **Ejemplo: Proyección sobre $|0\rangle$**

$$
P_0 =
|0\rangle\langle 0|
=
\begin{pmatrix}
1 & 0 \\
0 & 0
\end{pmatrix}
$$

Aplicando $P_0$ a $|\psi\rangle = a|0\rangle + b|1\rangle$:

$$
P_0|\psi\rangle =
\begin{pmatrix}
a \\ 0
\end{pmatrix}
= a|0\rangle
$$

---

## **Estados Puros y Mixtos (Ruido Cuántico)**

- **Estado puro:**
$$
\rho = |\psi\rangle\langle\psi|
$$

- **Estado mixto:**
$$
\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|
$$

- Los elementos diagonales $\rho_{kk}$ representan probabilidades.
- Los elementos fuera de la diagonal representan coherencia cuántica.
