import http.client
import json
from gerartoken import generate_token
from datetime import date, timedelta

def receitafederalv3():

    hoje = date.today()

    if hoje.weekday() == 0:  # Segunda-feira
        data_referencia = (hoje - timedelta(days=3)).strftime("%Y-%m-%d")  # Obtém a data de sexta-feira anterior
    else:
        data_referencia = (hoje - timedelta(days=1)).strftime("%Y-%m-%d")  # Obtém a data de ontem

    token = generate_token()

    conn = http.client.HTTPSConnection("api.legalbot.com.br")
    payload = json.dumps({
        "sort": [],
        "should": {},
        "must": {},
        "must_not": {},
        "filter": {
            "term_filters": {
                "origin": [
                    "Receita Federal"
                ]
            },
            "range_filters": {
                "issuance_date": {
                    "gte": data_referencia,
                    "lte": data_referencia
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
        'Authorization': 'Bearer ' + token
    }
    conn.request("POST", "/norms/norms/search_count", payload, headers)
    res = conn.getresponse()
    data = res.read()

    response_data = json.loads(data.decode("utf-8"))
    total = response_data.get("total", 0)

    return total