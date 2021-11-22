import cv2 #pip install opencv-python
import numpy as np
img1 = cv2.imread('mdu1.jpg')#讀照片
img2 = cv2.imread('mdu2.jpg')#讀照片
print(img1.shape)
print(img2.shape)
imgup = np.hstack((img1,img2))#平行
imgdown = np.hstack((img2,img1))
imgCom=np.vstack((img1,img2))#直的
cv2.imshow('img1',img1)#檢視照片
cv2.imshow('imgdown',imgdown)#檢視照片
cv2.imshow('imgCom',imgCom)#檢視照片
cv2.waitKey(0)