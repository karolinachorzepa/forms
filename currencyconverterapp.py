import requests, csv
from pprint import pprint

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
pprint(data)
data=data[0]
print(data.keys())
print(data["rates"])
print(data["rates"][0].keys())
currencies = data["rates"]

for currency in currencies:
    print(f"{currency['currency']} costs {currency['bid']}.")


def create_csv():
    with open("currency_exchange_rates.csv", "w", end="") as csvfile:
        filednames = ['currency', 'code', 'bid', 'ask']
        writer = csv.DictWriter(csvfile, fieldnames=filednames, delimiter=";")
        writer.writeheader()
        writer.writerows(currency_list)
        print("csv created")
