import csv
import pandas as pd
from lxml import html
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def cetrizine_scrape():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)  # Web Browser = Chrome + Web Driver location = PATH

    review_list = []

    for page in range(1, 6):
        url = f"https://www.webmd.com/drugs/drugreview-12065-" \
              f"cetirizine-oral?conditionid=&sortval=1&page={page}&next_page=true"
        driver.get(url)
        print(f"Getting page: {page}")

        tree = html.fromstring(driver.page_source)

        for product_tree in tree.xpath(
                "//div[@id='ContentPane28']//div[@class='shared-reviews-container']"
                "//div[@class='review-details-holder']"):
            age = product_tree.xpath(".//div[@class='details']/span[2]/text()")
            gender = product_tree.xpath(".//div[@class='details']/span[3]/text()")
            condition = product_tree.xpath(".//strong[@class='condition']/text()")
            rating = product_tree.xpath(".//div[@class='overall-rating']/strong/text()")
            review_show = product_tree.xpath(".//span[@class='showSec']/text()")
            review_hidden = product_tree.xpath(".//span[@class='hiddenSec']/text()")
            review_long = review_show + review_hidden
            review_short = product_tree.xpath(".//p[@class='description-text']/text()")

            review_dict = {'age': age,
                           'gender': gender,
                           'condition': condition,
                           'rating': rating,
                           'review_long': review_long,
                           'review_short': review_short
                           }
            review_list.append(review_dict)
        df = pd.DataFrame(review_list)
        df.to_csv('cetrizine_reviews.csv', index=False)
    print('Finished')
    driver.close()


cetrizine_scrape()


def zyrtec_scrape():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)  # Web Browser = Chrome + Web Driver location = PATH

    review_list = []

    for page in range(1, 20):
        url = f"https://www.webmd.com/drugs/drugreview-12127-zyrtec-oral?" \
              f"conditionid=&sortval=1&page={page}&next_page=true"
        driver.get(url)
        print(f"Getting page: {page}")

        tree = html.fromstring(driver.page_source)

        for product_tree in tree.xpath(
                "//div[@id='ContentPane28']//div[@class='shared-reviews-container']"
                "//div[@class='review-details-holder']"):
            age = product_tree.xpath(".//div[@class='details']/span[2]/text()")
            gender = product_tree.xpath(".//div[@class='details']/span[3]/text()")
            condition = product_tree.xpath(".//strong[@class='condition']/text()")
            rating = product_tree.xpath(".//div[@class='overall-rating']/strong/text()")
            review_show = product_tree.xpath(".//span[@class='showSec']/text()")
            review_hidden = product_tree.xpath(".//span[@class='hiddenSec']/text()")
            review_long = review_show + review_hidden
            review_short = product_tree.xpath(".//p[@class='description-text']/text()")

            review_dict = {'age': age,
                           'gender': gender,
                           'condition': condition,
                           'rating': rating,
                           'review_long': review_long,
                           'review_short': review_short
                           }
            review_list.append(review_dict)
        df = pd.DataFrame(review_list)
        df.to_csv('zyrtec_reviews.csv', index=False)
    print('Finished')
    driver.close()


zyrtec_scrape()

