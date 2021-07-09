import json, os.path
from os import path
# Wallet class, auto generated from a passed dictionary.
# It is being used to build objects from a list of dicts.

# ToDo:
# this could be done in a more pythonic manner with setattr and delattr for example
# Validation of CRUD
# Full obj printout
# Object to dict conversion method.
class Wallet:
    def __init__(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)

# Main class for program.
# Requires JSON data of some kind during initialization

# Todo
# Validation/Error handling
# More functionality
# URL / JSON String dual functionality
class WalletScout:
    def __init__(self, jData):
        if isinstance(jData, str) and path.exists(jData):
            self._jData = open(jData)
        else:
            self._jData = jData

        self._dsData  = self.__deserializeData()
        self._wallets = []
        self.__loadWallets(self._dsData)

    def __deserializeData(self):
        if isinstance(self._jData, str):
            try:
                self._dsData = json.loads(self._jData)
            except json.decoder.JSONDecodeError as e:
                print("String object does not meet JSON formatting specifications. Error: ", e)
                return
        else:
            self._dsData = json.load(self._jData)
        return self._dsData

    def __loadWallets(self, dsData):
        for key, value in dsData.items():
            if isinstance(value, dict):
                self.__loadWallets(value)
            elif isinstance(value[0].get('assets'), list):
                for item in value[0].get('assets'):
                    self._wallets.append(Wallet(item))
