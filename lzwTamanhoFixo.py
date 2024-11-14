from trieCompacta import *

class lzwTamanhoFixo:
    def __init__(self):
        self.dicionario = TrieCompacta()
        self.quantidadeMaxCodigos = pow(2, 12)
        self.iniciarDicionario()
        
    def iniciarDicionario(self):
        for i in range(256):
            representacaoBinaria = format(i, '012b')
            self.dicionario.inserir(representacaoBinaria, i)
            
    def codificar(self, texto):
        codigos_codificados = []
        prefixo = ''
        
        for caractere in texto:
            novo_prefixo = prefixo + caractere
            print("Novo prefixo: ", novo_prefixo)
    
            codigo = self.dicionario.buscar(novo_prefixo)
            print("Codigo que foi encontrado: ", codigo)
            
            if codigo is not None: 
                prefixo = novo_prefixo
                print("Prefixo: ", prefixo)
            else:
                codigo_prefixo = self.dicionario.buscar(prefixo)
                codigos_codificados.append(codigo_prefixo)

                if self.dicionario.getTamanho() < self.quantidadeMaxCodigos:
                    self.dicionario.inserir(novo_prefixo, self.dicionario.getTamanho())
                
                prefixo = caractere
        
        if prefixo:
            codigo_prefixo = self.dicionario.buscar(prefixo)
            codigos_codificados.append(codigo_prefixo)
        
        return codigos_codificados
