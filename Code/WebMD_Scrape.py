import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # Web Browser = Chrome + Web Driver location = PATH

driver.get("https://www.webmd.com/a-to-z-guides/health-topics")

try:
    # click allergies
    link_al = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Allergies'))
    )
    link_al.send_keys(Keys.RETURN)

    # click treatment
    link_tr = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Treatment'))
    )
    link_tr.send_keys(Keys.RETURN)

    # find drug names and links
    list_links = driver.find_elements(By.XPATH, "//div[@class='article-page active-page']//section[2]//ul[1]//a[@href]")

    link = []
    name = []

    # loop over all AntiHistamine (ah) links and drug names found in the href attribute (within section[2]//ul[1])
    for i in list_links:
        ah_links = i.get_attribute('href')
        link.append(ah_links)

    for j in list_links:
        ah_name = j.get_attribute('innerHTML')
        name.append(ah_name)

finally:
    time.sleep(5)
    driver.quit()

file_name = 'antihistamine.csv'

with open(file_name, "w", encoding="utf-8") as f:
    f.write = csv.writer(f)
    f.write.writerow(['No.', 'Drug Name', 'Link'])  # headers of the Excel file

    # for loop cycles through the arrays and prints out on each row in the Excel file
    for i in range(len(name)):
        f.write.writerow([i+1, name[i], link[i]])

