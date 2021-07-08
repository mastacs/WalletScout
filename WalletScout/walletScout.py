import json
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
        self._jData   = jData
        self._dsData  = self.__deserializeData()
        self._wallets = []
        self._
        self.__loadWallets(self._dsData)

    def __deserializeData(self):
        self._dsData = json.load(self._jData)
        return self._dsData

    def __loadWallets(self, dsData):
        for key, value in dsData.items():
            if isinstance(value, dict):
                self.__loadWallets(value)
            elif isinstance(value[0].get('assets'), list):
                for item in value[0].get('assets'):
                    self._wallets.append(Wallet(item))
