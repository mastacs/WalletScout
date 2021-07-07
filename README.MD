# Wallet Scout

Zapper API parser written in `Python` version `3.9.5`

This module contains 2 classes

 - Wallet
 - WalletScout

 Wallet builds an object from key/value pairs passed as a dictionary. Should have more validation.

 WalletScout is used to deserialize JSON, parse the data and build a list of Wallet objects from the zapper API call.

 Most of the class should be considered as private methods with the only real user interaction being instantiation and retrieval of _wallets list.

 Example usage:

 ```python
from Wallets import Wallet, WalletScout

 #Creating objects, passing JSON data
zapperData0 = WalletScout(json0)

zapperData1 = WalletScout(json1)

# Iterate _wallets list attr
# print each address and balance in USD
for wallet in zapperData._wallets:
    print('Address: ', wallet.address)
    print('Balance (USD): ', wallet.balanceUSD)

# Iterates _wallets list attr
# Sums balance in USD
totalBalance = 0
for wallet in walletScout._wallets:
    totalBalance += wallet.balanceUSD
print('Total Balance (USD)', totalBalance)

example result 1:
Address:  0x111111111117dc0aa78b770fa6a738034120c302
Balance (USD):  378.1620114147085
Address:  0xfc1e690f61efd961294b3e1ce3313fbd8aa4f85d
Balance (USD):  5.261462092496711
Address:  0x028171bca77440897b824ca71d1c56cac55b68a3
Balance (USD):  28.344636483486713
Address:  0x94d863173ee77439e4292284ff13fad54b3ba182
Balance (USD):  0.8932323670770684
Address:  0x06af07097c9eeb7fd685c692751d5c66db49c215
Balance (USD):  0.8925991
...

example result 2:
Total Balance (USD) 1338.0863295425552
```
