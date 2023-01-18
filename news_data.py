import requests as req
import datetime as dt

today = dt.date.today()
two_days_before = str(today - dt.timedelta(days=2))

API_KEY = "4aff8babe58a4e4fb2babdce5a4c3017"


def get_news_data( keyword="TESLA") -> list:
    """get popular news from 2 days to today , keyword set to Tesla """
    parameters = {
        "q": keyword,
        "from": two_days_before,
        "to":str(today),
        "sortBy": "popularity",
        "apikey": API_KEY,
        "language": "en",
        "searchIn": "title",
    }
    res = req.get("https://newsapi.org/v2/everything", params=parameters)
    res.raise_for_status()
    # print(res.url)
    data = res.json()
    data_articles = data['articles'][:3]
    newss = []
    for i in range(len(data_articles)):
        news = f"{i + 1}. {data_articles[i]['title']}\n" \
                f"Description: {data_articles[i]['description'][:200]}\n"
        newss.append(news)
    return newss


if __name__ == "__main__":
    print(get_news_data(keyword="Tesla"))
