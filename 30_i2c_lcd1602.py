import LCD1602
import time
from datetime import datetime
from binance.client import Client
from binance.websockets import BinanceSocketManager

PUBLIC_API_KEY = ''
PRIVATE_API_KEY = ''

symbol = 'BTCUSDT'


def process_message(msg):
    if msg['e'] == 'error':
        print("There's an error")
    else:
        timestamp = msg['T'] / 1000
        timestamp = datetime.fromtimestamp(timestamp).strftime('%m-%d')
        line_one = symbol + "   " + timestamp
        line_two = msg['p'][:-6]
        LCD1602.write(0, 0, line_one)
        LCD1602.write(0, 1, line_two)


def setup():
        LCD1602.init(0x27, 1)   # init(slave address, background light)
        LCD1602.write(0, 0, 'r/wallstreetbets')
        LCD1602.write(1, 1, 'Presents...')
        time.sleep(3)
        LCD1602.clear()
        #LCD1602.clear()

        
def balance():
        client = Client(PUBLIC_API_KEY, PRIVATE_API_KEY)
        bm = BinanceSocketManager(client)
        bal = client.get_asset_balance('BTC')['free']
        LCD1602.write(0, 0, bal)
        time.sleep(3)
        LCD1602.clear()


def destroy():
        pass


if __name__ == "__main__":
        try:
                setup()
                print('Screen initialized...')
                balance()
                client = Client(PUBLIC_API_KEY, PRIVATE_API_KEY)
                bm = BinanceSocketManager(client)
                bm.start_aggtrade_socket(symbol, process_message)
                bm.start()
                print('Feed streaming :)')
        except KeyboardInterrupt:
                destroy()
