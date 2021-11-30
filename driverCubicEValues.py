from baseCubic import *
from readWriteEValues import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\BFCM9000.txt"
evsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\testEValues.txt"
normEvsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\testNormEValues.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\image\\"

RWEValues = rwEValues()

RWBFM = rwBFM(bfmPath)
rowGuide, colGuide = RWBFM.readBFMGuide()
rowDict, colDict = RWBFM.guideToDict(rowGuide), RWBFM.guideToDict(colGuide)

maxNorm = 3750

maxNorms = list([3]) + list(range(7, maxNorm, 6)) + list(range(4, maxNorm, 24))
maxNorms.sort()
eValueNums = set()
eValuesArray = []
normEValuesArray = []
bT = time.time()
for maxNorm in maxNorms:
    vE = computeViableElementsCubic(maxNorm)
    if(len(vE) not in eValueNums):
        print(maxNorm)
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
            rowSubset = [rowDict[toStringEisenstein(element)] for element in vE]
            colSubset = rowSubset
            m = constructMatrixCubicFromBFM(RWBFM.readBFM(rowSubset, colSubset), len(rowSubset), len(colSubset))
            A = m.H * m
            eValues = extractEigen(A)[0]
            eValuesArray.append(eValues[0])
            normEValuesArray.append(eValues[1])
            RWEValues.setWritePath(evsPath)
            RWEValues.writeEValues([str(element) for element in eValues[0][:]])
            RWEValues.setWritePath(normEvsPath)
            RWEValues.writeEValues([str(element) for element in eValues[1][:]])
print(time.time() - bT)
createPlot(eValuesArray, normEValuesArray, True, 5, imgPath)