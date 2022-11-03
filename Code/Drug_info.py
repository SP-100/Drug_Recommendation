import csv
import time
import pandas as pd
from selenium import webdriver
from lxml import html
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Appending links found in csv to a list


def get_links():
    links = []
    path = r'C:\Users\ShrawanPun\Drug Recommendation Project\Code\antihistamine.csv'
    with open(path) as ah_csv:
        links_df = csv.DictReader(ah_csv)
        for row in links_df:
            links.append(row['Link'])
    return links

# with open('Reviews.csv', 'w') as file:
#     file.write("Age; Gender; Condition; Rating; Review_long; Review_short \n")

PATH = "C:\Program Files (x86)\chromedriver.exe"
# Web Browser = Chrome + Web Driver location = PATH
driver = webdriver.Chrome(PATH)

for urls in get_links():
    driver.get(urls)
    time.sleep(1)

    # Click and open reviews
    review_click = driver.find_element(By.PARTIAL_LINK_TEXT, "Reviews")
    review_click.send_keys(Keys.RETURN)
    time.sleep(1)

    # age = driver.find_elements(By.XPATH, "//div[@class='card-header']/div/span[2]")
    # gender = driver.find_elements(By.XPATH, "//div[@class='card-header']/div/span[3]")
    # condition = driver.find_elements(By.XPATH, "//strong[@class='condition']")
    # rating = driver.find_elements(By.XPATH, "//div[@class='overall-rating']/strong")
    # review_show = driver.find_elements(By.XPATH, "//div[@class='description']/p[@class='description-text']/span[1]")
    # review_hidden = driver.find_elements(By.XPATH, "//div[@class='description']/p[@class='description-text']/span[2]")
    # review_long = review_show + review_hidden
    # review_short = driver.find_elements(By.XPATH, "//div[@class='description']/p[@class='description-text']")

    review_list = []
    tree = html.fromstring(driver.page_source)
    for product_tree in tree.xpath(
            "//div[@id='ContentPane28']//div[@class='shared-reviews-container']//div[@class='review-details-holder']"):
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
    df.to_csv('test_reviews.csv', index=False)
    next_page = driver.find_element(By.XPATH, "//div[@class='filter-section']/section[@class='pagination']/button[2]")
    next_page.send_keys(Keys.RETURN)
print('Finished!')
driver.close()

#     df = pd.DataFrame(review_list)
#     df.to_excel('reviews.xlsx', index=False)
#     # next_page = driver.find_element(By.XPATH, "//div[@class='filter-section']//section[@class='pagination']"
#     #                                           "//span[@class='webmd-icon-right-arrow']")
#     # driver.execute_script("arguments[0].click();", next_page)
# print('Finished')
# driver.close()
