# first import the module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time
from fileUploader import fileUploader
names=["kozarec18","jan2012"]

st=4

name=names[0]
def formattTExt(Kat,Naslov, Cena, OpisOglasa, stanje,lokacija1,lokacija2,lokacija3): #formatiranje texta za shranjevanje
    formatted=Kat+ "--END--\n" + Naslov + "\n--END--\n"  + Cena + "\n--END--\n" + OpisOglasa
    formatted+= "\n--END--\n" + stanje + "\n--END--\n" + lokacija1 +"\n" + lokacija2 +"\n" + lokacija3
    with open('oglas.txt', 'w', encoding="utf-8") as f:
        f.write(formatted)
def preberiPrikljucke(driver):
    DVI = driver.find_element("id", 'ad-connectorType_DVI').get_property("checked")
    DP = driver.find_element("id", 'ad-connectorType_DisplayPort').get_property("checked")
    HDMI = driver.find_element("id", 'ad-connectorType_HDMI').get_property("checked")
    SCART = driver.find_element("id", 'ad-connectorType_SCART').get_property("checked")
    USB = driver.find_element("id", 'ad-connectorType_USB').get_property("checked")
    THU = driver.find_element("id", 'ad-connectorType_Thunderbolt').get_property("checked")
    VGA = driver.find_element("id", 'ad-connectorType_VGA (D-sub)').get_property("checked")

    return DVI,DP,HDMI,SCART,USB,THU,VGA
def izberiPrikljucke(driver,DVI, DP, HDMI, SCART, USB, THU, VGA):
    if DVI:
        driver.find_element("id", 'ad-connectorType_DVI').click()
    if DP:
        driver.find_element("id", 'ad-connectorType_DisplayPort').click()
    if HDMI:
        driver.find_element("id", 'ad-connectorType_HDMI').click()
    if SCART:
        driver.find_element("id", 'ad-connectorType_SCART').click()
    if USB:
        driver.find_element("id", 'ad-connectorType_USB').click()
    if THU:
        driver.find_element("id", 'ad-connectorType_Thunderbolt').click()
    if VGA:
        driver.find_element("id", 'ad-connectorType_VGA (D-sub)').click()

driver = webdriver.Chrome('chromedriver')
# then make a url variable
url = "https://www.bolha.com/prijava/"

# then call the default open method described above
driver.get(url)
time.sleep(2)
driver.find_element("id", 'didomi-notice-agree-button').click()

loginName = driver.find_element("id", 'login_username')
loginName.send_keys(name)
loginPass = driver.find_element("id", 'login_password')
loginPass.send_keys("Majn1ce2")

driver.find_element("id", 'login_login').click()

url="https://www.bolha.com/moja-bolha/uporabnik/moji-oglasi/aktivni-oglasi"
driver.get(url)
x = driver.find_elements(By.CLASS_NAME, "UserEntityActions-action.TooltipWrap")
links=[]
for i,a in enumerate(x):
    #a.click()
    if(i%3==0):
        links.append(a.get_attribute("href"))
for i in range(st,len(links)):
    driver.get(str(links[i]))

    Naslov = driver.find_element("id", 'ad-title')
    Naslov  = Naslov.get_property("value")
    Vsebina = driver.find_element("id", 'ad-description').text
    Stanje = driver.find_element("id", 'ad-condition_id')
    Stanje  = Stanje.get_property("value")
    Cena = driver.find_element("id", 'ad-price-amount')
    Cena= Cena.get_property("value")
    #print(Cena + " " + Naslov)

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

    if dolKat>2 and kategorija[1]=="Monitorji":
        diagonala=driver.find_element("id", "ad-screenSize")
        diagonala = diagonala.get_property("value")
        proizvajalec = driver.find_element("id", "ad-manufacturer")
        proizvajalec = proizvajalec.get_property("value")
        resolucija = driver.find_element("id", "ad-screenResolution")
        resolucija = resolucija.get_property("value")
        vrstaZas = driver.find_element("id", "ad-screenPanel")
        vrstaZas = vrstaZas.get_property("value")
        formatZas = driver.find_element("id", "ad-screenFormat")
        formatZas = formatZas.get_property("value")
        DVI, DP, HDMI, SCART, USB, THU, VGA = preberiPrikljucke(driver)


    # slike=driver.find_element(By.CLASS_NAME, "Uploader-fileList")
    # slike=slike.find_elements(By.TAG_NAME,"src")
    # for s in slike:
    #     print()

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
    #izpolnjevanje forme oglasa
    driver.find_element("id", 'ad-title').send_keys(Naslov)
    driver.find_element("id", 'ad-description').send_keys(Vsebina)
    select = Select(driver.find_element("id", 'ad-condition_id'))
    select.select_by_value(Stanje)
    driver.find_element("id", 'ad-price-amount').clear()
    driver.find_element("id", 'ad-price-amount').send_keys(Cena)

    element=driver.find_element("id", 'adLocalitySelector-location_id_level_0')
    element.click()
    select = Select(element)
    select.select_by_value(Lokacija_1)
    element=driver.find_element("id", 'adLocalitySelector-location_id_level_1')
    element.click()
    time.sleep(1)
    select = Select(element)
    select.select_by_value(Lokacija_2)
    element=driver.find_element("id", 'adLocalitySelector-location_id_level_2')
    element.click()
    time.sleep(1)
    select = Select(element)
    select.select_by_value(Lokacija_3)
    element=driver.find_element("id","ad-onlinePaymentSelector-isOnlinePaymentEnabled_1")
    element.click()

    if dolKat > 2 and kategorija[1] == "Monitorji":
        driver.find_element("id", "ad-screenSize").send_keys(diagonala)
        driver.find_element("id", "ad-manufacturer").send_keys(proizvajalec)
        driver.find_element("id", "ad-screenResolution").send_keys(resolucija)
        driver.find_element("id", "ad-screenPanel").send_keys(vrstaZas)
        driver.find_element("id", "ad-screenFormat").send_keys(formatZas)
        izberiPrikljucke(driver,DVI, DP, HDMI, SCART, USB, THU, VGA)

    print(Naslov)
    files=fileUploader().listFilesForName(Naslov)
    for k in files:
        print(k)
        driver.find_element("id", 'item_file_10').send_keys(k)
        time.sleep(1)
    #time.sleep(10000)
    driver.find_element("id", "ad-submitButton").click()
    time.sleep(1)
    print("done")

#driver.close()
