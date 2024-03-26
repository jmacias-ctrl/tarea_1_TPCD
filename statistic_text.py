import sys
import os 

if(len(sys.argv)<2):
    print("Error: No ha ingresado el nombre del archivo: py main.py ejemplo.txt")
    exit()

ruta_archivo = "input/"+sys.argv[1]
archivo = open(ruta_archivo, 'r', encoding="UTF-8")



def words_paragraph_total(content):
    text = [x for x in content.splitlines() if x]
    count = 0
    set_words = set()
    for string in text:
        words = string.split()
        count += len(words)
        set_words.update(words)
    return len(text), count, len(set_words)


        
    