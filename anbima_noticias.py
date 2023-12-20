from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime


def noticias(data_desejada):
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)


    data_desejada = datetime.strptime(data_desejada, '%Y-%m-%d')

    # Abre a página desejada
    url = "https://www.anbima.com.br/pt_br/noticias/"
    driver.get(url)

    # Espera o conteúdo dinâmico ser carregado (pode ser necessário ajustar o tempo)
    driver.implicitly_wait(10)

    # Define o seletor dos itens de notícia
    news_item_selector = "#noticias-interna > div > div"

    # Extrai os elementos de notícia da página
    news_items = driver.find_elements(By.CSS_SELECTOR, news_item_selector)

    # Inicializa o contador para notícias com a data desejada
    count_desired_date = 0

    # Compare cada data com a data desejada e atualize o contador
    for news_item in news_items:
        # Extrai o texto da notícia
        news_text = news_item.text

        # Verifica se a data desejada está presente no texto da notícia
        if data_desejada.strftime('%d/%m/%Y') in news_text:
            count_desired_date += 1

    # Retorna o contador
    return count_desired_date