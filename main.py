import os
import sys
from statistic_text import * 
from replacing_text import *
def read_filetext(file_path):
    with open(file_path, "r", encoding="UTF-8") as file:
        content = file.read()
    return content

filename_list = os.listdir('io')

def pre_replacing_process(case_sensitive, content):
    exist = False
    s_find = ""
    while(exist==False):
        print("Introduzca la palabra o substring que desea reemplazar")
        s_find = input()
        exist = check_if_exist(content, s_find, case_sensitive)
        if(exist == False):
            print("Error: palabra o substring no fue encontrado")
    print("Introduzca la palabra o substring a reemplazar")
    s_replace = input()
    replacing_substring(content, file_path, s_find, s_replace)
    print("El archivo de texto fue modificado de manera exitosa")
    input("Presione Enter para volver al menu")

print('Seleccione el archivo de texto que desea trabajar')
for i in range(1,len(filename_list)+1):
    print(str(i)+".- "+filename_list[i-1])
index_filename = int(input())

file_path = "io/"+filename_list[index_filename-1]

user_input = -1

while(user_input!=0):
    os.system('cls||clear')
    print(filename_list[index_filename-1])
    print("Seleccione la accion que desea realizar")
    print("1.- Estadistica del Texto")
    print("2.- Leer Texto")
    print("3.- Buscar en el Texto")
    print("4.- Reemplazar palabra o substring en el Texto (Sin distincion de Mayusculas y Minusculas)")
    print("5.- Reemplazar palabra o substring en el Texto (Con distincion de Mayusculas y Minusculas)")
    print("0.- Salir")
    user_input = int(input())
    content = read_filetext(file_path)
    os.system('cls||clear')
    if(user_input==1):
        total_paragraph, total_words, total_unique_words, total_char, total_char_b = wpc_total(content)
        print("Estadisticas del Texto "+filename_list[i-1]+":")
        print("Total de Parrafos: "+str(total_paragraph))
        print("Total de Palabras: "+str(total_words))
        print("Total de Palabras Unicas: "+str(total_unique_words))
        print("Total de Caracteres: "+str(total_char))
        print("Total de Caracteres (Sin Espacio): "+str(total_char_b))
    elif(user_input==2):
        print(content)
    elif(user_input==4):
        s_find = pre_replacing_process(False, content)
    elif(user_input==5):
        s_find = pre_replacing_process(True, content)
    if(user_input!=0):
        input("Presione Enter para volver al menu")
    
        

    
