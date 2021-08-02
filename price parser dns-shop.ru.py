import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SELECTOR1 = " div > div.product-buy__price.product-buy__price"
SELECTOR2 = " div > div.product-buy__price.product-buy__price_active"
link = "https://www.dns-shop.ru"


#считывание с таблицы
def product_name():
    pass

#поиск цены: 2 цены - старая и новая
def get_price_active():
    price1 = browser.find_element_by_css_selector(SELECTOR2).text
    print(price1)
    price2 = price1.replace(" ","")
    print(price2[0:5])

#поиск цены: 2 цены - старая и новая
def get_price():
    price1 = browser.find_element_by_css_selector(SELECTOR1).text
    print(price1)
    price2 = price1.replace(" ","")
    print(price2[0:5])

#добавление в таблицу
    def append():
        pass

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector("nav div div form div input.ui-input-search__input.ui-input-search__input_presearch")
input1.send_keys("NB144")
input1.send_keys(Keys.ENTER)

try:
    get_price_active()
except:
    get_price()
finally:
    time.sleep(3)
    browser.quit()


