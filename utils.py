def converterTextoBinario12bits(texto):
    return [format(ord(caractere), '012b') for caractere in texto]


def converterParaASCII(texto):
    return [ord(c) for c in texto]