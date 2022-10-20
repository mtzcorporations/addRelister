# first import the module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def formattTExt(Kat,Naslov, Cena, OpisOglasa, stanje,lokacija1,lokacija2,lokacija3): #formatiranje texta za shranjevanje
    formatted=Kat+ "--END--\n" + Naslov + "\n--END--\n"  + Cena + "\n--END--\n" + OpisOglasa
    formatted+= "\n--END--\n" + stanje + "\n--END--\n" + lokacija1 +"\n" + lokacija2 +"\n" + lokacija3
    with open('oglas.txt', 'w', encoding="utf-8") as f:
        f.write(formatted)


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
x = driver.find_elements(By.CLASS_NAME, "UserEntityActions-action.TooltipWrap")
links=[]
for a in x:
    #a.click()
    links.append(a.get_attribute("href"))
driver.get(str(links[3]))

Naslov = driver.find_element("id", 'ad-title')
Naslov  = Naslov.get_property("value")
Vsebina = driver.find_element("id", 'ad-description').text
Stanje = driver.find_element("id", 'ad-condition_id')
Stanje  = Stanje.get_property("value")
Cena = driver.find_element("id", 'ad-price-amount')
Cena= Cena.get_property("value")
print(Cena + " " + Naslov)

Lokacija_1 = driver.find_element("id", "adLocalitySelector-location_id_level_0")
Lokacija_1= Lokacija_1.get_property("value")
Lokacija_2 = driver.find_element("id", "adLocalitySelector-location_id_level_1")
Lokacija_2= Lokacija_2.get_property("value")
Lokacija_3 = driver.find_element("id", "adLocalitySelector-location_id_level_2")
Lokacija_3= Lokacija_3.get_property("value")

formattTExt("nic",Naslov,Cena,Vsebina,Stanje,Lokacija_1,Lokacija_2,Lokacija_3)

kategorija = driver.find_element(By.CLASS_NAME, "edit-category").text
kategorija=kategorija.split("\n")
dolKat=len(kategorija)
#Branje podatkov KONEC


#Kreiranje novega oglasa ---
driver.get("https://www.bolha.com/objava-oglasa/")
first=driver.find_element(By.CLASS_NAME,"SubmitCategorySelector-items.is-firstLevel")
elements=first.find_elements(By.TAG_NAME,"li")
for el in elements:
    if el.text == kategorija[0]:
        el.click()
if dolKat > 1:
    second=driver.find_element(By.CLASS_NAME,"SubmitCategorySelector-items.is-remainingLevel")
    elements=second.find_elements(By.TAG_NAME,"li")
    for el in elements:
        if el.text == kategorija[1]:
            el.click()
    if dolKat >2:
        third = driver.find_elements(By.CLASS_NAME, "SubmitCategorySelector-items.is-remainingLevel")
        elements = third[1].find_elements(By.TAG_NAME, "li")
        for el in elements:
            if el.text == kategorija[2]:
                el.click()
        if dolKat >3:
            last = driver.find_elements(By.CLASS_NAME, "SubmitCategorySelector-items.is-remainingLevel")
            elements = last[2].find_elements(By.TAG_NAME, "li")
            for el in elements:
                if el.text == kategorija[3]:
                    el.click()
driver.find_element(By.CLASS_NAME,"form-action.form-action--submit.button-standard.button-standard--alpha.SubmitCategorySelector-submit").click()

#driver.find_element("id", "submitCategorySelectorLevelCategory3").click()
#Select(driver.find_element(By.XPATH, "//*[contains(text(), 'Računalništvo')]"))
#razred.click()
#driver.find_elements_by_xpath()
#driver.close()
