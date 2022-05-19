import json

with open('arquivo.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # Faz um arquivo json voltar a ser um dicionário


for chave, valor in d1_json.items():
    for k, v in valor.items():
        print(k, v)
