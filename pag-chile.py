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
    browser.get('https://emotions.cl/')
    delay = 15 # seconds
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user"]/div[2]')))
    finally:
        login = browser.find_element_by_xpath('//*[@id="dLabel"]')
        login.click()
        time.sleep(5)
        user = browser.find_element_by_name("nombre")
        user.click()
        user.send_keys("Roberto Yamashita")
        region = Select(browser.find_element_by_id("region"))
        region.select_by_value("13")
        time.sleep(5)
        comuna = Select(browser.find_element_by_id("comuna"))
        comuna.select_by_value("13119")
        email = browser.find_element_by_id("register-email")
        email.send_keys("roberto.yamashita420@outlook.com")
        dia = Select(browser.find_element_by_name("nac_dia"))
        dia.select_by_value("20")
        mes = Select(browser.find_element_by_name("nac_mes"))
        mes.select_by_value("4")
        ano = Select(browser.find_element_by_name("nac_ano"))
        ano.select_by_value("1969")
        password = browser.find_element_by_id("register-password")
        password.send_keys("epicogamer69")
        password = browser.find_element_by_id("register-repeat-password")
        password.send_keys("epicogamer69")
        terms = browser.find_element_by_xpath('//*[@id="register-form"]/div[1]/div[5]/div/label/span')
        terms.click()
        confirm = browser.find_element_by_xpath('//*[@id="register-form"]/div[1]/div[7]/button')
        confirm.click()
    return

def login():
    browser.get('https://emotions.cl/')
    delay = 15 # seconds
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user"]/div[2]')))
    finally:
        login = browser.find_element_by_xpath('//*[@id="dLabel"]')
        login.click()
        time.sleep(5)
        email = browser.find_element_by_id("email")
        email.send_keys("roberto.yamashita420@outlook.com")
        password = browser.find_element_by_id("pass")
        password.send_keys("epicogamer69")
        confirm2 = browser.find_element_by_xpath('//*[@id="login-section"]/form/div/p[4]/button')
        confirm2.click()
    return

def recover():
    browser.get('https://emotions.cl/')
    delay = 15 # seconds
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user"]/div[2]')))
    finally:
        login = browser.find_element_by_xpath('//*[@id="dLabel"]')
        login.click()
        time.sleep(5)
        recovery = browser.find_element_by_xpath('//*[@id="login-section"]/form/div/p[2]/a')
        recovery.click()
        time.sleep(5)
        email = browser.find_element_by_id("email")
        email.send_keys("roberto.yamashita420@outlook.com")
        confirm3 = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[2]/form/p[2]/input')
        confirm3.click()
    return

def brute_force():
    browser.get('https://emotions.cl/')
    delay = 15 # seconds
    count = 0
    element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user"]/div[2]')))
    login = browser.find_element_by_xpath('//*[@id="dLabel"]')
    login.click()
    time.sleep(5)
    email = browser.find_element_by_id("email")
    email.send_keys("roberto.yamashita420@outlook.com")
    password = browser.find_element_by_id("pass")
    password.send_keys("epicogamer69")
    confirm2 = browser.find_element_by_xpath('//*[@id="login-section"]/form/div/p[4]/button')
    confirm2.click()
    new_login = browser.find_element_by_xpath('//*[@id="email"]')
    while new_login:
        if count == 100:
            break
        else:
            try:
                count = count + 1
            finally:
                time.sleep(5)
                email = browser.find_element_by_id("email")
                email.send_keys("roberto.yamashita420@outlook.com")
                password = browser.find_element_by_id("pass")
                password.send_keys("Epicogamer69")
                confirm2 = browser.find_element_by_xpath('//*[@id="login-section"]/form/div/p[4]/button')
                confirm2.click()
    print(count)
    return

#se puede ir descomentando la funcion que se quiera probar :)
#registro()
#login()
#recover()
brute_force()