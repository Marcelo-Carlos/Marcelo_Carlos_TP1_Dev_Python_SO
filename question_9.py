#Escreva um programa que mostre as datas de criação e modificação de cada arquivo em um diretório.
import os, time

arq = os.stat('question_1.py')
print(f'Data de criação: {time.ctime(arq.st_ctime)}')
print(f'Data de modificação: {time.ctime(arq.st_atime)}')