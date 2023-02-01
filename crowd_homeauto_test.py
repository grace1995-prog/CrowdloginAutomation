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
        dashboard = driver.find_element(By.XPATH, "//a[@class='BaseButton Polaris-Button Primary']").click()
        time.sleep(2)
        project = driver.find_element(By.XPATH, "//input[@id='project-test-detail-name']").send_keys("Demo")
        time.sleep(2)
        description = driver.find_element(By.XPATH, "//input[@id='project-test-detail-description'] ").send_keys("This is a demo")
        time.sleep(2)
        RR = driver.find_element(By.CSS_SELECTOR,"span[class='relative rounded-full w-18 h-18 border inline-flex fill-before before:!w-10 before:!h-10 before:!inset-[auto] before:bg-action-primary-default items-center justify-center before:scale-0 before:transition-transform lg:transition-all bg-surface-default group-focus-within:border-action-primary-pressed group-focus-within:border-2 border-interactive-default !border-2 before:scale-100 group-active:before:scale-[0.95] before:delay-75']").click()
        time.sleep(3)
        driver.execute_script("window.scrollBy,(0,50);")
        pro = driver.find_element(By.XPATH,"//input[@id='project-welcome-screen-title']").send_keys("You've been invitend to participate in a test")
        time.sleep(2)
        desp= driver.find_element(By.XPATH,"//textarea[@id='project-welcome-screen-message']").send_keys("Click on button")
        time.sleep(2)
        scrg =driver.find_element(By.XPATH,"//input[@id='project-welcome-screen-button-text']").send_keys("Get started")
        time.sleep(2)
        Thanky= driver.find_element(By.XPATH,"//input[@id='project-thank-you-screen-title']").send_keys("Welcome")
        time.sleep(2)
        screen=driver.find_element(By.XPATH,"//textarea[@id='project-thank-you-screen-message']").send_keys("Thanks forcoming")
        time.sleep(2)
        boa =driver.find_element(By.CSS_SELECTOR,"div[class='grid'] ").click()
        contd =driver.find_element(By.XPATH,"//body/div[@id='__nuxt']/div[@id='__layout']/div/div[@role='document']/main/div/div/div/div/div/aside/div/div/button[@type='button']/span[1]").is_selected()
        if contd is None:
            print("yes")
        else:
            print("No")
        time.sleep(3)
Demob=Login()
Demob.test()
