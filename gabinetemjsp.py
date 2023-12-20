import requests
from bs4 import BeautifulSoup
import re

def count_gabinetemjsp():
    urls = [
        "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Minist%C3%A9rio+da+Justi%C3%A7a+e+Seguran%C3%A7a+P%C3%BAblica&orgSub=Gabinete+do+Ministro",
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