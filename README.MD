# Wallet Scout

Crypto API parser written in `Python` version `3.9.5`

This module contains 2 classes

 - Wallet
 - WalletScout

 Wallet builds an object from key/value pairs passed as a dictionary. Should have more validation.

 WalletScout is used to deserialize JSON, parse the data and build a list of Wallet objects from the zapper API call.

 Most of the class should be considered as private methods with the only real user interaction being instantiation and retrieval of _wallets list.

 Example Zapper Usage:

 ```python
from WalletScout import Wallet, WalletScout

 #Creating objects, passing JSON data
zapperData0 = WalletScout(json0)

zapperData1 = WalletScout(json1)

# Iterate _wallets list attr
# print each address and balance in USD
for wallet in zapperData0._wallets:
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
...

example result 2:
Total Balance (USD) 1338.0863295425552
```

Example Etherscan Balance Check Usage:

```python
import requests
from WalletScout import Wallet

<<<<<<< HEAD
# example etherscan Account Balance API call
=======
# example API URL
>>>>>>> 6528e857ef9c85f7226ded475fc9d78b6e6591dd
eth_url = "https://api.etherscan.io/api?module=account&action=balance&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&tag=latest&apikey="

# Make the GET request
response = requests.get(url = eth_url)
# Instantiate the Wallet object passing response as JSON object
wallet = Wallet(response.json())
# Access API response attributes.
print(wallet.result)

Result:
40891626854930000000000
```

Example of how Zapper wallet data is structured:
```json
"assets": [
  {
    "type": "wallet",
    "category": "wallet",
    "address": "0x111111111117dc0aa78b770fa6a738034120c302",
    "symbol": "1INCH",
    "decimals": 18,
    "label": "1INCH",
    "img": "networks/ethereum/0x111111111117dc0aa78b770fa6a738034120c302.png",
    "hide": false,
    "canExchange": false,
    "price": 2.31,
    "balance": 163.70649844792575,
    "balanceRaw": "163706498447925745505",
    "balanceUSD": 378.1620114147085
  },
```
