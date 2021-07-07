import sys, json
from Wallets import Wallet, WalletScout

# Mostly for testing, using cmd line argv for file I/O
# ex. Call from cmd: python app.py Test.json
# Drag and drop Test.json onto app.py
# etc. This will likely be removed in future and replaced.
if len(sys.argv) > 1:
    file = open(sys.argv[1])
else:
    file = input("No file found. Enter path:")

# The only purpose of app.py is for testing both classes
# and as usage examples.
walletScout = WalletScout(file)

# Iterate _wallets list attr
# print each address and balance in USD
for wallet in walletScout._wallets:
    print('Address: ', wallet._address)
    print('Balance (USD): ', wallet._balanceUSD)

# Iterates _wallets list attr
# Sums balance in USD
totalBalance = 0
for wallet in walletScout._wallets:
    totalBalance += wallet._balanceUSD
print('Total Balance (USD)', totalBalance)

# Simple printout of each wallet object and all attributes.
for item in wallets:
    print("WALLET OBJECT")
    print(item._type)
    print(item._category)
    print(item._address)
    print(item._symbol)
    print(item._decimals)
    print(item._label)
    print(item._img)
    print(item._hide)
    print(item._canExchange)
    print(item._price)
    print(item._balance)
    print(item._balanceRaw)
    print(item._balanceUSD)
    print("************")
