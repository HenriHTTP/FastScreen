import http.client
import json
from gerartoken import generate_token
from datetime import date

def get_total_for_origin(origin):
    # Obtém a data atual
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
          "origin": [origin]
        },
        "range_filters": {
          "issuance_date": {
            "gte": data_atual,
            "lte": data_atual
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

    # Extrai o valor "2" da resposta
    response_data = json.loads(data.decode("utf-8"))
    total = response_data.get("total", 0)

    return total

def bacendouv3():
    total_bacen = get_total_for_origin("BACEN/DOU")
    total_dti = get_total_for_origin("DTI/DOU")
    total_coaf = get_total_for_origin("COAF/DOU")

    return total_bacen + total_dti + total_coaf

# Exemplo de uso:
print(bacendouv3())
