import re


def remove_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)
