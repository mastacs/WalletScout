#zapper_protocols = [
#   "aave", "aave-amm", "aave-v2", "adamant", "alchemix", "alpha", "augur", "autofarm", "b-protocol", "badger", "balancer", "bancor", "barnbridge", "beefy", "bella", "belt", "bitcoin", "bzx", "compound", "convex", "cover", "cream", "curve", "defisaver", "defi-swap", "derivadex", "deversifi","dforce","dhedge", "dodo", "dsd", "dydx", "88mph", "ellipsis", "epns", "esd", "futureswap","harvest", "hegic", "idle", "inverse", "keeper-dao", "kyber-dmm", "linkswap", "liquity", "loopring", "maker", "mintr", "mooniswap", "mushroom", "nft", "1inch", "opyn", "other", "pancakeswap", "pickle", "pooltogether", "quickswap", "rari", "realt", "reflexer", "ribbon", "sablier", "saddle", "sfinance", "shell", "smoothy", "snowswap", "spookyswap", "sushiswap", "swerve", "synthetix", "the-graph", "tokensets", "tokens", "uniswap", "uniswap-v2", "uniswap-v3", "unit", "value", "venus", "vesper", "waultswap", "xsigma", "yaxis", "yearn"
#]

zapper_protocols = [
    "yearn", "alchemix"
]

zapper_networks = [
    "ethereum"
]

#zapper_networks = [
#   "ethereum", "fantom", "polygon", "optimism", "xdai", "binance-smart-chain"
#]

zapper_walletBalance_url = "https://api.zapper.fi/v1/protocols/tokens/balances?addresses[]=%s&network=%s&api_key=96e0cc51-a62e-42ca-acee-910ea7d2a241"
zapper_protocolBalance_url = "https://api.zapper.fi/v1/protocols/%s/balances?addresses[]=%s&network=%s&api_key=96e0cc51-a62e-42ca-acee-910ea7d2a241"
etherscan_url = "https://api.etherscan.io/api?module=account&action=%s&address=%s&startblock=0&endblock=999999999&sort=asc&apikey=M4SIQFEQ5D6KXNQMIZXF86MX2R8XAK5NDJ"

testAddress = "0x01e6fd0aE73D9194b19f9B376065577927A0D5f5"
