# Wallet Scout
==============

Zapper API parser written in `Python` version `3.9.5`

This module contains 2 classes

 - Wallet
 - WalletScout

 Wallet is used for manipulation of each dict within the Asset list returned by the Zapper API call

 WalletScout is mostly unnecessary as is but a class based approach will make it easier for future development.

 For now it simply accepts JSON data in some form during instantiation, parses the data, and populates a List of Wallet objects.

 Most of the class should be considered as private methods with the only real user interaction being instantiation and getWallets method.

 Example usage:

 ```walletScout = WalletScout(json)

 for wallet in walletScout._wallets:
    print(wallet._address)
```
