import cv2
import image_contours
import dft
import fourier_components
import animation
image = cv2.imread('./test-images/umb.png')
if image is None:
    raise FileNotFoundError("Could not load image.")

contours = image_contours.extract_contours(image)
complex_contours = image_contours.contours_to_complex(contours)
contour_coeff = dft.extract_coefficients(complex_contours)

comp = fourier_components.build_components(contour_coeff)
animation.draw(comp)