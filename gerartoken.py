import http.client
import json


def generate_token():
    conn = http.client.HTTPSConnection("api.legalbot.com.br")
    payload = json.dumps({
        "username": "willian.lima@legalbot.com.br",
        "password": "Trymore1@3"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/sec/auth/token", payload, headers)
    res = conn.getresponse()
    data = res.read()
    token = json.loads(data.decode("utf-8"))["bearer"]  # Atualiza a chave para "bearer"
    return token
