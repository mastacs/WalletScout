from walletScout import Scout, Zapper
from zapperVariables import testAddress, zapper_networks


def main():
   totalBalance = 0
   for network in zapper_networks:
      zapper = Zapper(testAddress, network)
      for results in zapper._totalAssets:
         print("Contract Address: " + results.address)
         totalBalance += results.balanceUSD
   print("Total balance: ", totalBalance)
main()
