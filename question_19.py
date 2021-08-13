#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de armazenamento disponível
# há na partição do sistema (onde o sistema está instalado).
import psutil

print(f'Total: {round(psutil.disk_usage(path="C:").total/(1024*1024*1024), 2)} GB')