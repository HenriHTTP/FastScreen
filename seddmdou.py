import requests
from bs4 import BeautifulSoup
import re


def count_seddmdou():
    url = "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Minist%C3%A9rio+da+Economia&orgSub=Secretaria+Especial+de+Desestatiza%C3%A7%C3%A3o%2C+Desinvestimento+e+Mercados"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    contagem_str = soup.find(class_="text-default").get_text(strip=True)
    contagem_str = re.sub(r'\D', '', contagem_str)
    contagem = int(contagem_str) if contagem_str else 0

    return contagem
