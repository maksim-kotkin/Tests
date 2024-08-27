import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
     
login = ''
password = ''


chrome_path = ChromeDriverManager().install()
options = ChromeOptions()
browser_service = Service(executable_path=chrome_path)
browser = Chrome(service=browser_service, options=options)


def auth_yandex(login, password):
    browser.get("https://passport.yandex.ru/auth")
    email = browser.find_element(by='id', value='passp-field-login')
    time.sleep(3)
    email.clear()
    email.send_keys(login)
    time.sleep(3)
    email.send_keys(Keys.ENTER)
    time.sleep(3)
    passwd = browser.find_element(by='id', value='passp-field-passwd')
    passwd.clear()
    passwd.send_keys(password)
    time.sleep(3)
    passwd.send_keys(Keys.ENTER)
    time.sleep(5)
    result = browser.current_url
    return result 



auth_yandex(login, password)
# import time
# https://passport.yandex.ru/auth/challenge?retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fprepare%3Fuuid%3D2d41f6a1-311c-4fe2-b970-8b9dcffb57ab%26goal%3Dhttps%253A%252F%252Fya.ru%252F%26finish%3Dhttps%253A%252F%252Fpassport.yandex.ru%252Fprofile&track_id=2179e0289f2e96694a09f65ec5800a8897
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys

# login = 'kotkin.macsim@yandex.ru'
# password = 'stRpxGET'

# chrome_driver_path = ChromeDriverManager().install()
# browser_service = Service(executable_path=chrome_driver_path)
# browser = webdriver.Chrome(service=browser_service)

# def auth_yandex(login, passw):
#     browser.get('https://passport.yandex.ru/auth/list')
#     time.sleep(3)

#     email_input = browser.find_element(by='id', value='passp-field-login')
#     email_input.clear()
#     email_input.send_keys(login)
#     time.sleep(1)
#     email_input.send_keys(Keys.ENTER)
#     time.sleep(3)


#     passw_input = browser.find_element(by='id', value='passp-field-passwd')
#     passw_input.send_keys(passw)
#     time.sleep(1)
#     passw_input.send_keys(Keys.ENTER)
#     time.sleep(5)

#     return browser.find_element(by='class', value='Card_label__AG2MY')

#     browser.close()
#     browser.quit()
    
# auth_yandex(login, password)