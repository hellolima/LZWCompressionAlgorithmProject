from trieCompacta import *

class lzwTamanhoFixo:
    def __init__(self):
        self.dicionario = TrieCompacta()
        self.quantidadeMaxCodigos = pow(2, 12) #limitando a 4096 codigos
        self.iniciarDicionario() 
        
    def iniciarDicionario(self):
        for i in range(256):
            representacaoBinaria = format(i, '012b')
            self.dicionario.inserir(representacaoBinaria, i)
            
    def codificar(self, texto):
        codificacoes = []
        prefixo = ''
        
        for caractere in texto:
            novoPrefixo = prefixo + caractere

            codigo = self.dicionario.buscarString(novoPrefixo)
            
            if codigo is not None: 
                prefixo = novoPrefixo
            else:
                codigoPrefixo = self.dicionario.buscarString(prefixo)
                codificacoes.append(format(codigoPrefixo, '012b'))

                if self.dicionario.getTamanho() < self.quantidadeMaxCodigos:
                    self.dicionario.inserir(novoPrefixo, self.dicionario.getTamanho())
                
                else:
                    pass #simplesmente para de adicionar
                
                prefixo = caractere
        
        if prefixo:
            codigoPrefixo = self.dicionario.buscarString(prefixo)
            codificacoes.append(format(codigoPrefixo, '012b'))
        
        return codificacoes 

    
    def decodificar(self, codificacao): #codificacao é uma lista com todos os codigos
        prefixoAnterior = ''
        sufixo = ''
        sequenciaCodigo = ''
        prefixo = ''
        resultado = []
        novoCodigo = 256
        
        cW = codificacao.pop(0) #isso sempre sera uma raiz. cW = primeiro codigo da lista
        sequenciaCodigo = self.dicionario.buscarCodigo(cW)
        resultado.append(sequenciaCodigo)
        
        prefixo = sequenciaCodigo
        for cW in codificacao:
            if self.dicionario.buscarCodigo(cW) is not None:#significa que essa string ja esta no diiconario
                sequenciaCodigo = self.dicionario.buscarCodigo(cW)
                resultado.append(sequenciaCodigo)
                prefixoAnterior = prefixo
                sufixo = sequenciaCodigo[:12] #lembrar que quando o arquivo base fala "primeiro caracter da string cw" estamos querendo os primeiros 12 bits.
                novaString = prefixoAnterior + sufixo
                self.dicionario.inserir(novaString, novoCodigo)
                novoCodigo += 1
            else:
                prefixoAnterior = prefixo
                sufixo = prefixo[:12]
                
                novaString = prefixoAnterior + sufixo
                resultado.append(novaString)
                self.dicionario.inserir(novaString, novoCodigo)
                novoCodigo += 1
                
            prefixo = sequenciaCodigo
        
        return ''.join(resultado)