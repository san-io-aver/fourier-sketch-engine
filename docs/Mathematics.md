# Mathematics

This document explains the mathematics behind Fourier Drawing, starting from the Fourier Series and ending with the Discrete Fourier Transform (DFT) used to reconstruct image contours.

---

## Fourier Series

Any periodic function can be approximated as a sum of sine and cosine waves:

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

For example:

- $C_1$ is the contribution of $\sin(x)$.
- $D_1$ is the contribution of $\cos(x)$.
- $C_2$ is the contribution of $\sin(2x)$.
- $D_2$ is the contribution of $\cos(2x)$.

The next question is:

> **How do we calculate these coefficients?**

To isolate the coefficient of a particular basis function, we multiply the entire Fourier series by that same basis function and integrate over one complete period.

For example, to find $C_1$, we multiply both sides by $\sin(x)$:

$$
f(x)\sin(x)=
C_0\sin(x)
+C_1\sin^2(x)
+D_1\sin(x)\cos(x)
+C_2\sin(2x)\sin(x)
+\cdots
$$

Now integrate both sides:

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
\right)
dx
$$

Because sine and cosine functions are **orthogonal**, every cross-term becomes zero:

$$
\int_{-\pi}^{\pi}\sin(mx)\sin(nx)\,dx=0
\qquad (m\ne n)
$$

$$
\int_{-\pi}^{\pi}\sin(mx)\cos(nx)\,dx=0
$$

The only term that survives is

$$
\int_{-\pi}^{\pi}f(x)\sin(x)\,dx
=
C_1\int_{-\pi}^{\pi}\sin^2(x)\,dx
=
C_1\pi.
$$

Therefore,

$$
C_1=\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\sin(x)\,dx
$$

Similarly,

$$
C_2=\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\sin(2x)\,dx
$$

and, in general,

$$
C_n=\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\sin(nx)\,dx
$$

Likewise, the cosine coefficients are

$$
D_n=\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\cos(nx)\,dx
$$

Orthogonality acts like a filter: when we multiply by one basis function and integrate, every other basis function averages to zero. This leaves only the coefficient of the basis function we are interested in.

---

## From Sine & Cosine to Complex Exponentials

While the Fourier Series is written using separate sine and cosine functions, implementing this directly in code is inconvenient because we would need to calculate two coefficients for every frequency.

Using **Euler's Formula**, we can combine sine and cosine into a single complex exponential:

$$
e^{i\theta}=\cos(\theta)+i\sin(\theta)
$$

Using this identity, every sine and cosine wave can be represented as a rotating vector in the complex plane.

Instead of calculating separate sine and cosine coefficients, we calculate a single **complex coefficient** for each frequency.

The Fourier coefficient for frequency $k$ is

$$
X_k=\sum_{n=0}^{N-1}
x_n\,e^{-i2\pi kn/N}
$$

where

- $x_n$ is the $n^{th}$ sample of the signal.
- $N$ is the total number of samples.
- $k$ is the frequency being analysed.
- $X_k$ is the complex Fourier coefficient.

Notice that the integral from the Fourier Series has become a summation.

This is because computers work with **discrete samples** instead of continuous functions.
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

Each iteration of the outer loop computes **one Fourier coefficient**.

The inner loop performs the summation

$$
\sum_{n=0}^{N-1}
x_n e^{-i2\pi kn/N}
$$

exactly as written in the mathematical formula.

The resulting coefficient is a **complex number**.

Its

- magnitude represents the radius of an epicycle,
- phase represents the starting angle,
- frequency is simply the current value of $k$.

Repeating this process for every frequency produces all the rotating vectors required to reconstruct the original signal.

---

## Applying the DFT to Image Contours

So far, the samples have represented values of a one-dimensional signal.

For Fourier Drawing, however, the samples are the coordinates of the contour extracted from an image.

Each contour point has the form

$$
(x,y)
$$

Instead of treating these as two separate values, we represent each point as a complex number

$$
z=x+yi
$$

For example,

$$
(10,20)
\longrightarrow
10+20i
$$

or in Python,

```python
complex_points = []

for point in contour:

    x = point[0][0]
    y = point[0][1]

    complex_points.append(complex(x, y))
```

The DFT equation itself does **not** change.

Instead of passing signal amplitudes into the transform, we now pass these complex coordinates.

$$
X_k=
\sum_{n=0}^{N-1}
z_n\,e^{-i2\pi kn/N}
$$

where $z_n$ is the complex representation of the $n^{th}$ contour point.

Each Fourier coefficient now contains three important pieces of information:

- **Magnitude** — the radius of the rotating vector.
- **Phase** — the starting angle of the vector.
- **Frequency** — how fast the vector rotates.

---

## From Fourier Coefficients to Epicycles

Each Fourier coefficient becomes one rotating vector (epicycle).

For every coefficient we compute

```python
radius = abs(coefficient)
phase = cmath.phase(coefficient)
frequency = k
```

The endpoint of one vector becomes the centre of the next vector.

Adding all of these rotating vectors together produces the final endpoint.

As time progresses, this endpoint traces the original contour.

In other words,

> **The Discrete Fourier Transform converts a sequence of points describing a shape into a collection of rotating circles whose combined motion redraws that shape.**

[← Back to README](../README.md)