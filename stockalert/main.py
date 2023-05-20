import requests
from datetime import datetime, timedelta
from twilio.rest import Client
#############set up twilio SMS##############
account_sid = 'AC1328a99e41bb958f92196c3f1178822d'
auth_token = '5601ba5694eee16329689fc0f1c46508'
client = Client(account_sid, auth_token)
#############get todays and yesterdays day###########
todays_date = str(datetime.today())
yesterdays_date = str(datetime.today() - timedelta(days=1))
today = todays_date.split(" ")[0]
yesterday = yesterdays_date.split(" ")[0]
#########given variables###############
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "a09f72ed65924a58a2cf6d67eb5e2eb7"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "K0V829IJOJNL6CPU"
########API parameters##########
stock_parameters = {

    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY

}

news_parameters = {
    "q" : COMPANY_NAME,
    "from" : yesterday,
    "sortBy" : "popularity",
    "apiKey" : NEWS_API_KEY

}
##########API requests#############
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
articles = news_data["articles"][:3]
today_close =stock_data["Time Series (Daily)"][today]["4. close"] 
yesterday_close = stock_data["Time Series (Daily)"][yesterday]["4. close"]
stock_diff = float(today_close)-float(yesterday_close)+2.00


def price_increase():
    for article in articles:
        description = article["description"]
        message = client.messages \
                .create(
                     body=f"TSLA UP {stock_diff}% 📈 \n {description}",
                     from_='+18667148590',
                     to='+15109195563'
                 )

def price_decrease():
    for article in articles:
        description = article["description"]
        message = client.messages \
                .create(
                     body=f"TSLA DOWN {stock_diff}% 📉 \n {description}",
                     from_='+18667148590',
                     to='+15109195563'
                 )
if stock_diff > 5.00:
    price_increase()
    print("Sent!")
elif stock_diff < -5.00:
    price_decrease()
    print("Sent!")




## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

