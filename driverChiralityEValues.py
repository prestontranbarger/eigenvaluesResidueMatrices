from baseChirality import *
from readWriteEValues import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\3\\chiralityTest\\BFCM9000.txt"
evsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\3\\chiralityTest\\logEValues.txt"
normEvsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\3\\chiralityTest\\logNormEValues.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\3\\chiralityTest\\image\\"

RWEValues = rwEValues()

RWBFM = rwBFM(bfmPath)
rowGuide, colGuide = RWBFM.readBFMGuide()
rowDict, colDict = RWBFM.guideToDict(rowGuide), RWBFM.guideToDict(colGuide)

maxNorm = 500

maxNorms = list(range(2, maxNorm, 3))
maxNorms.sort()
eValueNums = set()
eValuesArray = []
normEValuesArray = []
norms = []
normalizationMethod = 'l'
bT = time.time()
for maxNorm in maxNorms:
    vE = computeViableElementsMultiplicative(maxNorm)
    if(len(vE) not in eValueNums):
        print(maxNorm)
        norms.append(maxNorm)
        eValueNums.add(len(vE))
        RWEValues.setReadPath(evsPath)
        dict = RWEValues.guideToDict(RWEValues.readEValuesGuide())
        try:
            i = dict[str(len(vE))]
            print("Eigenvalues found")
            rEvs = RWEValues.readEValues([i])
            eValuesArray.append([float(element) for element in rEvs[0]])
            RWEValues.setReadPath(normEvsPath)
            normEValuesArray.append([float(element) for element in RWEValues.readEValues([i])[0]])
        except:
            rowSubset = [rowDict[toStringEisensteinPair(pair)] for pair in vE]
            colSubset = rowSubset
            rowSubset.sort()
            colSubset.sort()
            m = constructMatrixCubicFromBFM(RWBFM.readBFM(rowSubset, colSubset), len(rowSubset), len(colSubset))
            A = m.H * m
            eValues = extractEigen(A, normalizationMethod)[0]
            eValuesArray.append(eValues[0])
            normEValuesArray.append(eValues[1])
            RWEValues.setWritePath(evsPath)
            RWEValues.writeEValues([str(element) for element in eValues[0][:]])
            RWEValues.setWritePath(normEvsPath)
            RWEValues.writeEValues([str(element) for element in eValues[1][:]])
print(time.time() - bT)
createPlot(eValuesArray, normEValuesArray, normalizationMethod, 5, imgPath, False)