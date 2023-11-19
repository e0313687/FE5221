import requests
import pandas as pd
from datetime import datetime, timedelta

# API settings
api_key = '4eb5625593802efb45e9cb4a2b3bf457'
base_url = 'http://api.exchangeratesapi.io/v1'
default_base_currency = 'EUR'  # Default base currency
target_currencies = 'SGD,CNY'

# Define the date range
start_date = datetime(2023, 10, 11)
end_date = datetime(2023, 11, 10)

# Function to fetch data for a single day
def fetch_daily_data(date):
    formatted_date = date.strftime('%Y-%m-%d')
    url = f'{base_url}/{formatted_date}?access_key={api_key}&symbols={target_currencies}'
    response = requests.get(url)
    return response.json()

# Fetch data for each day in the range
date_range = pd.date_range(start_date, end_date)
all_data = {}
for single_date in date_range:
    daily_data = fetch_daily_data(single_date)
    all_data[single_date.strftime('%Y-%m-%d')] = daily_data

# Convert to DataFrame for easier handling
df = pd.DataFrame.from_dict(all_data, orient='index')

# Calculate SGD/CNY rate indirectly
df['SGD_CNY_Rate'] = df.apply(lambda row: row['rates']['CNY'] / row['rates']['SGD'] if 'rates' in row and 'SGD' in row['rates'] and 'CNY' in row['rates'] else None, axis=1)

# Save the complete data to a CSV file
df.to_csv('Complete_SGD_CNY_Exchange_Rates_Data.csv')

print(df)