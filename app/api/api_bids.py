import httpx
from app.utils.formatters import toDoubleDecimal
from app.models.bids import Bids

# Endpoint da API de cotações
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL'

# Faz uma requisição GET para a API
response = httpx.get(url)

# Analisa a resposta da API como um objeto JSON
data = response.json()

# Lista de objetos Cotacoes
bids: list[Bids] = []

i = 0

# Loop pelos dados da API e cria objetos Cotacoes
for code, item in data.items():
    i += 1
    name = item['name']
    bid = toDoubleDecimal(item['bid'])
    bid_obj = Bids(i, name, bid)
    bids.append(bid_obj)

def returnBids():
  return bids

def returnBidByCode(value):
  return [bid for bid in bids if bid.code == value][0]