from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
PROMISED_DOWN = 500
PROMISED_UP = 50
#get twitter login
auth = []
with open("../api/twitter") as file:
    d = file.readlines()
    for dat in d:
        auth.append(str(dat.strip("\n")))



#get web speed data
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.speedtest.net/")

go_button_1 = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go_button_1.click()
time.sleep(60)
download = round(float(driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text))
upload = round(float(driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text))

if download < PROMISED_DOWN or upload < PROMISED_UP:
    #post tweet
    twit = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    twit.get("https://twitter.com/")
    time.sleep(10)
    login_button = twit.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
    login_button.click()
    time.sleep(5)
    username = twit.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
    username.send_keys(auth[0])
    next1 = twit.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')
    next1.click()
    time.sleep(5)
    pw = twit.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    pw.send_keys(auth[1])
    time.sleep(2)
    pw.send_keys(Keys.ENTER)

    time.sleep(10)
    write = twit.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    write.send_keys(f"@tele2sweden My internet speed is {download} mb down and {upload}. I'm paying for 500 down and 50 up. Is this right?")

    time.sleep(1)
    post = twit.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
    post.click()

else:
    print("Passed test")





