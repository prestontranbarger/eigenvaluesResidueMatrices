from baseJacobi import *
from readWriteEvs import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\2\\square\\BFQM9000.txt"
evsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\2\\square\\evs.txt"
normEvsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\2\\square\\normEvs.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\2\\square\\image\\"

RWEvs = rwEvs()

RWBFM = rwBFM(bfmPath)
rowGuide, colGuide = RWBFM.readBFMGuide()
rowDict, colDict = RWBFM.guideToDict(rowGuide), RWBFM.guideToDict(colGuide)

maxNorms = list(range(1, 10000, 2))
evNums = set()
evsArray = []
normEvsArray = []
bT = time.time()
for maxNorm in maxNorms:
    #print("Compute Elements: ", end = "")
    vE = computeViableElementsJacobi(maxNorm)
    if(len(vE) not in evNums):
        #print(maxNorm)
        evNums.add(len(vE))
        RWEvs.setReadPath(evsPath)
        rEvs = RWEvs.readEvs(len(vE))
        if(rEvs == -1):
            #print("Construct Matrix: ", end = "")
            rowSubset = [rowDict[str(element)] for element in vE]
            colSubset = rowSubset
            m = constructMatrixJacobiFromBFM(RWBFM.readBFM(rowSubset, colSubset), len(rowSubset), len(colSubset))
            svdDecomp = svd(m)
            evs = extractEigenvals(svdDecomp, len(vE))
            evsArray.append(evs[0])
            normEvsArray.append(evs[1])
            RWEvs.setWritePath(evsPath)
            RWEvs.writeEvs(evs[0][:])
            RWEvs.setWritePath(normEvsPath)
            RWEvs.writeEvs(evs[1][:])
        else:
            print("Eigenvalues Found")
            evsArray.append(rEvs)
            RWEvs.setReadPath(normEvsPath)
            normEvsArray.append(RWEvs.readEvs(len(vE)))
print(time.time() - bT)
createPlot(evsArray, normEvsArray, False, 5, imgPath)
