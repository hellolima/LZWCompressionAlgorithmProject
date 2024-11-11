from trieCompacta import *
from lzwTamanhoFixo import *


instanciaSolucao1 = lzwTamanhoFixo()

print(instanciaSolucao1.dicionario.getTamanho())

print(instanciaSolucao1.dicionario.buscar('00000000'))