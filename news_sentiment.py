import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Initialize the Vader Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment(text):
    if text:  # Check if the text is not empty
        return sia.polarity_scores(text)['compound']  # Returns the compound score
    else:
        return 0  # Return 0 for empty text

# Read CSV files
china_news_df = pd.read_csv('ch_news_articles.csv')
singapore_news_df = pd.read_csv('sg_news_articles.csv')

# Analyze sentiment for each news title and description
china_news_df['title_sentiment'] = china_news_df['Title'].apply(analyze_sentiment)
china_news_df['description_sentiment'] = china_news_df['Description'].apply(analyze_sentiment)

singapore_news_df['title_sentiment'] = singapore_news_df['Title'].apply(analyze_sentiment)
singapore_news_df['description_sentiment'] = singapore_news_df['Description'].apply(analyze_sentiment)

# Handle dates with no news by filling NaN values with 0
china_news_df.fillna(0, inplace=True)
singapore_news_df.fillna(0, inplace=True)

# Output to new CSV files
china_news_df.to_csv('china_news_with_sentiment.csv', index=False)
singapore_news_df.to_csv('singapore_news_with_sentiment.csv', index=False)
