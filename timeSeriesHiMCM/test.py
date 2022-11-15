from pandas import read_csv
from pandas import datetime
import pandas as pd
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from pandas.tseries.offsets import DateOffset
import sys,os
from math import sqrt
from pandas.plotting import autocorrelation_plot
from pandas import DataFrame
# load dataset
series = read_csv(os.path.join("CalvoSeko.github.io", "timeSeriesHiMCM", "OriginalCO2Data.csv"), header=0, parse_dates=True, index_col=0, squeeze=True)
series.index = series.index.to_period('M')
series.columns = ["date", "value"]
series.plot()
pyplot.show()
 
# fit model
model = ARIMA(series, order=(5,1,0))
model_fit = model.fit()

# line plot of autocorrelation
autocorrelation_plot(series)
pyplot.show()
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(series, lags = 20)
pyplot.show()
#p = 2