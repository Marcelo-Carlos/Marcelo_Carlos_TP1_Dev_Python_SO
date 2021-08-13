#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de memória principal e 
# quanto de memória de paginação (swap) existem no computador.
import psutil

memoria_principal = psutil.virtual_memory()

print(f'Memória principal: {round(memoria_principal.total/(1024*1024*1024), 2)} GB')

memoria_swap = psutil.swap_memory()
print(f'Memória swap: {round(memoria_swap.total/(1024*1024*1024), 2)} GB')