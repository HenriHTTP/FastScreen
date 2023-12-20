import http.client
import json
from gerartoken import generate_token
from datetime import datetime, timedelta, date

def aneelv3():
    # Obtém a data atual
    today = date.today()
    # Obtém o token utilizando a função generate_token()
    token = generate_token()

    # Calcula a data de ontem ou a sexta-feira anterior, conforme a lógica desejada
    if today.weekday() == 0:  # Se hoje for segunda-feira (weekday() retorna 0 para segunda-feira)
        yesterday = today - timedelta(days=3)  # Pegar a sexta-feira anterior (3 dias atrás)
    else:
        yesterday = today - timedelta(days=1)  # Pegar o dia anterior

    # Faz a requisição à API utilizando o token obtido
    conn = http.client.HTTPSConnection("api.legalbot.com.br")
    payload = json.dumps({
        "sort": [],
        "should": {},
        "must": {},
        "must_not": {},
        "filter": {
            "term_filters": {
                "origin": [
                    "ANEEL"
                ]
            },
            "range_filters": {
                "issuance_date": {
                    "gte": yesterday.strftime("%Y-%m-%d"),
                    "lte": yesterday.strftime("%Y-%m-%d")
                }
            }
        },
        "aggs": {
            "term_aggs": [
                "origin",
                "norm_type"
            ]
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token  # Utiliza o token obtido na autorização
    }
    conn.request("POST", "/norms/norms/search_count", payload, headers)
    res = conn.getresponse()
    data = res.read()

    response_data = json.loads(data.decode("utf-8"))
    total = response_data.get("total", 0)

    return total

# Exemplo de uso da função
total_normas_aneel = aneelv3()
print(f"Total de normas ANEEL: {total_normas_aneel}")
