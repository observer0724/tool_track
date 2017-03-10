import cv2 as cv
import numpy as np
import glob as gl
from matplotlib import pyplot as plt

folder = "/home/user/Desktop/yida/yida_pictures/11/touch/"
names = gl.glob(folder + "*.png")



def filter(img):
    lower = np.array([75,100,100])
    upper = np.array([100,120,110])
    filted = cv.inRange(img,lower, upper)
    filted_2 = np.zeros(np.shape(img))
    filted_2[:,:,2] = filted
    # return filted,filted_2
    return filted_2


def filter_2(img):
    lower = np.array([120,123,128])
    upper = np.array([152,186,183])
    filted = cv.inRange(img,lower, upper)
    filted_2 = np.zeros(np.shape(img))
    filted_2[:,:,2] = filted
    # return filted,filted_2
    return filted_2




def do_canny(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray2 = gray[5:,:]
    canny = cv.Canny(gray2,200,250)
    return canny
def do_sobel(img):
    img_g = cv.GaussianBlur( img,(3,3), 0, 0, cv.BORDER_DEFAULT )
    gray = cv.cvtColor(img_g, cv.COLOR_BGR2GRAY)
    sobelx = cv.Sobel(gray,cv.CV_16S,1,0,ksize=3)
    sobely = cv.Sobel(gray,cv.CV_16S,0,1,ksize=3)
    abs_x = cv.convertScaleAbs(sobelx)
    abs_y = cv.convertScaleAbs(sobely)
    grad = cv.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    grad_2 = cv.inRange(grad,np.array([10]),np.array([75]))
    return grad_2
for i in range(len(names)):
    filename = names[i]
    pic_num = int(filename.replace(folder,"").replace(".png",""))
    savename = "/home/user/Desktop/yida/gripper/touch/"+str(pic_num)+".png"
    img = cv.imread(filename)
    filted = do_canny(img)
    # deleter = np.zeros(np.shape(img))
    # deleter[:,:,0] = filted
    # deleter[:,:,1] = filted
    # deleter[:,:,2] = filted
    # del_pic = img-deleter
    temper = np.zeros(np.shape(img))
    temper[5:,:,1] = filted
    new_img = img + temper
    cv.imwrite(savename,new_img)
# pic_17 = cv.imread(folder+"22.png")
#
# filted = do_sobel(pic_17)
# deleter = np.zeros(np.shape(pic_17))
# deleter[:,:,0] = filted
# deleter[:,:,1] = filted
# deleter[:,:,2] = filted
# del_pic = pic_17-deleter
# new_pic = filter(del_pic)
# cv.imwrite("/home/user/Desktop/filted.png",new_pic)
# plt.imshow(filted)
# plt.show()
