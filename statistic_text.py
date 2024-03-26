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

t_paragraphs, t_words, t_words_unique = words_paragraph_total(archivo.read())
print(t_paragraphs, t_words, t_words_unique)
#contenido = archivo.read().splitlines()
#texto = [x for x in contenido if x]


#count = 0
#set_palabras = set()
#for string in texto:
#    palabras = string.split()
#    count += len(palabras)
#    set_palabras.update(palabras)

#print(len(texto))
#print(count)
#print(len(set_palabras))



        
    