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
    print('Address: ', wallet.address)
    print('Balance (USD): ', wallet.balanceUSD)

# Iterates _wallets list attr
# Sums balance in USD
totalBalance = 0
for wallet in walletScout._wallets:
    totalBalance += wallet.balanceUSD
print('Total Balance (USD)', totalBalance)

# Simple printout of each wallet object and all attributes.
for item in walletScout._wallets:
    print("WALLET OBJECT")
    print(item.type)
    print(item.category)
    print(item.address)
    print(item.symbol)
    print(item.decimals)
    print(item.label)
    print(item.img)
    print(item.hide)
    print(item.canExchange)
    print(item.price)
    print(item.balance)
    print(item.balanceRaw)
    print(item.balanceUSD)
    print("************")
