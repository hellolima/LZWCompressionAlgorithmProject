import matplotlib.pyplot as plt
from lzwTamanhoFixo import *

def gerarRelatorio(instancia):
    # calcular a taxa de compressão final
    taxaCompressaoFinal = (1 - ((instancia.totalCodificadosBits / 8) / instancia.totalOriginalBytes)) * 100
    
    relatorio = [
        "===================== Relatório de Compressão LZW =====================",
        f"Tamanho do Texto Original (em bytes): {instancia.totalOriginalBytes:.2f}",
        f"Tamanho do Texto Codificado (em bytes): {instancia.totalCodificadosBits / 8:.2f}",
        f"Taxa de Compressão Final: {taxaCompressaoFinal:.2f}%",
        f"Quantidade de códigos no dicionário: {instancia.totalEntradasDicionario}",
        f"Tempo de Execução da Codificação: {instancia.tempoExecucaoCodificar:.4f} segundos",
        "======================================================================="
    ]
    
    with open("relatorio.txt", "w") as arquivo:
        arquivo.write("\n".join(relatorio))
   
    plt.figure(figsize=(10, 6))
    plt.plot(instancia.tiposCodificacao, instancia.taxaCompressao, label='Taxa de Compressão', color='g')
    plt.xlabel('Passo da Codificação')
    plt.ylabel('% Taxa de Compressão (bytes codificado / bytes lidos)')
    plt.title('Taxa de Compressão ao Longo do Processo')
    plt.legend()
    
    plt.savefig('taxaCompressaoAoLongoProcessamento.png', format='png')
    
