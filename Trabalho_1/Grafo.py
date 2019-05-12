from collections import defaultdict 

class Grafo:
    def __init__(self, matriz, n):
        self.grafo = defaultdict(list)
        self.ouros = []
        self.bateriaInicial = n**1.5
        self.n = n
        aux = 0
        for x in matriz:
            auy = 0
            for y in x:
                if (y == '*' or y == '0'):
                    # Se for Ouro
                    if (y == '*'):
                        self.ouros.append((aux)+(n*auy))

                    # Se tiver caminho pra esquerda
                    if (auy > 0 and (matriz[aux][auy-1] == '0' or matriz[aux][auy-1] == '*')):
                        self.AddVertice(aux + (auy*n), aux + n*(auy-1))

                    # Se tiver caminho pra direita
                    if (auy < n-1 and (matriz[aux][auy+1] == '0' or matriz[aux][auy+1] == '*')):
                        self.AddVertice(aux + (auy*n), aux + n*(auy+1))

                    # Se tiver caminho pra cima
                    if (aux > 0 and (matriz[aux-1][auy] == '0' or matriz[aux-1][auy] == '*')):
                        self.AddVertice(aux + (auy*n), aux-1 + n*auy)

                    # Se tiver caminho pra baixo
                    if (aux < n-1 and (matriz[aux+1][auy] == '0' or matriz[aux+1][auy] == '*')):
                        self.AddVertice(aux + (auy*n), aux+1 + n*auy)
                        
                auy += 1
            aux += 1
    
    def AddVertice(self, u, v):
        self.grafo[u].append(v)

    def NOuros(self):
        return len(self.ouros)

    def PosDireita(self, pos):
        if pos + 8 in self.grafo[pos]:
            return pos+8
        return -1
    def PosEsquerda(self, pos):
        if pos - 8 in self.grafo[pos]:
            return pos-8
        return -1
    def PosCima(self, pos):
        if pos - 1 in self.grafo[pos]:
            return pos-1
        return -1
    def PosBaixo(self, pos):
        if pos + 1 in self.grafo[pos]:
            return pos+1
        return -1