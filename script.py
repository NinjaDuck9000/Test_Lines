import cv2
import numpy as np
from random import randint
import curses

img_number = str(randint(1, 292))
img = cv2.imread('Images/Street' + img_number +'.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

def drawLines(format):
    if (format == "1"):
        lines = cv2.HoughLines(edges,1,np.pi/180,120)
        for line in lines:
            for rho,theta in line:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))

                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    elif (format == "2"):
        minLineLength = 30
        maxLineGap = 10
        lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    else:
        print("invalid format.")
        return

cv2.imshow("Base Image", img)
drawLines(input("Enter format number "))
cv2.imshow("Hough Lines", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Edges Image", edges)
if (cv2.waitKey() == 27):
    cv2.destroyAllWindows()
if (cv2.waitKey() == 16):
    cv2.destroyWindow("Hough Lines")
    cv2.imshow("Hough Lines", img)