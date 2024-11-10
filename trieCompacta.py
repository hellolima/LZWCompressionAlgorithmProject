class NoTrie:
    def __init__(self):
        self.descendentes = [None] * 2  #somente dois filhos, nossos textos serão binários
        self.prefixo = ""               #armazena o prefixo do nó 
        self.codigo = None              #guarda o código associado

class TrieCompacta:
    def __init__(self):
        self.raiz = NoTrie()  #começamos a árvore pela raiz que é vazia

    def inserir(self, string, codigo):
        noAtual = self.raiz
        i = 0  #índice para o caractere atual de 'string'
        
        #caminha pela trie para inserir o novo prefixo
        while i < len(string):
            #encontra o próximo índice de descendente (0 ou 1)
            indice = int(string[i])
            
            if noAtual.descendentes[indice] is None:
                #novo nó com o restante do prefixo da string
                novoNo = NoTrie()
                novoNo.prefixo = string[i:]
                novoNo.codigo = codigo
                noAtual.descendentes[indice] = novoNo
                return
            
            #verifica o prefixo comum entre a string e nó existente
            proximoNo = noAtual.descendentes[indice]
            j = 0
            while j < len(proximoNo.prefixo) and i < len(string) and proximoNo.prefixo[j] == string[i]:
                i += 1
                j += 1
            
            if j == len(proximoNo.prefixo):
                #continua caminhando na trie
                noAtual = proximoNo
            else:
                #divide o nó existente e insere o novo
                novoNoInterno = NoTrie()
                novoNoInterno.prefixo = proximoNo.prefixo[:j]
                noAtual.descendentes[indice] = novoNoInterno
                
                #ajusta o nó existente com o sufixo restante
                proximoNo.prefixo = proximoNo.prefixo[j:]
                novoNoInterno.descendentes[int(proximoNo.prefixo[0])] = proximoNo
                
                #adiciona o novo nó com o sufixo restante da string
                novoNoFolha = NoTrie()
                novoNoFolha.prefixo = string[i:]
                novoNoFolha.codigo = codigo
                novoNoInterno.descendentes[int(string[i])] = novoNoFolha
                return

        if noAtual.codigo is not None: #encontrou exatamente a mesma string, ignora
            return
        
        noAtual.codigo = codigo

    def buscar(self, string): #realiza uma busca na trie pela string
        noAtual = self.raiz
        i = 0
        
        #caminha na Trie acumulando o prefixo
        while i < len(string):
            indice = int(string[i])
            if noAtual.descendentes[indice] is None:
                return None  #não encontrado
            
            noAtual = noAtual.descendentes[indice]
            j = 0
            while j < len(noAtual.prefixo) and i < len(string) and noAtual.prefixo[j] == string[i]:
                i += 1
                j += 1
            
            if j < len(noAtual.prefixo):
                return None  #prefixo diverge, não encontrado
        
        #retorna o código se encontrou a string (talvez mudar esse retorno)
        return noAtual.codigo if noAtual.codigo is not None else None

    
    def imprimir_trie(self):
        def imprimir_no(no, nivel=0):
            if no is None:
                return

            indentacao = "  " * nivel

            if no.codigo is not None:
                print(f"{indentacao}Nó - Prefixo: '{no.prefixo}', Código: {no.codigo}")
            else:
                print(f"{indentacao}Nó - Prefixo: '{no.prefixo}', Código: None")

            filhos = []
            if no.descendentes[0] is not None:
                filhos.append("Esquerda (0)")
            if no.descendentes[1] is not None:
                filhos.append("Direita (1)")

            if filhos:
                print(f"{indentacao}  Filhos: {', '.join(filhos)}")

            if no.descendentes[0] is not None:
                print(f"{indentacao}  Filho à esquerda (0):")
                imprimir_no(no.descendentes[0], nivel + 1)
            if no.descendentes[1] is not None:
                print(f"{indentacao}  Filho à direita (1):")
                imprimir_no(no.descendentes[1], nivel + 1)

        print("Estrutura da Trie Compacta:")
        imprimir_no(self.raiz)
