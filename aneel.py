from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time

def count_aneel():
    driver = webdriver.Chrome()


    url = 'https://biblioteca.aneel.gov.br/Busca/Avancada'

    driver.get(url)
    time.sleep(10)

    today = datetime.now()
    
    # Verifica se hoje é segunda-feira (dia da semana 0)
    if today.weekday() == 0:
        # Se for segunda-feira, ajusta a data para 3 dias atrás (sexta-feira)
        date_to_use = today - timedelta(days=3)
    else:
        # Nos outros dias, use a data de ontem
        date_to_use = today - timedelta(days=1)

    # Clicar no botão para mudar para a página "Legislação"
    botao_legislacao = driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div/button[2]')
    botao_legislacao.click()
    time.sleep(3)

    # Substituir o valor dos campos de data pelas variáveis
    campo_data1 = driver.find_element(By.XPATH, '//*[@id="LegislacaoDataPublicacao1"]')
    campo_data1.clear()
    campo_data1.send_keys(date_to_use.strftime("%d/%m/%Y"))

    campo_data2 = driver.find_element(By.XPATH, '//*[@id="LegislacaoDataPublicacao2"]')
    campo_data2.clear()
    campo_data2.send_keys(date_to_use.strftime("%d/%m/%Y"))

    # Clicar no botão "Buscar"
    botao_buscar = driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/form/div[4]/div[1]/button')
    botao_buscar.click()
    time.sleep(7)

    # Localizar o elemento pelo XPath e obter o valor
    elemento_valor = None
    try:
        elemento_valor = driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/div[1]/p/strong[1]')
        valor_texto = elemento_valor.text
        # Converter o valor de texto para número
        valor = int(valor_texto)  # ou float(valor_texto) se o valor puder ser decimal
    except NoSuchElementException:
        valor = 0

    # Imprimir o valor encontrado
    # print(valor)

    driver.quit()
    return valor

resultado = count_aneel()
print(resultado)
