from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('15829074904')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('gaolin19950214')
    btm1 = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')

    btm1.click()

except Exception as identifier:
    print(identifier)
finally:
    pass