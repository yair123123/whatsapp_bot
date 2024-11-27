import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.binary_location = r"C:\chrome-win64\chrome.exe"

service = Service(r"C:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://web.whatsapp.com")

input("סרוק את ה-QR Code ב-WhatsApp Web והקש Enter כדי להמשיך...")
group = driver.find_element("xpath", "//span[@title='Data Enosh Students']")
group.click()
messages = driver.find_elements("xpath", "//div[@class='copyable-text']")

for message in messages:
    print(message.text)

while True:
    messages = driver.find_elements("xpath", "//div[@class='copyable-text']")

    if messages:
        print(messages[-1].text)

    time.sleep(2)
