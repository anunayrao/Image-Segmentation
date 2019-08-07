import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)
from matplotlib import pyplot as plt
se = [[255,255,255],[255,255,255],[255,255,255]]
se = np.asarray(se)

def dilation(image, se):
	heigth ,width = image.shape
	pimg = [[ 0 for x in range(width + 2)] for w in range(height + 2)]
	pimg = np.asarray(pimg)
	dimg = [[ 0 for x in range(width + 2)] for w in range(height + 2)]
	dimg = np.asarray(dimg)
	img = [[ 0 for x in range(width)] for w in range(height)]
	img = np.asarray(img).astype(np.uint8)
	for i in range(height):
		for j in range(width):
			dimg[i+1][j+1] = image[i][j]
			pimg[i+1][j+1] = image[i][j]
	for i in range(height):
		for j in range(width):
			if((pimg[i][j]== se[0][0]) or (pimg[i][j+1]==se[0][1]) or (pimg[i][j+2]==se[0][2]) or (pimg[i+1][j]==se[1][0]) or (pimg[i+1][j+1]==se[1][1]) or (pimg[i+1][j+2]==se[1][2]) or (pimg[i+2][j]==se[2][0]) or (pimg[i+2][j+1]==se[2][1]) or (pimg[i+2][j+2]==se[2][2])):
				dimg[i+1][j+1] = 255
			else:
				dimg[i+1][j+1] = 0
	for i in range(height):
		for j in range(width):
			img[i][j]= dimg[i+1][j+1]
			
	return img

def erosion(image, se):
	height,width = image.shape
	pimg = [[ 255 for x in range(width + 2)] for w in range(height + 2)]
	pimg = np.asarray(pimg)
	dimg = [[ 255 for x in range(width + 2)] for w in range(height + 2)]
	dimg = np.asarray(dimg)
	img = [[ 255 for x in range(width)] for w in range(height)]
	img = np.asarray(img)
	for i in range(height):
		for j in range(width):
			dimg[i+1][j+1] = image[i][j]
			pimg[i+1][j+1] = image[i][j]
	for i in range(height):
		for j in range(width):
			if((pimg[i][j]== se[0][0]) and (pimg[i][j+1]==se[0][1]) and (pimg[i][j+2]==se[0][2]) and (pimg[i+1][j]==se[1][0]) and (pimg[i+1][j+1]==se[1][1]) and (pimg[i+1][j+2]==se[1][2]) and (pimg[i+2][j]==se[2][0]) and (pimg[i+2][j+1]==se[2][1]) and (pimg[i+2][j+2]==se[2][2])):
				dimg[i+1][j+1] = 255
			else:
				dimg[i+1][j+1] = 0
	for i in range(height):
		for j in range(width):
			img[i][j]= dimg[i+1][j+1]
			
	return img


image = cv2.imread('segment.jpg',0)
height,width = image.shape
p = [[ 0 for x in range(width)] for w in range(height)]
p = np.asarray(p).astype(np.uint8)
o = [[ 0 for x in range(width)] for w in range(height)]
o = np.asarray(o).astype(np.uint8)
threshold =  cv2.imread('segment.jpg',0)
for i in range(height):
	for j in range(width):
		if(image[i][j]<204):
			threshold[i][j] = 0
			p[i][j]=0
		else:
			threshold[i][j] = image[i][j]
			p[i][j]=255
#retval, threshold = cv2.threshold(image, 204, 255, cv2.THRESH_BINARY)
#cv2.imshow('original',image)
#cv2.waitKey(0)
#cv2.imshow('threshold',threshold)
cv2.imwrite('threshold.png',threshold)
#cv2.waitKey(0)

eroded = erosion(p,se)
cv2.imwrite('threshold-eroded.png',eroded)
eroded = eroded/255
#cv2.imshow('d',eroded)
#cv2.waitKey(0)


