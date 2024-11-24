import feedparser

# # Using RSS feeder
# url = 'https://news.google.com/news/rss'  # Replace with any specific feed URL
# feed = feedparser.parse(url)
#
# for entry in feed.entries[:5]:  # Top 5 headlines
#     print(entry.title)

# Using Web Scraping
import requests
from bs4 import BeautifulSoup

url = 'https://news.google.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('h3')
print(f"Headlines Count: {len(headlines)}")
for headline in headlines:
    if headline.find(attrs={'href': True}):
        print("{}: {}".format(headline.get_text(), (headline.find(attrs={'href': True}).get('href')).replace(".", url)))
    else:
        print("{}: No href link attached".format(headline.get_text()))