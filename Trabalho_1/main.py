import BuscaProfundidadeLimitada as bp
import crud

def main(file = "default.txt"):
    c = crud.Crud(file)
    r = c.read()
    co = r[0]
    col = r[0][0]
    r.remove(co)
    b = bp.BPLs(r,int(col))
    b.Miner()
    #c = BELs()
    #c.BEL(g, g.bateriaInicial, 0)

    
file = input("Digite o nome do arquivo (ou deixe em branco para Default):")
if file != "":
	main(file)
else:
	main()