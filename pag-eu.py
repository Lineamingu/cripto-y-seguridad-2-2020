from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome('C:/Users/Lineamingo/Downloads/selenium_chromedriver/chromedriver')
browser.maximize_window()

def registro():
    browser.get('https://www.hofmann.es/')
    delay = 15 # seconds
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="siteHeader"]/div/div[3]/div/div/div/ul/li[2]/a')))
    finally:
        login = browser.find_element_by_xpath('//*[@id="siteHeader"]/div/div[3]/div/div/div/ul/li[2]/a')
        login.click()
        time.sleep(5)
        register = browser.find_element_by_xpath('//*[@id="pbx_loginform"]/div[3]/a')
        register.click()
        time.sleep(5)
        user = browser.find_element_by_id("pbx_customer_first_name")
        user.click()
        user.send_keys("Roberto Yamashita")
        email = browser.find_element_by_id("pbx_customer_email")
        email.send_keys("roberto.yamashita420@outlook.com")
        password = browser.find_element_by_id("pbx_customer_password")
        password.send_keys("epicogamer69")
        terms = browser.find_element_by_id('pbx_confirm_terms')
        terms.click()
        newsletter = browser.find_element_by_id('customer_news_no')
        newsletter.click()
        confirm = browser.find_element_by_xpath('//*[@id="submitSection"]/span/input')
        confirm.click()
    return

def login():
    browser.get('https://www.hofmann.es/')
    delay = 15 # seconds
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="siteHeader"]/div/div[3]/div/div/div/ul/li[2]/a')))
    finally:
        login = browser.find_element_by_xpath('//*[@id="siteHeader"]/div/div[3]/div/div/div/ul/li[2]/a')
        login.click()
        time.sleep(5)
        email = browser.find_element_by_id("pbx_login_email")
        email.send_keys("roberto.yamashita420@outlook.com")
        password = browser.find_element_by_id("pbx_login_password")
        password.send_keys("epicogamer69")
        confirm2 = browser.find_element_by_xpath('//*[@id="pbx_submit_login"]')
        confirm2.click()
    return

def recover():
    browser.get('https://www.hofmann.es/')
    delay = 15 # seconds
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="siteHeader"]/div/div[3]/div/div/div/ul/li[2]/a')))
    finally:
        login = browser.find_element_by_xpath('//*[@id="siteHeader"]/div/div[3]/div/div/div/ul/li[2]/a')
        login.click()
        time.sleep(5)
        recover = browser.find_element_by_xpath('//*[@id="pbx_loginform"]/div[2]/a')
        recover.click()
        time.sleep(5)
        email = browser.find_element_by_id("uc_passwordforgotten_email")
        email.send_keys("roberto.yamashita420@outlook.com")
        confirm3 = browser.find_element_by_xpath('//*[@id="pbx_submit_resetpassword"]')
        confirm3.click()
    return

def brute_force():
    browser.get('https://www.hofmann.es/')
    delay = 15 # seconds
    count = 0
    element0 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="siteHeader"]/div/div[3]/div/div/div/ul/li[2]/a')))
    login = browser.find_element_by_xpath('//*[@id="siteHeader"]/div/div[3]/div/div/div/ul/li[2]/a')
    login.click()
    time.sleep(3)
    email = browser.find_element_by_id("pbx_login_email")
    email.send_keys("roberto.yamashita420@outlook.com")
    password = browser.find_element_by_id("pbx_login_password")
    password.send_keys("epicogamer69")
    confirm2 = browser.find_element_by_xpath('//*[@id="pbx_submit_login"]')
    confirm2.click()
    time.sleep(3)
    new_login = browser.find_element_by_xpath('//*[@id="pbx_login_email"]')
    while new_login:
        if count == 100:
            break
        else: 
            try:
                count = count + 1
            finally:
                time.sleep(5)
                email = browser.find_element_by_id("pbx_login_email")
                email.send_keys("roberto.yamashita420@outlook.com")
                password = browser.find_element_by_id("pbx_login_password")
                password.send_keys("epicogamer69")
                confirm2 = browser.find_element_by_xpath('//*[@id="pbx_submit_login"]')
                confirm2.click()
    print(count)
    return

#se puede ir descomentando la funcion que se quiera probar :)
#registro()
#login()
#recover()
#brute_force()