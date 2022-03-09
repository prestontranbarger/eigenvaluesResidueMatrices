from baseJacobi import *
from readWriteEVectors import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\2\\square\\BFQM9000.txt"
eVectorsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\2\\square\\eVectors.txt"

RWEVectors = rwEVectors()

RWBFM = rwBFM(bfmPath)
rowGuide, colGuide = RWBFM.readBFMGuide()
rowDict, colDict = RWBFM.guideToDict(rowGuide), RWBFM.guideToDict(colGuide)

maxNorms = list(range(1, 1250, 2))
evNums = set()
bT = time.time()
for maxNorm in maxNorms:
    vE = computeViableElementsJacobi(maxNorm)
    if(len(vE) not in evNums):
        print(maxNorm)
        evNums.add(len(vE))
        RWEVectors.setReadPath(eVectorsPath)
        dict = RWEVectors.guideToDict(RWEVectors.readEVectorsGuide())
        try:
            i = dict[str(len(vE))]
            print("Eigenvalues Found")
        except KeyError:
            rowSubset = [rowDict[str(element)] for element in vE]
            colSubset = rowSubset
            m = constructMatrixJacobiFromBFM(RWBFM.readBFM(rowSubset, colSubset), len(rowSubset), len(colSubset))
            A = m.H * m
            eVectors = extractEigen(A)[1]
            RWEVectors.setWritePath(eVectorsPath)
            RWEVectors.writeEVectors(eVectors)
print(time.time() - bT)