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
cv2.destroyAllWindows()
