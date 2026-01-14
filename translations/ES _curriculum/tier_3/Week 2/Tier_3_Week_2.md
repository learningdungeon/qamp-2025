
# Semana 2 Tier 3: Formalismo Computacional y Dominio de la Fase

**Audiencia:** Universitarios / Avanzado

**Objetivo:** Transitar de una comprensión geométrica del qubit (la esfera de Bloch) al motor computacional subyacente: el álgebra lineal.

---

## Recapitulación: El Qubit como Vector de Estado

En la **Semana 1**, aprendimos que cualquier estado de qubit puede describirse por su posición en la esfera de Bloch. Matemáticamente, esta posición se define por un vector de estado, que escribimos en notación de Dirac como $\psi$.

Este vector es una combinación lineal (superposición) de los dos estados base, $|0\rangle$ y $|1\rangle$:

$$
\psi = \alpha |0\rangle + \beta |1\rangle
$$

Donde $\alpha$ y $\beta$ son números complejos llamados **amplitudes de probabilidad**. En álgebra lineal, representamos este vector abstracto como un vector columna $2 \times 1$:

$$
\psi = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}
$$

donde $|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ y $|1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

La **Regla de Born** (vista en la Semana 1) establece que la probabilidad de medir $|0\rangle$ o $|1\rangle$ es el cuadrado del módulo de su amplitud:

$$
P(0) = |\alpha|^2 \qquad P(1) = |\beta|^2
$$

Para que el estado sea válido, las probabilidades deben sumar 1:

$$
|\alpha|^2 + |\beta|^2 = 1 \quad \text{(Normalizado)}
$$

---

## Puertas Cuánticas como Matrices

Las puertas como $H$ (Hadamard) y $R_X$ (Tilt) pueden visualizarse como rotaciones en la esfera de Bloch.  
Ahora, trataremos estas puertas como lo que realmente son: **operadores matriciales**. Aplicar una puerta a un qubit es simplemente realizar una multiplicación de matrices.

Si un qubit está en un estado inicial $\psi_{in}$ y aplicamos una puerta $U$, el estado final es:

$$
U \cdot \psi_{in} = \psi_{out}
$$

Todas las puertas cuánticas deben ser **matrices unitarias**, lo que significa que preservan la longitud del vector (normalización): rotan el vector sin cambiar su magnitud, asegurando que las probabilidades sigan sumando 1.

---

## Recapitulación: Matrices de Puertas Fundamentales

### Puerta Pauli-X (NOT)

Equivalente a una rotación $R_X(\pi)$ (rotar por $\pi$ alrededor del eje $x$). Invierte $|0\rangle$ a $|1\rangle$ y viceversa.

$$
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

**Ejemplo:**

$$
X |0\rangle = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |1\rangle
$$

---

### Puerta Hadamard (Superposición)

Crea superposición. Rota de la base $Z$ ($|0\rangle$, $|1\rangle$) a la base $X$ ($|+\rangle$, $|-\rangle$).

$$
H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

**Ejemplo:**

$$
H |0\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = |+\rangle
$$

---

### Puerta $R_X$ (Rotación en X)

Rota el estado del qubit alrededor del eje $x$ de la esfera de Bloch.

$$
R_X(\theta) = \begin{pmatrix} \cos(\theta/2) & -i\sin(\theta/2) \\ -i\sin(\theta/2) & \cos(\theta/2) \end{pmatrix}
$$

**Ejemplo:**

$$
R_X(\pi) |0\rangle = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ -i \end{pmatrix}
$$

En este ejemplo, ignoramos el coeficiente $-i$, conocido como **fase global** (lo discutiremos más adelante).

---

### Puerta $R_Y$ (Rotación en Y)

Rota el estado del qubit alrededor del eje $y$ de la esfera de Bloch.

$$
R_Y(\theta) = \begin{pmatrix} \cos(\theta/2) & \sin(\theta/2) \\ -\sin(\theta/2) & \cos(\theta/2) \end{pmatrix}
$$

**Checkpoint:**  
¿Cómo actúa la puerta $R_Y$ sobre el qubit cuando el ángulo de rotación es $\pi$?

---

## La Puerta $R_Z$ y la Fase

La puerta $R_Z$ representa una rotación alrededor del eje $z$ de la esfera de Bloch.

$$
R_Z(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}
$$

### Ejemplo: Puerta Z ($R_Z(\pi)$)

Para $\theta = \pi$, $e^{-i\pi/2} = -i$ y $e^{i\pi/2} = i$.

$$
R_Z(\pi) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}
$$

Si factorizamos $-i$, obtenemos la forma estándar de la puerta Z:

$$
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

La puerta Z invierte el signo (la fase) del componente $|1\rangle$.

