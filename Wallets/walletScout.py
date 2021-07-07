import json
from .wallet import Wallet

# Main class for program.
# Requires JSON data of some kind during initialization

# Todo
# Validation/Error handling
# More functionality
# URL / JSON String dual functionality
class WalletScout:
    def __init__(self, jData):
        self._jData   = jData
        self._dsData  = self.__deserializeData()
        self._wallets = []
        self.__loadWallets(self._dsData)

    def __deserializeData(self):
        self._dsData = json.load(self._jData)
        return self._dsData

    def __loadWallets(self, dsData):
        for key, value in dsData.items():
            if isinstance(value, dict):
                self.__loadWallets(value)
            else:
                assets = value[0].get('assets')
                if isinstance(assets, list):
                    for item in assets:
                        asset = Wallet(item.get('type'),
                                       item.get('category'),
                                       item.get('address'),
                                       item.get('symbol'),
                                       item.get('decimals'),
                                       item.get('label'),
                                       item.get('img'),
                                       item.get('hide'),
                                       item.get('canExchange'),
                                       item.get('price'),
                                       item.get('balance'),
                                       item.get('balanceRaw'),
                                       item.get('balanceUSD'))
                        self._wallets.append(asset)

    def getWallets(self):
        return self._wallets
