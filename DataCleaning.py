import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def csv_conversion(data):
    dataframe = pd.read_csv(data, encoding="ISO-8859-1")
    return dataframe
