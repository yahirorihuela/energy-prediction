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
######################
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, Dropout
from tensorflow.python.keras.losses import MeanSquaredLogarithmicError
######################

def scale_datasests(x_train, x_test):
    ''' 
    Standard Scale test and train data
    Z - Score normalization.
    '''
    standard_scaler = StandardScaler()
    x_train_scaled = pd.DataFrame(
        standard_scaler.fit_transform(x_train),
        columns=x_train.columns
    )

    x_test_scaled = pd.DataFrame(
        standard_scaler.transform(x_test),
        columns = x_test.columns
    )
    return x_train_scaled, x_test_scaled

#optimization and loss function required for backward propagation
#Regularizers needed at each layer to prevent overfitting.