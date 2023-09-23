def contador_letra(string, letra):
    contador = 0
    for caracter in string:
        if caracter.lower() == letra.lower():
            contador += 1
    return contador

mi_string = "Hola, yo soy alba cristina, tengo sueño, estoy cansada"
mi_letra = "i"
resultado = contador_letra(mi_string, mi_letra)
print(f"La letra '{mi_letra}' aparece {resultado} veces en mi string")
