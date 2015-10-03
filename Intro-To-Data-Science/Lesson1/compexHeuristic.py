import numpy
import pandas
import statsmodels.api as sm

def complex_heuristic(file_path):
    '''
    You are given a list of Titantic passengers and their associated
    information. More information about the data can be seen at the link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data

    For this exercise, you need to write a more sophisticated algorithm
    that will use the passengers' gender and their socioeconomical class and age 
    to predict if they survived the Titanic diaster. 
    
    You prediction should be 79% accurate or higher.
    
    Here's the algorithm, predict the passenger survived if:
    1) If the passenger is female or
    2) if his/her socioeconomic status is high AND if the passenger is under 18
    
    Otherwise, your algorithm should predict that the passenger perished in the disaster.
    
    
    
    You can also look at the Titantic data that you will be working with
    at the link below:
    https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        # 
        # your code here
        if passenger['Sex']=='female' or (passenger['Age']<18 and passenger['Pclass']<=2):
            predictions[passenger_id]=1
        else:
            predictions[passenger_id]=0
    return predictions
