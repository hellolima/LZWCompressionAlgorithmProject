from trieCompacta import *  
from lzwTamanhoFixo import *  
from utils import *  

instanciaSolucao1 = lzwTamanhoFixo()

with open('entrada.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

binarioTexto = converterTextoBinario12bits(texto)

codigos = instanciaSolucao1.codificar(binarioTexto)
print("Códigos Codificados:", codigos)

with open('codigosCodificados.txt', 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(' '.join(map(str, codigos)))

print("Códigos gravados com sucesso no arquivo 'codigosCodificados.txt'.")

asciiTexto = converterParaASCII(texto)
with open('entradaEmASCII.txt', 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(' '.join(map(str, asciiTexto)))

print("Arquivo com codificação ASCII gravado com sucesso em 'entradaEmASCII.txt'.")