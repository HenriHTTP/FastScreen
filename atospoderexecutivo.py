import requests
from bs4 import BeautifulSoup
import re

def count_atospoderexecutivo():
    urls = [
        "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Atos+do+Poder+Executivo",
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