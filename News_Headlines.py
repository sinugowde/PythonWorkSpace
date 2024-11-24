import requests
from bs4 import BeautifulSoup
import schedule
import time


# Function to fetch news from a website
def fetch_news():
    # url = "https://www.livemint.com/latest-news"  # Replace with the desired news site's URL
    url = "https://www.thehindu.com/news/national"  # Not working
    # url = "https://timesofindia.indiatimes.com/home/headlines"  # Not working
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    # response = requests.get(url, headers=headers, allow_redirects=False)

    # s = requests.Session()
    # s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    # response = s.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Example: Modify this to match the site's HTML structure
        # news_headlines = soup.find_all("h2", class_="headline", limit=10)
        news_headlines = soup.find_all("h1", class_="headline", limit=10)

        print("Top News Headlines:")
        for index, headline in enumerate(news_headlines, 1):
            title = headline.text.strip()
            link = headline.find("a")["href"]
            print(f"{index}. {title}")
            print(f"Link: {link}\n")
    else:
        print(f"Failed to fetch news. HTTP Status Code: {response.status_code}")


# Schedule the function to run daily
# schedule.every().day.at("09:00").do(fetch_news)  # Adjust the time as needed

# print("News fetching script is running... Press Ctrl+C to exit.")
# while True:
    # schedule.run_pending()
    # time.sleep(1)

fetch_news()
