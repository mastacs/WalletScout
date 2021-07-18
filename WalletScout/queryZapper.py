from walletScout import Scout
import requests

# Zapper API call
eth_url = "https://api.zapper.fi/v1/protocols/tokens/balances?addresses[]=%s&network=%s&api_key=96e0cc51-a62e-42ca-acee-910ea7d2a241"
testAddress = "0x41146f3acB162FA19daC0cdC54C495a45c8aFefF"

# Add network supported by API here
networks = [
   "ethereum"
]

for network in networks:
   # Make the GET request
   response = requests.get(url = (eth_url % (testAddress.rstrip(), network)))
   # Instantiate the Wallet object passing response as JSON object
   zapper = Scout(response.json(), network)

   # Testing
   totalUSD = 0
   
   # Ex. Check Ethereum Network for balance
   for token in zapper._network["ethereum"]:
      totalUSD += token.balanceUSD
      print('Address: ' + token.address)

   # Check Fantom Network, etc

   # Testing
   print('Total Balance (USD): ', totalUSD)
