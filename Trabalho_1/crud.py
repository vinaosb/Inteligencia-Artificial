class Crud:
    def __init__(self, stringFile):
        self.stringFile = stringFile
    
    def read(self):
        f = open(self.stringFile,"r")
        temp = False
        col = 0
        ret = []
        f1 = f.readlines()
        for x in f1:
            if (temp == False):
                col = int(x)
                temp = True
            k = x.strip()
            ret.append(k.split('    ', col))
        return ret