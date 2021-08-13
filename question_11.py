#Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo, usando o módulo ‘os’, 
# de bloco de notas (notepad) para abri-lo.
import os 

nome_arq = input('Digite o nome do arquivo texto: ')
arq = "notepad.exe " + nome_arq
os.system(arq)
