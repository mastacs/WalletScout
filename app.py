import sys, json
from wallet import Wallet
from walletScout import WalletScout

# Mostly for testing, using cmd line argv for file I/O
# ex. Call from cmd: python app.py Test.json
# Drag and drop Test.json onto app.py
# etc. This will likely be removed in future and replaced.
if len(sys.argv) > 1:
    file = open(sys.argv[1])
else:
    file = input("No file found. Enter path:")

walletScout = WalletScout(file)

wallets = walletScout.getWallets()

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
