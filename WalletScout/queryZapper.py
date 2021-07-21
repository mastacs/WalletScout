import requests
from os import path
from walletScout import Scout
from zapperVariables import zapper_protocols, zapper_networks, walletBalance_url, protocolBalance_url, testAddress


# Object Structure:
#
#     {"walletAssets": {
#           "network1": [{
#                "asset1": [
#                    address
#                     balanceUSD
#                     etc
#
#     ,"protocolAssets": {
#           "network1": [{
#              "protocol1": [{
#                    "asset1": [
#                       address
#                       balanceUSD
#                       etc
# 

class ZapperQuery:
   def __init__(self, address):
      # Top level dictionary for all wallet assets + protocol token assets
      self._totalZapperAssets = {}
      # All wallet assets
      self._walletAssetsByNetwork = {}
      # All protocol token assets
      self._protocolAssetsByNetwork = {}
      # Loop through Zappers supported networks
      for network in zapper_networks:
         # Get wallet assets
         self._walletBalance = self.__checkWalletsBalance(address, network)
         # Get protocol token assets
         self._protocolTokenBalance = self.__checkWalletsProtocolBalance(address, network)
         # Add results to respective dictionary based on current network
         self._walletAssetsByNetwork[network] = self._walletBalance._assets
         self._protocolAssetsByNetwork[network] = self._protocolTokenBalance
      # Add results to top level dictionary
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
      # Loop through supported Protocol
      for protocol in zapper_protocols:
         assetsPerProtocol = []
         # Get results based on current Protocol/dApp and provided address/network
         response = requests.get(url = (
            protocolBalance_url % (
               protocol,
               address,
               network
            )
         ))
         # Instantiate the Wallet object via Scout class, passing response as object
         perProtocol = Scout(response.json())
         # Loop through assets
         for asset in perProtocol._assets:
            # Append asset to assets object
            assetsPerProtocol.append(asset)
         # Add list of assets to dictionary with associated protocol being the key 
         perProtocolAssets[protocol] = assetsPerProtocol
      # Append Protocols dictionary to list containing total Assets  
      totalAssetsPerProtocol.append(perProtocolAssets)
      # Returns list of protocols 
      return totalAssetsPerProtocol

def getZapperBalanceUSD(obj):
   # Ex: Retrieving USD Balance of all assets in object
   totalBalance = 0
   for assetType, networks in obj._totalZapperAssets.items():
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

def main():
   # Pass testAddress to Zapper Class
   zapper = ZapperQuery(testAddress)
   getZapperBalanceUSD(zapper)
main()
