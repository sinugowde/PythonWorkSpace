from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

my_url = 'https://www.amazon.in/s/ref=nb_sb_ss_c_1_6?url=search-alias%3Daps&field-keywords='
book_to_search = "Python Programming"
url = 'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Python+Programming'

file_name = 'amazon_books.csv'
file_handle = open(file_name, 'w')
csv_header = 'Sl No, Book Title, Author, Price\n'
file_handle.write(csv_header)

# my_client = urlopen(my_url + book_to_search)
my_client = urlopen(url)
page_html = my_client.read()
my_client.close()

page_soup = BeautifulSoup(page_html, 'html.parser')
# containers = page_soup.findAll("li", {"class": "s-result-item celwidget"})
# containers = page_soup.findAll("li")
containers = page_soup.find_all('li', id=re.compile('^result_'))

for i, container in enumerate(containers):
    container_book = container.find_all('div', class_='a-fixed-left-grid-col a-col-right')
    if container_book:
        book_title = container.h2.text
        container_author = container_book[0].find_all('div', class_="a-row a-spacing-small")
        book_author = ''
        for item in container_author[0].find_all('span', class_="a-size-small a-color-secondary")[2:]:
            # print(item.text)
            book_author += item.text
        book_price = container_book[0].find_all('span', class_="a-size-base a-color-price s-price a-text-bold")[0].text\
            .strip()
        print("{}. book_title: {}, boot_author: {}, book_price: Rs.{}/-".format(i+1, book_title, book_author,
                                                                                book_price))
        file_handle.write(str(i + 1) + ',' + book_title.replace(',', '|') + ',' + book_author.replace(',', '')
                          + ',' + book_price.replace(',', '') + '\n')

