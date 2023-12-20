from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options

def anbima_distribuicao_de_produtos_de_investimento(data_desejada):
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)

    # Abra a URL desejada
    url = "https://www.anbima.com.br/pt_br/autorregular/codigos/distribuicao-de-produtos-de-investimento.htm"
    driver.get(url)

    # Encontre os elementos usando o JS Path fornecido
    elements1 = driver.execute_script('return Array.from(document.querySelectorAll("#N_402880DC6340DBD401634191EE9C1A48_bibliotecas-interna > li > a > small"))')
    elements2 = driver.execute_script('return Array.from(document.querySelectorAll("#N_402880DC6340DBD4016340FE2A8802D2_bibliotecas-interna > li > a > small"))')
    elements3 = driver.execute_script('return Array.from(document.querySelectorAll("#N_402880DC6340DBD40163415E56170C44_bibliotecas-interna > li > a > small"))')

    elements = elements1 + elements2 + elements3

    # Inicialize o contador
    contador = 0

    # Verifique cada elemento
    for element in elements:
        # Obtenha o texto do elemento
        texto_elemento = element.text

        # Verifique se o texto do elemento é uma data
        try:
            data_elemento = datetime.strptime(texto_elemento, "%d/%m/%Y")
            
            # Compare diretamente a data do elemento com a data desejada
            if data_elemento.date() == data_desejada:
                contador += 1
        except ValueError as e:
            print(f"Erro ao processar elemento: {e}")
            pass

    # Feche o navegador
    driver.quit()

    # Retorna o contador
    return contador
