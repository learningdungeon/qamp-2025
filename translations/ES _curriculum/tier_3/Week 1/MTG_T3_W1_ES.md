
## **Resumen y Puente: De Vectores Simples a Notación de Dirac**

Recuerda que el estado de un solo qubit se introdujo usando notación de vector simple, muy similar a lo que se ve en álgebra lineal de preparatoria.

En computación cuántica, el estado de un solo qubit, a menudo denotado como $\psi$, se representa como un vector columna de dos componentes (estado base computacional):

$$
\psi = \begin{pmatrix} a \\ b \end{pmatrix} = a \begin{pmatrix} 1 \\ 0 \end{pmatrix} + b \begin{pmatrix} 0 \\ 1 \end{pmatrix} = a|0\rangle + b|1\rangle
$$

Aquí, $a$ y $b$ son números complejos que representan las amplitudes de probabilidad de encontrar el qubit en el:
- estado base $|0\rangle$ (correspondiente a $a$)
- o el estado base $|1\rangle$ (correspondiente a $b$)

La regla fundamental de probabilidad asegura que este es un estado cuántico válido y requiere que la suma de los cuadrados de las magnitudes absolutas de las amplitudes sea igual a uno:

$$
|a|^2 + |b|^2 = 1
$$

Nota: $|a|^2 = a \times a^*$, donde $a^*$ es el conjugado complejo de $a$.

---

### ¿Qué pasa con más qubits?

Para dos qubits:

$$
\phi = \begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix}
$$

Donde $a$, $b$, $c$, $d$ son números complejos que representan las amplitudes de probabilidad de los estados $|00\rangle$, $|01\rangle$, $|10\rangle$, $|11\rangle$ respectivamente.

La condición de normalización es:

$$
|a|^2 + |b|^2 + |c|^2 + |d|^2 = 1
$$

---

## **Notación de Dirac**

La notación de Dirac, o notación Bra-Ket, es el lenguaje estándar en mecánica cuántica para representar estados y operaciones en el espacio de Hilbert.

El producto interno (o producto punto) de dos vectores se representa como:

$$
\langle \text{bra} | \text{ket} \rangle
$$

---

### **Punto de Control**
¿Cuáles son las combinaciones posibles de un sistema de 4 qubits con $|0\rangle$ y $|1\rangle$ como estados base computacionales?

---

## **Producto Tensorial en Sistemas de Múltiples Qubits**

Por ejemplo:

$$
|1\rangle \otimes |0\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \otimes \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}
$$

Así, en un sistema de 2 qubits tenemos un vector columna de 4 dimensiones. El número de estados base crece como $2^N$, donde $N$ es el número de qubits.

---

### **Punto de Control**
Calcula $|0\rangle \otimes |1\rangle$ y escríbelo como vector columna. ¿Cuál es la dimensión del espacio de estados para 3 qubits?

---

## **El Vector Ket: $|\Psi\rangle$**

Para un sistema de $n$ estados:

$$
|\Psi\rangle = \begin{pmatrix} a_1 \\ \vdots \\ a_n \end{pmatrix}
$$

o

$$
|\Psi\rangle = a_1 |\psi_1\rangle + a_2 |\psi_2\rangle + \ldots + a_n |\psi_n\rangle = \sum_{n} a_n |\psi_n\rangle
$$

Por ejemplo, para dos qubits:

$$
|\Phi\rangle = a|00\rangle + b|01\rangle + c|10\rangle + d|11\rangle
$$

---

## **El Vector Bra: $\langle\Psi|$**

La notación bra es el conjugado transpuesto del ket:

$$
\langle\Psi| = (a_1^*, \ldots, a_n^*)
$$

o

$$
\langle\Psi| = a_1^* \langle\psi_1| + a_2^* \langle\psi_2| + \ldots + a_n^* \langle\psi_n| = \sum_{n} a_n^* \langle\psi_n|
$$

---

