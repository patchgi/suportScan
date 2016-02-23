# coding utf-8
import cv2
import numpy as np
import sys

THRESHOLD=128

def readImage(_filename,_th):
	input_image=cv2.imread(_filename)
	for x in range(input_image.shape[0]):
		for y in range(input_image.shape[1]):
			gray=(int(input_image[x,y][0])+int(input_image[x,y][1])+int(input_image[x,y][2]))/3

			if gray>_th:
				input_image[x,y]=[255,255,255]
			else:
				input_image[x,y]=[0,0,0]
	return input_image

def writeImage(cells,_filename):
	filename="R_"+_filename
	cv2.imwrite(filename,cells)

if __name__=="__main__":
	filename=sys.argv[1]
	input=readImage(filename,THRESHOLD)
	writeImage(input,filename)
