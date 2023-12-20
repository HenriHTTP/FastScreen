from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options

def anbima_negociacao_de_instrumentos_financeiros(data_desejada):
    # Inicialize o WebDriver (certifique-se de ter o driver adequado instalado)
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)
    
    data_desejada = datetime.strptime(data_desejada, '%Y-%m-%d')


    # Abra a URL desejada
    url = "https://www.anbima.com.br/pt_br/autorregular/codigos/negociacao-de-instrumentos-financeiros.htm"
    driver.get(url)

    # Encontre os elementos usando o JS Path fornecido
    elements1 = driver.execute_script('return Array.from(document.querySelectorAll("#N_4028B88155DF85870155DF8631D1029B_bibliotecas-interna > li > a > small"))')
    elements2 = driver.execute_script('return Array.from(document.querySelectorAll("#N_4028B88155DF85870155DF86428B029E_bibliotecas-interna > li > a > small"))')

    elements = elements1 + elements2

    # Inicialize o contador
    contador = 0

    # Compare cada data com a data desejada e atualize o contador
    for element in elements:
        # Obtenha o texto do elemento
        texto_elemento = element.text

        # Verifique se o texto do elemento é uma data
        try:
            data_elemento = datetime.strptime(texto_elemento, "%d/%m/%Y").strftime("%d/%m/%Y")

            # Compare a data do elemento com a data desejada
            if data_elemento == data_desejada.strftime("%d/%m/%Y"):
                contador += 1
        except ValueError as e:
            print(f"Erro ao processar elemento: {e}")

    # Feche o navegador
    driver.quit()

    # Retorna o contador
    return contador
