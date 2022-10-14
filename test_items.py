import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_the_button(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    #time.sleep(30) #убрать коммент перед time для проверки установки языка
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "Button is missing"
    
if __name__ == "__main__":
    test_find_the_button()
    print("Everything passed")