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

def csv_conversion(data):
    dataframe = pd.read_csv(data, encoding="ISO-8859-1")
    return dataframe

def csv_description(dataset, commentary=None):
    if dataset == "municipal-building-energy-use-2009-2014.csv":
        link = "https://catalog.data.gov/dataset/municipal-building-energy-usage"
        message = "\nThis data set contains energy use data from 2009-2014 for 139 municipally operated buildings. Metrics include: Site & Source EUI, annual electricity, natural gas and district steam consumption, greenhouse gas emissions and energy cost. Weather-normalized data enable building performance comparisons over time, despite unusual weather events."
        note = "NOTE: has per year energy estimates of the same locations"
        location = ("Location: Allegheny County / City of Pittsburgh")
    elif dataset == "DCAS_Managed_Building_Energy_Usage.csv":
        link = "https://catalog.data.gov/dataset/dcas-managed-building-energy-usage"
        message = "\nCity Building Energy Usage Data."
        note = "NOTE: Could be useful, data dictionary claims that the spreadsheet is annually updated"
        location = ("Location: City of New York/ New York")
    elif dataset == "Energy_Usage_From_DOE_Buildings.csv":
        link = "https://catalog.data.gov/dataset/energy-usage-from-doe-buildings"
        message = "\nEnergy data from a select portfolio of City-Owned buildings (DOE)"
        note = "NOTE: Useful for per month building total predictions!"
        location = ("Location: City of New York/ New York")
    elif dataset == "Municipal_Building_Energy_Use_and_Energy_Star_Score.csv":
        link = "https://catalog.data.gov/dataset/municipal-building-energy-use-and-energy-star-score"
        message = "\nEnergy data on Providence Municipal buildings by year"
        note = ("NOTE: Useful for per year building total predictions!")
        location = ("Location: City of Providence/Rhode Island")
    elif dataset == "Energy_Usage_2010.csv":
        link = "https://catalog.data.gov/dataset/energy-usage-2010"
        message = "\nDisplays several units of energy consumption for households, businesses, and industries in the City of Chicago during 2010. Electric The data was aggregated from ComEd and Peoples Natural Gas by Accenture. Electrical and gas usage data comprises 88 percent of Chicago's buildings in 2010. The electricity data comprises 68 percent of overall electrical usage in the city while gas data comprises 81 percent of all gas consumption in Chicago for 2010. Census blocks with less than 4 accounts is displayed at the Community Area without further geographic identifiers. This dataset also contains selected variables describing selected characteristics of the Census block population, physical housing, and occupancy."
        note = ("")
        location = ("Location: City of Chicago/ Illinois")
    elif dataset == "F6a29a0f-cc32-4fd4-8adb-d45e11e09022.csv":
        link = "https://catalog.data.gov/dataset/allegheny-county-municipal-building-energy-and-water-use"
        message = "\nThis dataset contains energy and water use information from 2010 to the previous full month for County-operated buildings. Metrics include: kBtu (thousand British thermal units), site and source EUI (energy use intensity), annual electricity, natural gas and steam consumption and cost, and water and sewer use and cost. Weather-normalized data enable building performance comparisons over time, despite unusual weather events."
        note = ("")
        location = ("Location: Allegheny County / City of Pittsburgh")
    print(dataset + location + ". " + message + "\n" + note)
    return link

def columns(dataframe):
    return dataframe.columns

def column_types(dataframe):
    return dataframe.dtypes

def sort(dataframe, sort_by_columns=None, sort_by_rows=None, column_used_for_row_lookup=None):
    '''
    Intended as a quality of life function that can help
    the user rearrange the format of a DataFrame object if they wish

    sort_by_columns should be a list,
    column used_for_row_lookup should be a string of a columnname'''
    if (sort_by_columns != None) and (sort_by_rows == None):
        new_dataframe = dataframe[sort_by_columns]
    elif sort_by_columns and sort_by_rows != None: 
        new_dataframe = dataframe.loc[dataframe[column_used_for_row_lookup] == sort_by_rows, sort_by_columns]
    return new_dataframe

def integer_conversion_of_columns(dataframe, list_of_integer_columns, coordinate_column=None):
    '''
    A necessary function for the data cleaning process.
    Forces the cells of a .csv file to conform to integer values.

    If an error arises in the process, the entire row on which the invalid cell rests on is dropped.
    '''
    if coordinate_column == None:
        dataframe[list_of_integer_columns] = dataframe[list_of_integer_columns].apply(pd.to_numeric, errors='coerce', downcast=None)
        dataframe = dataframe.dropna(axis=0, how="any")
    else:
        dataframe[coordinate_column] = dataframe[coordinate_column].apply(pd.to_numeric, errors='coerce', downcast=None)
        dataframe[coordinate_column] = dataframe.dropna(axis=0, how="any")
    return dataframe
    
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

MBESS = csv_conversion("Training_Datasets/Municipal_Building_Energy_Use_and_Energy_Star_Score.csv")
print(columns(MBESS))
MBESS_New = sort(MBESS, sort_by_columns=["Year Built", "Electricity Use - Grid Purchase (kWh)", "Natural Gas Use (therms)", "Direct GHG Emissions (Metric Tons CO2e)", "ENERGY STAR Score", "Property GFA - Self-Reported (ftÂ²)", "Site Energy Use (kBtu)"])
print(MBESS_New.head())
int_convert_MBESS_New = integer_conversion_of_columns(MBESS_New, ["Year Built", "Electricity Use - Grid Purchase (kWh)", "Natural Gas Use (therms)", "Direct GHG Emissions (Metric Tons CO2e)", "ENERGY STAR Score", "Property GFA - Self-Reported (ftÂ²)", "Site Energy Use (kBtu)"])

linear_regression(int_convert_MBESS_New, ["ENERGY STAR Score", "Property GFA - Self-Reported (ftÂ²)"], "Site Energy Use (kBtu)", .2)
