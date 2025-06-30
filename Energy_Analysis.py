import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def original_dataset(data):
    '''
    self-explanatory, a minimalist version of pandas's .read_csv

    If the user desires to exclude columns from a .csv file, utilize the
    "Selecting_Relevant_Columns" and "Filtered_Dataset" functions instead.
    '''
    Original_Dataset = pd.read_csv(data)
    return Original_Dataset

def Selecting_Relevant_Columns(name_of_dataset, list_of_relevant_abbreviations):
    '''
    This function, in conjunction with the custom function "Filtered_Dataset", excises undesired columns
    from an original .csv file when creating a DataFrame object.
     
    On its own, this function only returns a list of columns from a .csv 
    that the user deems relevant. The special thing about this function is that it
    can accept a sliced version of columnnames (beginning from the first letter) deemed relevant

    For example:

    Within a .csv file containing the columns "January, February, March, ... , October, November, December"
    If you only desire the data underscored by "January", "February", and "March", then:
    
    "Selecting_Relevant_Columns(filename.csv, [Jan, Feb, Mar])"
    would do the trick in getting you a smaller, relevant, dataframe. 
    '''
    Original_Dataset = pd.read_csv(name_of_dataset)
    Original_Columns = list(Original_Dataset)
    Relevant_Columns = []
    for Column in Original_Columns:
        verify_column = any(Column.startswith(r_abbrev) for r_abbrev in list_of_relevant_abbreviations)
        if verify_column == True:
            Relevant_Columns.append(Column)
    return Relevant_Columns

def Filtered_Dataset(old_dataset_name, transferred_columns):
    '''
    the "transferred_columns" parameter is designed to accept
    the return value from the function "Selecting_Relevant_Columns" 

    Example:
    '''
    new_df = pd.read_csv(old_dataset_name, usecols = transferred_columns)
    return new_df

def Determine_Multiple_Rows(df, column_of_interest, unique_identifiers_list, abbreviations):
    '''
    Creates a dictionary consisting of the row numbers of desired cells from a DataFrame object.

    For example, take a .csv file in which the columns are "Address", "City", "State", and "Electricity Usage (kWh)"
    (Thus, each row in the .csv represents a single property.)

    If we only wish to obtain the isolated energy measurements of properties in California and Hawaii then:

    Determine_Multiple_Rows(DataFrame_Name, "State", ["California", "Hawaii], ["Jan", "Feb"])

    Returns the row numbers in which such data is found.
    '''
    nested = any(isinstance(i, list) for i in unique_identifiers_list)
    relevant_rows_per_identifier = []
    principal_dictionary = {}
    if nested == False:
        for unique_identifier in unique_identifiers_list:
            relevant_rows = df[df[column_of_interest] == unique_identifier].index
            relevant_row_numbers = list(relevant_rows)
            relevant_rows_per_identifier.append(unique_identifier)
            relevant_rows_per_identifier.append(relevant_row_numbers)
        principal_dictionary = {relevant_rows_per_identifier[i] : relevant_rows_per_identifier[i + 1] for i in range(0, len(relevant_rows_per_identifier), 2)}
    else: #may delete this else statement, work in progress, not pertinent to function description
        for similar_identifier in unique_identifiers_list:
            relevant_row_numbers = []
            for unique_identifier in similar_identifier:
                relevant_row = df[df[column_of_interest] == unique_identifier].index
                relevant_row_numbers.append(relevant_row[0])
            for abbrev in abbreviations:
                if unique_identifier.startswith(abbrev):
                    relevant_rows_per_identifier.append(abbrev)
                    break
            relevant_rows_per_identifier.append(relevant_row_numbers)
        principal_dictionary = {relevant_rows_per_identifier[i] : relevant_rows_per_identifier[i + 1] for i in range(0, len(relevant_rows_per_identifier), 2)}
    return principal_dictionary

def Dictionary_Maker(df, range1, range2, row_dictionary):
    '''
    Constructs a dictionary composing of the relevant rows
    (found in the return value of the func. "Determine_Multiple_Rows")
    and relevant columns (range1 and range2 parameters).

    This dictionary prepares for another function which constructs another
    DataFrame object out of the dictionary created herein.

    Possible optimizations: could shrink the for loop on 112 each time it iterates
    '''
    storage = []
    principal_dictionary = {}
    for column in df.columns[range1:range2]: ## only uses the following columns
        iterator = -1
        for value in df[column]:
            value_row = df[df[column] == value].index
            value_row = list(value_row) #changes int64 type (return type of .index func) to list type
            iterator += 1 #should increment 
            if len(value_row) > 1: #this if block handles presence of duplicate values from the .index function
                for item in value_row[:]:
                    if iterator != item:
                        value_row.remove(item)
            for rows_of_interest in row_dictionary.values(): #this for block checks to see if the raw rows correspond to a relevant row number.
                for relevant_rows in rows_of_interest:
                    if value_row[0] == relevant_rows:
                        real_values = df._get_value(value_row[0], column)
                        storage.append(value_row[0])
                        storage.append(real_values)
        new_dictionary = {storage[i]:storage[i + 1] for i in range(0, len(storage), 2)}
        storage.clear()
        principal_dictionary.update({column : new_dictionary})
        return principal_dictionary
