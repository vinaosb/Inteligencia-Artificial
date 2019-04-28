from collections import defaultdict 

class Grafo:
    def __init__(self, matriz, n):
        self.grafo = defaultdict(list)
        self.ouros = []
        self.nouro = n/2
        self.bateriaInicial = n**1.5
        self.n = n
        aux = 0
        for x in matriz:
            auy = 0
            for y in x:
                if (y == '*' or y == '0'):
                    # Se for Ouro
                    if (y == '*'):
                        self.ouros.append((8*aux)+(auy))

                    # Se tiver caminho pra cima
                    if (auy > 0 and (matriz[aux][auy-1] == '0' or matriz[aux][auy-1] == '*')):
                        self.AddVertice(aux + (auy*8), aux + 8*(auy-1))

                    # Se tiver caminho pra baixo
                    if (auy < n-1 and (matriz[aux][auy+1] == '0' or matriz[aux][auy+1] == '*')):
                        self.AddVertice(aux + (auy*8), aux + 8*(auy+1))

                    # Se tiver caminho pra esquerda
                    if (aux > 0 and (matriz[aux-1][auy] == '0' or matriz[aux-1][auy] == '*')):
                        self.AddVertice(aux + (auy*8), aux-1 + 8*auy)

                    # Se tiver caminho pra direita
                    if (aux < n-1 and (matriz[aux+1][auy] == '0' or matriz[aux+1][auy] == '*')):
                        self.AddVertice(aux + (auy*8), aux-1 + 8*auy)
                        
                auy += 1
            aux += 1
    
    def AddVertice(self, u, v):
        self.grafo[u].append(v)