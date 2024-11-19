# lzw.py

import time
import matplotlib.pyplot as plt
from trieCompacta import *

class lzwTamanhoFixo:
    def __init__(self):
        self.dicionario = TrieCompacta()
        self.quantidadeMaxCodigos = pow(2, 12)  # limitando a 4096 códigos
        self.iniciarDicionario()
        
        self.totalOriginalBytes = 0  
        self.totalCodificadosBits = 0  
        self.totalLidosBits = 0  
        self.totalEspacoDicionario = (256 * 64 ) + (256 * 12)
        self.tempoExecucaoCodificar = 0  
        self.tempoExecucaoDecodificar = 0  

        self.taxaCompressao = []  
        self.tiposCodificacao = [] 
        self.taxaDescompressao = []  # Lista para taxa de descompressão
        self.tiposDescompressao = []  # Lista para tipos de descompressão
     

    def iniciarDicionario(self):
        for i in range(256):
            representacaoBinaria = format(i, '012b')
            self.dicionario.inserir(representacaoBinaria, i)

    def codificar(self, texto):
        start_time = time.time()  
        codificacoes = []
        prefixo = ''
        
        self.totalOriginalBytes = len(texto)   

        for i, caractere in enumerate(texto):
            self.totalLidosBits += 12
            novoPrefixo = prefixo + caractere
            codigo = self.dicionario.buscarString(novoPrefixo)
            
            if codigo is not None: 
                prefixo = novoPrefixo
            else:
                codigoPrefixo = self.dicionario.buscarString(prefixo)
                codificacoes.append(format(codigoPrefixo, '012b'))
                self.totalCodificadosBits += 12  
                
                if self.dicionario.getTamanho() < self.quantidadeMaxCodigos:
                    self.dicionario.inserir(novoPrefixo, self.dicionario.getTamanho())
                    self.totalEspacoDicionario += 64 + len(novoPrefixo) # assumindo que cada inteiro ocupa 64 bits. Em python esse é o máximo. Também somamos os bits para representar o prefixo.
                prefixo = caractere

            taxaCompressao = (1 - (self.totalCodificadosBits / 8) / (self.totalLidosBits / 8) ) * 100 # queremos esse numero menor que 1 (na verdade que 100, pois estamos pegando %)
            self.taxaCompressao.append(taxaCompressao)
            self.tiposCodificacao.append(i + 1)
             

        if prefixo:
            codigoPrefixo = self.dicionario.buscarString(prefixo)
            codificacoes.append(format(codigoPrefixo, '012b'))
            self.totalCodificadosBits += 12
        
        self.tempoExecucaoCodificar = time.time() - start_time  
        
        return codificacoes 

    def decodificar(self, codificacao): 
        prefixoAnterior = ''
        sufixo = ''
        sequenciaCodigo = ''
        prefixo = ''
        resultado = []
        novoCodigo = 256
        
        cW = codificacao.pop(0)
        sequenciaCodigo = self.dicionario.buscarCodigo(cW)
        resultado.append(sequenciaCodigo)
        
        prefixo = sequenciaCodigo
        for cW in codificacao:
            if self.dicionario.buscarCodigo(cW) is not None:
                sequenciaCodigo = self.dicionario.buscarCodigo(cW)
                resultado.append(sequenciaCodigo)
                prefixoAnterior = prefixo
                sufixo = sequenciaCodigo[:12]
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
