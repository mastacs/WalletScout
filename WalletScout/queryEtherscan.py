import requests
from os import path
from walletScout import Scout
from queryData import testAddress, etherscan_url

searchType = {
   "externalTx": "txlist",
   "internalTx": "txlistinternal",
   "tokenEvents": "tokentx"
}

class EtherScanQuery:
   def __init__(self, address):
      self._etherscanData = {}
      self.__getData(address)
   
   def __getData(self, address):
       self._internalTx = []
       self._externalTx = []
       self._tokenEvents = []
       for key, value in searchType.items():
            response = requests.get(url = (
                etherscan_url % (
                    searchType[key],
                    address
         )
      ))
            results = Scout(response.json())
            for result in results._assets:
                if key == 'externalTx':
                    self._externalTx.append(result)
                elif key == 'interalTx':
                    self._internalTx.append(result)
                elif key == 'tokenEvents':
                    self._tokenEvents.append(result)
            self._etherscanData["external"] = self._externalTx
            self._etherscanData["internal"] = self._internalTx
            self._etherscanData["tokenEvents"] = self._tokenEvents

def main():
   results = EtherScanQuery(testAddress)
   for internal in results._etherscanData["internal"]:
      print(internal.hash)
   for token in results._etherscanData["tokenEvents"]:
      print(token.hash)
main()
