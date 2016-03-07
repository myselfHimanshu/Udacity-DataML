#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print len(enron_data)
print len(enron_data["SKILLING JEFFREY K"])
#print enron_data["SKILLING JEFFREY K"].keys()
print sum(1 for i in enron_data if enron_data[i]['poi']==True)
#print [i  for i in enron_data if enron_data[i]['poi']==True]

print enron_data["PRENTICE JAMES"]['total_stock_value']
print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print enron_data["SKILLING JEFFREY K"]['exercised_stock_options']
count1=0
count2=0
count3=0
count4=0
for word in enron_data:
	if enron_data[word]['salary']!='NaN':count1+=1
	if enron_data[word]['email_address']!='NaN':count2+=1
	if (enron_data[word]['total_payments']=='NaN'): count3+=1
	if (enron_data[word]['total_payments']=='NaN') and (enron_data[word]['poi']==True):count4+=1	 
		 
print count1,count2,count3,(count3+10),(count4+10)







