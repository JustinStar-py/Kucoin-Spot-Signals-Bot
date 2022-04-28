import asyncio
from telethon import TelegramClient
import re,asyncio
from telethon import TelegramClient
from config import LAST_SIGNAL

# import socks
# https://t.me/socks?server=209.97.175.37&port=9050&bot=@mtpro_xyz_bot
# proxy = (socks.SOCKS5, '209.97.175.37', 9050)
# Remember to use your own values from my.telegram.org!

# Use your own values from my.telegram.org

api_id = 18820982
api_hash = 'd764ce02c21fc893f7e942b2c7602f7b'
posi_filters = {
  "buy" : {
            "buy_filters" : ["^Buying.#[A-Z]*",".[1-100].*","Risk"]
  },
  "sell" : {
            "sell_filters" : ["^#[A-Z]*.[A-Z]*","Target","Period"]
  }
}

position_detail = {
      "position" : "sell",
      "coin" : "BTCUSDT",
      "amount" : 1 # amount == US dollor
}

client = TelegramClient(
      'Space',
      api_id,
      api_hash,
      # connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
      # proxy=('Unity-Proxy.dynu.com', 443, 'ddf4359a9b325ff1d1e5084df0e0f7537b')
    )

async def send_msg(message):
    async with TelegramClient('Space', api_id, api_hash) as client:
            entity = await client.get_entity('SpotSignals_Robot')
            await client.send_message(entity=entity, message=message,parse_mode='html')
        

     
asyncio.run(send_msg(LAST_SIGNAL))