from base import *
from baseCubic import *
from readWriteEValues import *
from readWriteEVectors import *

eValuesPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\chiralityTest\\eValues.txt"
normEValuesPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\chiralityTest\\normEValues.txt"
eVectorsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\chiralityTest\\eVectors.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\chiralityTest\\image\\"

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

maxNorm = 250
eValuesArray = []
normEValuesArray = []
eValueNums = set()
bT = time.time()
for norm in range(2, maxNorm):
    vE = computeViableElementsMultiplicative(norm)
    if (len(vE) not in eValueNums):
        print(norm)
        eValueNums.add(len(vE))
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
createPlot(eValuesArray, normEValuesArray, True, 5, imgPath)
