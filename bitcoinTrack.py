from requests import Request,Session
import json

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"


parameters = {
    'slug': 'bitcoin',
    'convert':'USD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '9e1b50be-e032-4ea4-8962-9c8681a789ea'
}

session = Session()
session.headers.update(headers)
response = session.get(url,params=parameters)

data = response.json()
btc_price_usd = data['data']['1']['quote']['USD']['price']


print(f"比特幣（BTC）現在價格：${btc_price_usd}")
