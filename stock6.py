import yfinance as yf
import pandas as pd
import numpy as np
import mplfinance as mpf

df=yf.download('^GSPC',start='2023-01-01')

df 
#	data.Volume.rolling(5).min()  

#   supports=data[data.Low == data.Low.rolling(5,center=True).min()].Low
#   resistances=data[data.High == data.High.rolling(5,center=True).max()].High
#   levels=pd.concat([supports,resistances])

#  mpf.plot(data, type='candle', hlines=levels.to_list(), volume=True, style='charles')

   
