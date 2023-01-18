import requests as req

STOCK = "TSLA" #STOCK SYMBOL TO TRACK
API_KEY = YOUR_API_KEY


def get_stock_prc(symbol: str):
    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "apikey": API_KEY
    }
    res = req.get("https://www.alphavantage.co/query", params=parameters)
    res.raise_for_status()
    data = res.json()

    daily_data = data["Time Series (Daily)"]
    first_two_entries = []
    for key in daily_data:
        if len(first_two_entries) > 2:
            break
        first_two_entries.append(key)
    yest_close_price = float(daily_data[first_two_entries[0]]['4. close'])
    prev_close_price = float(daily_data[first_two_entries[1]]['4. close'])
    prc = round((yest_close_price - prev_close_price) * 100 / yest_close_price, 2)
    return prc


if __name__ == "__main__":
    prc_change = get_stock_prc(STOCK)
    if abs(prc_change) > 3:
        print("news")
