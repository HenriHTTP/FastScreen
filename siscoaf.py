import requests
from bs4 import BeautifulSoup
from datetime import datetime

def siscoaf():
    url = "https://www.gov.br/coaf/pt-br/pastas-antigas-disponiveis-para-pesquisa/sobre-o-coaf-1/publicacoes/avisos-e-comunicados-siscoaf?b_start:int=60"

    # Faz a requisição HTTP
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Analisa o HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Localiza a tabela desejada
        tabela = soup.find('table')

        # Lista para armazenar os textos das células
        textos_celulas = []

        # Verifica se a tabela foi encontrada
        if tabela:
            # Obtém as células desejadas com base no seletor CSS
            celulas_desejadas = soup.select('#content-core > div > table > tbody > tr > td:nth-child(1) > a')

            # Extrai o texto das células e adiciona à lista
            for celula_desejada in celulas_desejadas:
                texto_celula = celula_desejada.get_text(strip=True)
                textos_celulas.append(texto_celula)
        else:
            print("Tabela não encontrada.")
            return 0  # Retorna 0 se a tabela não for encontrada

        # Obtém a data atual
        data_atual = datetime.now().strftime("%d/%m/%Y")

        # Compara a data atual com os textos das células e conta as correspondências
        count = sum(1 for texto_celula in textos_celulas if texto_celula == data_atual)

        return count
    else:
        print("Erro na requisição. Código de status:", response.status_code)
        return 0  # Retorna 0 em caso de erro na requisição

# Exemplo de chamada da função
resultado_coaf = siscoaf()
print(resultado_coaf)
