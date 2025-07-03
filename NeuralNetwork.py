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

def build_model_using_sequential(hidden_units1, hidden_units2, hidden_units3):
    model = Sequential([
        Dense(hidden_units1, kernel_initializer='normal', activation='relu'),
        Dropout(0.2),
        Dense(hidden_units2, kernel_initializer='normal', activation='relu'),
        Dropout(0.2),
        Dense(hidden_units3, kernel_initializer='normal', activation='relu'),
        Dense(1, kernel_initializer='normal', activation='linear')
    ])
    return model

MBESS = DCG.csv_conversion("Training_Datasets/Municipal_Building_Energy_Use_and_Energy_Star_Score.csv")
MBESS_New = DCG.sort(MBESS, sort_by_columns=["Year Built", "Electricity Use - Grid Purchase (kWh)", "Natural Gas Use (therms)", "Direct GHG Emissions (Metric Tons CO2e)", "ENERGY STAR Score", "Property GFA - Self-Reported (ftÂ²)", "Site Energy Use (kBtu)"])
print(MBESS_New.head())
int_convert_MBESS_New = DCG.integer_conversion_of_columns(MBESS_New, ["Year Built", "Electricity Use - Grid Purchase (kWh)", "Natural Gas Use (therms)", "Direct GHG Emissions (Metric Tons CO2e)", "ENERGY STAR Score", "Property GFA - Self-Reported (ftÂ²)", "Site Energy Use (kBtu)"])
print(int_convert_MBESS_New.head())


X = int_convert_MBESS_New[["Year Built", "Electricity Use - Grid Purchase (kWh)", "Natural Gas Use (therms)", "Direct GHG Emissions (Metric Tons CO2e)", "ENERGY STAR Score", "Property GFA - Self-Reported (ftÂ²)"]] #Should be a two dimensional row of contributing variables (rows and columns)
y = int_convert_MBESS_New["Site Energy Use (kBtu)"] # Should only be a one dimensional row of answers/y-values (only includes rows?)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2,random_state=800, shuffle=False)


model = build_model_using_sequential(160, 480, 256)

msle = MeanSquaredLogarithmicError()

model.compile(
    loss=msle,
    optimizer = 'adam',
    metrics=[msle]
)

x_train_scaled, x_test_scaled = scale_datasests(X_train, X_test)

history = model.fit(
    x_train_scaled.values,
    y_train.values,
    epochs=500,
    batch_size=10,
    validation_split=0.2
)

def plot_history(history, key):
    plt.plot(history.history[key])
    plt.plot(history.history['val_'+key])
    plt.xlabel("Epochs")
    plt.ylabel(key)
    plt.legend([key, 'val_'+key])
    plt.show()
print(model.summary())

plot_history(history, 'mean_squared_logarithmic_error')

X_test['prediction'] = model.predict(x_test_scaled)

print(X_test['prediction'])
print(history.history)
model.save("MBESS.h5")

train_loss, train_acc = model.evaluate(x_train_scaled, y_train, batch_size=10)
test_loss, test_acc = model.evaluate(x_test_scaled, y_test, batch_size=10)
print('Train: %.3f, Test: %.3f' % (test_acc, test_loss))
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()