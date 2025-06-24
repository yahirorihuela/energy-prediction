import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def original_dataset(data):
    Original_Dataset = pd.read_csv(data)
    return Original_Dataset
def Selecting_Relevant_Columns(name_of_dataset, list_of_relevant_abbreviations):
    Original_Dataset = pd.read_csv(name_of_dataset)
    Original_Columns = list(Original_Dataset)
    Relevant_Columns = []
    for Column in Original_Columns:
        verify_column = any(Column.startswith(r_abbrev) for r_abbrev in list_of_relevant_abbreviations)
        if verify_column == True:
            Relevant_Columns.append(Column)
    return Relevant_Columns

def Filtered_Dataset(old_dataset_name, transferred_columns):
    new_df = pd.read_csv(old_dataset_name, usecols = transferred_columns)
    return new_df

