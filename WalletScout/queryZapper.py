import requests
from os import path
from walletScout import Scout
from zapperVariables import zapper_protocols, zapper_networks, walletBalance_url, protocolBalance_url, testAddress

class ZapperQuery:
   def __init__(self, address):
      # Object Structure
      #
      # {self._totalZapperAssets:[{
      #           "walletAssets": [{
      #                 "network1": [{
      #                       "asset1": [
      #                             address
      #                             balanceUSD
      #                             etc
      #
      #           "protocolAssets": [{
      #                    "network1": [{
      #                       "protocol1": [{
      #                             "asset1": [
      #                                address
      #                                balanceUSD
      #                                etc
      # 
      self._totalZapperAssets = {}
      self._walletAssets = []
      self._protocolAssets = []
      for network in zapper_networks:
         self._walletBalance = self.__checkWalletsBalance(address, network)
         self._protocolBalance = self.__checkWalletsProtocolBalance(address, network)
         for asset in self._walletBalance._assets:
            self._walletAssets.append(asset)
         self._protocolAssets.append(self._protocolBalance)
         self._totalZapperAssets['walletAssets'] = self._walletBalance._assets
         self._totalZapperAssets['protocolAssets'] = self._protocolBalance
   
   def __checkWalletsBalance(self, address, network):
      response = requests.get(url = (
         walletBalance_url % (
         address,
         network
         )
      ))
      # Instantiate the Wallet object passing response as JSON object
      return Scout(response.json())

   def __checkWalletsProtocolBalance(self, address, network):
      totalAssetsPerProtocol = []
      perProtocolAssets = {}
      for protocol in zapper_protocols:
         assetsPerProtocol = []
         response = requests.get(url = (
            protocolBalance_url % (
               protocol,
               address,
               network
            )
         ))
            # Instantiate the Wallet object passing response as JSON object
         perProtocol = Scout(response.json())
         for asset in perProtocol._assets:
            assetsPerProtocol.append(asset)
         perProtocolAssets[protocol] = assetsPerProtocol
      totalAssetsPerProtocol.append(perProtocolAssets)
      return totalAssetsPerProtocol
    # Todo:
    # support for various API data.


def main():
   totalBalance = 0
   zapper = ZapperQuery(testAddress)
   # Loop through wallet assets list
   for asset in zapper._walletAssets:
      print("Token Contract Address: " + asset.address)
      totalBalance += asset.balanceUSD
   # Loop through protcol assets list
   for totalProtocolAssets in zapper._protocolAssets:
      for protocolAssets in totalProtocolAssets:
         for key, value in protocolAssets.items():
            print("Protocol: " + key)
            for asset in value:
               print("Token: " + asset.label + " Contract Address: " + asset.address)
               totalBalance += asset.balanceUSD
   print("Total Balance (USD): ", totalBalance)
main()
