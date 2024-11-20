# LZWCompressionAlgorithmProject

Este repositório contém a implementação do algoritmo LZW (Lempel-Ziv-Welch) para a codificação e decodificação de arquivos. A implementação oferece duas abordagens distintas: uma em que o número de bits utilizados para a codificação é fixo e outra em que o número de bits pode variar conforme a necessidade.

O dicionário utilizado foi implementado como uma Trie compacta, na qual os prefixos são associados a códigos, permitindo uma compressão eficiente.

Para uma documentação mais detalhada, incluindo explicações sobre escolhas de projeto e resultados obtidos, acesse a página [https://hellolima.github.io/LZWCompressionAlgorithmProject/](https://hellolima.github.io/LZWCompressionAlgorithmProject/).

## Máquina

O projeto foi implementado utilizando o sistema operacional **Pop_OS** e Python (versão 3.10.12).

## Como rodar o código

### 1. Clone o repositório

Primeiro, clone este repositório para a sua máquina:

```bash
git clone git@github.com:hellolima/LZWCompressionAlgorithmProject.git
```

### 2. Pré-requisitos

Para codificar, tenha um arquivo `entrada.txt` ou um arquivo `.bmp` no seu repositório.
Para decodificar, tenha um arquivo `codificacao.bin` no seu repositório.

### 3. Codificar arquivos

Usando a implementação fixa (onde o número de bits é fixado):

``` bash
python3 program/main.py codificar entrada.txt codificacao.bin fixo
```

Gerar relatório e gráfico de estatísticas:

``` bash
python3 program/main.py codificar entrada.txt codificacao.bin fixo --testes
```

Usando a implementação variável (onde o número de bits pode variar, aqui utilizamos limite máximo de 12 bits):

``` bash
python3 program/main.py codificar entrada.txt codificacao.bin variavel --bits 12
```
Gerar relatório e gráfico de estatísticas:

```bash
python3 program/main.py codificar entrada.txt codificacao.bin variavel --bits 12 --testes
```

Nota: Não é obrigatorio informar a quantidade máxima de bits. Caso não seja informada, o valor padrão será de 12 bits.


### 4. Decodificar arquivos

Usando a implementação fixa:

``` bash
python3 program/main.py decodificar codificacao.bin saidaDecodificada.txt fixo
```

Usando a implementação variável (com limite máximo de 12 bits):

```bash
python3 program/main.py decodificar codificacao.bin saidaDecodificada.txt variavel --bits 12
```

A flag testes também pode ser utilizada na decodificação.

### 5. Observações importantes

Decodificação: Um arquivo só pode ser decodificado utilizando a abordagem fixa se ele foi codificado utilizando a abordagem fixa. O mesmo vale para a abordagem variável.
Limite de bits: Caso esteja utilizando a abordagem variável, atente-se ao limite de bits informado, que deve ser o mesmo utilizado durante a codificação.
