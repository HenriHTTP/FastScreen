import requests
import re
from lxml import html
from datetime import datetime, timedelta

def count_anp():
    # Obtém a data de ontem no formato desejado (dia-mês-ano)
    data_pesquisa = (datetime.now() - timedelta(days=1)).strftime("%d-%m-%Y")

    # URL da página com a data de ontem
    url = f"https://atosoficiais.com.br/anp/?q=&fieldsearch=ano&date_start={data_pesquisa}&date_end={data_pesquisa}"

    # Faz a requisição HTTP
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Converte o conteúdo da resposta para um objeto de árvore HTML
        tree = html.fromstring(response.content)

        # Extrai o texto usando o XPath fornecido
        resultado_xpath = tree.xpath('//*[@id="content"]/div/div[2]/div/section/div/h4/text()')

        # Verifica se a mensagem indicando nenhum ato encontrado está presente
        if 'Nenhum ato encontrado na sua pesquisa' in resultado_xpath[0]:
            return '0'
        else:
            # Se a mensagem não estiver presente, extrai o número de atos usando expressão regular
            numero_atos = re.search(r'\b(\d+)\b', resultado_xpath[0]).group(1)
            return numero_atos
    else:
        # Se a requisição não for bem-sucedida, retorna uma mensagem de erro
        return f"Erro na requisição. Código de status: {response.status_code}"

# Exemplo de chamada da função a partir de um script pai
if __name__ == "__main__":
    resultado = count_anp()
    print(resultado)
