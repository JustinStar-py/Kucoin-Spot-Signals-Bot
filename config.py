import json,requests
from symtable import Symbol

ID = "WU2ld5edUm"

COUNTER = 0

COLUMNS = ['timestamp', 'open', 'high', 'low', 'close', 'volume']  

SYMBOL = "btcusdt"

TRADE_DATA = {
                  f'{SYMBOL}': {'bought':545,
                                       'in-pos':'🔴 SELL',
                                       'profit':1,
                                       'sold':232
                 }
        }

DATA_CANDLES = []

STATUS = True

NEW_POSITION = False

INTERVAL = '1m'
# http_api = "https://api.kucoin.com/api/v1/bullet-public"
# data_values = json.loads(requests.post(http_api).text)
# return data_values['data']['token']

TOKEN = ""

KUCOIN_SOCKET = "wss://ws-api.kucoin.com/endpoint?token={}&[connectId={}]".format(TOKEN,ID)

SOCKET = "wss://stream.binance.com:9443/ws/{}@kline_{}".format(SYMBOL,INTERVAL)


LAST_SIGNAL = 'Started robot to send signals! 🐳'