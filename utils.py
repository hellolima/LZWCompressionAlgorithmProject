from bitstring import BitArray
from PIL import Image

def converterTextoBinario12bits(texto):
    return [format(ord(caractere), '012b') for caractere in texto]


def converterTextoBinario9bits(texto):
    return [format(ord(caractere), '09b') for caractere in texto]


def gravarEmBinario(codigos, arquivoSaida):
    print('entrou para gravar em bianrio')
    # junta todos os códigos do vetor em uma única string binária
    stringBinaria = ''.join(codigos)
    
    with open(arquivoSaida, 'wb') as binary_file:
        b = BitArray(bin=stringBinaria)
        b.tofile(binary_file)

    b = BitArray(filename=arquivoSaida)
    
    
    
def lerArquivoBinarioFixo(arquivoEntrada): # 12 em 12 bits
    b = BitArray(filename=arquivoEntrada)
    
    stringBinaria = b.bin
    
    tamanho_do_codigo = 12
    codigos = [int(stringBinaria[i:i+tamanho_do_codigo], 2) for i in range(0, len(stringBinaria), tamanho_do_codigo)]
    
    return codigos

def lerArquivoBinarioVariavel(arquivoEntrada):
    b = BitArray(filename=arquivoEntrada)
    
    stringBinaria = b.bin
    
    vetorBits = stringBinaria  # mantém a string inteira como uma única posição
    
    return vetorBits

def lerBitmapFixo(arquivoEntrada):
    print('entrou aqui')
    imagem = Image.open(arquivoEntrada)
    imagem = imagem.convert('RGB')
    
    binario = ''
    for pixel in imagem.getdata():
        binario += ''.join(format(canal, '012b') for canal in pixel)
    
    return binario

def lerBitmapVariavel(arquivoEntrada):
    imagem = Image.open(arquivoEntrada)
    imagem = imagem.convert('RGB')
    
    binario = ''
    for pixel in imagem.getdata():
        binario += ''.join(format(canal, '09b') for canal in pixel)
    
    return binario
