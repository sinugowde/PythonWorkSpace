import bs4
import requests


def get_amazon_price(url):
    result = requests.get(url)
    result.raise_for_status()

    soup = bs4.BeautifulSoup(result.text, features="html5lib")
    # elements = soup.select('#soldByThirdParty > span.a-size-medium.a-color-price.inlineBlock-display.offer-price.'
    #                        'a-text-normal.price3P')
    elements = soup.select('#result_0 > div > div > div > div.a-fixed-left-grid-col.a-col-right > div:nth-child(4) > div.a-column.a-span7 > div:nth-child(1) > a:nth-child(1) > span.a-size-base.a-color-price.s-price.a-text-bold')
    
    return elements[0].text.strip()


price = get_amazon_price('https://www.amazon.in/Automate-Boring-Python-Albert-Sweigart/dp/1593275994/ref=sr_1_1?'
                         'ie=UTF8&qid=1538698216&sr=8-1&keywords=automate+the+boring+stuff+with+python')
print("the Price of the Book is: {}".format(price))
