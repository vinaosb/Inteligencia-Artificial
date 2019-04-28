class BPLs:
    def BPLUtil(self, g, v , visitado, ouro, bateria, ouros, nouro):
        visitado[v] = True

        # Se acabar a bateria
        if (bateria == 0 and v != 0):
            return 0
        
        bateria -= 1

        # Se for casa de ouro
        if v in g.ouros:
            ouros.remove(v)
            ouro += 1
            nouro -= 1
            visitado = [False]*(g.n**2)
        
        # Se for casa inicial e tiver ouro p comprar baterias
        if (v == 0 and ouro > 0):
            limpo = [False]*(g.n**2)
            # Se nao existem mais minas de ouro
            if (nouro == 0):
                return ouro
            bateria += 5
            ouroaux = 0
            # Testa se recarregando bateria pode conseguir mais ouro
            for i in g.grafo[v]:
                ouroaux = self.BPLUtil(g, i, limpo, ouro-1, bateria, ouros, nouro)
                if (ouroaux > ouro):
                    ouro = ouroaux
            # Se nao for possivel retorna ouro que possui
            return ouro
        else: # Se for casa normal ou inicial sem ouro
            ouroaux = 0
            for i in g.grafo[v]:
                if (visitado[i] == False):
                    ouroaux = self.BPLUtil(g, i, visitado, ouro, bateria, ouros, nouro)
                    if (ouroaux > ouro):
                        ouro = ouroaux # Guarda maior quantidade de ouro que pode achar
        return ouro

    def BPL(self,g):
        visitado = [False]*(g.n**2)

        print("Ouro =", self.BPLUtil(g, 0,visitado, 0, g.bateriaInicial, g.ouros, g.nouro))
