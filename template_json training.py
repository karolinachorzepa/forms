import requests
from pprint import pprint

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
pprint(data)
#pprint jest do sprawdzenia jak wyglada odpowiedz z api, pprint ladnie interpretuje json plik z api,  
print(len(data))
#lista 1elementowa, 
data=data[0]
print(data.keys())
print(data["rates"])
#pod kluczem rates jest lista slownikow, 
print(data["rates"][0].keys()) #tutaj obsluga api - wywolanie rates, 

#wyciaganie informacje z api: sprawdzenie odpowiedzi, poznanie struktur, az w koncu konkretna odpowiedz - to co potrzebujesz  
currencies = data["rates"]
for currency in currencies:
    print(f"{currency['currency']} costs {currency['bid']}.")
def create_csv():
    with open("currency_exchange_rates.csv", "w", newline="") as csvfile:
        filednames = ['currency', 'code', 'bid', 'ask']
        writer = csv.DictWriter(csvfile, fieldnames=filednames, delimiter=";")
        writer.writeheader()
        writer.writerows(currency_list)
        print("csv created")
