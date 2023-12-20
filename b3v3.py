import http.client
import json
from gerartoken import generate_token
from datetime import datetime, timedelta, date  # Importe a classe timedelta

def b3v3():
    # Obtém a data atual e subtrai um dia para obter a data de ontem
    yesterday = date.today() - timedelta(days=1)
    data_atual = date.today().strftime("%Y-%m-%d")

    # Obtém o token utilizando a função generate_token()
    token = generate_token()

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
            "B3"
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
