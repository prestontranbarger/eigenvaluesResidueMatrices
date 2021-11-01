from baseJacobi import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\2\\square\\BFQM9000.txt"
RWBFM = rwBFM()
RWBFM.setReadPath(bfmPath)
RWBFM.setWritePath(bfmPath)

maxNorm = 100000
vE = computeViableElementsJacobi(maxNorm)

m = []
counter = 0
for a in vE:
    counter += 1
    m.append([jacobiSymbol(a, b)[0] for b in vE])
    print(str(counter) + "/" + str(len(vE)))
RWBFM.writeBFM(m, vE, vE)