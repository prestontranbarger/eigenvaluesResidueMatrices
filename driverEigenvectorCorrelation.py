from baseEigenvectorCorrelation import *

imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\image\\egnCorrel\\"
eVectorsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\eVectors.txt"

min = 4
max = 250
minAB = -5
maxAB = 5

for a in range(minAB, maxAB + 1):
    for b in range(minAB, maxAB + 1):
        mu = a + b * omega
        vEs, csms = egnCorrelModule(eVectorsPath, min, max, muEgnvecFuction, [mu])
        correlationPlotPColorMesh(vEs, csms, imgPath, toStringEisenstein(mu))