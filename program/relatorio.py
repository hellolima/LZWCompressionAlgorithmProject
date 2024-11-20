import os
import matplotlib.pyplot as plt
from lzwTamanhoFixo import *

def gerarRelatorioCompressao(instancia):
    # Calcular a taxa de compressão final
    taxaCompressaoFinal = (1 - ((instancia.totalCodificadosBits / 8) / instancia.totalOriginalBytes)) * 100
    
    # Cria o diretório "estatisticas" caso ele não exista
    if not os.path.exists('estatisticas'):
        os.makedirs('estatisticas')
    
    # Relatório de compressão
    relatorio = [
        "===================== Relatório de Compressão LZW =====================",
        f"Tamanho do Texto Original (em bytes): {instancia.totalOriginalBytes:.2f}",
        f"Tamanho do Texto Codificado (em bytes): {instancia.totalCodificadosBits / 8:.2f}",
        f"Taxa de Compressão Final: {taxaCompressaoFinal:.2f}%",
        f"Quantidade de códigos no dicionário: {instancia.dicionario.getTamanho()}",
        f"Quantidade de memória utilizada no dicionário (em bytes): {instancia.totalEspacoDicionario/8}",
        f"Tempo de Execução da Codificação: {instancia.tempoExecucaoCodificar:.4f} segundos",
        "======================================================================="
    ]
    
    # Salvar o relatório na pasta 'estatisticas'
    with open('estatisticas/relatorio.txt', 'w') as arquivo:
        arquivo.write("\n".join(relatorio))
    
    # Criar o gráfico da taxa de compressão
    plt.figure(figsize=(10, 6))
    plt.plot(instancia.tiposCodificacao, instancia.taxaCompressao, label='Taxa de Compressão', color='g')
    plt.xlabel('Passo da Codificação')
    plt.ylabel('% Taxa de Compressão (bytes codificado / bytes lidos)')
    plt.title('Taxa de Compressão ao Longo do Processo')
    plt.legend()
    
    # Salvar o gráfico na pasta 'estatisticas'
    plt.savefig('estatisticas/taxaCompressaoAoLongoProcessamento.png', format='png')

def gerarRelatorioDescompressao(instancia):
    # Calcular a taxa de descompressão final
    taxaDescompressaoFinal = (1 - ((instancia.totalCodificadosBits / 8) / instancia.totalOriginalBytes)) * 100
    
    # Cria o diretório "estatisticas" caso ele não exista
    if not os.path.exists('estatisticas'):
        os.makedirs('estatisticas')
    
    # Relatório de descompressão
    relatorio = [
        "===================== Relatório de Descompressão LZW =====================",
        f"Tamanho do Texto Original (em bytes): {instancia.totalOriginalBytes:.2f}",
        f"Tamanho do Texto Descodificado (em bytes): {instancia.totalCodificadosBits / 8:.2f}",
        f"Taxa de Descompressão Final: {taxaDescompressaoFinal:.2f}%",
        f"Quantidade de códigos no dicionário: {instancia.dicionario.getTamanho()}",
        f"Quantidade de memória utilizada no dicionário (em bytes): {instancia.totalEspacoDicionario/8}",
        f"Tempo de Execução da Descodificação: {instancia.tempoExecucaoDecodificar:.4f} segundos",
        "======================================================================="
    ]
    
    # Salvar o relatório na pasta 'estatisticas'
    with open('estatisticas/relatorio_descompressao.txt', 'w') as arquivo:
        arquivo.write("\n".join(relatorio))
    
    # Criar o gráfico da taxa de descompressão
    plt.figure(figsize=(10, 6))
    plt.plot(instancia.tiposDescompressao, instancia.taxaDescompressao, label='Taxa de Descompressão', color='b')
    plt.xlabel('Passo da Descompressão')
    plt.ylabel('% Taxa de Descompressão (bytes codificado / bytes lidos)')
    plt.title('Taxa de Descompressão ao Longo do Processo')
    plt.legend()
    
    # Salvar o gráfico na pasta 'estatisticas'
    plt.savefig('estatisticas/taxaDescompressaoAoLongoProcessamento.png', format='png')