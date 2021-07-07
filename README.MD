# Wallet Scout

Zapper API parser written in `Python` version `3.9.5`

This module contains 2 classes

 - Wallet
 - WalletScout

 Wallet is used for manipulation of each dict within the Asset list returned by the Zapper API call

 WalletScout is mostly unnecessary as is but a class based approach will make it easier for future development.

 For now it simply accepts JSON data in some form during instantiation, parses the data, and populates a List of Wallet objects.

 Most of the class should be considered as private methods with the only real user interaction being instantiation and retrieval of _wallets list.

 Example usage:

 ```python
 #Creating the object, passing JSON data
 walletScout = WalletScout(json)

#Iterating the list of Wallet objects in _wallets
for wallet in walletScout._wallets:
    print('Address: ', wallet._address)
    print('Balance (raw): ', wallet._balanceRaw)

totalBalance = 0
for wallet in walletScout._wallets:
    totalBalance += wallet._balanceUSD

print(totalBalance)

example result 1:
Address:  0x111111111117dc0aa78b770fa6a738034120c302
Balance (raw):  163706498447925745505
Address:  0xfc1e690f61efd961294b3e1ce3313fbd8aa4f85d
Balance (raw):  5261462092496710734
Address:  0x028171bca77440897b824ca71d1c56cac55b68a3
Balance (raw):  28344636483486713708
Address:  0x94d863173ee77439e4292284ff13fad54b3ba182
Balance (raw):  16096597114486205404
Address:  0x06af07097c9eeb7fd685c692751d5c66db49c215
Balance (raw):  950000000000000000
...

example result 2:
Total Balance (USD) 1338.0863295425552
```
