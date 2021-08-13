#Escreva um programa em Python usando o módulo ‘psutil’, que imprima para a partição corrente:
import psutil

datas_system = psutil.disk_partitions()
print(f'Nome do dispositivo: {datas_system[0][0]}')
print(f'Tipo de sistema de arquivos: {datas_system[0][2]}')

storage = psutil.disk_usage(path=datas_system[0][0])
print(f'Total de armazenamento: {round(storage.used/(1024*1024*1024), 2)} GB')

print(f'Total de armazenamento disponivel: {round(storage.free/(1024*1024*1024), 2)} GB')
