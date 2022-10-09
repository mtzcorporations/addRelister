# first import the module
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('chromedriver')
# then make a url variable
url = "https://www.bolha.com/prijava/"

# then call the default open method described above
driver.get(url)

loginName = driver.find_element("id", 'login_username')
loginName.send_keys("kozarec18")
loginPass = driver.find_element("id", 'login_password')
loginPass.send_keys("Majn1ce2")
driver.find_element("id", 'didomi-notice-agree-button').click()
driver.find_element("id", 'login_login').click()

url="https://www.bolha.com/moja-bolha/uporabnik/moji-oglasi/aktivni-oglasi"
driver.get(url)
x = driver.find_element(By.CLASS_NAME, "UserEntityList-itemList")
for a in x:
    print(a)

#elements=driver.find_elements(By.TAG_NAME, "li")

    #.get_attribute("href")
#driver.find_element("class", 'ClassifiedDetailDescription-textWrapper').click()

driver.close()
