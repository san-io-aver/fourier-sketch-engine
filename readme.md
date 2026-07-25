# Fourier Drawing

A Python implementation of Fourier Drawing that reconstructs image contours using rotating vectors (epicycles).

The project begins by extracting contours from an image using OpenCV. These contours are converted into complex-valued points and transformed into the frequency domain using a manually implemented **Discrete Fourier Transform (DFT)**. After verifying the implementation, NumPy's **Fast Fourier Transform (FFT)** is used as an optimized alternative for improved performance.

The primary goal of this project is to understand the mathematics behind Fourier analysis rather than relying solely on existing libraries.

---

# Mathematical Foundation

## Fourier Series

Fourier's remarkable discovery states that **any periodic function can be represented as a sum of sine and cosine waves**.

$$
f(x)=
C_0
+C_1\sin(x)
+D_1\cos(x)
+C_2\sin(2x)
+D_2\cos(2x)
+C_3\sin(3x)
+D_3\cos(3x)
+\cdots
$$

Each coefficient represents the contribution of its corresponding basis function.

For example,

- $C_1$ is the contribution of $\sin(x)$.
- $D_1$ is the contribution of $\cos(x)$.
- $C_2$ is the contribution of $\sin(2x)$.
- $D_2$ is the contribution of $\cos(2x)$.

---

## Computing the Fourier Coefficients

The next question is:

> **How do we determine these coefficients?**

To isolate the coefficient of a particular basis function, we multiply the entire Fourier series by that same basis function and integrate over one complete period.

For example, to compute $C_1$, multiply both sides by $\sin(x)$.

$$
f(x)\sin(x)=
C_0\sin(x)
+C_1\sin^2(x)
+D_1\sin(x)\cos(x)
+C_2\sin(2x)\sin(x)
+\cdots
$$

Now integrate over one period.

$$
\int_{-\pi}^{\pi}f(x)\sin(x)\,dx
=
\int_{-\pi}^{\pi}
\left(
C_0\sin(x)
+C_1\sin^2(x)
+D_1\sin(x)\cos(x)
+C_2\sin(2x)\sin(x)
+\cdots
\right)dx
$$

Because sine and cosine functions are **orthogonal**, every cross term becomes zero.

$$
\int_{-\pi}^{\pi}\sin(mx)\sin(nx)\,dx=0
\qquad (m\neq n)
$$

$$
\int_{-\pi}^{\pi}\sin(mx)\cos(nx)\,dx=0
$$

The only surviving term is

$$
\int_{-\pi}^{\pi}f(x)\sin(x)\,dx
=
C_1
\int_{-\pi}^{\pi}\sin^2(x)\,dx
=
C_1\pi
$$

Therefore,

$$
C_1=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\sin(x)\,dx
$$

Similarly,

$$
C_n=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\sin(nx)\,dx
$$

and

$$
D_n=
\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\cos(nx)\,dx
$$

Orthogonality acts as a filter. Multiplying by one basis function and integrating causes every other basis function to average to zero, leaving only the coefficient we wish to compute.

---

# From Fourier Series to the Discrete Fourier Transform

Computers cannot evaluate continuous integrals directly. Instead, they work with a finite set of samples.

The continuous Fourier Series therefore becomes the **Discrete Fourier Transform (DFT)**.

Rather than using separate sine and cosine terms, we use **Euler's Formula**

$$
e^{i\theta}=\cos(\theta)+i\sin(\theta)
$$

which combines both into a single complex exponential.

The DFT coefficient for frequency $k$ is

$$
X_k=
\sum_{n=0}^{N-1}
x_n
e^{-i2\pi kn/N}
$$

where

- $x_n$ is the $n^{th}$ sample,
- $N$ is the total number of samples,
- $k$ is the frequency,
- $X_k$ is the complex Fourier coefficient.

Notice that the integral has been replaced by a summation because the input now consists of discrete samples.

---

## Manual DFT Implementation

The mathematical equation translates almost directly into Python.

```python
coefficients = []

N = len(samples)

for k in range(N):

    coefficient = 0j

    for n in range(N):

        angle = -2 * math.pi * k * n / N
        coefficient += samples[n] * cmath.exp(1j * angle)

    coefficient /= N
    coefficients.append(coefficient)
```

Each iteration of the outer loop computes one Fourier coefficient.

The inner loop evaluates

$$
\sum_{n=0}^{N-1}
x_n
e^{-i2\pi kn/N}
$$

exactly as written in the mathematical definition.

---

# Applying the DFT to Images

For ordinary signals, each sample is a single real number.

For image contours, each sample is a point

$$
(x,y)
$$

which is represented as the complex number

$$
z=x+iy
$$

For example,

```python
complex_points = []

for point in contour:
    x = point[0][0]
    y = point[0][1]

    complex_points.append(complex(x, y))
```

These complex points are passed directly into the DFT.

The resulting Fourier coefficient contains

- **Magnitude** → radius of the epicycle
- **Phase** → starting angle
- **Frequency** → angular velocity

---

# From Fourier Coefficients to Epicycles

Each Fourier coefficient becomes one rotating vector.

```python
radius = abs(coefficient)
phase = cmath.phase(coefficient)
frequency = k
```

The endpoint of one vector becomes the centre of the next.

As every vector rotates, the endpoint traces the original contour.

> **The Discrete Fourier Transform converts a sequence of contour points into a collection of rotating circles whose combined motion reconstructs the original drawing.**

---

# Working Demo

![Fourier Animation](assets/apple_silh.gif)

---

# Features

- Manual implementation of the Discrete Fourier Transform (DFT)
- Optional NumPy FFT implementation for comparison
- Image contour extraction using OpenCV
- Conversion of contours to complex numbers
- Fourier coefficient computation
- Epicycle-based contour reconstruction
- Real-time animation using Pygame

---

# Project Structure

```text
.
├── main.py
├── animation.py
├── fourier_components.py
├── dft.py
├── image_contours.py
└── test-images/
```

---

# Technologies

- Python
- NumPy
- OpenCV
- Pygame

---

# Status

This project is under active development. Future updates will include SVG support, improved contour extraction, additional mathematical explanations, and performance optimizations.