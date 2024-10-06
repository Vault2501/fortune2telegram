from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import json
import os
import time
import datetime
import random
from subprocess import run
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chat = 'https://web.telegram.org/k/<room_id>'# URI from Telegram WebUI
min_seconds = 3600 # minimum time in between posts
max_seconds = 14400 # maximum time in between posts
auth_seconds = 60 # When not logged in, give user 60 sec to log in
message_field = '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]' # XPATH to input field

chrome_options = Options()
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--user-data-dir=' + os.path.join(os.getcwd(), 'User_Data'))
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd()}
chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument('--headless')  # Uncomment for headless mode
webdriver_path = ChromeDriverManager().install()

expect_binary_name = 'chromedriver'
if os.name == 'nt':
    expect_binary_name += '.exe'
actual_binary_name = os.path.basename(webdriver_path)
if actual_binary_name != expect_binary_name:
    webdriver_dir_path = os.path.dirname(webdriver_path)
    webdriver_path = os.path.join(webdriver_dir_path, expect_binary_name)

chrome_service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.maximize_window()
driver.get(chat)
actions = ActionChains(driver)

while True:
    if driver.current_url == 'https://web.telegram.org/a/':
        time.sleep(60) # If not authenticated, wait for 60 sec for user to authenticate
        try:
            driver.get(chat)
        except Exception as e:
            print(f"Auth..")
        time.sleep(2)

    time.sleep(2)
    result = run( [ './fortunate' ], capture_output=True )
    stdout = result.stdout.decode()
    print(stdout)

    driver.find_element(By.XPATH, message_field).send_keys(stdout);
    driver.find_element(By.XPATH, message_field).send_keys(Keys.RETURN);
    stdout = "zzzzZZZZZ"

    time.sleep(random.randint(min_seconds,max_seconds))
