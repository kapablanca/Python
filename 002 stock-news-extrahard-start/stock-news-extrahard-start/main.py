import requests
import smtplib
from datetime import datetime, timedelta


my_email = "teststathovits@gmail.com"
password = "fxfqvghhdhxdhgsx"
alpha_vantage_api_key = "SWZSQW6BRNRZ6BK9"
news_api_key = "81d8b2049b9e429cb5a81d4d398b99f1"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_vantage_api_key
}

news_parameters = {
    "apiKey": news_api_key,
    "q": COMPANY_NAME,
    "searchin": "title",
    "sortBy": "publishedAt",
    "pageSize": 3
}


arrow = None
today = datetime.now()
yesterday = today - timedelta(1)
day_before_yesterday = yesterday - timedelta(1)


if today.weekday() != (6 or 0):
    response = requests.get(url=stock_url, params=stock_parameters)
    data = response.json()["Time Series (Daily)"]
    yesterday_close = float(data[f"{yesterday.date()}"]["4. close"])
    if today.weekday() != 1:
        day_before_close = float(data[f"{day_before_yesterday.date()}"]["4. close"])
    else:
        friday = today - timedelta(4)
        day_before_close = float(data[f"{friday.date()}"]["4. close"])

    change_percentage = round(((yesterday_close - day_before_close)/day_before_close) * 100, 2)
    # if abs(change_percentage) >= 5:
    if change_percentage > 0:
        arrow = "🔺".encode('utf-8')
    else:
        arrow = "🔻".encode('utf-8')
    response = requests.get(url=news_url, params=news_parameters)
    data = response.json()["articles"][:3]
    news = [f"Headline:{article['title']}\nBrief: {article['description']}" for article in data]

    for article in news:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="stathovits@hotmail.com",
                msg=f"Suject:{STOCK}: {arrow}{change_percentage}%\n\n"
                    f"{article}"

        )


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

