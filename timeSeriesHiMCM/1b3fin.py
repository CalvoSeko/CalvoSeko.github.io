from pandas import read_csv
from pandas import datetime
import pandas as pd

from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from pandas.tseries.offsets import DateOffset
import sys,os
import matplotlib.pyplot as plt
import numpy as np
# load dataset
series = read_csv(os.path.join("CalvoSeko.github.io", "timeSeriesHiMCM", "OriginalCO2Data.csv"), header=0, parse_dates=True, index_col=0, squeeze=True)
series.index = series.index.to_period('Y')
series.columns = ["date", "value"]

mod = ARIMA(series, order=(2, 2, 0))
fit_mod = mod.fit()
#change this for the number of years after
predicted_df = fit_mod.forecast(steps=150)
fig, ax = plt.subplots(figsize=(15, 5))

# Construct the forecasts
fcast = fit_mod.get_forecast('2071').summary_frame()
fcast['mean'].plot(ax=ax, style='k--')
ax.fill_between(fcast.index, fcast['mean_ci_lower'], fcast['mean_ci_upper'], color='k', alpha=0.1)
series.plot()
plt.show()

