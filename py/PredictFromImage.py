

import cv2
import argparse
import numpy as np
from sklearn.cluster import KMeans
import ColorExtract as CE
from colordescriptor import ColorDescriptor
from sklearn.svm import SVC
import numpy as np
import pandas as pd
from helpers import pyramid
from helpers import sliding_window

cd = ColorDescriptor((8, 12, 3))



def svmalg(dataset,test_features):
	df = pd.read_csv(dataset)
	cols = [0,1,2]
	X=df.drop(df.columns[cols],axis=1)
	Y=df = df.iloc[:,2]
	dt = SVC()
	dt.fit(X,Y); # Build a forest of trees from training set
	test_features=np.array(test_features)
	test_features=test_features.reshape(1,-1)
	y_pred = dt.predict(test_features) 
	print(y_pred)
	return y_pred[0]





def process(dataset,path):
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
			features = cd.describe(crop_img)
			features = [str(f) for f in features]
			st=svmalg(dataset,features)
			print(st)
			if st==0:
				cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
				cv2.putText(clone, 'Healthy', (x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 1)
				cv2.imshow("cropped", crop_img)
				cv2.waitKey(0)

			if st==1:
				cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
				cv2.putText(clone, 'Damage', (x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 1)
				cv2.imshow("cropped", crop_img)
				cv2.waitKey(0)

#process("dataset.csv","88_100.jpg")