class BELs:
    def BEL(self, g, bateria, ouro):
        visitados = [False] * (len(g.grafo))

        fila = []

        fila.append(0)
        visitados[0] = True

        while fila:
            s = fila.pop(0)

            for i in g.grafo[s]:
                if (visitados[i] == False):
                    fila.append(i)
                    visitados[i] = True