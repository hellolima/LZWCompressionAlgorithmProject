from trieCompacta import *

trie = TrieCompacta()
trie.inserir("101", 1)
trie.inserir("1001", 2)
trie.inserir("111", 3)
trie.inserir("00", 4)

trie.imprimir_trie()
print("*" * 10)
trie.remover('101')
trie.imprimir_trie()