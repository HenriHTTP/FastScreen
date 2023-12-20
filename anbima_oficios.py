from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.chrome.options import Options

def oficios(data_desejada):
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)
    
    data_desejada = datetime.strptime(data_desejada, '%Y-%m-%d')


    # Abre a página desejada
    url = "https://www.anbima.com.br/pt_br/institucional/comunicados-oficiais/oficios/oficios.htm"
    driver.get(url)

    # Espera o conteúdo dinâmico ser carregado (pode ser necessário ajustar o tempo)
    driver.implicitly_wait(10)

    # Define o seletor dos dados
    data_selector = "#Form_4028B88156568443015656C243F00B4C > div > div.ultimas-noticias.area-scroll > ul > li:nth-child(1) > a"

    # Extrai o texto do elemento
    element_text = driver.find_element(By.CSS_SELECTOR, data_selector).text

    # Obtém a data desejada como uma string no formato dd/mm/yyyy
    desired_date_str = data_desejada.strftime('%d/%m/%Y')

    # Inicializa um contador para contabilizar as vezes que a data desejada aparece no texto
    count_desired_date = element_text.count(desired_date_str)

    # Fecha o navegador
    driver.quit()

    # Retorna o contador
    return count_desired_date
