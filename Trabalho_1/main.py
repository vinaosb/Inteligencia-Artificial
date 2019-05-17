import BuscaProfundidadeLimitada as bp
import Dijkstra as diji
import BuscaEmLargura as BEL
import Aestrela as aes
import crud

def main(file = "default.txt"):
	c = crud.Crud(file)
	r = c.read()
	co = r[0]
	col = r[0][0]
	r.remove(co)
	i = bp.BPLs(r,int(col))
	i.Miner()
	j = diji.Dijkstra(r,int(col))
	j.Miner()
	k = BEL.BELs(r,int(col))
	k.Miner()
	l = aes.AEstrela(r,int(col))
	l.Miner()

	
file = input("Digite o nome do arquivo (ou deixe em branco para Default):")
if file != "":
	main(file)
else:
	main()