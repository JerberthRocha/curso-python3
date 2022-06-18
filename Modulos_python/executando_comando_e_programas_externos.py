import subprocess
# comandos:
# windows - ping numero_de_ip (windows para automaticamente)
# linux/mac - ping numero_de_ip -c 4 (-c 4 é o comando p/ parar no linux) 

saida = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4'],
    capture_output=True,
    text=True
)

print(saida)