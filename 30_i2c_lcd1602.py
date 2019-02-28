import LCD1602
import time
from binance.client import Client
from binance.websockets import BinanceSocketManager

PUBLIC_API_KEY = ''
PRIVATE_API_KEY = ''

symbol = 'BTCUSDT'


def kline_handle(msg):
    if msg['e'] == 'error':
        print("There's an error")
    else:
        LCD1602.write(0, 0, msg['k']['s'])
        LCD1602.write(0, 1, msg['k']['c'])
        time.sleep(0.4)


def socket_conn():
    try:
        client = Client(PUBLIC_API_KEY, PRIVATE_API_KEY)
        bm = BinanceSocketManager(client)
        bm.start_kline_socket(symbol, kline_handle, client.KLINE_INTERVAL_1MINUTE)
        bm.start()
    except:
        print("Error - exiting...")


def setup():
        LCD1602.init(0x27, 1)   # init(slave address, background light)
        LCD1602.write(0, 0, 'r/wallstreetbets')
        LCD1602.write(1, 1, 'Presents')
        time.sleep(3)


def destroy():
        pass


if __name__ == "__main__":
        try:
                setup()
                while True:
                        socket_conn()
        except KeyboardInterrupt:
                destroy()
