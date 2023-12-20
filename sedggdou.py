import requests
from bs4 import BeautifulSoup
import re


def count_sedggdou():
    url = "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Ministerio+da+Economia&orgSub=Secretaria+Especial+de+Desburocratiza%C3%A7%C3%A3o,+Gest%C3%A3o+e+Governo+Digital"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    contagem_str = soup.find(class_="text-default").get_text(strip=True)
    contagem_str = re.sub(r'\D', '', contagem_str)
    contagem = int(contagem_str) if contagem_str else 0

    return contagem
