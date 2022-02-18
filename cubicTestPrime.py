from base import *
from baseCubic import *
from readWriteEValues import *
from readWriteEVectors import *

eValuesPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\primeTest\\eValues.txt"
normEValuesPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\primeTest\\normEValues.txt"
eVectorsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\primeTest\\eVectors.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\primeTest\\image\\"

RWEValues = rwEValues()
RWEVectors = rwEVectors()

maxNorm = 2500
eValuesArray = []
normEValuesArray = []
eValueNums = set()
bT = time.time()
for norm in range(4, maxNorm):
    vE = computeViablePrimeElementsCubic(norm)
    if (len(vE) not in eValueNums):
        print(norm)
        eValueNums.add(len(vE))
        m = constructMatrixCubic(vE)
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