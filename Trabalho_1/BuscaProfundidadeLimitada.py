import Grafo

class BPLs:
    coletado = 0
    ouroAtual = 0

    def __init__(self, matriz, n):
        self.g = Grafo.Grafo(matriz, n)
        self.visitado = [False]*(self.g.n**2)
        self.bateriaAtual = self.g.bateriaInicial
        self.retorno = list()
        self.caminho = list()
        self.SeqAcoes = list()

    def Miner(self):
        self.Mineirar(0)
        while (self.ouroAtual > 0 and self.g.NOuros() > 0):
            self.RecarregarBateria()
            self.Mineirar(0)
        
        print("Ouro coletado =", self.coletado)
        print("Caminho:", self.caminho)
        print("Numero de posicoes visitadas:", len(self.caminho))
        print("Seq de Acoes:",self.SeqAcoes)
        print("Numero de acoes realizadas:", len(self.SeqAcoes))

    # Recebe posicao atual e retorna proxima acao
    def Mineirar(self, pos):
        self.visitado[pos] = True
        self.retorno.append(pos)

        # Se esta em posicao com ouro a ser mineirado, mineirar
        if (pos in self.g.ouros):
            self.PegarOuro(pos)

        # Se so tem bateria suficiente para voltar, voltar
        if (self.bateriaAtual <= len(self.retorno) + 1):
            return self.Retornar(pos, False)

        if len(self.caminho) <= 0 or self.caminho[len(self.caminho) - 1] != pos:
            self.caminho.append(pos)
        # Se possui lugar a esquerda, andar a esquerda
        if self.Esquerda(pos) > 0:
            self.GastarBateria()
            self.SeqAcoes.append("E")
            self.Mineirar(self.Esquerda(pos))
        # Se possui lugar acima, andar acima
        elif self.Cima(pos) > 0:
            self.GastarBateria()
            self.SeqAcoes.append("C")
            self.Mineirar(self.Cima(pos))
        # Se possui lugar a direita, andar a direita
        elif self.Direita(pos) > 0:
            self.GastarBateria()
            self.SeqAcoes.append("D")
            self.Mineirar(self.Direita(pos))
        # Se possui lugar a baixo, andar a baixo
        elif self.Baixo(pos) > 0:
            self.GastarBateria()
            self.SeqAcoes.append("B")
            self.Mineirar(self.Baixo(pos))
        # Se nao possui destinos, retornar para posicao anterior e continua mineirando
        else:
            self.GastarBateria()
            self.Retornar(pos, True)
    
    # @pos = posicao atual
    # @continuarOuInicio = Continuar a mineirar, ou retornar ao inicio
    def Retornar(self, pos, continuarOuInicio):
        self.visitado[pos] = continuarOuInicio
        self.retorno.remove(pos)
        # Se for para continuar mineirando, minera a casa anterior
        if continuarOuInicio:
            self.Mineirar(self.retorno[len(self.retorno) - 1])
        else:
            if len(self.caminho) <= 0 or self.caminho[len(self.caminho) - 1] != pos:
                self.caminho.append(pos)
            if pos != 0:
                self.bateriaAtual -= 1

                if self.g.PosDireita(pos) == self.retorno[len(self.retorno) - 1]:
                    self.SeqAcoes.append("D")
                elif self.g.PosEsquerda(pos) == self.retorno[len(self.retorno) - 1]:
                    self.SeqAcoes.append("E")
                elif self.g.PosCima(pos) == self.retorno[len(self.retorno) - 1]:
                    self.SeqAcoes.append("C")
                elif self.g.PosBaixo(pos) == self.retorno[len(self.retorno) - 1]:
                    self.SeqAcoes.append("B")

                self.Retornar(self.retorno[len(self.retorno) - 1], continuarOuInicio)

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
