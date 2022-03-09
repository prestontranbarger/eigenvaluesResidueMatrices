from base import *
from readWriteEValues import *
from readWriteEVectors import *

eValuesPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\3\\randomTest\\eValues.txt"
normEValuesPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\3\\randomTest\\normEValues.txt"
eVectorsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\3\\randomTest\\eVectors.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\3\\randomTest\\image\\"

RWEValues = rwEValues()
RWEVectors = rwEVectors()

n = 3
p = [1 / n for i in range(n)]
X = GeneralDiscreteDistribution(p)

maxNorm = 250
eValuesArray = []
normEValuesArray = []
bT = time.time()
for norm in range(1, maxNorm):
    print(norm)
    m = matrix(CDF, norm, norm, lambda x, y: omega ** X.get_random_element())
    A = m.H * m
    eValuesVectors = extractEigen(A)
    eValues = eValuesVectors[0]
    eVectors = eValuesVectors[1]
    eValues.append(eValues[0])
    normEValuesArray.append(eValues[1])
    RWEValues.setWritePath(eValuesPath)
    RWEValues.writeEValues([str(element) for element in eValues[0][:]])
    RWEValues.setWritePath(normEValuesPath)
    RWEValues.writeEValues([str(element) for element in eValues[1][:]])
    RWEVectors.setWritePath(eVectorsPath)
    RWEVectors.writeEVectors(eVectors)
createPlot(eValuesArray, normEValuesArray, True, 5, imgPath)