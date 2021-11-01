from baseCubic import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\BFCM9000.txt"
RWBFM = rwBFM(bfmPath)

maxNorm = 5000
vE = computeViableElementsCubic(maxNorm)
vEGuide = [toStringEisenstein(alpha) for alpha in vE]

m = []
i = 0
for a in tqdm(vE):
    i += 1
    m.append([toStringEisenstein(extendedCubicResidueSymbol(a, b)[0]) for b in vE])
    print(str(i) + "/" + str(len(vE)))
RWBFM.writeBFM(m, vEGuide, vEGuide)
