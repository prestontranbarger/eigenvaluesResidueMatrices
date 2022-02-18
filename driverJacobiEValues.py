from baseJacobi import *
from readWriteEValues import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\2\\square\\BFQM9000.txt"
eValuesPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\2\\square\\testEValues.txt"
normEValuesPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\2\\square\\testNormEValues.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\2\\square\\image\\"

RWEValues = rwEValues()

RWBFM = rwBFM(bfmPath)
rowGuide, colGuide = RWBFM.readBFMGuide()
rowDict, colDict = RWBFM.guideToDict(rowGuide), RWBFM.guideToDict(colGuide)

maxNorms = list(range(1, 100, 2))
norms = []
evNums = set()
evsArray = []
normEvsArray = []
bT = time.time()
for maxNorm in maxNorms:
    vE = computeViableElementsJacobi(maxNorm)
    if(len(vE) not in evNums):
        print(maxNorm)
        norms.append(maxNorm)
        evNums.add(len(vE))
        RWEValues.setReadPath(eValuesPath)
        dict = RWEValues.guideToDict(RWEValues.readEValuesGuide())
        try:
            i = dict[str(len(vE))]
            print("Eigenvalues Found")
            rEvs = RWEValues.readEValues([i])
            evsArray.append([float(element) for element in rEvs[0]])
            RWEValues.setReadPath(normEValuesPath)
            normEvsArray.append([float(element) for element in RWEValues.readEValues([i])[0]])
        except KeyError:
            rowSubset = [rowDict[str(element)] for element in vE]
            colSubset = rowSubset
            m = constructMatrixJacobiFromBFM(RWBFM.readBFM(rowSubset, colSubset), len(rowSubset), len(colSubset))
            A = m.H * m
            eValues = extractEigen(A)[0]
            evsArray.append(eValues[0])
            normEvsArray.append(eValues[1])
            RWEValues.setWritePath(eValuesPath)
            RWEValues.writeEValues([str(element) for element in eValues[0][:]])
            RWEValues.setWritePath(normEValuesPath)
            RWEValues.writeEValues([str(element) for element in eValues[1][:]])
print(time.time() - bT)
createPlot(evsArray, normEvsArray, True, 5, imgPath, norms)
print("Plot complete.")