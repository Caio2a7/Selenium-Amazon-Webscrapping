from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options


def lambda_handler(event, context):
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.com.br")
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, '[data-csa-c-content-id="nav_cs_bestsellers"]').click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/bestsellers/videogames/ref=zg_bs_nav_0"]').click()
    sleep(3)
    lista_produtos = []
    while True:
        while True:
            lista_nomes = driver.find_elements(By.CSS_SELECTOR, f'[data-a-card-type="basic"]')
            lista_produtos.append(lista_nomes[0].text)
            break
        try:
            driver.find_element(By.XPATH, '//*[@id="dealsGridLinkAnchor"]/div/div[3]/div/ul/li[4]/a').click()
            sleep(5)
        except NoSuchElementException:
            break

    response = {
        "statusCode": 200,
        "scrap": lista_produtos
    }

    return print(response)


lambda_handler(1, 2)
