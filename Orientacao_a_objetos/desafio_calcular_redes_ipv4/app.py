from calculando_redes_ipv4 import CalculaIpv4

calcula_ipv4 = CalculaIpv4(ip='192.168.0.1', mascara='255.255.255.192')

print(f'IP: {calcula_ipv4.ip}')
print(f'MÁSCARA: {calcula_ipv4.mascara}')
print(f'REDE: {calcula_ipv4.rede}')
print(f'BROADCAST: {calcula_ipv4.broadcast}')
print(f'PREFIXO: {calcula_ipv4.prefixo}')
print(f'NÚMERO DE IPS DA REDE: {calcula_ipv4.numero_de_ips}')