def get_ids():
    currency_id = ['AUD', 'AZN', 'DZD', 'GBP', 'AMD', 'BHD', 'BYN', 'BGN', 'BOB', 'BRL', 'HUF', 'VND', 'HKD', 'GEL', 'DKK', 'AED', 'USD', 'EUR', 'EGP', 'INR', 'IDR', 'IRR', 'KZT', 'CAD', 'QAR', 'KGS', 'CNY', 'CUP', 'MDL', 'MNT', 'NGN', 'NZD', 'NOK', 'OMR', 'PLN', 'SAR', 'RON', 'XDR', 'SGD', 'TJS', 'THB', 'BDT', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 'ETB', 'RSD', 'ZAR', 'KRW', 'JPY', 'MMK']
    return currency_id

"""import requests

def get_currencies(url="https://www.cbr-xml-daily.ru/daily_json.js") -> dict:
    request = requests.get(url)
    values = {}

    data = request.json()
    itog = []
    dataid = (data["Valute"]).keys()
    for dataid in dataid:
        itog.append(data["Valute"][dataid]["CharCode"])
    return itog
print(get_currencies())"""