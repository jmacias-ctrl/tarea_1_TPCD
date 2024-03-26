import sys
import os 

if(len(sys.argv)<2):
    print("Error: No ha ingresado el nombre del archivo: py main.py ejemplo.txt")
    exit()

ruta_archivo = "input/"+sys.argv[1]
archivo = open(ruta_archivo, 'r', encoding="UTF-8")


def replacing_substring(content, s_find, s_replace):
    index = content.lower().find(s_find.lower())
    new_content = content[:index] + s_replace + content[index+len(s_find):]
    return new_content
    
def replacing_substring_cs(content, s_find, s_replace):
    content.replace(s_find, s_replace)
    return content
    
print(replacing_substring(archivo.read(), "sureste de Hampden", "noreste de Chile"))