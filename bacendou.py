import requests
from bs4 import BeautifulSoup
import re

def count_bacendou():
    total_bacendou = bacendou_total()
    total_dti = dti_total()
    total_coaddou = coafdou_total()

    return total_bacendou + total_dti + total_coaddou

def bacendou_total():
    urls = [
        "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Banco+Central+do+Brasil",  # ESSE É BACEN COMPLETO
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

def dti_total():
    urls = [
        # ESSE É DTI COMPLETO DERIVADO DO BACEN(SUBCATEGORIA)
        "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Banco+Central+do+Brasil&orgSub=%C3%81rea+de+Administra%C3%A7%C3%A3o&artType=Departamento+de+Tecnologia+da+Informa%C3%A7%C3%A3o",
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

def coafdou_total():
    urls = [
        # ESSE É COAF/DOU COMPLETO DERIVADO DO BACEN(SUBCATEGORIA)
        "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Banco+Central+do+Brasil&orgSub=Conselhode+Controle+de+Atividades+Financeiras",
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

# Example usage:
result = count_bacendou()
print(result)
