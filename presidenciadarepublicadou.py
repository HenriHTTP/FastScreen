import requests
from bs4 import BeautifulSoup
import re
from datetime import date


def count_presidenciadarepublicadou():
    today = date.today().strftime("%d-%m-%Y")
    # URLS
    #       Presidencia da Republica
    # Assessoria Especial do Presidente da República
    # Secretaria de Comunicação Social
    #       Secretaria de Relações Institucionais
    # Editais e avisos/Presi...
    # Gabinete Pessoal do Presidente da República
    urls = [
        f"https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Presid%C3%AAncia+da+Rep%C3%BAblica&orgSub=Casa+Civil",
        #f"https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Presid%C3%AAncia+da+Rep%C3%BAblica&orgSub=Presid%C3%AAncia+da+Rep%C3%BAblica",
        #f"https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Presid%C3%AAncia+da+Rep%C3%BAblica&orgSub=Secretaria+de+Rela%C3%A7%C3%B5es+Institucionais", #Secretaria de Relações Institucionais
        #f"https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Editais+e+Avisos&orgSub=Presid%C3%AAncia+da+Rep%C3%BAblica", #Editais / Presidência da República
        #f"https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Presid%C3%AAncia+da+Rep%C3%BAblica&orgSub=Presid%C3%AAncia+da+Rep%C3%BAblica", #Presidência da República
        #f"https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Presid%C3%AAncia+da+Rep%C3%BAblica&orgSub=Assessoria+Especial+do+Presidente+da+Rep%C3%BAblica",
        #f"https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Presid%C3%AAncia+da+Rep%C3%BAblica&orgSub=Secretaria+de+Comunica%C3%A7%C3%A3o+Social",
        #f"https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=todos&exactDate=dia&sortType=0&delta=20&orgPrin=Presid%C3%AAncia+da+Rep%C3%BAblica&orgSub=Gabinete+Pessoal+do+Presidente+da+Rep%C3%BAblica" #Gabinete Pessoal do Presidente da República
    ]

    contagem = 0

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        count_element = soup.find(class_="text-default")

        if count_element:
            count_str = count_element.get_text(strip=True)
            count_str = re.sub(r'\D', '', count_str)
            count = int(count_str) if count_str else 0
            contagem += count

    return contagem
