import logging
import requests
import pprint

logger = logging.getLogger()

# def get_contracts():

#     response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
#     #print(response_object.status_code, response_object.json())
#     #pprint.pprint(response_object.json()['symbols'])
#     contracts=[]
#     for contract in response_object.json()['symbols']:
#         #pprint.pprint(contract)
#         #print(contract['pair'])
#         contracts.append(contract['pair'])
#     return contracts


class BinanceFuturesClient:
    def __init__(self, testnet):
        if testnet:
            self.base_url = "https://testnet.binancefuture.com"
        else:
            self.base_url = "https://fapi.binance.com"
        
        logger.info("Binance Futures Client successfully initialized")
    
    def make_request(self, method, endpoint, data):
        if method == "GET":
            response = requests.get(self.base_url + endpoint, params=data)
        else:
            raise ValueError()
        
        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making %s request to %s: %s (error code %s)", 
                         method, endpoint, response.json(), response.status_code)
            return None

    def get_contracts(self):
        exchange_info = self.make_request("GET", "/fapi/v1/exchangeInfo", None)

        contracts = dict()

        if exchange_info is not None:
            for contract_data in exchange_info['symbols']:
                contracts[contract_data['pair']] = contract_data

        return contracts
    
    def get_historical_candles(self):
        requests.get()
        return None
