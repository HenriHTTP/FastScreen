import requests
from bs4 import BeautifulSoup
import re
import datetime

def count_anpddou(data_desejada=None):
    if data_desejada is None:
        # Use a data atual se não for especificada
        data_desejada = 'dia'
    else:
        # Formate a data fornecida para o formato correto
        data_desejada = datetime.strptime(data_desejada, '%d-%m-%Y').strftime('%d-%m-%Y')
    urls = [
        "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate={data_desejada}&sortType=0&delta=20&orgPrin=Minist%C3%A9rio+da+Justi%C3%A7a+e+Seguran%C3%A7a+P%C3%BAblica&orgSub=Autoridade+Nacional+de+Prote%C3%A7%C3%A3o+de+Dados",
    ]

    total_contagem = 0
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        contagem_str = soup.find(class_="text-default").get_text(strip=True)
        contagem_str = re.sub(r'\D', '', contagem_str)
        contagem = int(contagem_str) if contagem_str else 0
        total_contagem += contagem

    return total_contagem