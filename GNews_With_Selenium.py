# package installations
# pip install googlenewsdecoder

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from googlenewsdecoder import new_decoderv1
import pprint
import base64
import re

# # Setup WebDriver for Chrome
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome()
#
# # Go to Google News (for US)
# # url = "https://news.google.com/home?hl=en-US&gl=US&ceid=US:en"
# # url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
# url = r"https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
# driver.get(url)
#
# # Allow some time for the page to load dynamic content
# driver.implicitly_wait(5)
#
# # Extract headlines and URLs
# headlines = driver.find_elements(By.XPATH, '//h3/a')
#
# for headline in headlines:
#     title = headline.text
#     link = headline.get_attribute('href')
#     print(f"Title: {title}\nLink: {link}\n")
#
# # Close the driver after scraping
# driver.quit()

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode

driver = webdriver.Chrome(options=options)
url = r"https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
driver.get(url)
driver.implicitly_wait(5)
headline_componet = driver.find_elements(By.CLASS_NAME, 'IBr9hb')
news_source_componet = headline_componet[0].find_elements(By.CLASS_NAME, 'vr1PYe') #
# news_source_componet = headline_componet[0].find_elements(By.CLASS_NAME, 'a7P8l') #
article_componet = headline_componet[0].find_elements(By.CLASS_NAME, 'gPFEn')
# pprint.pprint(article[0].text)
# pprint.pprint(article[0].get_attribute('href'))
headline = article_componet[0].text
headline_url = article_componet[0].get_attribute('href')
news_source = news_source_componet[0].get_attribute('innerText')
print("Headline: {}".format(headline))
print("Headline-URL: {}".format(headline_url))
print("news_source: {}".format(news_source))
driver.quit()

interval_time = 5 # default interval is None, if not specified
try:
    decoded_url = new_decoderv1(headline_url, interval=interval_time)
    if decoded_url.get("status"):
        print("Decoded URL:", decoded_url["decoded_url"])
        open_url = decoded_url["decoded_url"]
    else:
        print("Error:", decoded_url["message"])
except Exception as e:
    print(f"Error occurred: {e}")

# driver = webdriver.Chrome()
# driver.get(open_url)
# driver.implicitly_wait(5)