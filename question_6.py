#Escreva um programa que indique a extensão de um arquivo usando função do módulo os.path.
import os
 
filename, file_extension = os.path.splitext('/path/to/somefile.ext')
print(file_extension)