import pandas as pd
import datetime as dt 
from binance import Client 
import csv
import time
import numpy
import requests



api_key='clEiLOWrdR5Ay7dxPnR2IYKKKNpy4C7W25t26hLuObr4FYc9Y1HeuJViWAhUua1v'
api_secret='S0SubR3o4AsnAFajLObIILgqAfKc8KxUGvbNL3YIzQrqyFuXMj5kS0gi6RmU5cyl'

client = Client(api_key, api_secret)

#Number of days we want to backtest this strategy
start_str = '180 days ago UTC'

#Time interval we want to get candlesticks for
#interval_data = '1d'

#get historical candlesticks
D = pd.DataFrame(client.get_historical_klines('XLMUSDT', client.KLINE_INTERVAL_1DAY, start_str))

D.columns = ['open_time', 'open', 'high', 'close', 'low', 'volume', 'close_time', 'qav', 'num_trades', 
'ticker_base_vol', 'ticker-quote_vol', 'is_best_match']

#print (D)

#print (D[['open', 'high', 'close', 'low']])

D_high_close = D[['high', 'close']]
#D_close = D[['close']]
D_high = D[['high']]

#print(D_high_close)

# index = D_high_close.index




for x in D_high_close['close']:
    #print(x, 'This is the value of x')
    num = (float(x) * 0.05) + float(x)
    print(num)

    #  if i == 0:
    #      percentage(num)
        
    #      i += 1
    #      print(percentage(num))
    

for i in D_high:
  print(D_high )
#print (D_close)




#find the value of five percent of the values of all values in close column
#def five_perc():

      



#for x in D_high_close:
  #  if x in D_high_close[['high']] >= x in D_high_close[['close']]
   # print (x)
    #else: break 