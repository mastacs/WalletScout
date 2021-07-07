# Wallet Scout

Zapper API parser written in `Python` version `3.9.5`

This module contains 2 classes

 - Wallet
 - WalletScout

 Wallet is used for manipulation of each dict within the Asset list returned by the Zapper API call

 WalletScout is mostly unnecessary as is but a class based approach will make it easier for future development.

 For now it simply accepts JSON data in some form during instantiation, parses the data, and populates a List of Wallet objects.

 Most of the class should be considered as private methods with the only real user interaction being instantiation and getWallets method.

 Example usage:

 ```python
 walletScout = WalletScout(json)

 for wallet in walletScout._wallets:
    print(wallet._address)

    example result:
    0x111111111117dc0aa78b770fa6a738034120c302
    0xfc1e690f61efd961294b3e1ce3313fbd8aa4f85d
    0x028171bca77440897b824ca71d1c56cac55b68a3
    0x94d863173ee77439e4292284ff13fad54b3ba182
    0x06af07097c9eeb7fd685c692751d5c66db49c215
    0x0000000000000000000000000000000000000000
    0x0954906da0bf32d5479e25f46056d22f08464cab
    0xc12d1c73ee7dc3615ba4e37e4abfdbddfa38907e
    0x8207c1ffc5b6804f6024322ccf34f29c3541ae26
    0x016bf078abcacb987f0589a6d3beadd4316922b0
    0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f
    0x57ab1ec28d129707052df4df418d58a2d46d5f51
    0x6b3595068778dd592e39a122f4f5a5cf09c90fe2
    0xc7283b66eb1eb5fb86327f08e1b5816b0720212b
    0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48
    0x49e833337ece7afe375e44f4e3e8481029218e5c
    0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
    0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e
    0x837010619aeb2ae24141605afc8f66577f6fb2e7
```
