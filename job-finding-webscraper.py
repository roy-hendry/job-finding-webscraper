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

searchTerm = input("What job would you like to search for?")

driver.get("https://uk.indeed.com/?from=gnav-jobsearch--jasx")

search = driver.find_element_by_id("text-input-what")
search.send_keys(searchTerm)
search.send_keys(Keys.RETURN)

"""""
try:
    main = WebDriver(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
except:
    driver.quit()
"""