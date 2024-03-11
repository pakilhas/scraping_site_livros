import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Importe a classe correta para o serviço do Edge
from selenium.webdriver.common.by import By
import time

# Iniciar o Microsoft Edge WebDriver
service = Service()  
options = webdriver.ChromeOptions()

# Iniciar o navegador Edge
driver = webdriver.Chrome(service=service, options=options)

#url que vamos fazer o scraping
url = 'https://books.toscrape.com/'
driver.get(url)

# meu navegador está fechando, deixei por enquanto até resolver
time.sleep(30) 

#loop definindo o começo em 58 pulando de 2 em 2 até o 95
elementos_a = driver.find_elements(By.TAG_NAME, 'a')
for i in range(58, 95, 2):
    if i < len(elementos_a):
        titulo = elementos_a[i].get_attribute('title')
        print(f"Título do elemento {i}: {titulo}")
# Fechar o navegador
driver.quit()