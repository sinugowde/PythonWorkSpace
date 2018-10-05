import webbrowser
import pyperclip
import sys
import bs4
import requests

# if sys.argv.__len__() > 1:
#     address = ' '.join(sys.argv[1:])
# else:
#     address = pyperclip.paste()


def get_book_list_from_amazon(url):
    result = requests.get(url)
    result.raise_for_status()

    soup = bs4.BeautifulSoup(result.text, features="html5lib")
    amazon_book_list = soup.select('#result_0 > div > div > div > div.a-fixed-left-grid-col.a-col-right > '
                           'div.a-row.a-spacing-small')
    # amazon_book_price_list = soup.select('#result_0 > div > div > div > div.a-fixed-left-grid-col.a-col-right > '
    #                                      'div:nth-child(4) > div.a-column.a-span7 > div:nth-child(1) > a:nth-child(1)')
    amazon_book_price_list = soup.select('#result_0 > div > div > div > div.a-fixed-left-grid-col.a-col-right > div:nth-child(4) > div.a-column.a-span7 > div:nth-child(1) > a:nth-child(1) > span.a-size-base.a-color-price.s-price.a-text-bold')
    return amazon_book_price_list


amazon_search_string = 'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='
address = 'Python Machine Learning By Example'
# webbrowser.open(amazon_search_string + address)


web_list = get_book_list_from_amazon(amazon_search_string + address)
print(type(web_list))

for book in web_list:
    print(book)
