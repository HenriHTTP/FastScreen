import requests
from bs4 import BeautifulSoup
from datetime import datetime

def cgu():
    url = "https://repositorio.cgu.gov.br/simple-search?location=1%2F33255&query=&rpp=10&sort_by=dc.date.issued_dt&order=desc&filter_field_1=dateIssued&filter_type_1=equals&filter_value_1=2023"

    # Faz a requisição HTTP
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Analisa o HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Localiza a tabela desejada
        tabela = soup.find('table')

        # Lista para armazenar as datas encontradas
        datas_encontradas = []

        # Verifica se a tabela foi encontrada
        if tabela:
            # Obtém a célula desejada com base no seletor CSS
            celula_desejada = soup.select_one('#content > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(3) > div > table > tbody > tr:nth-child(2) > td:nth-child(1)')

            # Extrai o texto da célula e adiciona à lista
            if celula_desejada:
                data_com_dou = celula_desejada.get_text(strip=True)
                data_sem_dou = data_com_dou.replace("DOU", "").strip()
                datas_encontradas.append(data_sem_dou)
            else:
                print("Célula não encontrada.")
                return 0  # Retorna 0 se a célula não for encontrada
        else:
            print("Tabela não encontrada.")
            return 0  # Retorna 0 se a tabela não for encontrada

        # Obtém a data atual
        data_atual = datetime.now().strftime("%d/%m/%Y")

        # Compara a data atual com as datas encontradas e conta as correspondências
        count = sum(1 for data in datas_encontradas if data == data_atual)

        return count
    else:
        print("Erro na requisição. Código de status:", response.status_code)
        return 0  # Retorna 0 em caso de erro na requisição

# Exemplo de chamada da função
resultado_repositorio = cgu()
print(resultado_repositorio)
