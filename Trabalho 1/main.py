from crud import Crud
from BuscaProfundidadeLimitada import BPLs
from BuscaEmLargura import BELs
from Grafo import Grafo

def main():
    c = Crud("test.txt")
    r = c.read()
    co = r[0]
    col = r[0][0]
    r.remove(co)
    g = Grafo(r,int(col))
    b = BPLs()
    b.BPL(g)
    c = BELs()
    c.BEL(g, g.bateriaInicial, 0)

    

main()