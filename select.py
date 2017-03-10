import cv2 as cv
import numpy as np
import glob as gl
from matplotlib import pyplot as plt

folder = "/home/yida/Downloads/yida_pictures/9/not_touch/"
names = gl.glob(folder + "*.png")



def filter(img):
    lower = np.array([75,100,100])
    upper = np.array([100,120,110])
    filted = cv.inRange(img,lower, upper)
    filted_2 = np.zeros(np.shape(img))
    filted_2[:,:,2] = filted
    return filted,filted_2
    return filted_2


def filter_2(img):
    lower = np.array([130,123,128])
    upper = np.array([152,186,183])
    filted = cv.inRange(img,lower, upper)
    filted_2 = np.zeros(np.shape(img))
    filted_2[:,:,2] = filted
    return filted,filted_2
    # return filted_2


# for i in range(len(names)):
#     filename = names[i]
#     pic_num = int(filename.replace(folder,"").replace(".png",""))
#     savename = "/home/yida/Desktop/gripper/not_touch/"+str(pic_num)+".png"
#     img = cv.imread(filename)
#     # img_g = cv.GaussianBlur( img,(,11), 0, 0, cv.BORDER_DEFAULT )
#     new_img = img + filter(img)
#     cv.imwrite(savename,new_img)
pic_17 = cv.imread(folder+"68.png")
filted, filted_2 = filter(pic_17)
plt.imshow(filted)
# plt.imshow(filted_2+pic_17)
plt.show()
# print pic_17[320,355,:]
# print pic_17[363,418,:]
