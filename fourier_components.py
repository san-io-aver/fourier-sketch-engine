from dataclasses import dataclass
import cmath

@dataclass
class FourierComponent():
    frequency: int
    coeff: complex
    amplitude: float
    phase: float

def build_components(contour_coeff):

    """
    Convert Fourier coefficients into FourierComponent objects.

    Parameters
    ----------
    contour_coeff : list[list[complex]]
        A list where each element contains the Fourier coefficients
        corresponding to a single contour.

    Returns
    -------
    list[list[FourierComponent]]
        A list where each element contains the FourierComponent objects
        for a single contour, sorted in descending order of amplitude.
    """
    all_components = [] #list of all components of each contours
    for contour in contour_coeff:
        components = [] #stores components of single contour
        N = len(contour)
        # frequency is stored as : 0 1 2 3 4 -3 -2 -1
        for k, coeff in enumerate(contour):
            if k <= N // 2:
                freq = k
            else:
                freq = k - N
            circle = FourierComponent(
                frequency=freq,
                coeff=coeff,
                amplitude=abs(coeff),
                phase=cmath.phase(coeff)
            )
            components.append(circle)
        components.sort(key=lambda x: x.amplitude, reverse=True)
        all_components.append(components)
    return all_components
    