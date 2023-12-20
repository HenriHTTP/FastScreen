from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import subprocess

subprocess.call(["python", "marinha.py"])


links_and_search_terms = {
    'https://www.gov.br/coaf/pt-br/acesso-a-informacao/Institucional/a-atividade-de-supervisao/regulacao/supervisao/normas-1': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'https://www.gov.br/coaf/pt-br/sistemas/siscoaf/comunicados-siscoaf': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'http://conama.mma.gov.br/atos-normativos-sistema': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'https://www.cpc.org.br/CPC/Documentos-Emitidos/Revisoes': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'https://www.cpc.org.br/CPC/Documentos-Emitidos/Orientacoes': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'https://www.cpc.org.br/CPC/Documentos-Emitidos/Contribuicoes-Enviadas-ao-IASB': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'https://www.cpc.org.br/CPC/Audiencias-e-Consultas/Em-Andamento': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'https://www.cpc.org.br/CPC/Documentos-Emitidos/Interpretacoes': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'https://www.ppi.gov.br/legislacao/': [
        datetime.now().strftime('%d de %B de %Y').lower(),  # Formato "dd de mês de aaaa" em letras minúsculas
    ],
    'https://conteudo.cvm.gov.br/audiencias_publicas/': [
        'Consulta Pública SNC 06/23',  # Formato "dd de mês de aaaa" em letras minúsculas
    ],
    'https://conteudo.cvm.gov.br/legislacao/index.html?numero=&lastNameShow=&lastName=&filtro=todos&dataInicio=&dataFim=&buscado=false&contCategoriasCheck=7': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'https://portal.autorregulacaobancaria.com.br/paginas/16/pt-br/normativos': [
        'SARB nº 027/2023',  # Formato dd/mm/aaaa
    ],
    'https://www.gov.br/pgfn/pt-br/assuntos/consultoria-administrativa/pareceres-referenciais': [
        'Parecer Referencial CCA/PGFN nº 03/2023',  # Formato dd/mm/aaaa
    ],
    'https://www.gov.br/pgfn/pt-br/acesso-a-informacao/consultas-publicas': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],
    'https://www.gov.br/economia/pt-br/orgaos/entidades-vinculadas/autarquias/previc/regulacao/normas/portarias': [
        '2023',  # Formato dd/mm/aaaa
    ],
    'https://www.gov.br/economia/pt-br/orgaos/entidades-vinculadas/autarquias/previc/regulacao/normas/instrucoes/instrucoes-previc': [
        '2023',  # Formato dd/mm/aaaa
    ],
    'http://sped.rfb.gov.br/': [
        datetime.now().strftime('%d/%m/%Y'),  # Formato dd/mm/aaaa
    ],

    # Adicione mais links e termos de pesquisa aqui
}

driver = webdriver.Chrome()

for url, search_terms in links_and_search_terms.items():
    driver.get(url)
    time.sleep(1)
    page_text = driver.find_element(By.TAG_NAME, 'body').text

    for search_term in search_terms:
        count = page_text.count(search_term)
        if count > 0:
            print(f'!!!Encontrei {count} ocorrências de "{search_term}" em {url}!!!')
            break
    else:
        print(f'Não encontrei nenhum dos termos de pesquisa em {url}')

driver.close()
