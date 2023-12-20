import requests
from bs4 import BeautifulSoup
from datetime import datetime

def cfc():
    url = "https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/normas-completas/"

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
            # Itera sobre as linhas da tabela, excluindo o cabeçalho
            for linha in tabela.find_all('tr')[1:]:
                # Obtém todas as células da linha
                celulas = linha.find_all('td')
                
                # Extrai o texto da segunda célula (índice 1), remove "DOU" e adiciona à lista
                if len(celulas) > 1:
                    data_com_dou = celulas[1].get_text(strip=True)
                    data_sem_dou = data_com_dou.replace("DOU", "").strip()
                    datas_encontradas.append(data_sem_dou)
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
resultado = cfc()
print(resultado)
