from pandas import read_csv
from pandas import datetime
import pandas as pd
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from pandas.tseries.offsets import DateOffset
import sys,os
from math import sqrt
# load dataset
series = read_csv(os.path.join("CalvoSeko.github.io", "questionOnTemp", "2022_HiMCM_Data.csv"), header=0, parse_dates=True, index_col=0, squeeze=True)
series.index = series.index.to_period('M')
series.columns = ["date", "value"]
# split into train and test sets
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
 
model = ARIMA(history, order=(2,2,5))
model_fit = model.fit()
predicted_df = model_fit.forecast(steps=500)
predictions.append(predicted_df)
for i in predictions:
  print(i)
  print("")