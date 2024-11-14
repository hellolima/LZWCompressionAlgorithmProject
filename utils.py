def converterTextoBinario12bits(texto):
    return [format(ord(caractere), '012b') for caractere in texto]
