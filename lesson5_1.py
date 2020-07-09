from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions
import time

client = MongoClient('localhost', 27017)
db = client['yandex_mail']
collection = db['db']


chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome('./chromedriver.exe',options=chrome_options)


driver.get("https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1")
elem = driver.find_element_by_id("passp-field-login")
elem.send_keys('alina-gol@yandex.ru')
elem.send_keys(Keys.ENTER)
time.sleep(0.9)
elem1 = driver.find_element_by_id("passp-field-passwd")
elem1.send_keys('Oobp140308')
elem1.send_keys(Keys.ENTER)

first_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'ns-view-messages-item-wrap')
    )
)
first_message.click()
pages = 0
while True:
     try:
         button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'след.')))
         button.click()
         time.sleep(0.9)
         pages += 1
     except:
         print({pages})
         break