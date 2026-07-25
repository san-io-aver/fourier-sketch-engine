# Fourier Drawing

A Python implementation of Fourier Drawing that reconstructs image contours using rotating vectors (epicycles).

The project begins by extracting contours from an image using OpenCV. These contours are converted into complex-valued points and transformed into the frequency domain using a manually implemented Discrete Fourier Transform (DFT). Once the algorithm is verified, NumPy's Fast Fourier Transform (FFT) is used as an optimized alternative for improved performance.

The primary goal of this project is to understand the mathematics behind Fourier drawing rather than relying solely on existing libraries.

---

## Mathematics

A complete mathematical derivation of the algorithm is available in **[docs/Mathematics.md](docs/Mathematics.md)**.

It covers:

- Fourier Series
- Orthogonality of sine and cosine
- Derivation of Fourier coefficients
- Euler's Formula
- Discrete Fourier Transform (DFT)
- Applying the DFT to image contours
- Converting Fourier coefficients into epicycles

---

## Working Demo

![Fourier Animation](assets/apple_silh.gif)

---

## Features

- Extract contours from images using OpenCV
- Convert contour coordinates into complex numbers
- Manual implementation of the Discrete Fourier Transform (DFT)
- Fourier coefficient visualization
- Epicycle animation for contour reconstruction
- Optional FFT implementation for faster computation
- Comparison between manual DFT and NumPy FFT

---

## Project Structure

```text
.
├── main.py
├── animation.py
├── fourier_components.py
├── dft.py
├── image_contours.py
├── docs/
│   └── Mathematics.md
├── assets/
│   └── apple_silh.gif
└── test-images/
```

---

## Technologies

- Python
- OpenCV
- NumPy
- Pygame

---

## Status

This project is currently under development. Additional features, documentation, mathematical explanations, and visual examples will be added as development progresses.