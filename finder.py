import cv2 as cv
import numpy as np
matrix = np.zeros((13,5,3))
folder = "/home/yida/Downloads/yida_pictures/9/not_touch/"
img = cv.imread(folder + "55.png")
matrix = img[411:425,298:303,:]

matrix_1 = matrix[:,:,0]
matrix_2 = matrix[:,:,1]
matrix_3 = matrix[:,:,2]

print np.max(matrix_1),np.min(matrix_1)
print np.max(matrix_2),np.min(matrix_2)
print np.max(matrix_3),np.min(matrix_3)
