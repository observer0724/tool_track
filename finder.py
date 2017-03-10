import cv2 as cv
import numpy as np
matrix = np.zeros((21,9,3))
folder = "/home/user/Desktop/yida/yida_pictures/9/not_touch/"
img = cv.imread(folder + "68.png")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# matrix = hsv[175:295,295:303,:]
#
# matrix_1 = matrix[:,:,0]
# matrix_2 = matrix[:,:,1]
# matrix_3 = matrix[:,:,2]
#
# print np.max(matrix_1),np.min(matrix_1)
# print np.max(matrix_2),np.min(matrix_2)
# print np.max(matrix_3),np.min(matrix_3)
print hsv[299,182,:]
