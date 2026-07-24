import cv2
import numpy as np
CANNY_LOW = 30
CANNY_HIGH = 200


def extract_contours(image : np.ndarray) -> tuple:

    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image,CANNY_LOW,CANNY_HIGH)

    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    return contours


def contours_to_complex(contours : tuple):
    # contours = [contour1,contour2,...]
    # contour = [[[x,y]],[x2,y2]],[x3,y3]]]
    complex_contours = []
    for contour in contours:
        complex_points=[] 
        for point in contour:
            # contour = [ point, point, point]; point = [[x,y]]
            x = point[0][0]
            y = point[0][1]
            complex_points.append(complex(x,y))
        complex_contours.append(complex_points)    
    return complex_contours


def main():
    image = cv2.imread('./test-images/banana.png')
    if image is None:
        raise FileNotFoundError("Could not load image.")
    
    contours = extract_contours(image)
    complex_contours = contours_to_complex(contours)
    print(complex_contours[:5])

    cv2.drawContours(image,contours,-1,(0,0,0),3)
    cv2.imshow('Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()