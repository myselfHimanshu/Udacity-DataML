#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    cleaned_data=zip(ages,net_worths,[(float(pred-true))**2 for pred,true in zip(predictions,net_worths)])
    
    cleaned_data.sort(key = lambda x:x[2])
    for i in range(int(len(cleaned_data) * 0.1)):
        cleaned_data.pop() 

    
    return cleaned_data

