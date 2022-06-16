"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
QUANDO CONVERTIDO DE PYTHON PARA JSON -=-=-=
Python    -->   JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################

QUANDO CONVERTIDO DE JSON PARA PYTHON -=-=-=
JSON	-->     Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""

from dados import *
import json

# dados_json = json.dumps(clientes_dicionario, indent=4)
# print(dados_json)

# dicionario = json.loads(clientes_json)

# for chave, valor in dicionario.items():
#     print(chave)
#     print(valor)

# with open('clientes.txt', 'w') as arquivo:
#     json.dump(clientes_dicionario, arquivo, indent=4)
    
with open('clientes.txt', 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)
