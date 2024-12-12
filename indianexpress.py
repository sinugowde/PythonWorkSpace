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


# url = r"https://indianexpress.com/article/education/study-abroad/educational-qualification-new-rbi-governor-sanjay-malhotra-ias-iit-kanpur-princeton-university-9715328/"
url = r'https://indianexpress.com/article/india/supreme-court-criticises-misuse-ipc-section-498a-husbands-kin-9719169/'
web_driver = webdriver.Chrome()
web_driver.get(url)

news_article = dict()
art = web_driver.find_elements(By.CLASS_NAME, "ie_single_story_container")
news_article['headline'] = art[0].find_elements(By.TAG_NAME, 'h1')[0].text
news_article['synopsis'] = art[0].find_elements(By.TAG_NAME, 'h2')[0].text
news_body = art[0].find_elements(By.ID, 'pcl-full-content')[0]
news_article['body'] = list()
body_sections = news_body.find_elements(By.TAG_NAME, 'p')
for i, sect in enumerate(body_sections):
    # time.sleep(1)
    brk = sect.get_attribute('class')
    news_article['body'].append(sect.text)
    print("DEBUG-{}: [{}] - {}".format(i, brk, sect.text))
    if brk == 'no_first_intro_para':
        break
pprint.pprint(news_article)
web_driver.quit()