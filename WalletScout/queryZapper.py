from typing import Protocol
from walletScout import Scout
import requests

# Zapper API call
walletBalance_url = "https://api.zapper.fi/v1/protocols/tokens/balances?addresses[]=%s&network=%s&api_key=96e0cc51-a62e-42ca-acee-910ea7d2a241"
protocolBalance_url = "https://api.zapper.fi/v1/protocols/%s/balances?addresses[]=%s&network=%s&api_key=96e0cc51-a62e-42ca-acee-910ea7d2a241"
testAddress = "0x01e6fd0aE73D9194b19f9B376065577927A0D5f5"

protocols = [
   "aave", "aave-amm", "aave-v2", "adamant", "alchemix", "alpha", "augur", "autofarm", "b-protocol", "badger", "balancer", "bancor", "barnbridge", "beefy", "bella", "belt", "bitcoin", "bzx", "compound", "convex", "cover", "cream", "curve", "defisaver", "defi-swap", "derivadex", "deversifi","dforce","dhedge", "dodo", "dsd", "dydx", "88mph", "ellipsis", "epns", "esd", "futureswap","harvest", "hegic", "idle", "inverse", "keeper-dao", "kyber-dmm", "linkswap", "liquity", "loopring", "maker", "mintr", "mooniswap", "mushroom", "nft", "1inch", "opyn", "other", "pancakeswap", "pickle", "pooltogether", "quickswap", "rari", "realt", "reflexer", "ribbon", "sablier", "saddle", "sfinance", "shell", "smoothy", "snowswap", "spookyswap", "sushiswap", "swerve", "synthetix", "the-graph", "tokensets", "tokens", "uniswap", "uniswap-v2", "uniswap-v3", "unit", "value", "venus", "vesper", "waultswap", "xsigma", "yaxis", "yearn"
]

networks = [
   "ethereum", "fantom", "polygon", "optimism", "xdai", "binance-smart-chain"
]

def checkWalletsBalance(address, network):
   _totalBalanceUSD = 0
   response = requests.get(url = (
      walletBalance_url % (
         address,
         network
      )
   ))
   # Instantiate the Wallet object passing response as JSON object
   zapper = Scout(response.json(), network)
   #Check Balance in Wallet 
   for token in zapper._network[network]:
      _totalBalanceUSD += token.balanceUSD
      print('Balance Found in Contract Address: ' + token.address)
   return _totalBalanceUSD

def checkBalancePerProtocol(address, network):
   _totalBalanceUSD = 0

   for protocol in protocols:
      response = requests.get(url = (
         protocolBalance_url % (
            protocol,
            address,
            network
         )
      ))
      # Instantiate the Wallet object passing response as JSON object
      zapper = Scout(response.json(), network)
      #Check Balance in Wallet 
      for protocolBalance in zapper._network[network]:
         _totalBalanceUSD += protocolBalance.balanceUSD
         print('Protocol Address: ' + protocolBalance.address)
         print(_totalBalanceUSD)
   return _totalBalanceUSD


def main():
   for network in networks:
      #Check Wallets Balance in Protocols
      walletBalance = checkWalletsBalance(testAddress, network)
      protocolBalance = checkBalancePerProtocol(testAddress, network)
      # (Testing)
      totalUSD = walletBalance + protocolBalance
      print('Total Balance (USD): ', totalUSD)

main()
