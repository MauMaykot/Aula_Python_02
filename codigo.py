filename = "estantevirtual.csv"
f = open(filename, "w", encoding="utf-8")
headers = "Titulo; Novos; Usados; Data\n"
f.write(headers)


links = []

#while True:

precios = driver.find_elements_by_xpath('//a[@class="busca-box m-group ga_tracking_event desktop"]')

for i in precios:

    links.append(i.get_attribute('href'))
                
    print(links)

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