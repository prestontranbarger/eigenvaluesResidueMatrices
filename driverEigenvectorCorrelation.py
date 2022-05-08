from baseEigenvectorCorrelation import *

imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\image\\egnCorrel\\"
eVectorsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\eVectors.txt"
tempOutPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\tempOut\\tempOut.txt"


min = 4
max = 100
minAB = -2
maxAB = 2

file = open(tempOutPath, 'w')
for a in range(minAB, maxAB + 1):
    for b in range(minAB, maxAB + 1):
        print(a, b)
        mu = a + b * omega
        vEs, csms = egnCorrelModule(eVectorsPath, min, max, muEgnvecFuction, [mu])
        file.writelines(toStringEisenstein(mu) + "|" + str(vEs) + "\n")
        file.writelines(str(csms) + "\n")
        correlationPlotPColorMesh(vEs, csms, imgPath, toStringEisenstein(mu))
        time.sleep(1)
file.close()