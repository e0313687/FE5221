from newsapi import NewsApiClient
import csv
# Init
newsapi = NewsApiClient(api_key='083a35e13285461da368fa6637e0982a')

all_articles = newsapi.get_everything(
                                    q='China',
                                #   q='Singpoare',
                                #   sources='bbc-news,google-news',
                                #   domains='bbc.co.uk,techcrunch.com',
                                    from_param='2023-10-11',
                                    to='2023-11-10',
                                    language='en',
                                    sort_by='relevancy')

# print(all_articles)

# Function to save articles to a CSV file
def save_articles_to_csv(articles, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Published At', 'Title', 'Source', 'Author', 'URL', 'Description', 'Content'])

        # Write the article data
        for article in articles:
            writer.writerow([article['publishedAt'],
                            article['title'],
                            article['source']['name'],
                            article['author'],
                            article['url'],
                            article['description'],
                            article['content']])

# Check if there are articles in the response
if all_articles and all_articles['articles']:
    save_articles_to_csv(all_articles['articles'], 'ch_news_articles.csv')
    # save_articles_to_csv(all_articles['articles'], 'sg_news_articles.csv')
else:
    print("No articles found.")

