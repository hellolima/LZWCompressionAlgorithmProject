from bitstring import BitArray

def converterTextoBinario12bits(texto):
    return [format(ord(caractere), '012b') for caractere in texto]


def converterTextoBinario9bits(texto):
    return [format(ord(caractere), '09b') for caractere in texto]


def gravarEmBinario(codigos, arquivoSaida):
    # junta todos os códigos do vetor em uma única string binária
    stringBinaria = ''.join(codigos)
    
    with open(arquivoSaida, 'wb') as binary_file:
        b = BitArray(bin=stringBinaria)
        b.tofile(binary_file)

    # Abre o arquivo binário para leitura e exibe os dados
    b = BitArray(filename=arquivoSaida)
    
    print(f"Arquivo binário gravado com sucesso em '{arquivoSaida}'.")
    
    
def lerArquivoBinarioFixo(arquivoEntrada): # 12 em 12 bits
    # Abre o arquivo binário para leitura
    b = BitArray(filename=arquivoEntrada)
    
    # Converte o conteúdo lido em uma string binária
    stringBinaria = b.bin
    
    # Dividir a string binária em segmentos de 12 bits e converter cada um para inteiro
    tamanho_do_codigo = 12
    codigos = [int(stringBinaria[i:i+tamanho_do_codigo], 2) for i in range(0, len(stringBinaria), tamanho_do_codigo)]
    
    return codigos

from bitstring import BitArray

def lerArquivoBinarioVariavel(arquivoEntrada):
    # Abre o arquivo binário para leitura
    b = BitArray(filename=arquivoEntrada)
    
    # Converte o conteúdo lido em uma string binária
    stringBinaria = b.bin
    
    # Armazenar o conteúdo binário como uma string contínua
    vetorBits = stringBinaria  # Mantém a string inteira como uma única posição
    
    return vetorBits


