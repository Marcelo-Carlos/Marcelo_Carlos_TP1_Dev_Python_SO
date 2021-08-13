#Escreva um programa que indique se um arquivo existe ou não. Caso exista, indique se é realmente um arquivo ou não.
import os

def arq_existe(arquivo):
    if os.path.exists(arquivo):
        print(arquivo, 'existe!')
        if os.path.isfile(arquivo):
            print(arquivo, 'é um arquivo!')
        else:
            print(arquivo, 'não é um arquivo!')
    else:
        print(arquivo, 'não existe!')
        
p = 'question_1.py'     
arq_existe(p)