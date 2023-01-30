import time

from selenium import webdriver
from selenium.webdriver.common.by import By
class Login():
    def test(self):
        driver = webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
        baseurl = "https://crowdapp.io/auth/login"
        driver.get(baseurl)
        driver.implicitly_wait(10)
        driver.maximize_window()
        elementbyId = driver.find_element(By.ID,"email").send_keys("mfonmamondayuko@gmail.com")
        time.sleep(2)
        elementbyId = driver.find_element(By.ID,"password").send_keys("Inem4040$1")
        time.sleep(2)
        elementbypath  = driver.find_element(By.XPATH," //button[@type='submit']").click()
        time.sleep(2)
        if elementbypath is None:
            print("sucessful")
        else:
            print("please signup")
Demob=Login()
Demob.test()
