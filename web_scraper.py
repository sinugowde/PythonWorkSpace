from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url = 'https://www.amazon.in/s/ref=nb_sb_ss_c_1_6?url=search-alias%3Daps&field-keywords=python+programming+books&sprefix=python%2Caps%2C311&crid=2WY3BUKQYEM9Y'

my_client = urlopen(my_url)
# page_soup = BeautifulSoup(page_html, 'html.parser')
page_html = my_client.read()
my_client.close()
page_soup = BeautifulSoup(page_html, 'html.parser')
containers = page_soup.findAll("div", {"class": "a-fixed-left-grid-col a-col-right"})
# container = containers[0]
for container in containers:
    book_title = container.div.div.a['title']
    book_author = container.div.findAll('span', {'class': 'a-size-small a-color-secondary'})[2].text
    book_price_container = container.findAll('span', {'class': 'a-size-base a-color-price s-price a-text-bold'})
    book_price = book_price_container[0].text.strip()
    print("book_title: {}".format(book_title))
    print("book_author: {}".format(book_author))
    print("book_price: {}\n".format(book_price))
    print('-' * 50)
