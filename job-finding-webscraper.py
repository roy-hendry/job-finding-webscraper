from typing import final
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#The console throws a lot of stuff at us so this will give it time to throw us the stuff
#Then we clear it so that the user can see their options
time.sleep(3)
clear = lambda: os.system("cls")
clear()

#searchTerm = input("What job would you like to search for?")
searchTerm = "graduate software developer"
#searchTerm = "test"

driver.get("https://uk.indeed.com/?from=gnav-jobsearch--jasx")
#driver.get("https://techwithtim.net")

search = driver.find_element_by_id("text-input-what")
#search = driver.find_element_by_id("s")
search.send_keys(searchTerm)
search.send_keys(Keys.RETURN)


try:
    jobCards = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mosaic-provider-jobcards"))
    )
    titles = jobCards.find_elements_by_tag_name("span")
    for title in titles:
        #header = title.find_element_by_xpath("//div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/span").get_attribute("title")
        header = title.get_attribute("title")
        if not len(header.strip()) == 0:
            print(header)

finally:
    driver.quit()

"""
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-header").find_element_by_class_name("entry-meta").find_element_by_class_name("posted-on")
        print(header.text)

finally:
    driver.quit()
"""