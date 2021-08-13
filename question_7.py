#Escreva um programa que imprima apenas o caminho absoluto de um arquivo com nome relativo. A impressão não deve conter o nome do arquivo, apenas o caminho.
import os

cam_absoluto = os.path.abspath("C:/Users/marca/Desktop/Python/aula3/jogo.py")
print(os.path.split(cam_absoluto)[0])