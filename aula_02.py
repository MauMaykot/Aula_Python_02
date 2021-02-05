from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import csv
from datetime import datetime

driver = webdriver.Chrome(executable_path=r"C:/Users/mauricio.gomes\Desktop\Aula_02_Python/chromedriver.exe")
driver.maximize_window()
driver.get('https://www.estantevirtual.com.br/estante/literatura-brasileira')

filename = "estantevirtual.csv"
f = open(filename, "w", encoding="utf-8")
headers = "Titulo; Novos; Usados; Data\n"
f.write(headers)

links = []

precios = driver.find_elements_by_xpath('//a[@class="busca-box m-group ga_tracking_event desktop"]')

for i in precios:

    links.append(i.get_attribute('href'))
                
    #print(links)

wait = WebDriverWait(driver, 10)

for linkbylink in links:
    driver.get(linkbylink)

    titulo = wait.until(EC.presence_of_element_located(
                            (By.XPATH, '//html/body/div[1]/div/div/div/main/section[1]/div[1]/div/div/div[2]/h1'))).text
    print(titulo)

    novos = wait.until(EC.presence_of_element_located(
                            (By.XPATH, '//button[@id="linkFiltroNovo"]'))).text
    print(novos)

    usados = wait.until(EC.presence_of_element_located(
                            (By.XPATH, '//button[@id="linkFiltroUsado"]'))).text
    print(usados)

    dat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Data: " + dat)

    f.write(titulo + ";" + novos + ";" + usados + ";" + dat + ";" + "\n")
