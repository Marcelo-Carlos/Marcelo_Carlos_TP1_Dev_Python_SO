#Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele.
import subprocess

processo = subprocess.Popen("notepad")
print('PID do processo: ', processo.pid)