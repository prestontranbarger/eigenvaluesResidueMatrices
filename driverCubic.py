from baseCubic import *
from readWriteEvs import *

evsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\evs.txt"
normEvsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\normEvs.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\image\\"

RWEvs = rwEvs()

maxNorms = list(range(3, 500))
evNums = set()
evsArray = []
normEvsArray = []
for maxNorm in maxNorms:
    vE = computeViableElementsCubic(maxNorm)
    if(len(vE) not in evNums):
        print(maxNorm)
        evNums.add(len(vE))
        RWEvs.setReadPath(evsPath)
        rEvs = RWEvs.readEvs(len(vE))
        if(rEvs == -1):
            m = constructMatrixCubic(vE)
            svdDecomp = svd(m)
            evs = extractEigenvals(svdDecomp, len(vE))
            evsArray.append(evs[0])
            normEvsArray.append(evs[1])
            RWEvs.setWritePath(evsPath)
            RWEvs.writeEvs(evs[0][:])
            RWEvs.setWritePath(normEvsPath)
            RWEvs.writeEvs(evs[1][:])
        else:
            evsArray.append(rEvs)
            RWEvs.setReadPath(normEvsPath)
            normEvsArray.append(RWEvs.readEvs(len(vE)))
createPlot(evsArray, normEvsArray, True, 5, imgPath)