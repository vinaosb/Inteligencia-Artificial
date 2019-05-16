class BELs:
    coletado = 0
    ouroAtual = 0

    def __init__(self, matriz, n):
        self.g = Grafo.Grafo(matriz, n)
        self.visitado = [False]*(self.g.n**2)
        self.bateriaAtual = self.g.bateriaInicial
        self.retorno = list()
        self.caminho = list()
        self.SeqAcoes = list()

    def GastarBateria(self):
        self.bateriaAtual -= 1

    def PegarOuro(self, pos):
        self.g.ouros.remove(pos)
        self.SeqAcoes.append("PO")
        self.ouroAtual += 1
        self.coletado += 1

    # Retorna -1 se for parede e 0 se ja foi visitado
    def Direita(self, pos):
        if self.g.PosDireita(pos) == -1:
            return -1
        if self.visitado[self.g.PosDireita(pos)]:
            return 0
        return self.g.PosDireita(pos)
    
    # Retorna -1 se for parede e 0 se ja foi visitado
    def Esquerda(self, pos):
        if self.g.PosEsquerda(pos) == -1:
            return -1
        if self.visitado[self.g.PosEsquerda(pos)]:
            return 0
        return self.g.PosEsquerda(pos)
    
    # Retorna -1 se for parede e 0 se ja foi visitado
    def Cima (self, pos):
        if self.g.PosCima(pos) == -1:
            return -1
        if self.visitado[self.g.PosCima(pos)]:
            return 0
        return self.g.PosCima(pos)
    
    # Retorna -1 se for parede e 0 se ja foi visitado
    def Baixo (self, pos):
        if self.g.PosBaixo(pos) == -1:
            return -1
        if self.visitado[self.g.PosBaixo(pos)]:
            return 0
        return self.g.PosBaixo(pos)
    
    def RecarregarBateria(self):
        self.bateriaAtual += 5*(self.g.n**1.5)
        self.ouroAtual -= 1
