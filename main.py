import cv2
import numpy as np

img = cv2.imread('./color.png')

channel1 = img[:,:,0]
channel2 = img[:,:,1]
channel3 = img[:,:,2]

cv2.imwrite('c1.png',channel1)
cv2.imwrite('c2.png',channel2)
cv2.imwrite('c3.png',channel3)

rgba = cv2.cvtColor(img,cv2.COLOR_RGB2BGRA)
# the alpha channel is periodic from 0 to 255, if the value is out of this range, 
# it still works, with the equal effect as the corresponding value in 0~255
for i in range(500):
    rgba[:,:,3] = np.ones((112,112))*i
    cv2.imwrite('./rgba/'+str(i)+'.png',rgba)
