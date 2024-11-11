from trieCompacta import *

class lzwTamanhoFixo:
    def __init__(self):
        self.dicionario = TrieCompacta()
        self.quantidadeMaxCodigos = pow(2, 12)
        self.iniciarDicionario()
        
    def iniciarDicionario(self):
        for i in range(256):
            representacaoBinaria = format(i, '08b')
            self.dicionario.inserir(representacaoBinaria, i)