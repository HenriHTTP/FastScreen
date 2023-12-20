import requests
from lxml import etree
from datetime import date


def count_conselhoppidou():
    # Define a URL da página web
    url = "https://www.ppi.gov.br/legislacao/?input_from=&input_from_submit=&input_to=05%2F06%2F2023&input_to_submit=Y65&setores=&tipo_de_legislacao=#"

    # Faz a requisição GET à página web
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Obtém o conteúdo HTML da página
        html_content = response.text

        # Cria um objeto ElementTree a partir do conteúdo HTML
        tree = etree.HTML(html_content)

        # Define o XPath para o título desejado
        xpath = '//*[@id="table"]/tbody/tr[1]/td[1]/text()'

        # Avalia o XPath para obter o título
        title = tree.xpath(xpath)

        # Verifica se encontrou o título
        if title:
            # Extrai a data do título
            date_str = title[0].strip()  # Remove espaços em branco
            date_obj = date.today().strftime("%d/%m/%Y")  # Obtém a data atual no formato dd/mm/aaaa

            # Verifica se a data corresponde à data atual
            if date_str == date_obj:
                count = 1  # Contabiliza como 1 se a data corresponder à data atual
            else:
                count = 0
        else:
            count = 0
    else:
        count = 0

    return count