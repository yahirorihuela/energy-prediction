import DataCleaning as DCG
##############################
import pandas as pd
##############################
import numpy as np
##############################
import matplotlib.pyplot as plt
##############################
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
##############################
'''Does not have tensorflow libraries.'''

def linear_regression(data, features, target, test_proportion):
    '''
    A preliminary to the larger goal of a shallow neural network.
    I wanted to familiarize myself more with scikit-learn library before advancing
    (and refresh on numpy and matplotlib)
    '''
    X = data[features] #2D because more than one feature is being utilized
    Y = data[target] #1D because this is a univariate linear regression (1 predicted output per set of inputs)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_proportion, random_state=800, shuffle=False) #shuffle to False means the same train_test split will run each time.
    clf = LinearRegression()
    clf.fit(X_train, Y_train)
    predicted = clf.predict(X_test)
    expected = Y_test
    a, b = np.polyfit(expected, predicted, 1)
    plt.scatter(expected, predicted)
    plt.plot(expected, a*expected + b)
    plt.axis('tight')
    plt.title(target + " from " + str(features))
    plt.xlabel("predicted " + target)
    plt.ylabel("actual " + target)
    print("r-squared = {:.3f}".format(r2_score(expected,predicted)), (0,1))
    plt.annotate("r-squared = {:.3f}".format(r2_score(expected,predicted)),(0,1))
    plt.show()

'''
Example of functions in play:
MBESS = DCG.csv_conversion("Training_Datasets/Municipal_Building_Energy_Use_and_Energy_Star_Score.csv")
MBESS_New = DCG.sort(MBESS, sort_by_columns=["Year Built", "Electricity Use - Grid Purchase (kWh)", "Natural Gas Use (therms)", "Direct GHG Emissions (Metric Tons CO2e)", "ENERGY STAR Score", "Property GFA - Self-Reported (ftÂ²)", "Site Energy Use (kBtu)"])
int_convert_MBESS_New = DCG.integer_conversion_of_columns(MBESS_New, ["Year Built", "Electricity Use - Grid Purchase (kWh)", "Natural Gas Use (therms)", "Direct GHG Emissions (Metric Tons CO2e)", "ENERGY STAR Score", "Property GFA - Self-Reported (ftÂ²)", "Site Energy Use (kBtu)"])
linear_regression(int_convert_MBESS_New, ["ENERGY STAR Score", "Property GFA - Self-Reported (ftÂ²)"], "Site Energy Use (kBtu)", .2)
'''