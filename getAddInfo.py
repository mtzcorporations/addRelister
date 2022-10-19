from selenium import webdriver
from selenium.webdriver.common.by import By

def formattTExt(Kat,Naslov, Cena, OpisOglasa): #formatiranje texta za shranjevanje
    formatted=Kat+ "--END--\n" + Naslov + "\n--END--\n"  + Cena + "\n--END--\n" + OpisOglasa
    return formatted
def textProcesor(drive): #branje in shranjevanja texta oglasa v datoteko
    Kategorija=drive.find_elements(By.CLASS_NAME, "breadcrumb-item")
    KategorijaKoncna=""
    for k in Kategorija[2:]:
        KategorijaKoncna+=k.text+"\n"

    Naslov = drive.find_element(By.CLASS_NAME, "entity-title").text
    Cena = drive.find_element(By.CLASS_NAME, "price.price--hrk").text
    Cena=''.join(Cena.split(' ')[0])
    OpisOglasa = drive.find_element("id", "base-entity-description-wrapper").text
    OpisOglasa = '\n'.join(OpisOglasa.split('\n')[1:])

    text=formattTExt(KategorijaKoncna,Naslov,Cena,OpisOglasa)
    with open('oglas.txt', 'w', encoding="utf-8") as f:
        f.write(text)

driver = webdriver.Chrome('chromedriver')
# then make a url variable
url = "https://www.bolha.com/procesor-amd-ryzen/gaming-pc-ryzen-2600x-16gb-ddr4-rtx-2060-512-ssd-2tb-hdd-oglas-10116261"

# then call the default open method described above
driver.get(url)
driver.find_element("id", 'didomi-notice-agree-button').click()
textProcesor(driver)


driver.quit()



