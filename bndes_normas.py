import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def bndes_normas():
    # Instanciar o driver do Selenium (certifique-se de ter o chromedriver no PATH)
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)

    
    # Navegar até a URL desejada
    url = "https://www.bndes.gov.br/wps/portal/site/home/instituicoes-financeiras-credenciadas/normas/normas-operacoes-indiretas"
    driver.get(url)

    # Aguarde o carregamento da página (você pode ajustar esse tempo conforme necessário)
    driver.implicitly_wait(10)

    # Execute o JavaScript usando XPath para obter os textos de todos os links na primeira coluna
    js_script = '''
        var xpath = '//*[contains(concat(" ", @class, " "), concat(" ", "titulo", " "))]';
        var elements = document.evaluate(xpath, document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);
        var dates = [];
        for (var i = 0; i < elements.snapshotLength; i++) {
            var text = elements.snapshotItem(i).textContent;
            var dateMatch = text.match(/(\d{2}\.\d{2}\.\d{4})/);
            if (dateMatch) {
                dates.push(dateMatch[0]);
            }
        }
        return dates;
    '''

    # Obtenha os resultados do JavaScript
    result = driver.execute_script(js_script)

    # Obtenha a data atual
    data_atual = datetime.now().strftime("%d.%m.%Y")

    # Inicialize o contador
    contador = 0

    # Realize o comparativo de datas
    for date in result:
        if date == data_atual:
            contador += 1

    # Feche o navegador
    driver.quit()

    # Retorne o valor do contador
    return contador

# Chamada da função e impressão do resultado
resultado = bndes_normas()
print(resultado)
