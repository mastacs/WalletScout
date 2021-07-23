import json, sys
from os import path


# Wallet class, auto generated from a passed dictionary.
# It is being used to build objects from a list of dicts.

class Asset:
    def __init__(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)

# Todo
# More Validation/Error handling
# More functionality

# WalletScout main class, prepares and parses JSON data. Used to build Wallet objects
# Accepts multiple JSON data objects, file path, string, etc.
class Scout:
    def __init__(self, jData):
        if isinstance(jData, str) and path.exists(jData):
            self._jData = open(jData)
        else:
            self._jData = jData
        self._dsData = self.__deserializeData()
        self._assets = []
        self.__loadAssets(self._dsData)

    # Deserialize JSON data. Catch incorrectly formatted JSON data.
    # Performs file deserialization and string deserialization
    def __deserializeData(self):
        if isinstance(self._jData, str):
            try:
                self._dsData = json.loads(self._jData)
            except json.decoder.JSONDecodeError as e:
                print("String object does not meet JSON formatting specifications. Error: ", e)
                return
        else:
            self._dsData = self._jData
        return self._dsData

    # _loadWallets from Zapper API response
    # Iterates deserialized dict, recursion if nested dicts.
    # Grabs "assets" list containing wallet dictionaries. Builds list of wallet objects.
    def __loadAssets(self, dsData):
        for key, value in dsData.items():
            try:
                if isinstance(value, dict):
                    self.__loadAssets(value)
                elif value == 501:
                    break
                elif isinstance(value[0].get('assets'), list):
                    for item in value[0].get('assets'):
                        self._assets.append(Asset(item))
                elif key == "result":
                    for item in value:
                        self._assets.append(Asset(item))
            except AttributeError:
                continue

    # Todo:
    # support for various API data.
