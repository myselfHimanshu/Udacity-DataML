#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

clf=svm.SVC(C=10000.,kernel='linear')

'''
for C in [10.,100.,1000.,10000.]:
	clf=svm.SVC(C=C,kernel='rbf')
	clf.fit(features_train,labels_train)
	pred=clf.predict(features_test)
	accuracy=accuracy_score(pred,labels_test)
	print accuracy,C
'''
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

t1=time()
pred=clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

#print pred[10],pred[26],pred[50]
#print sum(pred)

accuracy=accuracy_score(pred,labels_test)
print accuracy




#########################################################


