import Grafo
import Queues
class BELs:
	coletado = 0
	ouroAtual = 0

	def __init__(self, matriz, n):
		self.g = Grafo.Grafo(matriz, n)
		self.bateriaAtual = self.g.bateriaInicial
		self.ouroAtual = 0
		self.coletado = 0
		self.explorados = 0
		self.SeqAcoes = list()
		self.distancias = {}

	def Miner(self):
		
		aux = self.g.ouros.copy()
		ini = self.Mineirar(0)
		while self.ouroAtual > 0 and self.g.NOuros() > 0 and ini in aux:
			self.RecarregarBateria()
			aux = self.g.ouros
			ini = self.Mineirar(0)

		print("\n\nBusca em Largura\n\n")
		print("Ouro coletado:", self.coletado)
		print("Casas exploradas:", self.explorados)
		print("Bateria final:", self.bateriaAtual)
		print("Sequencia de Acoes:",self.SeqAcoes)

	def Mineirar(self, ini):
		ret = []
		while True:
			atual,veio_de = self.BuscaEmLargura(ini,self.g.ouros)
			path = self.ReconstruirAcoes(ini,atual,veio_de)
			if (len(ret) + len(path))*2 < self.bateriaAtual and atual in self.g.ouros:
				ret += path
				ret.append("PO")
				self.PegarOuro(atual)
			else:
				aux = len(ret)
				for i in ret:
					if i == "PO":
						aux -= 1
				self.GastarBateria(aux)
				ret += self.AcoesDeRetorno(ret)
				self.SeqAcoes += ret
				ret.clear()
				break
		return atual

	def BuscaEmLargura(self, inicial, metas):
		fronteira = Queues.Queue()
		fronteira.put(inicial)
		veio_de = {}
		veio_de[inicial] = None

		while not fronteira.empty():
			self.explorados += 1
			atual = fronteira.get()

			if atual in metas:
				break

			for prox in self.g.grafo[atual]:
				if prox not in veio_de:
					fronteira.put(prox)
					veio_de[prox] = atual
		return atual,veio_de

	def ReconstruirAcoes(self, inicial, meta, veio_de = {}):
		atual = meta
		path = []
		while atual != inicial:
			if (veio_de[atual] == self.Direita(atual)):
				path.append("E")
			elif (veio_de[atual] == self.Esquerda(atual)):
				path.append("D")
			elif (veio_de[atual] == self.Cima(atual)):
				path.append("B")
			elif (veio_de[atual] == self.Baixo(atual)):
				path.append("C")
			atual = veio_de[atual]

		path.reverse()
		return path

	def AcoesDeRetorno(self, path):
		path2 = []
		for i in path:
			if i == "E":
				path2.append("D")
			if i == "D":
				path2.append("E")
			if i == "C":
				path2.append("B")
			if i == "B":
				path2.append("C")
		path2.reverse()
		return path2

	def GastarBateria(self, bat = 1):
		self.bateriaAtual -= bat

	def PegarOuro(self, pos):
		self.g.ouros.remove(pos)
		self.ouroAtual += 1
		self.coletado += 1

	# Retorna -1 se for parede
	def Direita(self, pos):
		if self.g.PosDireita(pos) == -1:
			return -1
		return self.g.PosDireita(pos)
	
	# Retorna -1 se for parede
	def Esquerda(self, pos):
		if self.g.PosEsquerda(pos) == -1:
			return -1
		return self.g.PosEsquerda(pos)
	
	# Retorna -1 se for parede
	def Cima (self, pos):
		if self.g.PosCima(pos) == -1:
			return -1
		return self.g.PosCima(pos)
	
	# Retorna -1 se for parede
	def Baixo (self, pos):
		if self.g.PosBaixo(pos) == -1:
			return -1
		return self.g.PosBaixo(pos)
	
	def RecarregarBateria(self):
		self.bateriaAtual += 5*(self.g.n**1.5)
		self.ouroAtual -= 1
