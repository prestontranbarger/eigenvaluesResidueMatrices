from baseCubic import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\BFCM9000.txt"
RWBFM = rwBFM()
RWBFM.setReadPath(bfmPath)
RWBFM.setWritePath(bfmPath)

maxNorm = 1000
vE = computeViableElementsCubic(maxNorm)
vEGuide = [toStringEisenstein(alpha) for alpha in vE]

m = []
i = 0
for a in vE:
    i += 1
    m.append([toStringEisenstein(extendedCubicResidueSymbol(a, b)[0]) for b in vE])
    print(str(i) + "/" + str(len(vE)))
RWBFM.writeBFM(m, vEGuide, vEGuide)