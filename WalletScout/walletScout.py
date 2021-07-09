import json, os.path
from os import path
# Wallet class, auto generated from a passed dictionary.
# It is being used to build objects from a list of dicts.

# ToDo:
# Full obj printout
# Object to dict conversion method.
# Support for required functionality:
#   API calls
#   Derivation
#   Calculated information
class Wallet:
    def __init__(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)

# Main class for program.
# Todo
# More Validation/Error handling
# More functionality
class WalletScout:
    # Initializer - Accepts multiple JSON obj types
    def __init__(self, jData):
        # Loading jData if data is unloaded file path
        if isinstance(jData, str) and path.exists(jData):
            self._jData = open(jData)
        else:
            self._jData = jData
        # Deserializing JSON data to pythonic objects
        self._dsData  = self.__deserializeData()
        # Instantiating wallet list for zapper api response
        self._wallets = []
        self.__loadWallets(self._dsData)

    # Deserialize JSON data. Catch incorrectly formatted JSON data.
    def __deserializeData(self):
        if isinstance(self._jData, str):
            try:
                # Deserialize as string
                self._dsData = json.loads(self._jData)
            except json.decoder.JSONDecodeError as e:
                print("String object does not meet JSON formatting specifications. Error: ", e)
                return
        else:
            # Deserialize as file
            self._dsData = json.load(self._jData)
        return self._dsData

    # Should be called loadWalletsFromZapper.
    # Specifically targets 'assets' list of wallets from Zapper API response JSON
    # First API specific function.
    def __loadWallets(self, dsData):
        # Iterate deserialized dictionary
        for key, value in dsData.items():
            # If nested dictionary - recursion
            if isinstance(value, dict):
                self.__loadWallets(value)
            # Grab "assets" list containing wallet dictionaries. Build list of wallet objects
            elif isinstance(value[0].get('assets'), list):
                for item in value[0].get('assets'):
                    self._wallets.append(Wallet(item))

    # Todo:
    # support for various API data. 
