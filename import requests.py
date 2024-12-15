import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize Sentiment Analyzer
nltk.download('vader_lexicon')
sentiment_analyzer = SentimentIntensityAnalyzer()

# API Keys (replace with your actual keys)
SENATE_STOCK_API_KEY = "your_senate_stock_api_key"
YAHOO_FINANCE_API_KEY = "your_yahoo_finance_api_key"
NEWS_API_KEY = "your_news_api_key"

# API URLs
SENATE_STOCK_URL = "https://api.senatestockwatcher.com/v1/transactions"
YAHOO_FINANCE_URL = "https://yfapi.net/v6/finance/quote"
NEWS_API_URL = "https://newsapi.org/v2/everything"

# Fetch Politicians' Trades
def fetch_politician_trades():
    headers = {"Authorization": f"Bearer {SENATE_STOCK_API_KEY}"}
    response = requests.get(SENATE_STOCK_URL, headers=headers)
    return response.json()

# Fetch Stock Data
def fetch_stock_data(symbol):
    params = {"symbols": symbol, "region": "US"}
    headers = {"x-api-key": YAHOO_FINANCE_API_KEY}
    response = requests.get(YAHOO_FINANCE_URL, headers=headers, params=params)
    return response.json()

# Fetch News Sentiment
def fetch_news_sentiment(company_name):
    params = {"q": company_name, "apiKey": NEWS_API_KEY}
    response = requests.get(NEWS_API_URL, params=params)
    news_articles = response.json().get("articles", [])
    sentiments = [sentiment_analyzer.polarity_scores(article["description"])["compound"] for article in news_articles if "description" in article]
    return sum(sentiments) / len(sentiments) if sentiments else 0

# Main Analysis Pipeline
def analyze_politician_trading():
    trades = fetch_politician_trades()
    data = []

    for trade in trades.get("data", []):
        symbol = trade.get("ticker")
        company_name = trade.get("company")
        trade_type = trade.get("transaction_type")
        trade_date = trade.get("transaction_date")

        # Fetch stock data
        stock_data = fetch_stock_data(symbol)
        stock_price = stock_data.get("quoteResponse", {}).get("result", [{}])[0].get("regularMarketPrice", None)

        # Fetch news sentiment
        news_sentiment = fetch_news_sentiment(company_name)

        data.append({
            "Politician": trade.get("senator"),
            "Company": company_name,
            "Symbol": symbol,
            "Transaction Type": trade_type,
            "Transaction Date": trade_date,
            "Stock Price": stock_price,
            "News Sentiment": news_sentiment
        })

    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df

# Visualization
def visualize_data(df):
    sns.set_theme(style="whitegrid")

    # Bar Plot: Stock Prices by Politicians
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="Politician", y="Stock Price", hue="Transaction Type")
    plt.title("Politicians' Trades and Stock Prices")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Sentiment Analysis
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x="News Sentiment", kde=True, hue="Transaction Type")
    plt.title("News Sentiment of Companies Traded by Politicians")
    plt.tight_layout()
    plt.show()

# Execute
if __name__ == "__main__":
    df = analyze_politician_trading()
    print(df.head())  # Display top rows
    visualize_data(df)

