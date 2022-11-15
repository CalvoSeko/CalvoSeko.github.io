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
series = read_csv(os.path.join("CalvoSeko.github.io", "questionOnTemp", "2022_HiMCM_Data.csv"), header=0, parse_dates=True, index_col=0, squeeze=True)
series.index = series.index.to_period('M')
series.columns = ["date", "value"]

 
# fit model
model = ARIMA(series, order=(2,2,5))
model_fit = model.fit()
residues = DataFrame(model_fit.resid)
residues.plot()
pyplot.show()
# line plot of autocorrelation
#autocorrelation_plot(series)
#pyplot.show()
#from statsmodels.graphics.tsaplots import plot_pacf
#plot_pacf(series, lags = 20)
#pyplot.show()
#p = 2
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(series)
pyplot.show()