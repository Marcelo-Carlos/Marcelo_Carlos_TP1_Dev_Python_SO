#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo.
import psutil

print(psutil.cpu_times(percpu=True))