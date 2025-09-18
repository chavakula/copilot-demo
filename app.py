import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Function to fetch live cryptocurrency prices
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            prices = {}
            for coin in data:
                prices[coin['name']] = coin['current_price']
            return prices
        else:
            return {coin: "Error fetching price" for coin in [
                "Bitcoin", "Ethereum", "Tether", "BNB", "Solana", "USDC", "XRP", "Dogecoin", "Toncoin", "Cardano", 
                "TRON", "Avalanche", "Shiba Inu", "Polygon", "Polkadot", "Chainlink", "Bitcoin Cash", "NEAR Protocol",
                "Uniswap", "Litecoin", "Dai", "Internet Computer", "Kaspa", "Ethereum Classic", "Monero", "Stellar",
                "OKB", "Filecoin", "Mantle", "Arbitrum", "Pepe", "WETH", "Aptos", "Hedera", "LEO Token", "Cronos",
                "VeChain", "Polygon MATIC", "Algorand", "Fantom", "Optimism", "Cosmos", "Injective", "Stacks",
                "Theta Network", "Render", "Immutable", "First Digital USD", "Maker", "Lido DAO", "Aave", "The Graph",
                "Quant", "Synthetix", "Bitcoin SV", "Zcash", "IOTA", "Flow", "Tezos", "Elrond", "PancakeSwap",
                "THORChain", "Helium", "Axie Infinity", "Kava", "Enjin Coin", "1inch Network", "Compound", "Decentraland",
                "Sandbox", "Chiliz", "Basic Attention Token", "Loopring", "Curve DAO Token", "yearn.finance", "Sushi",
                "Bancor", "OMG Network", "0x", "Kyber Network Crystal", "Balancer", "Numeraire", "Storj", "Ocean Protocol",
                "Civic", "Augur", "district0x", "Power Ledger", "Status", "Request Network", "Aragon", "Gnosis",
                "Golem", "WazirX", "Smooth Love Potion", "Perpetual Protocol", "Harvest Finance", "Badger DAO",
                "Alpha Finance Lab", "BarnBridge"
            ]}
    except requests.exceptions.RequestException:
        return {coin: "Error fetching price" for coin in [
            "Bitcoin", "Ethereum", "Tether", "BNB", "Solana", "USDC", "XRP", "Dogecoin", "Toncoin", "Cardano", 
            "TRON", "Avalanche", "Shiba Inu", "Polygon", "Polkadot", "Chainlink", "Bitcoin Cash", "NEAR Protocol",
            "Uniswap", "Litecoin", "Dai", "Internet Computer", "Kaspa", "Ethereum Classic", "Monero", "Stellar",
            "OKB", "Filecoin", "Mantle", "Arbitrum", "Pepe", "WETH", "Aptos", "Hedera", "LEO Token", "Cronos",
            "VeChain", "Polygon MATIC", "Algorand", "Fantom", "Optimism", "Cosmos", "Injective", "Stacks",
            "Theta Network", "Render", "Immutable", "First Digital USD", "Maker", "Lido DAO", "Aave", "The Graph",
            "Quant", "Synthetix", "Bitcoin SV", "Zcash", "IOTA", "Flow", "Tezos", "Elrond", "PancakeSwap",
            "THORChain", "Helium", "Axie Infinity", "Kava", "Enjin Coin", "1inch Network", "Compound", "Decentraland",
            "Sandbox", "Chiliz", "Basic Attention Token", "Loopring", "Curve DAO Token", "yearn.finance", "Sushi",
            "Bancor", "OMG Network", "0x", "Kyber Network Crystal", "Balancer", "Numeraire", "Storj", "Ocean Protocol",
            "Civic", "Augur", "district0x", "Power Ledger", "Status", "Request Network", "Aragon", "Gnosis",
            "Golem", "WazirX", "Smooth Love Potion", "Perpetual Protocol", "Harvest Finance", "Badger DAO",
            "Alpha Finance Lab", "BarnBridge"
        ]}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/prices')
def get_prices():
    return jsonify(fetch_crypto_prices())

if __name__ == '__main__':
    app.run(debug=True)