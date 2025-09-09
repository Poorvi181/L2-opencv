#Basic utility function
import cv2
import numpy as np
img1=cv2.imread("Buildings.jpg")
img2=cv2.imread("Space.jpg")
sum=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow("Space Buildings",sum)
cv2.waitKey(0)
minus=cv2.subtract(img2,img1)
cv2.imshow("minus",minus)
cv2.waitKey(0)
img3=cv2.imread("Pika.png")
cv2.imshow("Og image",img3)
cv2.waitKey(0)
img4=cv2.resize(img3,(200,200))
cv2.imshow("Resized image",img4)
cv2.waitKey(0)
#erosion =corners are trimmed in erosion
karnel=np.ones((5,5),np.uint8)
img5=cv2.erode(img3,karnel)
cv2.imshow("eroded image",img5)
cv2.waitKey(0)
#Gaussian Blur- used mostly in machine learning preprocessing steps.
gausian=cv2.GaussianBlur(img3,(9,9),0)
cv2.imshow("pika",gausian)
cv2.waitKey(0)
#Median Blur- used in digital processing preserves edges but removes noise.
median=cv2.medianBlur(img3,17)
cv2.imshow("clear",median)
cv2.waitKey(0)
#Bilateral Blur- only sharp edges preserved here.
a= cv2.bilateralFilter(img3,9,77,79)
#9-diameter of the pixel large in value= more blur
#77=sigma color- how much color difference is allowed higher= more colors get blurred together.
#79-sigma space- how far can pixels influence eachother higher= more distance pixels contribute to the blur.
cv2.imshow("Bilateral",a)
cv2.waitKey(0)
b=cv2.imread("borderimg.jpg")
c=cv2.copyMakeBorder(b,10,10,11,10,cv2.BORDER_CONSTANT,value=(25,25,117))
cv2.imshow("border",c)
cv2.waitKey(0)
d=cv2.copyMakeBorder(b,10,10,11,10,cv2.BORDER_REFLECT,value=(25,25,117))
cv2.imshow("border",d)
cv2.waitKey(0)

cv2.destroyAllWindows()


