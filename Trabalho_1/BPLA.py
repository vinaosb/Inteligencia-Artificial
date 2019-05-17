import Grafo

class BPLAs:
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

    def fx(self, pos):
        return self.gx() + self.hx(pos)
    def gx(self):
        return len(self.retorno)
    def hx(self, pos):
		ret = self.g.n*self.g.n
		poy = pos//self.g.n
		pox = pos%poy
		for o in self.g.ouros:
			auy = o//self.g.n
			aux = o%auy
			ret = min(ret, ((aux-pox)**2) + ((auy-poy)**2))
        return ret

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

		temp = 'T'
		tempm = self.fx(pos)**2
		tempt = False
		# Enquanto houver caminho fazer:
		while temp != R:
			# Se o caminho a esquerda possuir fx menor que atual, ir para esquerda
			if self.Esquerda(pos) > 0 and tempm - self.fx(self.Esquerda(pos)) < 0:
				tempm = self.fx(self.Esquerda(pos))
				temp = 'E'
				tempt = True
			# Se o caminho a direita possuir fx menor que atual, ir para direita
			if self.Direita(pos) > 0 and tempm - self.fx(self.Direita(pos)) < 0:
				tempm = self.fx(self.Direita(pos))
				temp = 'D'
				tempt = True
			# Se o caminho acima possuir fx menor que atual, ir para cima
			if self.Cima(pos) > 0 and tempm - self.fx(self.Cima(pos)) < 0:
				tempm = self.fx(self.Cima(pos))
				temp = 'C'
				tempt = True
			# Se o caminho abaixo possuir fx menor que atual, ir para baixo
			if self.Baixo(pos) > 0 and tempm - self.fx(self.Baixo(pos)) < 0:
				temp = 'B'
				tempt = True
			# Se nao tem nenhum caminho com fx menor que atual ou todos ja foram percorridos, retorna
			if tempt = False:
				temp = 'R'

			tempt = False
			tempm = self.fx(pos)**2

			# Mineira para o caminho escolhido anteriormente
			if temp == 'E':
				self.GastarBateria()
				self.SeqAcoes.append("E")
				self.Mineirar(self.Esquerda(pos))
			elif temp == 'D':
				self.GastarBateria()
				self.SeqAcoes.append("D")
				self.Mineirar(self.Direita(pos))
			elif temp == 'C':
				self.GastarBateria()
				self.SeqAcoes.append("C")
				self.Mineirar(self.Cima(pos))
			elif temp == 'B':
				self.GastarBateria()
				self.SeqAcoes.append("B")
				self.Mineirar(self.Baixo(pos))

		# Retorna para posicao anterior e continua a mineirar
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
