from trieCompacta import *
from lzwTamanhoFixo import *
from utils import *

instanciaSolucao1 = lzwTamanhoFixo()

with open('entrada.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    
binarioTexto = converterTextoBinario12bits(texto)

codigo = 0  # Código inicial para o primeiro prefixo, você pode ajustar conforme necessário
for string in binarioTexto:
    # Inserir na trie
    dicionario.inserir(string, codigo)
    codigo += 1  # Incrementa o código para o próximo prefixo

# Verificando o tamanho da trie após as inserções
print(f"Tamanho da trie após inserções: {dicionario.getTamanho()}")

# Opcional: Para testar a busca ou impressão da trie
dicionario.imprimir()
