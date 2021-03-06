from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

amazon_home_page = 'https://www.amazon.in'
amazon_book_search = 'https://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Dstripbooks&field-keywords='
amazon_general_search = 'https://www.amazon.in/s/ref=nb_sb_ss_c_1_6?url=search-alias%3Daps&field-keywords='
book_to_search = "Python Programming"
# page_2 = '/Python-Programming/s?ie=UTF8&amp;page=2&amp;rh=i%3Aaps%2Ck%3APython%20Programming'
# url = 'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=Python+Programming'

file_name = 'amazon_books.csv'
file_handle = open(file_name, 'w')
csv_header = 'Sl No, Book Title, Author, Price, Rating, No of Ratings\n'
file_handle.write(csv_header)

my_client = urlopen(amazon_book_search + book_to_search.replace(' ', '+'))
# my_client = urlopen(url)
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

            # Finding Book Title
            if container.h2.text:
                book_title = container.h2.text
                book_title = (book_title.encode('ascii', 'ignore')).decode("utf-8")
            else:
                book_title = 'NA'

            # Finding Book Author
            container_author = container_book[0].find_all('div', class_="a-row a-spacing-small")
            book_author = ''
            for item in container_author[0].find_all('span', class_="a-size-small a-color-secondary")[2:]:
                if 'by' not in item.text:
                    book_author += item.text
            if not book_author:
                book_author = 'NA'

            # Finding Book Price
            book_price = 'NA'
            container_price = container_book[0].find_all('span', class_="a-size-base a-color-price s-price a-text-bold")
            if len(container_price) >= 1:
                book_price = (container_price[0].text.strip()).replace(',', '')
                if (len(container_price) >= 2) and (float(book_price) == 0):
                    book_price = (container_price[1].text.strip()).replace(',', '')

            # Finding Book Rating & the number of given Ratings in the Amazon site
            book_rate = 'Not Rated'
            book_rating_num = 'Not Rated'
            container_rating = container.find('span', class_="a-declarative")

            if container_rating:
                rating_text = container_rating.text

                if rating_text:
                    rating_text = re.findall('(\d\.?\d*) out of 5 stars', rating_text)
                    if rating_text:
                        book_rate = rating_text[0]

                        container_book_rating_num = container.find_all('div', class_="a-column a-span5 a-span-last")
                        if container_book_rating_num:
                            container_book_rating_num = \
                                container_book_rating_num[0].find_all('a',
                                                                      class_="a-size-small a-link-normal a-text-normal")

                            if container_book_rating_num:
                                book_rating_num = container_book_rating_num[0].text

            # Printing the data to the python console
            print("{}. book_title: {}, book_author: {}, book_price: Rs.{}/-, book_rating: {}, book_rating_num: {}"
                  .format(search_results, book_title, book_author, book_price, book_rate, book_rating_num))

            # Printing the data to the amazon_books.csv file
            file_handle.write(str(search_results) + ',' + book_title.replace(',', '|') + ',' +
                              book_author.replace(',', '') + ',' + book_price.replace(',', '') + ',' + book_rate + ','
                              + book_rating_num + '\n')

    # Searching for "Next Page" link in the search results
    container_search_string = page_soup.find('a', class_="pagnNext")
    if container_search_string:
        search_string = container_search_string.get('href')
        print("\n{} - search_pages: {}".format(page_num, search_string))
    else:
        search_string = ''
        print(*"\nQuitting.. there are no more Pages left.\n")


file_handle.close()
