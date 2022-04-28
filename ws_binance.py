from data_bars import writer_data
import websocket,json,time
from config import (
    SOCKET,
    COLUMNS,
    COUNTER,
)


def on_message(ws, message):
    global COUNTER

    last_bar = []
    data_bar = json.loads(message)
    timestamp = data_bar['k']['t']
    current_columns = [c[0] for c in COLUMNS]

    if data_bar['k']['x'] == True:
       last_bar = [float(data_bar['k'][i]) for i in data_bar['k'] if i in current_columns]
       writer_data(last_bar,timestamp)
    #    print("{} >> Found closed bar! >> {} \n".format(COUNTER,last_bar))
    # else:
    #    print('{})-Found same bars! \n  closed : {} \n'.format(COUNTER,data_bar['k']['x']))
    #    pass

    COUNTER += 1

def on_error(ws, error):
    print("Found Error > {} \n".format(error))

def on_close(close_msg):
    print(close_msg)

def re_connect():
    time.sleep(10)
    ws.run_forever(ping_interval=20 , ping_timeout=10)
    re_connect()

def streamKline():
    global SOCKET,ws

    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(SOCKET,on_message=on_message,on_error=on_error,on_close=on_close)

    ws.run_forever(ping_interval=20 , ping_timeout=10)
    re_connect()

streamKline()
