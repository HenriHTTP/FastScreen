from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Configurando o WebDriver (neste exemplo, estou usando o Chrome)
driver = webdriver.Chrome()

# Abrindo a URL desejada
url = "https://www3.bcb.gov.br/audpub/HomePage?0"
driver.get(url)

# Esperando a página carregar completamente (você pode ajustar o tempo conforme necessário)
driver.implicitly_wait(10)

# Obtendo o elemento da terceira linha usando JS Path
elemento_linha = driver.execute_script('return document.querySelector("body > div:nth-child(9) > table > tbody > tr:nth-child(3)")')

# Verificando se o elemento foi encontrado
if elemento_linha is not None:
    # Obtendo o elemento da segunda coluna da terceira linha usando JS Path
    elemento_coluna = driver.execute_script('return document.querySelector("body > div:nth-child(9) > table > tbody > tr:nth-child(3) > td:nth-child(2)")')

    # Verificando se o elemento tem algum valor diferente de 0
    if elemento_coluna.text != "0":
        # Se o elemento tiver algum valor diferente de 0, clicar no link na primeira coluna da terceira linha
        link = driver.execute_script('return document.querySelector("body > div:nth-child(9) > table > tbody > tr:nth-child(3) > td:nth-child(1) > a")')
        link.click()

        time.sleep(3)

        # Adicionando uma espera explícita
        wait = WebDriverWait(driver, 10)

        # Esperando até que o elemento interno esteja presente na página
        elemento_interno = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(9) > ul > li > a")))
        # Clicando no elemento interno
        elemento_interno.click()

        time.sleep(3)

        # Encontrar o elemento pelo ID "dataInicio"
        elemento_data_inicio = driver.find_element(By.ID, "dataInicio")

        # Obter o texto do elemento
        data_inicio_texto = elemento_data_inicio.text

        # Comparar a data retornada com a data atual
        data_atual = datetime.now().strftime("%d/%m/%Y")
        #data_atual = "14/12/2023"
        if data_inicio_texto == data_atual:
            contagem = 1
        else:
            contagem = 0

        # Imprimir o resultado
        print("Contagem:", contagem)

# Fechando o navegador
driver.quit()
