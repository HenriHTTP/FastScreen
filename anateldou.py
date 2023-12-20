# Arquivo: agudou.py
import requests
from bs4 import BeautifulSoup
import re
from datetime import date, datetime


def anateldou(data_desejada=None):
    if data_desejada is None:
        # Use a data atual se não for especificada
        data_desejada = date.today().strftime("%Y-%m-%d")
    else:
        # Formate a data fornecida para o formato correto
        data_desejada = datetime.strptime(data_desejada, '%d-%m-%Y').strftime('%Y-%m-%d')
    url = "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate={data_desejada}&sortType=0&delta=20&orgPrin=Minist%C3%A9rio+das+Comunica%C3%A7%C3%B5es&orgSub=Ag%C3%AAncia+Nacional+de+Telecomunica%C3%A7%C3%B5es"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    contagem_str = soup.find(class_="text-default").get_text(strip=True)
    contagem_str = re.sub(r'\D', '', contagem_str)
    contagem = int(contagem_str) if contagem_str else 0

    return contagem
