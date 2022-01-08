import tkinter as tk
import logging
#from binance_futures import get_contracts
#from bitmex import get_contracts
from connectors.binance_futures import BinanceFuturesClient

PUBLIC_KEY = '8e0009e1a5e4efae7c57854105f78f134d0cab038fa690703615373aa3e385da'
SECRET_KEY = '1ca0558674082266851ab618b3ddccc596bc29997ceb9853ab275ff5e9c8e5f6'

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient(PUBLIC_KEY, SECRET_KEY, True)
    print(binance.get_balances())
    #print(binance.place_order("BTCUSDT", "BUY", 0.01, "LIMIT", 20000, "GTC"))
    print(binance.get_order_status("BTCUSDT", 2962294324))
    print(binance.cancel_order("BTCUSDT", 2962294324))

    root = tk.Tk()
    root.mainloop()