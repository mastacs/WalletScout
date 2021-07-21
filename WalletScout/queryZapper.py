import requests
from os import path
from walletScout import Scout
from zapperVariables import zapper_protocols, zapper_networks, walletBalance_url, protocolBalance_url, testAddress

# {"walletAssets": {
#       "network1": [{
#           "asset1": [
#                address
#                balanceUSD
#                etc
#
# ,"protocolAssets": {
#       "network1": [{
#          "protocol1": [{
#              "asset1": [
#                   address
#                   balanceUSD
#                   etc
# 

class ZapperQuery:
   def __init__(self, address):
      self._totalZapperAssets = {}
      self._walletAssetsByNetwork = {}
      self._protocolAssetsByNetwork = {}
      for network in zapper_networks:
         self._walletBalance = self.__checkWalletsBalance(address, network)
         self._protocolTokenBalance = self.__checkWalletsProtocolBalance(address, network)
         self._walletAssetsByNetwork[network] = self._walletBalance._assets
         self._protocolAssetsByNetwork[network] = self._protocolTokenBalance
      self._totalZapperAssets['walletAssets'] = self._walletAssetsByNetwork
      self._totalZapperAssets['protocolAssets'] = self._protocolAssetsByNetwork
   
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
   
   # Pass testAddress to Zapper Class
   zapper = ZapperQuery(testAddress)

   # Ex: Retrieving USD Balance of all assets in object
   totalBalance = 0
   for assetType, networks in zapper._totalZapperAssets.items():
      # Two options (walletAssets, protocolAssets)
      if assetType == "walletAssets":
         for network in networks:
            for asset in networks[network]:
               totalBalance += asset.balanceUSD
      elif assetType == "protocolAssets":
         for network in networks:
            for protocols in networks[network]:
               for protocol in protocols:
                  for asset in protocols[protocol]:
                     totalBalance += asset.balanceUSD
      else:
         print("Couldn't find assetType that met critera")
         break
   print("Total Balance (USD): ", totalBalance)
main()
