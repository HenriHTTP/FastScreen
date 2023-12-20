from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.chrome.options import Options

def anpd():
    # Configuração do WebDriver (certifique-se de ter o WebDriver apropriado para seu navegador instalado)
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)

    
    # URL alvo
    url = "https://www.gov.br/anpd/pt-br/assuntos/noticias/"

    # Acessa a URL
    driver.get(url)

    # Espera até que a página esteja completamente carregada (você pode ajustar o tempo conforme necessário)
    driver.implicitly_wait(10)

    # Localiza todos os elementos usando o XPath fornecido
    xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "data", " " ))]'
    elementos = driver.find_elements(By.XPATH, xpath)

    # Obtém a data atual
    data_atual = datetime.date.today().strftime("%d/%m/%Y")

    # Variável para contabilizar as datas correspondentes à data atual
    datas_correspondentes = 0

    # Itera sobre os elementos encontrados
    for indice, elemento in enumerate(elementos, start=1):
        # Usa get_attribute para obter o texto do elemento
        texto = elemento.get_attribute("textContent").strip()
        
        # Compara com a data atual
        if data_atual in texto:
            datas_correspondentes += 1

    # Fecha o navegador
    driver.quit()

    # Retorna o resultado como um número inteiro
    return datas_correspondentes

# Exemplo de chamada da função
result = anpd()
print(f"\nNúmero de datas correspondentes à data atual: {result}")
