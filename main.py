# include date n send massage

from sending_sms import send_massage
from stock_price_data import get_stock_prc
from news_data import get_news_data

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

price_change = get_stock_prc(symbol=STOCK)
newss = get_news_data(keyword=COMPANY_NAME)
status = "UP" if price_change > 0 else "DOWN"
for news in newss:
    massage = f"{COMPANY_NAME.upper()} : {status} {abs(price_change)} \n{news}"
    print(massage)
    send_massage(massage=massage, to_num="+918901116612")