**Checkpoint:**  
Aplica la puerta Z a $|0\rangle$ y $|1\rangle$ y observa la diferencia en ambos resultados usando cálculo matricial.

---

### Ejemplo: Puerta S ($R_Z(\pi/2)$)

Para $\theta = \pi/2$:

$$
R_Z(\pi/2) = \begin{pmatrix} e^{-i\pi/4} & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
$$

La forma estándar de la puerta S es:

$$
S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}
$$

La puerta S aplica una fase de $i$ al componente $|1\rangle$.

---

## Fase vs. Probabilidad: El Efecto de $R_Z$

¿Qué hace realmente una puerta $R_Z$? ¿Por qué considerar la fase?

Supón un qubit en el estado $|+\rangle$ (superposición 50/50):

$$
|+\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

Aplicamos una puerta S a este estado:

$$
\psi_{out} = S|+\rangle = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i \end{pmatrix}
$$

**¿Cambió la probabilidad de medición?**

Usando la Regla de Born:

$$
P(0) = |\alpha|^2 = \left| \frac{1}{\sqrt{2}} \right|^2 = \frac{1}{2}
$$

$$
P(1) = |\beta|^2 = |i/\sqrt{2}|^2 = \frac{1}{2}
$$

Las probabilidades de medición son exactamente las mismas (50/50) que el estado $|+\rangle$ original.

Esto muestra que la rotación $R_Z$ es "oculta" o "sutil". No cambia las probabilidades de medición en la base $Z$, sino la **fase relativa** entre los coeficientes $\alpha$ y $\beta$.  
Esta fase es invisible si solo mides ese qubit, pero es **crítica** cuando interactúa con otros qubits (por ejemplo, en una puerta CNOT), ya que determina si los estados interfieren constructiva o destructivamente.

---

## Fase Global y Fase Relativa

La fase es una propiedad fundamental de los números complejos y lo que separa la computación cuántica de la probabilidad clásica. Debemos distinguir cuidadosamente entre dos tipos:

### Fase Global

Una fase global es un factor $e^{i\gamma}$ que multiplica **todo** el vector de estado.

$$
\psi' = e^{i\gamma} \psi
$$

La fase global es físicamente indistinguible:  
Cuando medimos el estado, no podemos distinguir entre $\psi$ y $\psi'$.

La Regla de Born solo se preocupa por el **módulo cuadrado** de las amplitudes, por lo que la fase global es inobservable.

### Fase Relativa

Una fase relativa es una diferencia de fase **entre** las amplitudes complejas de los estados base.

$$
\psi = \alpha |0\rangle + \beta |1\rangle \\
\psi' = \alpha |0\rangle + e^{i\phi} \beta |1\rangle
$$

Por ejemplo, los estados $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ y $\psi_{out} = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)$ son diferentes y tienen distinta fase relativa.

Aunque no cambia las probabilidades de medición en la base $Z$, sí cambia las probabilidades en otra base (como la base $X$).

---

## Interferencia: La raíz matemática

Esto es la raíz matemática de la **interferencia**.

Medimos ambos estados en la base $X$ (probabilidad de medir $|+\rangle$):

### Caso 1: $|+\rangle$

$$
P_+ = |\langle +|+\rangle|^2 = 1
$$

(El estado es $|+\rangle$, así que la probabilidad de medirlo es 100%).

### Caso 2: $\psi_{out} = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)$

$$
\langle +|\psi_{out}\rangle = \frac{1}{\sqrt{2}} \left( \langle 0| + \langle 1| \right) \cdot \frac{1}{\sqrt{2}} \left( |0\rangle + i|1\rangle \right) = \frac{1}{2} (1 + i)
$$

La probabilidad es:

$$
P_+ = \left| \frac{1 + i}{2} \right|^2 = \frac{1 + 1}{4} = \frac{1}{2}
$$

La fase relativa cambió la probabilidad de medir $|+\rangle$ de 100% a 50%.  
Esto prueba que la fase relativa es **físicamente real, medible y clave en los algoritmos cuánticos**.

---

## Checkpoint: Secuencia de puertas

Para encontrar el resultado de una secuencia de puertas, aplicamos las matrices una por una, comenzando por la derecha.

Si aplicamos la puerta 1 y luego la puerta 2, la operación es:

$$
\psi_{final} = \text{puerta}_2 \cdot \text{puerta}_1 \cdot \psi_{in}
$$

**Ejemplo:**

Un qubit inicia en el estado $|0\rangle$.  
Aplicamos una puerta Hadamard $H$, seguida de una puerta Z. ¿Cuál es el vector de estado final?

1. **Estado inicial:**

$$
|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

2. **Aplicar Hadamard:**

$$
H|0\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = |+\rangle
$$

3. **Aplicar Z:**

$$
Z|+\rangle = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix} = |-\rangle
$$
