from base import *
from baseCubic import *
from readWriteEValues import *
from readWriteEVectors import *

eValuesPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\chiralityTest\\eValuesBugTest.txt"
normEValuesPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\chiralityTest\\normEValuesBugTest.txt"
eVectorsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\chiralityTest\\eVectorsBugTest.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\chiralityTest\\image\\"

RWEValues = rwEValues()
RWEVectors = rwEVectors()

def nonChiralExtendedCubicResidue(a, b, c, d):
    return extendedCubicResidueSymbol(c, a)[0] *\
           conjugateEisenstein(extendedCubicResidueSymbol(c, b)[0]) *\
           conjugateEisenstein(extendedCubicResidueSymbol(d, a)[0]) *\
           extendedCubicResidueSymbol(d, b)[0]

def computeViableElementsMultiplicative(maxNorm):
    viablePairs = set()
    for maxNormA in range(1, maxNorm):
        for vEA in computeViableElementsCubic(maxNormA):
            for maxNormB in range(1, maxNorm // maxNormA):
                for vEB in computeViableElementsCubic(maxNormB):
                    if gcdEisenstein(vEA, vEB):
                        viablePairs.add((vEA, vEB))
    return list(viablePairs)

def constructMatrixNonChiral(vE):
    return matrix(CDF, len(vE), len(vE), lambda x, y: nonChiralExtendedCubicResidue(vE[x][0],\
                                                                                    vE[x][1],\
                                                                                    vE[y][0],\
                                                                                    vE[y][1]))

maxNorm = 200
eValuesArray = []
normEValuesArray = []
eValueNums = set()
bT = time.time()
for norm in range(155, maxNorm):
    vE = computeViableElementsMultiplicative(norm)
    if (len(vE) not in eValueNums):
        print(norm)
        eValueNums.add(len(vE))
        RWEValues.setReadPath(eValuesPath)
        dict = RWEValues.guideToDict(RWEValues.readEValuesGuide())
        try:
            i = dict[str(len(vE))]
            print("Eigenvalues Found")
            rEvs = RWEValues.readEValues([i])
            eValuesArray.append([float(element) for element in rEvs[0]])
            RWEValues.setReadPath(normEValuesPath)
            normEValuesArray.append([float(element) for element in RWEValues.readEValues([i])[0]])
        except:
            m = constructMatrixNonChiral(vE)
            A = m.H * m
            eValuesVectors = extractEigen(A)
            eValues = eValuesVectors[0]
            eVectors = eValuesVectors[1]
            eValuesArray.append(eValues[0])
            normEValuesArray.append(eValues[1])
            RWEValues.setWritePath(eValuesPath)
            RWEValues.writeEValues([str(element) for element in eValues[0][:]])
            RWEValues.setWritePath(normEValuesPath)
            RWEValues.writeEValues([str(element) for element in eValues[1][:]])
            RWEVectors.setWritePath(eVectorsPath)
            RWEVectors.writeEVectors(eVectors)
createPlot(eValuesArray, normEValuesArray, False, 5, imgPath, True)