import requests
from datetime import date
import json
from lxml import html
import datetime
from selenium import webdriver
import re
import time
from datetime import datetime

# Função para converter a data
def converter_data(data):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    data = datetime.strptime(data, '%d/%m/%Y')
    return f"{data.day} de {meses[data.month-1]} de {data.year}"

def count_bacen():
    today = date.today().isoformat()
    url = f"https://www.bcb.gov.br/api/search/app/normativos/buscanormativos?querytext=ContentType:normativo%20AND%20contentSource:normativos&rowlimit=15&startrow=0&sortlist=Data1OWSDATE:descending&refinementfilters=Data:range(datetime({today}),datetime({today}T23:59:59))"
    #url = f"https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?dataInicioBusca={today}&dataFimBusca={today}&tipoDocumento=Todos"

    response = requests.get(url)
    body = json.loads(response.text)
    contagem_bacen = body['TotalRows']

    return contagem_bacen

def count_sicornoticias():
    # Configurando o WebDriver (neste exemplo, estou usando o Chrome)
    driver = webdriver.Chrome()

    # Abrindo a URL desejada
    url = "https://www.bcb.gov.br/estabilidadefinanceira/sicornoticias"
    driver.get(url)

    # Esperando a página carregar completamente (você pode ajustar o tempo conforme necessário)
    driver.implicitly_wait(10)
    time.sleep(3)

    # Executando o script JavaScript para obter o elemento usando o novo JS Path fornecido
    element = driver.execute_script('return document.querySelector("body > app-root > app-root > div > div > main > dynamic-comp > div > div > div.col-md-8 > div:nth-child(2) > div:nth-child(2)")')

    # Inicializando a contagem como 0
    contagem = 0

    # Verificando se o elemento foi encontrado
    if element is not None:
        # Obtendo o texto do elemento
        element_text = element.text

        # Definindo a data específica no formato desejado (por exemplo, "15/12/2023")
        data_especifica = converter_data(datetime.today().strftime('%d/%m/%Y'))

        # Usando uma expressão regular para encontrar todas as ocorrências da data no texto
        regex = re.compile(r'\b\d{1,2} de [^\d]+ \d{4}\b')
        correspondencias = regex.findall(element_text)

        # Contando quantas vezes a data específica ocorre nas correspondências
        contagem = correspondencias.count(data_especifica)

    # Fechando o navegador
    driver.quit()

    # Imprimindo a contagem final
    print("Contagem:", contagem)

    return contagem

def count_total():
    contagem_bacen = count_bacen()
    contagem_sicornoticias = count_sicornoticias()

    total = contagem_bacen + contagem_sicornoticias

    # Modificação aqui: Converta o total para uma string antes de retornar
    return str(total)

# Exemplo de uso:
total_contagem = count_total()

print(total_contagem)
