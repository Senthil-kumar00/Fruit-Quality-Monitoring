import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn import linear_model
#from sklearn.model_selection cross_validation
from scipy.stats import norm


from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from random import seed
from random import randrange
from csv import reader
import csv
import numpy as np
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

from sklearn.svm import SVC

def process(path):
	df = pd.read_csv(path)

	cols = [0,1,2]
	X=df.drop(df.columns[cols],axis=1)
	Y=df = df.iloc[:,2]
	print(X)
	print(Y)

	# Splitting dataset into training and test set
	train_features, test_features, train_labels, test_labels = train_test_split(X, Y, test_size =.20)

	dt = SVC()
	dt.fit(train_features, train_labels.ravel());
	y_pred = dt.predict(test_features) 
	print(y_pred)

	result2=open("results/resultSVM.csv","w")
	result2.write("ID,Predicted Value" + "\n")
	for j in range(len(y_pred)):
	    result2.write(str(j+1) + "," + str(y_pred[j]) + "\n")
	result2.close()
	
	mse=mean_squared_error(test_labels, y_pred)
	mae=mean_absolute_error(test_labels, y_pred)
	r2=r2_score(test_labels, y_pred)
	
	
	print("---------------------------------------------------------")
	print("MSE VALUE FOR SVM IS %f "  % mse)
	print("MAE VALUE FOR SVM IS %f "  % mae)
	print("R-SQUARED VALUE FOR SVM IS %f "  % r2)
	rms = np.sqrt(mean_squared_error(test_labels, y_pred))
	print("RMSE VALUE FOR SVM IS %f "  % rms)
	ac=accuracy_score(test_labels,y_pred)
	print ("ACCURACY VALUE SVM IS %f" % ac)
	print("---------------------------------------------------------")
	

	result2=open('results/SVMMetrics.csv', 'w')
	result2.write("Parameter,Value" + "\n")
	result2.write("MSE" + "," +str(mse) + "\n")
	result2.write("MAE" + "," +str(mae) + "\n")
	result2.write("R-SQUARED" + "," +str(r2) + "\n")
	result2.write("RMSE" + "," +str(rms) + "\n")
	result2.write("ACCURACY" + "," +str(ac) + "\n")
	result2.close()
	
	
	df =  pd.read_csv('results/SVMMetrics.csv')
	acc = df["Value"]
	alc = df["Parameter"]
	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  
	
	fig = plt.figure()
	plt.bar(alc, acc,color=colors)
	plt.xlabel('Parameter')
	plt.ylabel('Value')
	plt.title('SVM Metrics Value')
	fig.savefig('results/SVMMetricsValue.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()
	
#process("dataset.csv")	
