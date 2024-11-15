from trieCompacta import *  
from lzwTamanhoFixo import *  
from utils import *  

instanciaCodificacao = lzwTamanhoFixo()

with open('entrada.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

binarioTexto = converterTextoBinario12bits(texto)

codigos = instanciaCodificacao.codificar(binarioTexto)

with open('codificacao.txt', 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(''.join(map(str, codigos)))

print("Códigos gravados com sucesso no arquivo 'codificacao.txt'.")

instanciaDecodificacao = lzwTamanhoFixo()

sequenciaCodificada = []

with open('codificacao.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        for i in range(0, len(linha), 12):
            bloco = linha[i:i+12]  
            numero = int(bloco, 2)
            sequenciaCodificada.append(numero)
            
sequenciaDecodificada = instanciaDecodificacao.decodificar(sequenciaCodificada)

with open('saidaDecodificada.txt', 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(''.join(sequenciaDecodificada))

print("Arquivo com a sequência decodificada gravado com sucesso em 'saidaDecodificada.txt'.")