#Escreva uma função em Python que, dado um número PID, imprima o nome do usuário proprietário, 
# o tempo de criação e o uso de memória em KB.
import psutil, datetime

def print_infos(pid):
    processo = psutil.Process(pid)
    print(f'Nome do dono do processo: {processo.username()}')
    data = datetime.datetime.fromtimestamp(processo.create_time()).strftime("%d-%m-%Y %H:%M:%S")
    print(f'Tempo de criação: {data}')
    print(f'Uso da memória: {processo.memory_info()[0]} KB')

print_infos(34364)