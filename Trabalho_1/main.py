import BuscaProfundidadeLimitada as bp
import BPLA as bpa
import crud

def main(file = "default.txt"):
    c = crud.Crud(file)
    r = c.read()
    co = r[0]
    col = r[0][0]
    r.remove(co)
    i = bp.BPLs(r,int(col))
    i.Miner()
    j = bpa.BPLAs(r,int(col))
    j.Miner()

    
file = input("Digite o nome do arquivo (ou deixe em branco para Default):")
if file != "":
	main(file)
else:
	main()