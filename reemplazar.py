textoArchivo = "textos_entrada/En_el_Mar_Remoto.txt"

with open(textoArchivo, "r", encoding="UTF-8") as textoEntrada:
    content = textoEntrada.read()

palabraBuscar = input("Escriba la palabra que desea cambiar: ")
palabraReemplazar = input("Escriba la nueva palabra: ")


conDistincion = input("¿Desea que la búsqueda distinga mayusculas de minusculas? (S/N): ")
conDistincion = conDistincion.upper() == "S"

words = content.split()
new_words = [palabraReemplazar if (word == palabraBuscar and conDistincion) or (word.lower() == palabraBuscar.lower() and not conDistincion) else word for word in words]
new_content = " ".join(new_words)

with open(textoArchivo, "w", encoding="UTF-8") as TextoSalida:
    TextoSalida.write(new_content)


with open(textoArchivo, "r", encoding="UTF-8") as TextoSalida:
    textoModificado = TextoSalida.read()

print(textoModificado)