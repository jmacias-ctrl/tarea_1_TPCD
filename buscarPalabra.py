textoArchivo = "textos_entrada/En_el_Mar_Remoto.txt"

with open(textoArchivo, "r", encoding="UTF-8") as textoEntrada:
    contenidoTexto = textoEntrada.read()
    contenidoTexto1 = contenidoTexto.lower()

    signos = ['.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '"', "'","«"]
    for signo in signos:
        contenidoTexto1 = contenidoTexto1.replace(signo, ' ')
        contenidoTexto = contenidoTexto.replace(signo, ' ')

    palabraBuscar = input("Escriba la palabra que desea buscar: ")
    cantidadPalabrasSinDistincion = contenidoTexto1.split().count(palabraBuscar)
    cantidadPalabrasConDistincion = contenidoTexto.split().count(palabraBuscar)

    if palabraBuscar in contenidoTexto.split():
        print("La cantidad de veces que se repite la palabra sin distinción es:", cantidadPalabrasSinDistincion)
        print("La cantidad de veces que se repite la palabra con distinción es:", cantidadPalabrasConDistincion)
    else:
        print("La palabra no se encuentra en el texto.")