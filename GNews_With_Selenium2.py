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
import time

# Google Headlines page URL
google_url = r"https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"

# Number top headline count
HEADLINE_COUNT = 5


# Get the Web driver handle
def get_WebDriver(url):
    # Set up Chrome options
    options = Options()
    # options.add_argument("--headless")  # Run in headless mode

    web_driver = webdriver.Chrome(options=options)
    web_driver.get(url)
    web_driver.implicitly_wait(5)
    return web_driver


# Get Tops coverage links
def coverage_links(url):
    links = list()
    # Get Google headline page driver
    driver = get_WebDriver(url)
    coverages = driver.find_elements(By.CLASS_NAME, "jKHa4e")

    for i in range(HEADLINE_COUNT):
        links.append(coverages[i].get_attribute('href'))
    driver.quit()

    for i, link in enumerate(links):
        print("{}: {}".format(i, link))

    return links


def get_article_links(coverages):
    interval_time = 5
    collection = list()
    for i, lnk in enumerate(coverages):
        time.sleep(3)
        details = dict()
        coverage = "coverage_{}".format(i)
        details['gLink'] = lnk
        details[coverage] = list()
        driver = get_WebDriver(lnk)
        driver.implicitly_wait(5)
        main_div = driver.find_elements(By.CSS_SELECTOR, ".ndSf3d.eDrqsc.eVhOjb.Oc0wGc.j7vNaf.dIgQgd")
        if not main_div:
            main_div = driver.find_elements(By.CSS_SELECTOR, ".lBwEZb.BL5WZb.GndZbb.ENDuKc")

        articles = main_div[0].find_elements(By.TAG_NAME, "article")
        # articles[0].find_elements(By.CLASS_NAME, "VDXfz")[0].get_attribute('href')
        # art[0].find_elements(By.CSS_SELECTOR, "article:nth-of-type(1) a")[0].get_attribute('href')

        for j in range(len(articles)):
            temp_dict = dict()
            g_url = articles[j].find_elements(By.CLASS_NAME, "ipQwMb.ekueJc.RD0gLb")[0].find_element(By.TAG_NAME,"a").get_attribute('href')
            decoded_url = new_decoderv1(g_url, interval=interval_time)
            if decoded_url.get("status"):
                art_url = decoded_url["decoded_url"]
            else:
                print("Error:", decoded_url["message"])
                art_url = "Couldn't Decode the article URL."
            art_title = articles[j].find_elements(By.CLASS_NAME, "ipQwMb.ekueJc.RD0gLb")[0].find_element(By.TAG_NAME, "a").text
            art_source = articles[j].find_element(By.CLASS_NAME, "N0NI1d.AVN2gc.WfKKme ").find_element(By.CLASS_NAME,'wEwyrc').get_attribute('innerText')
            print("art_title: {}".format(art_title))
            print("art_source: {}".format(art_source))
            print("art_url: {}".format(art_url))
            temp_dict['art_title'] = art_title
            temp_dict['art_source'] = art_source
            temp_dict['art_url'] = art_url
            details[coverage].append(temp_dict)
            print('-' * 5)
        driver.quit()
        collection.append(details)
        print('~' * 5)
    return collection


# Collect top Coverage links from Google News
top_coverages = coverage_links(google_url)
print("=" * 5)

# Scrape coverage links one by one & get the source website links of them
coverage_details = get_article_links(top_coverages)
print("=" * 5)
pprint.pprint(coverage_details)

