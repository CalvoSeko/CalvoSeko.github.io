from pandas import read_csv
from pandas import datetime
import pandas as pd

from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from pandas.tseries.offsets import DateOffset
import sys,os
from math import sqrt
from sklearn.metrics import mean_squared_error
# load dataset
series = read_csv(os.path.join("CalvoSeko.github.io", "timeSeriesHiMCM", "OriginalCO2Data.csv"), header=0, parse_dates=True, index_col=0, squeeze=True)
series.index = series.index.to_period('M')
series.columns = ["date", "value"]
# split into train and test sets
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
 
# walk-forward validation
for t in range(len(test)):
	model = ARIMA(history, order=(2,2,0))
	model_fit = model.fit()
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))

rmse = sqrt(mean_squared_error(test, predictions))
# evaluate forecasts
rmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)
# plot forecasts against actual outcomes
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()
