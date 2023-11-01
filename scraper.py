from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome()

browser.implicitly_wait(1)

browser.get('https://www.instagram.com/')

sleep(1)

username_field = browser.find_element(By.NAME, 'username')
password_field = browser.find_element(By.NAME, 'password')
username_field.send_keys('yourUsername')
password_field.send_keys('yourPassword')

# Corrected the line below
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
browser.execute_script("arguments[0].click();", login_button)

sleep(5)

#navigate to the page
browser.get('https://www.instagram.com/username/reels/')

#scroll thru the pages to get urls
reel_urls = []
last_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)  # Allow time for page to load new content
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # No more content loaded
        break
    last_height = new_height

        # Locate Reels elements and extract URLs
    reels = browser.find_elements(By.CSS_SELECTOR, "a[href*='/reel/']")
    for reel in reels:
        url = reel.get_attribute('href')
        if url not in reel_urls:
            reel_urls.append(url)


#store the urls in a txt file
with open('reel_urls.txt', 'w') as file:
    for url in reel_urls:
        file.write(f'{url}\n')

sleep(9999999)

browser.close()
