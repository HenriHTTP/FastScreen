from selenium import webdriver
import re
from datetime import datetime
from selenium.webdriver.chrome.options import Options

def bndes_programa_emergencial_de_suporte_a_empregos():
    # Configurando o WebDriver (neste exemplo, estou usando o Chrome)
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)
    
    # URL alvo
    url = "https://www.bndes.gov.br/wps/portal/site/home/financiamento/produto/programa-emergencial-de-suporte-a-empregos"
    driver.get(url)

    # Esperando a página carregar completamente (você pode ajustar o tempo conforme necessário)
    driver.implicitly_wait(10)

    # Executando o script JavaScript para obter o conteúdo de todos os elementos correspondentes ao seletor
    js_path = '#main > div > ul:nth-child(10) > li'
    elements_content = driver.execute_script(f'''
        var elements = document.querySelectorAll("{js_path}");
        var content = [];
        for (var i = 0; i < elements.length; i++) {{
            content.push(elements[i].textContent);
        }}
        return content;
    ''')

    # Processando e extraindo apenas as datas
    dates = []
    for content in elements_content:
        # Extrai a parte da data do texto usando uma expressão regular no Python
        date_match = re.search(r'\d{1,2}[\/.-]\d{1,2}[\/.-]\d{2,4}', content)
        if date_match:
            dates.append(date_match.group())

    # Obtendo a data atual
    current_date = datetime.now().strftime('%d.%m.%Y')

    # Contando o número de itens com a data atual
    count_current_date = sum(1 for date in dates if date == current_date)

    # Fechando o navegador
    driver.quit()

    # Retornando o número de itens com a data atual
    return count_current_date

# Exemplo de chamada da função
result = bndes_programa_emergencial_de_suporte_a_empregos()
print(result)
