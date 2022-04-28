# import ccxt

# exchange = ccxt.binance()
# bars = exchange.fetch_ohlcv("BTC/USDT", timeframe="1m", limit=10)
# print(bars)


#########################################################
#########################################################

# def get_ohlcv(symbol, interval='1m', limit=10) -> pd.DataFrame:

#     # headers
#     columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']

#     # get candles from exchange
#     bars = exchange.fetch_ohlcv(symbol, timeframe=interval, limit=limit)

#     # convert list of list to pandas dataframe
#     df = pd.DataFrame(bars, columns=columns)

#     # convert millisecond to datetime
#     df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

#     return df