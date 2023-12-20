import requests
from lxml import html
from datetime import date

def get_legislacao_cvm_result():
    current_date = date.today().strftime("%d/%m/%Y")

    url = f"https://conteudo.cvm.gov.br/legislacao/index.html?numero=&lastNameShow=&lastName=&filtro=todos&dataInicio={current_date}&dataFim={current_date}&buscado=false&contCategoriasCheck=7"

    response = requests.get(url)
    tree = html.fromstring(response.content)

    result = tree.xpath('//*[@id="main"]/div/section/section/form/div/span')
    if result:
        result = result[0].text_content()

        # Verificar se o resultado é "Nenhum resultado encontrado" e substituir por "0"
        if result == "Nenhum resultado encontrado":
            result = "0"

        # Extrair apenas o número da resposta
        result = ''.join(filter(str.isdigit, result))

    return result

