import argparse
from trieCompacta import *
from lzwTamanhoFixo import *
from lzwTamanhoVariavel import *
from utils import *


def main():
    parser = argparse.ArgumentParser(description="Codificação e Decodificação com LZW")
    
    parser.add_argument('operacao', choices=['codificar', 'decodificar'], help="Escolha a operação (codificar ou decodificar)")
    parser.add_argument('arquivoEntrada', help="Nome do arquivo de entrada (texto para codificação ou codificação para decodificação)")
    parser.add_argument('arquivoSaida', help="Nome do arquivo de saída (codificação ou decodificação)")
    parser.add_argument('tipoLzw', choices=['fixo', 'variavel'], default='fixo', help="Tipo de LZW (fixo ou variável)")
    parser.add_argument('--bits', type=int, default=12, help="Quantidade máxima de bits (padrão: 12)") # bits é opcional

    args = parser.parse_args()

    if args.tipoLzw == 'fixo':
        instanciaSolucao1 = lzwTamanhoFixo()
        
        if args.operacao == 'codificar':
            with open(args.arquivoEntrada, 'r', encoding='utf-8') as arquivo:
                texto = arquivo.read()
            
            binarioTexto = converterTextoBinario12bits(texto)
            codigos = instanciaSolucao1.codificar(binarioTexto) # listas com codigos de 12 bits
            
            gravarEmBinario(codigos, args.arquivoSaida)

        elif args.operacao == 'decodificar':
            sequenciaCodificada = lerArquivoBinarioFixo(args.arquivoEntrada)
            
            sequenciaDecodificada = instanciaSolucao1.decodificar(sequenciaCodificada)
            
            with open(args.arquivoSaida, 'w', encoding='utf-8') as arquivoSaida:
                arquivoSaida.write(''.join(sequenciaDecodificada))
            
            print(f"Arquivo com a sequência decodificada gravado com sucesso em '{args.arquivoSaida}'.")
            
    elif args.tipoLzw == 'variavel':
        
        maxBits = args.bits if args.bits else 12
        
        instanciaSolucao2 = lzwTamanhoVariavel(maxBits)
        
        if args.operacao == 'codificar':
            with open(args.arquivoEntrada, 'r', encoding='utf-8') as arquivo:
                texto = arquivo.read()
            
            binarioTexto = converterTextoBinario9bits(texto) 
            codigos = instanciaSolucao2.codificar(binarioTexto) # cada bloco em uma posicao
            
            gravarEmBinario(codigos, args.arquivoSaida)

        elif args.operacao == 'decodificar':
            sequenciaCodificada = lerArquivoBinarioVariavel(args.arquivoEntrada)
            
            sequenciaDecodificada = instanciaSolucao2.decodificar(sequenciaCodificada)
            
            with open(args.arquivoSaida, 'w', encoding='utf-8') as arquivoSaida:
                arquivoSaida.write(''.join(sequenciaDecodificada))
            
            print(f"Arquivo com a sequência decodificada gravado com sucesso em '{args.arquivoSaida}'.")
    

if __name__ == "__main__":
    main()