#Explique a principal semelhança e a principal diferença entre os comandos psutil.pids e psutil.process_iter.

#A principal semelhança é que todos retornam o PID
#a principal diferença é que o primeiro retorna uma lista classificada de PIDs em execução, e o segundo retorna uma instancia de classe para todos processos em execução, seguem exemplos:
import psutil

#Ex 1
print(psutil.pids())
#Ex 2
for i in psutil.process_iter(['pid', 'name', 'username']):
    print(i)
