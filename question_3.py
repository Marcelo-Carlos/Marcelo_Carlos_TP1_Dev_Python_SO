#Escreva um programa usando o módulo ‘os’ de Python que imprima o PID do próprio processo e também seu GID (identificador de grupo) caso seja sistema do tipo Linux.
import os
import platform

so = platform.system()
if so == 'Windows':    
    print(os.getpid())
elif so == 'Linux':
    print(os.getgid())

   

