#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

#from pprint import pprint
#pprint(data_dict)

max_salary = 0
max_salary_key = None

for key in data_dict:
	if data_dict[key]["salary"] != 'NaN' and data_dict[key]["salary"] > max_salary:
		max_salary = data_dict[key]["salary"]
		max_salary_key = key

data_dict.pop(max_salary_key, 0)

# Who made $6-8 mil bonus and over $1 mil salary

for key in data_dict:
	if data_dict[key]["salary"] != 'NaN' and data_dict[key]["bonus"] != 'NaN':
		if data_dict[key]["salary"] > 1.0e6 and data_dict[key]["bonus"] > 5.5e6:
			print key

features = ["salary", "bonus"]

data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
