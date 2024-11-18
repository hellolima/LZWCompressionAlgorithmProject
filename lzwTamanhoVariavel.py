from trieCompacta import *

class lzwTamanhoVariavel:
    def __init__(self, maxBits):
        self.dicionario = TrieCompacta()
        self.tamanhoMaxCodigos = maxBits
        self.tamanhoAtual = 9 # inicialmente 9 bits
        self.quantidadeMaxCodigos = pow(2, self.tamanhoMaxCodigos) 
        self.iniciarDicionario()

    def iniciarDicionario(self):
        # inicia com a tabela ASCII com codigos de 9 bits
        for i in range(256):
            representacaoBinaria = format(i, '09b') 
            self.dicionario.inserir(representacaoBinaria, i)
    
    def codificar(self, texto):
        codificacoes = []
        prefixo = ''
        codigosInseridos = 256 # começa a partir do codigo 256
        for caractere in texto:
            novoPrefixo = prefixo + caractere
            codigo = self.dicionario.buscarString(novoPrefixo)
            
            if codigo is not None: # ja esta

                prefixo = novoPrefixo
            else:
                codigoPrefixo = self.dicionario.buscarString(prefixo)
                codificacoes.append(format(codigoPrefixo, f'0{self.tamanhoAtual}b'))

                if self.dicionario.getTamanho() < self.quantidadeMaxCodigos:
                    self.dicionario.inserir(novoPrefixo, codigosInseridos)
                    codigosInseridos += 1

                    # se o número de códigos for maior que o limite atual, aumente o tamanho de bits em 1
                    if codigosInseridos >= pow(2, self.tamanhoAtual) and self.tamanhoAtual < self.tamanhoMaxCodigos:
                        self.tamanhoAtual += 1

                prefixo = caractere
        
        if prefixo:
            codigoPrefixo = self.dicionario.buscarString(prefixo)
            codificacoes.append(format(codigoPrefixo, f'0{self.tamanhoAtual}b'))
        
        return codificacoes

    def decodificar(self, codificacao):
        prefixoAnterior = ''
        sequenciaCodigo = ''
        resultado = []
        novoCodigo = 256

        
        cW = codificacao[:self.tamanhoAtual]  # pegando os primeiros 9 caracteres
        codificacao = codificacao[self.tamanhoAtual:]  # remover os primeiros 9 caracteres da codificação

        sequenciaCodigo = self.dicionario.buscarCodigo(int(''.join(cW), 2))  
        resultado.append(sequenciaCodigo)
        
        prefixo = sequenciaCodigo

        while codificacao:  
            cW = codificacao[:self.tamanhoAtual]  
            codificacao = codificacao[self.tamanhoAtual:]  
            
            sequenciaCodigo = self.dicionario.buscarCodigo(int(''.join(cW), 2))
           
            if sequenciaCodigo is not None:
                resultado.append(sequenciaCodigo)
                prefixoAnterior = prefixo
                
                sufixo = sequenciaCodigo[:self.tamanhoAtual]
                novaString = prefixoAnterior + sufixo
                self.dicionario.inserir(novaString, novoCodigo)
                novoCodigo += 1
            else:
                prefixoAnterior = prefixo
                sufixo = prefixo[:self.tamanhoAtual]
                
                novaString = prefixoAnterior + sufixo
                resultado.append(novaString)
                self.dicionario.inserir(novaString, novoCodigo)
                novoCodigo += 1
            
            if sequenciaCodigo is not None:
                prefixo = sequenciaCodigo

            # verifica se é necessário aumentar o tamanho do código
            if novoCodigo >= pow(2, self.tamanhoAtual) and self.tamanhoAtual < self.tamanhoMaxCodigos:
                self.tamanhoAtual += 1

        return ''.join(resultado)
