from baseCubic import *
from readWriteEVectors import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\BFCM9000.txt"
eVectorsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\eVectors.txt"

RWEVectors = rwEVectors()

RWBFM = rwBFM(bfmPath)
rowGuide, colGuide = RWBFM.readBFMGuide()
rowDict, colDict = RWBFM.guideToDict(rowGuide), RWBFM.guideToDict(colGuide)

maxNorm = 1000

maxNorms = list([3]) + list(range(7, maxNorm, 6)) + list(range(4, maxNorm, 24))
maxNorms.sort()
eValueNums = set()
bT = time.time()
for maxNorm in maxNorms:
    vE = computeViableElementsCubic(maxNorm)
    if(len(vE) not in eValueNums):
        print(maxNorm)
        eValueNums.add(len(vE))
        RWEVectors.setReadPath(eVectorsPath)
        dict = RWEVectors.guideToDict(RWEVectors.readEVectorsGuide())
        try:
            i = dict[str(len(vE))]
            print("Eigenvalues found")
        except:
            rowSubset = [rowDict[toStringEisenstein(element)] for element in vE]
            colSubset = rowSubset
            m = constructMatrixCubicFromBFM(RWBFM.readBFM(rowSubset, colSubset), len(rowSubset), len(colSubset))
            A = m.H * m
            eVectors = extractEigen(A)[1]
            RWEVectors.setWritePath(eVectorsPath)
            RWEVectors.writeEVectors(eVectors)
print(time.time() - bT)