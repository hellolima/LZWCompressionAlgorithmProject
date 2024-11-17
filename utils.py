def converterTextoBinario12bits(texto):
    return [format(ord(caractere), '012b') for caractere in texto]


def converterTextoBinario9bits(texto):
    return [format(ord(caractere), '09b') for caractere in texto]