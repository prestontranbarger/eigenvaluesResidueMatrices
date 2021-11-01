from baseCubic import *
from readWriteEvs import *

evsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\evs.txt"
normEvsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\normEvs.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\image\\"

RWEvs = rwEvs()

maxNorm = 500

maxNorms = list([3]) + list(range(7, maxNorm, 6)) + list(range(4, maxNorm, 24))
maxNorms.sort()
evNums = set()
evsArray = []
normEvsArray = []
bT = time.time()
for maxNorm in maxNorms:
    print(maxNorm)
    print("Compute elements: ", end = "")
    vE = computeViableElementsCubic(maxNorm, True)
    if(len(vE) not in evNums):
        evNums.add(len(vE))
        RWEvs.setReadPath(evsPath)
        rEvs = RWEvs.readEvs(len(vE))
        if(rEvs == -1):
            print("Construct matrix: ", end = "")
            m = constructMatrixCubic(vE, True)
            svdDecomp = svd(m)
            evs = extractEigenvals(svdDecomp, len(vE))
            evsArray.append(evs[0])
            normEvsArray.append(evs[1])
            RWEvs.setWritePath(evsPath)
            RWEvs.writeEvs(evs[0][:])
            RWEvs.setWritePath(normEvsPath)
            RWEvs.writeEvs(evs[1][:])
        else:
            print("Eigenvalues found")
            evsArray.append(rEvs)
            RWEvs.setReadPath(normEvsPath)
            normEvsArray.append(RWEvs.readEvs(len(vE)))
    else:
        print("No new eigenvalues")
    print("")
print(time.time() - bT)
createPlot(evsArray, normEvsArray, True, 5, imgPath)
