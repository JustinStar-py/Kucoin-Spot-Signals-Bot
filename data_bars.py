import csv,asyncio,ccxt
from candles_analyze import get_ohlcv
from config import (
      SYMBOL,
      API_KEY,
      API_SECRET,
      API_PASSPHRASE,
      DATA_CANDLES,
      TRADE_DATA
)

# API_KEY
# API_SECRET
# API_PASSPHRASE

# client = Trade(key=API_KEY, secret=API_SECRET, passphrase=API_PASSPHRASE, is_sandbox=False, url="https://api.kucoin.com")

data_csv = []
columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']

exchange = ccxt.binance()

async def old_candles(symbol="BTC/USDT"):
    global DATA_CANDLES,TRADE_DATA,SYMBOL
   
    data_result = exchange.fetch_ohlcv(symbol, timeframe="1m", limit=100)
    DATA_CANDLES = data_result

def writer_data(data,timestamp):
      global columns  
    #   data[0] = timestamp
      # print("> data \n {} \n".format(data))
      if len(data) > 3:

         DATA_CANDLES.append(data)
         DATA_CANDLES.remove(DATA_CANDLES[0])

         with open('data.csv', 'w', encoding='UTF8',newline="") as f:
                 writer = csv.writer(f)
                 writer.writerow(columns)
                 writer.writerows(DATA_CANDLES)

         get_ohlcv(DATA_CANDLES)

      else:
         print("۰ Data range index error!")
     

asyncio.run(old_candles())
