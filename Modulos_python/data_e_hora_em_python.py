# https://docs.python.org/3.0/library/datetime.html

from datetime import datetime, timedelta

#strptime(str, formato) -> converter em objeto de data a partir de uma string
# .strftime(formato) -> para formatar a data

# data = datetime(2022, 6, 14, 13,32,46)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))
# data = datetime.strptime('14/06/2022', '%d/%m/%Y')
# print(data.timestamp())
# data = datetime.fromtimestamp(1655179200.0)
# print(data)

data1 = datetime.strptime('14/06/2022 13:54:22', '%d/%m/%Y %H:%M:%S')
data2 = datetime.strptime('11/06/2022 22:34:02', '%d/%m/%Y %H:%M:%S')
print(data1)
data = data1 + timedelta(days=7, seconds=20)
print(data1.strftime('%d/%m/%Y %H:%M:%S'))
print(data2.strftime('%d/%m/%Y %H:%M:%S'))

diferenca = data1 - data2
print(diferenca)
print(diferenca.seconds)
print(diferenca.total_seconds())
print(diferenca.days)

print(data1 > data2)