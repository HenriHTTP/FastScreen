from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from datetime import datetime, date

def count_agu(data_desejada):
    # Configurações do Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Execução em modo headless (sem interface gráfica)
    driver = webdriver.Chrome(options=chrome_options)

    # URL específica
    site_url = "https://www.planalto.gov.br/CCIVIL_03/AGU/Pareceres/2023-2026/_Pareceres%20AGU%202023-2026.htm"

    # Dicionário para mapear os nomes dos meses para números
    month_dict = {'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04', 'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08', 'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'}

    # Data para comparação
    compare_date = datetime.strptime(data_desejada, '%d-%m-%Y').strftime('%d/%m/%Y')
    count = 0

    # Tentar encontrar todos os elementos com base no JS Path
    try:
        data_elements = driver.execute_script(
            'return Array.from(document.querySelectorAll("body > div:nth-child(6) > table > tbody > tr > td:nth-child(1) > font:nth-child(1)")).map(e => e.textContent);'
        )

        # Imprimir todos os dados encontrados, formatando as datas
        for data_element in data_elements:
            formatted_data = " ".join(data_element.split())
            date_match = re.search(r'\d+ de \w+ de \d+', formatted_data)
            if date_match:
                date_str = date_match.group()
                day, month, year = date_str.split(' de ')
                date_str = f'{day.zfill(2)}/{month_dict[month]}/{year}'
                #print(date_str)
                if date_str == compare_date:
                    count += 1

    except Exception as e:
        print(f"Erro ao obter elementos: {e}")

    # Encerrar o driver do Selenium
    driver.quit()

    # Retornar a contagem em vez de imprimi-la
    return count
