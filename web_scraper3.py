from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

amazon_home_page = 'https://www.amazon.in'
my_url = 'https://www.amazon.in/s/ref=nb_sb_ss_c_1_6?url=search-alias%3Daps&field-keywords='
book_to_search = "Python Programming"
page_2 = '/Python-Programming/s?ie=UTF8&amp;page=2&amp;rh=i%3Aaps%2Ck%3APython%20Programming'
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
search_pages = int(page_soup.find('span', class_="pagnDisabled").text)
containers = page_soup.find_all('li', id=re.compile('^result_'))
search_results = 0

for page_num in range(1, search_pages + 1):
    if page_num != 1:
        if not search_string:
            print(*"\nQuitting.. there are no more Pages left.\n")
        url = amazon_home_page + search_string
        my_client = urlopen(url)
        page_html = my_client.read()
        my_client.close()
        page_soup = BeautifulSoup(page_html, 'html.parser')
        containers = page_soup.find_all('li', id=re.compile('^result_'))

    for i, container in enumerate(containers):
        search_results += 1
        container_book = container.find_all('div', class_='a-fixed-left-grid-col a-col-right')
        if container_book:
            if container.h2.text:
                book_title = container.h2.text
            else:
                book_title = 'NA'

            container_author = container_book[0].find_all('div', class_="a-row a-spacing-small")
            book_author = ''
            for item in container_author[0].find_all('span', class_="a-size-small a-color-secondary")[2:]:
                if 'by' not in item.text:
                    book_author += item.text
            if not book_author:
                book_author = 'NA'

            # book_price = container_book[0].find_all('span', class_="a-size-base a-color-price s-price a-text-bold")[0]\
            #     .text.strip()

            book_price = 'NA'
            container_price = container_book[0].find_all('span', class_="a-size-base a-color-price s-price a-text-bold")
            if container_price:
                book_price = container_price[0].text.strip()

            print("{}. book_title: {}, book_author: {}, book_price: Rs.{}/-".format(search_results, book_title,
                                                                                    book_author, book_price))

            file_handle.write(str(search_results) + ',' + book_title.replace(',', '|') + ',' +
                              book_author.replace(',', '') + ',' + book_price.replace(',', '') + '\n')

    container_search_string = page_soup.find('a', class_="pagnNext")
    if container_search_string:
        search_string = container_search_string.get('href')
        print("\n{} - search_pages: {}".format(page_num, search_string))
    else:
        search_string = ''
        print(*"\nQuitting.. there are no more Pages left.\n")


file_handle.close()
