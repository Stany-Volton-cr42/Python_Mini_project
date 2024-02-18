import requests

# This is the API to fetch the current currency in the website
API_KEY = 'fca_live_sd92J4fFeohy1nEjJvHHsTGamVbYZfaUX1tPMP3k'

# This is the link of the website and adding api to convert
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

# sample currency code
CURRENCIES = ["USD","CAD","EUR","AUD","CNY"]

# base is given by the user 
def Convert_currency(base):
    currencies = ",".join(CURRENCIES)
    # in url it goes to the website and fetch the perticular api 
    #takes the base currecy to the user and add the target currencies
    url = f'{BASE_URL}&base_currency={base}&currencies={currencies}'
    try:
        response = requests.get(url)
        data = response.json() #json return the dictionary of the base result and the target
        return data["data"]
    except:
        print("Invlid Input!")
        return None

while True:
    print("Chose the currency from: USD CAD EUR AUD CNY")
    base = input("\nEnter the Currency: {q for Quit} ").upper()
    rate = int(input(f"Enter the rate of {base}\n"))
    if base == "Q":
        break


    data = Convert_currency(base)
    if not data:
        continue
    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}:{value*rate}")
