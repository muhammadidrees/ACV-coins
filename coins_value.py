import cv2
import numpy as np
import helpers as h

image_file = "data/pak_coins.jpg"

def main():
    # read image file
    image = cv2.imread(image_file) 
    
    # normalize image
    norm_img = h.normalize(image)


    circles = cv2.HoughCircles(norm_img, cv2.HOUGH_GRADIENT,  2, 120, minRadius=30, maxRadius=80)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            radius = i[2]

            # circle outline
            cv2.circle(norm_img, center, radius, (255, 255, 0), 3)

            # coin value
            value = h.radius2value(radius)
            cv2.putText(norm_img,value , center, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    
    circle_radai = [c[2] for c in circles[0]]
    print(list(set(circle_radai)))
    # show norm_img
    h.imshow(norm_img)

if __name__ == '__main__':
    main()