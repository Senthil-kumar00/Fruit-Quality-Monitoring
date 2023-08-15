

# import the necessary packages
from helpers import pyramid
from helpers import sliding_window
import time
import cv2
import ColorExtract as CE
from colordescriptor import ColorDescriptor
import os

def process():

	cd = ColorDescriptor((8, 12, 3))

	# open the output index file for writing
	output = open("dataset.csv", "w")

	trainpath="Training/"
	trainlist= os.listdir(trainpath)

	for m in trainlist:
		print("m value",m)
		trainlist1= os.listdir(trainpath+m+"/")
		col=-1
		if m=="damage":
			col=1
		if m=="healthy":
			col=0

		for n in trainlist1:
			print("n value",n)
			
			print(trainpath+m+"/"+n)
			path=trainpath+m+"/"+n
			print(path)
			image = cv2.imread(path)
			(winW, winH) = (64, 64)

			for resized in pyramid(image, scale=1.5):
				for (x, y, window) in sliding_window(resized, stepSize=32, windowSize=(winW, winH)):
					if window.shape[0] != winH or window.shape[1] != winW:
						continue
					clone = resized.copy()
					cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
					x_plus_w=x + winW
					y_plus_h=y + winH
					crop_img = clone[y:y_plus_h, x:x_plus_w]
					cv2.imshow("cropped", crop_img)
					cv2.waitKey(0)
					features = cd.describe(crop_img)
					
					features = [str(f) for f in features]
					output.write("%s,%s,%s,%s\n" % (path,m,col,",".join(features)))
		
					cv2.imshow("Window", clone)
					cv2.waitKey(1)
					time.sleep(0.025)
	output.close()		
