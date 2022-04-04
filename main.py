from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
PROMISED_DOWN = 500
PROMISED_UP = 50
#get twitter login
auth = []
with open("../api/twitter") as file:
    d = file.readlines()
    for dat in d:
        auth.append(str(dat.strip("\n")))

print(auth)

#get web speed data
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.speedtest.net/")

go_button_1 = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go_button_1.click()
time.sleep(60)
download = round(float(driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text))
upload = round(float(driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text))

print(download)
print(upload)

