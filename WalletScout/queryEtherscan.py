import requests
from os import path
from zapperScout import Scout
from zapperVariables import testAddress

etherscan_url = "https://api.etherscan.io/api?module=account&action=%s&address=%s&startblock=0&endblock=999999999&sort=asc&apikey=M4SIQFEQ5D6KXNQMIZXF86MX2R8XAK5NDJ"

searchType = {
   "externalTx": "txlist",
   "internalTx": "txlistinternal",
   "tokenEvents": "tokentx"
}

class EtherScanQuery:
   def __init__(self, address):
      self._etherscan = {}
      self.__getTx(address)
      self.__getERC20Events(address)
   
   def __getTx(self, address):
      self._internalTx = []
      self._externalTx = []
      
      externalTxResponse = requests.get(url = (
         etherscan_url % (
         searchType["externalTx"],
         address
         )
      ))
      internalTxResponse = requests.get(url = (
         etherscan_url % (
         searchType["internalTx"],
         address
         )
      ))

      results = Scout(externalTxResponse.json())
      for result in results._assets:
         self._externalTx.append(result)

      results = Scout(internalTxResponse.json())
      for result in results._assets:
         self._internalTx.append(result)

      self._etherscan["external"] = self._externalTx
      self._etherscan["internal"] = self._internalTx

   def __getERC20Events(self, address):
      self._tokenEvents = []
      response = requests.get(url = (
         etherscan_url % (
         searchType["tokenEvents"],
         address
         )
      ))
      results = Scout(response.json())
      for result in results._assets:
         self._tokenEvents.append(result)
      self._etherscan["tokens"] = self._tokenEvents

def main():
   results = EtherScanQuery(testAddress)
   for internal in results._etherscan["internal"]:
      print(internal.hash)
   for token in results._etherscan["tokens"]:
      print(token.hash)
main()
