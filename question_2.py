import os
#Sobre variáveis de ambiente, responda:
#O que são?
'''Variáveis de ambiente são valores nomeados dinamicamente que pode afetar o modo como os processos 
em execução irão se comportar em um computador. Elas são parte do ambiente no qual um processo executa.'''

#Como elas podem ser obtidas pelo módulo ‘os’ de Python?
print(os.environ)

#Como pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?
'''Ou para imprimir variaveis especificas'''
print(os.environ['HOMEDRIVE'])
print(os.environ['HOMEPATH'])

