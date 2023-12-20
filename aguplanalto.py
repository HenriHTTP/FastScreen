from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from datetime import datetime
from selenium.webdriver.chrome.options import Options

def aguplanalto():
    # Configuração do WebDriver (certifique-se de ter o WebDriver apropriado para seu navegador instalado)
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)
    # URL alvo
    url = "https://www.planalto.gov.br/CCIVIL_03/AGU/Pareceres/2023-2026/_Pareceres%20AGU%202023-2026.htm"

    # Acessa a URL
    driver.get(url)

    # Espera até que a página esteja completamente carregada (você pode ajustar o tempo conforme necessário)
    driver.implicitly_wait(10)

    # Localiza todos os elementos usando XPath
    xpath = "/html/body/div[3]/table/tbody/tr/td/font/a"
    elements = driver.find_elements(By.XPATH, xpath)

    # Lista para armazenar as datas no formato desejado
    datas_formatadas = []

    # Itera sobre os elementos encontrados
    for element in elements:
        element_text = element.text
        
        # Usa expressão regular para encontrar a data no texto
        padrao_data = re.search(r'(\d{1,2}) de ([a-zA-Z]+) de (\d{4})', element_text)
        
        # Verifica se o padrão foi encontrado
        if padrao_data:
            # Obtém os grupos da expressão regular
            dia, mes, ano = padrao_data.groups()
            
            # Converte o formato da data para xx/xx/xxxx
            mes_numerico = {
                'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04',
                'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08',
                'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'
            }[mes.lower()]
            
            data_formatada = f"{dia.zfill(2)}/{mes_numerico}/{ano}"
            
            # Adiciona a data formatada à lista
            datas_formatadas.append(data_formatada)

            # Imprime as datas formatadas
            print(f"Data formatada: {data_formatada}")

    # Obtém a data atual
    data_atual = datetime.now().strftime("%d/%m/%Y")

    # Verifica se a data atual está na lista de datas formatadas
    if data_atual in datas_formatadas:
        resultado = 1
    else:
        resultado = 0

    # Imprime o resultado
    print(f"Resultado: {resultado}")

    # Fecha o navegador
    driver.quit()

    # Retorna o resultado como número inteiro
    return int(resultado)

# Chama a função e armazena o resultado
resultado_final = aguplanalto()

# Usa o resultado como necessário no script pai
print(resultado_final)
