import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re


def count_receitafederal():
    today = datetime.now()
    if today.weekday() == 0:  # Segunda-feira
        friday = today - timedelta(days=3)
        date_str = friday.strftime("%d/%m/%Y")
    else:
        yesterday = today - timedelta(days=1)
        date_str = yesterday.strftime("%d/%m/%Y")

    url = f"http://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?facetsExistentes=&orgaosSelecionados" \
          f"=&tiposAtosSelecionados=&lblTiposAtosSelecionados=&ordemColuna=&ordemDirecao=&tipoConsulta=formulario" \
          f"&tipoAtoFacet=&siglaOrgaoFacet=&anoAtoFacet=&termoBusca=&numero_ato=&tipoData=2&dt_inicio={date_str}" \
          f"&dt_fim={date_str}&ano_ato=&optOrdem=Publicacao_DESC"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    contagem_element = soup.find('strong')
    contagem_text = contagem_element.text if contagem_element else 'N/A'

    # Extrair apenas o número da contagem
    contagem = re.search(r'\d+', contagem_text)
    if contagem:
        return contagem.group()
    else:
        return 'N/A'
