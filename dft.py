import cmath


# c_points = [[(),(),()], [(),(),()], [(),(),()]]
def extract_coefficients(c_points):
    contour_coeff=[]
    for contour in c_points:
        N = len(contour)
        coefficients = [0j]*N
        for k in range(N):
            s = 0j
            for n in range(N):
                angle = (-2 * cmath.pi * k * n)/N
                s += contour[n]*cmath.exp(1j * angle) 

            coefficients[k] = s/N    
        contour_coeff.append(coefficients)    
    return contour_coeff        