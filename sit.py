import requests
from lxml import html
from datetime import date


def count_sit():
    # URL para fazer a requisição
    url = "https://www.gov.br/trabalho-e-previdencia/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/ctpp/arquivos/normas-regulamentadoras?b_start:int=0"

    # Fazer a requisição GET à página
    response = requests.get(url)

    # Extrair o conteúdo HTML da resposta
    html_content = response.content

    # Parsear o conteúdo HTML
    tree = html.fromstring(html_content)

    # Encontrar todos os elementos com o XPath fornecido
    elementos_data = tree.xpath('//*[@id="content-core"]/div/table/tbody/tr/td[3]')

    # Obter a data atual
    data_atual = date.today().strftime("%d/%m/%Y")

    # Variável para armazenar o contador
    contador = 0

    # Verificar se os elementos foram encontrados
    if elementos_data:
        # Verificar se cada data é igual à data atual
        for elemento in elementos_data:
            data = elemento.text_content().strip()
            if data == data_atual:
                contador += 1

    # Retornar o resultado como um número
    return contador

resultado = count_sit()
print(resultado)
