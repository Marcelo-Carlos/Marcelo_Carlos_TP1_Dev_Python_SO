#Indique uma maneira de criar um processo externo ao seu programa usando o módulo ‘os’ e 
# usando o módulo ‘subprocess’ de Python. Dê um exemplo de cada.
import os, subprocess

exec_program = os.environ['SYSTEMROOT'] + '\\System32\\notepad.exe'
os.spawnl(os.P_NOWAIT, exec_program, " ")

#Subprocess
print(subprocess.run("notepad"))