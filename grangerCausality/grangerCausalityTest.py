import pandas as pd
import sys,os
df = pd.read_csv(os.path.join("CalvoSeko.github.io", "grangerCausality", "combinedData.csv"))

from statsmodels.tsa.stattools import grangercausalitytests
grangercausalitytests(df[['PPM', 'Degrees']], maxlag=[20])