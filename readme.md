# Fourier Drawing

A Python implementation of Fourier drawing that reconstructs image contours using rotating vectors (epicycles).

The project begins by extracting contours from an image using OpenCV. These contours are converted into complex-valued points and transformed into the frequency domain using a manually implemented Discrete Fourier Transform (DFT). Once the algorithm is verified, NumPy's Fast Fourier Transform (FFT) is used as an optimized alternative for improved performance.

The primary goal of this project is to understand the mathematics behind Fourier drawing rather than relying solely on existing libraries.

## Features

- Extract contours from images using OpenCV
- Convert contour coordinates into complex numbers
- Manual implementation of the Discrete Fourier Transform (DFT)
- Fourier coefficient visualization
- Epicycle animation for contour reconstruction
- Optional FFT implementation for faster computation
- Comparison between manual DFT and NumPy FFT

## Project Structure

```
.
├── main.py
├── contours.py
├── fourier.py
├── animation.py
└── test-images/
```

## Technologies

- Python
- OpenCV
- NumPy
- Matplotlib (or Pygame)

## Status

This project is currently under development. Additional features, documentation, mathematical explanations, and visual examples will be added as development progresses.

