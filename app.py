import sys, json
from asset import Asset

class Serialize:
    def __init__(self, json):
        self._json    = json

    wallets = []

    def loadWallets(self, dsData):
        for key, value in dsData.items():
            if isinstance(value, dict):
                self.loadWallets(value)
            else:
                assets = value[0].get('assets')
                if isinstance(assets, list):
                    wallets = []
                    for item in assets:
                        asset = Asset(item.get('type'),
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
                        wallets.append(asset)
                        

    def getWallets(self):
        data = json.load(self._json)
        self.loadWallets(data)
        return wallets

if len(sys.argv) > 1:
    file = open(sys.argv[1])
else:
    file = input("No file found. Enter path:")

#json = json.load(file)
wallets = []
def getWallets(data):
    for key, value in data.items():
        if isinstance(value, dict):
            getWallets(value)
        else:
            assets = value[0].get('assets')
            if isinstance(assets, list):
                wallets = []
                for item in assets:
                    asset = Asset(item.get('type'),
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
                    wallets.append(asset)

#getWallets(json)

ds = Serialize(file)
wallets = ds.getWallets()

for item in wallets:
    print("ASSET OBJECT")
    print(item._type)
    print(item._category)
    print(item._address)
    print(item._symbol)
    print(item._decimals)
    print(item._label)
    print(item._img)
    print(item._hide)
    print(item._canExchange)
    print(item._price)
    print(item._balance)
    print(item._balanceRaw)
    print(item._balanceUSD)
    print("************")


#asset = Asset("Test Address",
#              "Test Symbol",
#              "Test Label",
#              "Test RAW",
#              "Test USD")