### **Punto de Control**
Para un vector $|P\rangle = \begin{pmatrix} 2i \\ 5 \\ 7+2i \end{pmatrix}$, determina $\langle P|$.

---

## **Producto Interno: $\langle\Psi|\Psi\rangle$**

El producto interno se calcula como:

$$
\langle\Phi|\Psi\rangle = \sum_{k=1}^n b_k^* a_k
$$

---

### **Punto de Control**
Para $|P\rangle = \begin{pmatrix} 2i \\ 5 \\ 7+2i \end{pmatrix}$, determina $\langle P|P\rangle$. ¿El resultado es igual a 1 (normalizado)?  
Luego, determina $\langle 1|0\rangle$, ¿qué significa ese resultado?

---

## **Regla de Born**

La probabilidad de medir un estado es el cuadrado absoluto de la amplitud:

$$
P = |\langle \phi | \psi \rangle|^2
$$

Por ejemplo, para un qubit:

$$
|\psi\rangle = a|0\rangle + b|1\rangle
$$

La condición de normalización es:

$$
|a|^2 + |b|^2 = 1
$$

Para un estado no normalizado:

$$
|\gamma\rangle = \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix}
$$

La normalización es:

$$
|\gamma\rangle_{\text{normalizado}} = \frac{1}{\sqrt{\sum_n |c_n|^2}} \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix}
$$

---

### **Punto de Control**
Supón que tienes un estado de dos qubits no normalizado $|\gamma\rangle = \begin{pmatrix} 2 \\ i \\ 0 \\ 1 \end{pmatrix}$.  
Encuentra el estado $|\gamma\rangle$ normalizado.

---

## **Producto Externo**

El producto externo de dos vectores es:

$$
|\psi\rangle\langle\phi| = 
\begin{pmatrix}
a_1 \\ \vdots \\ a_n
\end{pmatrix}
(b_1^*, \ldots, b_n^*) =
\begin{pmatrix}
a_1 b_1^* & \ldots & a_1 b_n^* \\
\vdots & \ddots & \vdots \\
a_n b_1^* & \ldots & a_n b_n^*
\end{pmatrix}
$$

Cuando los dos estados son iguales, $|\psi\rangle\langle\psi|$, la matriz resultante es el **operador de proyección** y forma la **matriz de densidad** $\rho$ para un estado puro.

---

## **El Operador de Proyección**

Definición matemática:

$$
P = |\psi\rangle\langle\psi|
$$

Propiedad de idempotencia:

$$
P^2 = P
$$

---

## **Modelando la Medición**

Al medir un estado $|\psi\rangle$ respecto a un estado base $|k\rangle$:

$$
P_k = |k\rangle\langle k|
$$

$$
P_k|\psi\rangle = \langle k|\psi\rangle |k\rangle
$$

---

## **Ejemplo Simple: Proyección sobre $|0\rangle$**

$$
P_0 = |0\rangle\langle 0| = 
\begin{pmatrix} 1 \\ 0 \end{pmatrix}
(1, 0) =
\begin{pmatrix}
1 & 0 \\
0 & 0
\end{pmatrix}
$$

Aplicando $P_0$ a $|\psi\rangle = a|0\rangle + b|1\rangle$:

$$
P_0|\psi\rangle = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} a \\ 0 \end{pmatrix} = a|0\rangle
$$

---

## **Integración de Ruido: Modelos Formales (Estados Puros vs. Mixtos)**

- **Matriz de Densidad de Estado Puro:**
  $$
  \rho = |\psi\rangle\langle\psi|
  $$

- **Matriz de Densidad de Estado Mixto:**
  $$
  \rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|
  $$

- **Elementos diagonales:** $\rho_{kk}$ dan las probabilidades de medición.
- **Elementos fuera de la diagonal:** $\rho_{jk}$, $j \neq k$, representan coherencia (superposición y entrelazamiento).

---

¿Quieres que te ayude a convertir algún documento completo o sección específica a este formato? Si tienes ecuaciones concretas que quieras transformar, ¡envíalas y las convierto!
``
