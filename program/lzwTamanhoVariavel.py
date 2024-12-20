import time
from trieCompacta import *

class lzwTamanhoVariavel:
    def __init__(self, maxBits):
        self.dicionario = TrieCompacta()
        self.tamanhoMaxCodigos = maxBits
        self.tamanhoAtual = 9  # inicialmente 9 bits
        self.quantidadeMaxCodigos = pow(2, self.tamanhoMaxCodigos)
        self.iniciarDicionario()
        
        # Estatísticas
        self.totalOriginalBytes = 0  
        self.totalCodificadosBits = 0  
        self.totalLidosBits = 0  
        self.totalEspacoDicionario = (256 * 64)  + (256 * 9)
        self.tempoExecucaoCodificar = 0  
        self.tempoExecucaoDecodificar = 0  

        self.taxaCompressao = []  
        self.tiposCodificacao = []  
        self.taxaDescompressao = [] 
        self.tiposDescompressao = []  

    def iniciarDicionario(self):
        for i in range(256):
            representacaoBinaria = format(i, '09b')
            self.dicionario.inserir(representacaoBinaria, i)

    def codificar(self, texto):
        start_time = time.time()  
        codificacoes = []
        prefixo = ''
        codigosInseridos = 256  
        self.totalOriginalBytes = len(texto)  

        for i, caractere in enumerate(texto):
            self.totalLidosBits += self.tamanhoAtual  
            novoPrefixo = prefixo + caractere
            codigo = self.dicionario.buscarString(novoPrefixo)
            
            if codigo is not None:  # já está no dicionário
                prefixo = novoPrefixo
            else:
                codigoPrefixo = self.dicionario.buscarString(prefixo)
                codificacoes.append(format(codigoPrefixo, f'0{self.tamanhoAtual}b'))
                self.totalCodificadosBits += self.tamanhoAtual  

                if self.dicionario.getTamanho() < self.quantidadeMaxCodigos:
                    self.dicionario.inserir(novoPrefixo, codigosInseridos)
                    self.totalEspacoDicionario += 64 + len(novoPrefixo)
                    codigosInseridos += 1

                    if codigosInseridos >= pow(2, self.tamanhoAtual) and self.tamanhoAtual < self.tamanhoMaxCodigos:
                        self.tamanhoAtual += 1

                prefixo = caractere

            taxaCompressao = (1 - (self.totalCodificadosBits / 8) / (self.totalLidosBits / 8) ) * 100 # queremos esse numero menor que 1 (na verdade que 100, pois estamos pegando %)
            self.taxaCompressao.append(taxaCompressao)
            self.tiposCodificacao.append(i + 1)

        if prefixo:
            codigoPrefixo = self.dicionario.buscarString(prefixo)
            codificacoes.append(format(codigoPrefixo, f'0{self.tamanhoAtual}b'))
            self.totalCodificadosBits += self.tamanhoAtual

        self.tempoExecucaoCodificar = time.time() - start_time  

        return codificacoes

    def decodificar(self, codificacao):
        prefixoAnterior = ''
        sequenciaCodigo = ''
        resultado = []
        novoCodigo = 256
        
        self.totalOriginalBytes = len(codificacao) / 8
        momentosDescompressao = 1
        self.totalLidosBits = len(codificacao) 
        
        cW = codificacao[:self.tamanhoAtual]  
        codificacao = codificacao[self.tamanhoAtual:]  
        sequenciaCodigo = self.dicionario.buscarCodigo(int(''.join(cW), 2))
        resultado.append(sequenciaCodigo)
        
        prefixo = sequenciaCodigo
        self.totalCodificadosBits += 9
        
        while codificacao:
            self.totalLidosBits += self.tamanhoAtual
            cW = codificacao[:self.tamanhoAtual]  
            codificacao = codificacao[self.tamanhoAtual:]  
            
            sequenciaCodigo = self.dicionario.buscarCodigo(int(''.join(cW), 2))

            if sequenciaCodigo is not None:
                resultado.append(sequenciaCodigo)
                prefixoAnterior = prefixo
                sufixo = sequenciaCodigo[:self.tamanhoAtual]
                novaString = prefixoAnterior + sufixo
                self.dicionario.inserir(novaString, novoCodigo)
                self.totalCodificadosBits += self.tamanhoAtual
                novoCodigo += 1
            else:
                prefixoAnterior = prefixo
                sufixo = prefixo[:self.tamanhoAtual]
                novaString = prefixoAnterior + sufixo
                resultado.append(novaString)
                self.dicionario.inserir(novaString, novoCodigo)
                self.totalCodificadosBits += self.tamanhoAtual
                novoCodigo += 1

            if sequenciaCodigo is not None:
                prefixo = sequenciaCodigo

            if novoCodigo >= pow(2, self.tamanhoAtual) and self.tamanhoAtual < self.tamanhoMaxCodigos:
                self.tamanhoAtual += 1

            taxaCompressao = (1 - ((self.totalLidosBits / 8) / (self.totalCodificadosBits / 8) )) * 100
            self.taxaDescompressao.append(taxaCompressao)  
            momentosDescompressao += 1
            self.tiposDescompressao.append(momentosDescompressao)
            
        return ''.join(resultado)
