#Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório.
import os

print(os.stat('question_1.py').st_size)