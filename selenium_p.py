# from seleniumbase import Driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
class Selenium_Process:
    def __init__(self, url):
        baseurl=url
        #service = Service("chrome_driver/chromedriver.exe")
        #self.driver = webdriver.Chrome(service=service)
        ch_options = webdriver.ChromeOptions()
        ch_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(ch_options)
        self.driver.get(baseurl)

    def get_href_list(self):
        href_list=list()
        while (True):
            try:
                self.driver.execute_script("arguments[0].scrollIntoView()",
                self.driver.find_element(By.CLASS_NAME, 'contentosResult'))
                sleep(2)
                self.driver.execute_script("window.scrollBy(0, -200)", "")
                sleep(2)
                self.driver.find_element(By.CLASS_NAME, 'contentosResult').click()
                sleep(2)
            except ElementNotInteractableException:
                break
        laptop_conteyner = self.driver.find_element(By.CLASS_NAME, "contentos")
        laptop_list = laptop_conteyner.find_elements(By.CLASS_NAME, "prodItem")
        for item in laptop_list:
            a=item.find_element(By.CLASS_NAME, "prodItem__img ")
            href_list.append(a.get_attribute("href"))
        return href_list
