import pandas as pd
import pandas_ta as ta
from teluser import send_msg
import asyncio
from config import (
    COUNTER,
    SYMBOL,
    DATA_CANDLES,
    COLUMNS,
    TRADE_DATA,
    LAST_SIGNAL
    )

bought = True

def get_ohlcv(data) -> pd.DataFrame:
      global COLUMNS
      # get candles from exchange
      bars = data
      # convert list of list to pandas dataframe
      df = pd.DataFrame(bars, columns=COLUMNS)  
      # convert millisecond to datetime
      df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  
    #   return df
    #   with open('data.csv','r') as f:
    #           df = pd.read_csv(f)
    #           df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
     
      get_signal(df)

def get_signal(dataframe):
    global SYMBOL,LAST_SIGNAL,TRADE_DATA,COUNTER,bought,send_msg
    
    last_row = len(dataframe.index) - 2

    dataframe['signal'] = ta.supertrend(dataframe['high'], dataframe['low'], 
                                        dataframe['close'], 8, 2)['SUPERTd_8_2.0']
    
    current_price = dataframe['close'][last_row]
    current_time = dataframe['timestamp'][last_row]
    in_pos = TRADE_DATA[SYMBOL]['in-pos']
    
    if  not bought and dataframe['signal'][last_row] == 1:
            # exchange.create_market_buy_order(symbol, quantity)
            bought = True
            TRADE_DATA[SYMBOL]['in-pos'] = in_pos = '🟢 BUY' 
         
    elif bought and dataframe['signal'][last_row] == -1:
            # exchange.create_market_buy_order(symbol, quantity)
            bought = False
            TRADE_DATA[SYMBOL]['in-pos'] = in_pos = '🔴 SELL'
    
    else:
         TRADE_DATA[SYMBOL]['in-pos'] = in_pos = 'none'

    if in_pos != 'none':
        LAST_SIGNAL = f'{in_pos} SIGNAL #{SYMBOL} \n<pre>📉 Price:</pre> <b>{current_price}</b> \n<pre>⏰ Time: </pre> <b>{current_time} </b></b>'
        print(LAST_SIGNAL)
        asyncio.run(send_msg(LAST_SIGNAL))
                       
    
    
    
if __name__ == '__main__':
    print('bot is started!')

