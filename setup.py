from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from time import sleep

def __init__(browser_name):
    


def browsers_setup():

def amazon(event, occurency):
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com.br")

    driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[4]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="grid-main-container"]/div[2]/span[3]/ul/li[27]/label/input').click()
    driver.find_element(By.XPATH, '//*[@id="grid-main-container"]/div[2]/span[3]/ul/li[2]/label/input').click()
    driver.find_element(By.XPATH, '//*[@id="grid-main-container"]/div[2]/span[3]/ul/li[18]/label/input').click()
    sleep(3)
    item = 1
    lista_produtos = []
    while True:
        while True:
            try:
                lista_nomes = driver.find_elements(By.XPATH, f'//*[@id="grid-main-container"]/div[3]/div/div[{item}]/div/div/div/a[2]/div')
                lista_produtos.append(lista_nomes[0].text)
            except Exception:
                break
            item += 1
        try:
            driver.find_element(By.XPATH, '//*[@id="dealsGridLinkAnchor"]/div/div[3]/div/ul/li[4]/a').click()
            sleep(5)
        except NoSuchElementException:
            break
        item = 1
    response = {'statusCode': 200, 'body': lista_produtos}
    return print(response)