import requests

def get_currencies(currency_codes: list, url="https://www.cbr-xml-daily.ru/daily_json.js") -> dict:
    """
    функция принимает на вход список из имен валют
    и возвращает словарь с ключами - именами валют содержимыми - курсом к рублю

    пример:
    ["USD", "JPY", "AZN", "EUR"]
    >> {'USD': 78.2503, 'JPY': 50.2023, 'AZN': 46.0296, 'EUR': 90.788}
    """
    request = requests.get(url)
    values = {}

    data = request.json()
    for currency in currency_codes:
        values[currency] = data["Valute"][currency]["Value"]

    return values