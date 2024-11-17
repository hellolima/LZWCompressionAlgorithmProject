class NoTrie:
    def __init__(self):
        self.descendentes = [None] * 2  #somente dois filhos, nossos textos serão binários
        self.prefixo = ""               #armazena o prefixo do nó 
        self.codigo = None              #guarda o código associado

class TrieCompacta:
    def __init__(self):
        self.raiz = NoTrie()  #começamos a árvore pela raiz que é vazia
        self.tamanho = 0

    def inserir(self, string, codigo):
        noAtual = self.raiz
        i = 0  #índice para o caractere atual de 'string'
        
        #caminha pela trie para inserir o novo prefixo enquanto houver caracteres
        while i < len(string):
            #encontra o próximo índice de descendente (0 ou 1)
            indice = int(string[i])
            
            if noAtual.descendentes[indice] is None: #trie vazia ou não há nenhum prefixo a ser compartilhado
                #novo nó com o restante do prefixo da string
                novoNo = NoTrie()
                novoNo.prefixo = string[i:]
                novoNo.codigo = codigo
                noAtual.descendentes[indice] = novoNo
                self.tamanho += 1
                return
            
            #verifica o prefixo comum entre a string e nó existente
            proximoNo = noAtual.descendentes[indice]
            j = 0
            while j < len(proximoNo.prefixo) and i < len(string) - 1 and proximoNo.prefixo[j] == string[i]:
                i += 1
                j += 1
            
            if j == len(proximoNo.prefixo):
                #continua caminhando na trie
                noAtual = proximoNo
            else:
                #divide o nó existente e insere o novo
                novoNoInterno = NoTrie()
                novoNoInterno.prefixo = proximoNo.prefixo[:j] #até o prefixo compartilhado
                noAtual.descendentes[indice] = novoNoInterno
                
                #ajusta o nó existente com o sufixo restante
                proximoNo.prefixo = proximoNo.prefixo[j:]
                novoNoInterno.descendentes[int(proximoNo.prefixo[0])] = proximoNo
                
                #adiciona o novo nó com o sufixo restante da string
                novoNoFolha = NoTrie()
                novoNoFolha.prefixo = string[i:]
                novoNoFolha.codigo = codigo
                #print('posicao que estou tentando acessar = ', i, 'com conteudo: ', string[i], "e a string tem tamanho: ", len(string))
                novoNoInterno.descendentes[int(string[i])] = novoNoFolha
                self.tamanho += 1
                return

        if noAtual.codigo is not None: #encontrou exatamente a mesma string e já tem codigo associado, ignora
            return
        
        self.tamanho += 1
        noAtual.codigo = codigo

    def buscarString(self, string): #realiza uma busca na trie pela string
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

    def buscarCodigo(self, codigo):
        # Função auxiliar que realiza a busca recursivamente
        def buscarNo(noAtual, prefixoAtual):
            if noAtual is None:
                return None

            # Verifica se o nó atual tem o código procurado
            if noAtual.codigo == codigo:
                return prefixoAtual + noAtual.prefixo

            # Continua a busca nos descendentes (0 ou 1)
            for i in range(2):
                if noAtual.descendentes[i] is not None:
                    resultado = buscarNo(noAtual.descendentes[i], prefixoAtual + noAtual.prefixo)
                    if resultado:
                        return resultado

            return None

        # Inicia a busca a partir da raiz
        return buscarNo(self.raiz, "")


    def remover(self, string):
        def removerAux(noAtual, string, i):
            if noAtual is None:
                return False  #não há nada para remover

            #fim da recursao, chegou no final da string e ao nó
            if i == len(string):
                if noAtual.codigo is not None:
                    noAtual.codigo = None  #remove o codigo
                    self.tamanho -= 1

                    #verifica se não tem filhos
                    if all(filho is None for filho in noAtual.descendentes):
                        return True  #indica que o nó pode ser removido, não tem descendentes
                    return False  #nó não pode ser removido

                return False  #a string não tem código associado

            #continua na árvore com o próximo caractere da string se não tiver chegado ao final
            indice = int(string[i])
            proximoNo = noAtual.descendentes[indice]
            if proximoNo is None:
                return False  #não encontrou a string para remover

            #chamando recursivamente para o próximo nó
            if removerAux(proximoNo, string, i + len(proximoNo.prefixo)):
                noAtual.descendentes[indice] = None  #remove o ponteiro para o nó

                #verifica se o nó atual pode ser compactado
                filhos = [filho for filho in noAtual.descendentes if filho is not None]
                if len(filhos) == 1 and noAtual.codigo is None:
                    #compacta o nó atual com seu único filho
                    filho = filhos[0]
                    noAtual.prefixo += filho.prefixo
                    noAtual.codigo = filho.codigo
                    noAtual.descendentes = filho.descendentes

                #retorna True se o nó atual ainda pode ser removido
                return all(child is None for child in noAtual.descendentes) and noAtual.codigo is None

            return False  # o nó não pode ser removido

        #funcao auxiliar que se inicia na raiz com indice 0
        removerAux(self.raiz, string, 0)
        
    def imprimir(self):
        def imprimirNo(no, nivel=0):
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
                print(f"{indentacao}  Ramos: {', '.join(filhos)}")

            if no.descendentes[0] is not None:
                print(f"{indentacao}  Ramo à esquerda (0):")
                imprimirNo(no.descendentes[0], nivel + 1)
            if no.descendentes[1] is not None:
                print(f"{indentacao}  Ramo à direita (1):")
                imprimirNo(no.descendentes[1], nivel + 1)
        imprimirNo(self.raiz)

    def getTamanho(self):
        return self.tamanho