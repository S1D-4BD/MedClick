#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://accesrendezvous.telussante.com/#/")
wait = WebDriverWait(driver, 10)

prenom = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
prenom.send_keys("")

nom = driver.find_element(By.NAME, "lastName")
nom.send_keys("")

nam = driver.find_element(By.NAME, "hin")
nam.send_keys("")

seq = driver.find_element(By.NAME, "hinSequence")
seq.send_keys("")

femme = driver.find_element(By.XPATH, "//span[text()='Femme']")
driver.execute_script("arguments[0].click();", femme)

email = driver.find_element(By.NAME, "email")
email.send_keys("")

tel = driver.find_element(By.NAME, "mobilePhone")
tel.send_keys("")

francais = driver.find_element(By.XPATH, "//span[text()='Français']")
driver.execute_script("arguments[0].click();", francais)

sms = driver.find_element(By.XPATH, "//input[@name='radioCommPref' and @value='sms']")
driver.execute_script("arguments[0].click();", sms)

checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
driver.execute_script("arguments[0].click();", checkbox)

continuer = driver.find_element(By.XPATH, "//button[contains(text(), 'Continuer')]")
driver.execute_script("arguments[0].click();", continuer)

## page 2

time.sleep(5)

code_postal = wait.until(EC.presence_of_element_located((By.NAME, "postalCode")))
code_postal.clear()
code_postal.send_keys("")



while True:
    bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Rechercher')]")
    driver.execute_script("arguments[0].click();", bouton)
    print(f"Recherche TIME = - {time.strftime('%H:%M:%S')}")


    time.sleep(0.5)
    try:
        WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".el-loading-mask"))
        )
    except:
        pass
    time.sleep(0.5)

    dispos = driver.find_elements(By.CLASS_NAME, "availability")

    if len(dispos) > 0:
        print(f"RDV TROUVE {len(dispos)} dispo(s)")
        for d in dispos:
            print("   ", d.text.replace("\n", " - "))
        break

    print("vide")
    time.sleep(0.1)



first_rdv = dispos[0]
driver.execute_script("arguments[0].click();", first_rdv)

time.sleep(2)


fermer = driver.find_elements(By.XPATH, "//button[contains(text(), 'Fermer')]")
if fermer:
    driver.execute_script("arguments[0].click();", fermer[0])
    print("plage deja prise relancer la recherche")
else:
    reserver = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[@data-test-id='book-appt-btn']")))
    driver.execute_script("arguments[0].click();", reserver)
    print("RESERVE")


input("TTTT")
