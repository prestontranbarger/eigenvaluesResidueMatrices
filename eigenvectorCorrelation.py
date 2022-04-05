from baseCubic import *
from readWriteEVectors import *
from tqdm import tqdm
import matplotlib.pyplot as plt

imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\image\\"
eVectorsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\eVectors.txt"

def tradEgnvecFunction(element):
    return conjugate(simplifyComplex(normalizedGaussSum(element)))

def muEgnvecFuction(egnNum, element):
    return conjugate(simplifyComplex(normalizedGaussMuSum(egnNum, element)))

def twistedEigvecFunction(egnNum, element):
    return simplifyComplex(eisensteinToComplex(extendedCubicResidueSymbol(0 * omega + egnNum, element)) * conjugate(normalizedGaussMuSum(1, element)))

RWEVectors = rwEVectors()

egnNum = 2
min = 4
max = 100
x = []
y = []
vEs = []
tally = []

tally = [0 for i in range(len(computeViableElementsCubic(min)))]
for n in range(min, max):
    #print(n)
    v = []
    l = 0
    vE = computeViableElementsCubic(n)
    #x.append(n)
    if len(vE) not in vEs:
        tally.append(0)
        for element in tqdm(vE):
            ngs = muEgnvecFuction(egnNum, element)
            v.append(ngs)
            l += ngs.real() ** 2 + ngs.imag() ** 2
        l = math.sqrt(l)
        for i in range(len(v)):
            v[i] /= l
        RWEVectors.setReadPath(eVectorsPath)
        rowDict = RWEVectors.guideToDict(RWEVectors.readEVectorsGuide())
        egnVec = [[parseComplex(z) for z in eV] for eV in RWEVectors.readEVectors([rowDict[str(len(vE))]])]
        cs = []
        MIndx = 0
        MAbs = 0
        for eVi in range(len(egnVec)):
            ci = (vector(v).hermitian_inner_product(vector(egnVec[eVi]))) / (vector(egnVec[eVi]).hermitian_inner_product(vector(egnVec[eVi])))
            cs.append(ci)
            if ci.abs() > MAbs:
                MAbs = ci.abs()
                MIndx = eVi
        mag = 0
        try:
            row = egnVec[egnNum - 1]
            mag = vector(v).hermitian_inner_product(vector(row)).abs()
            tally[MIndx] += 1
        except:
            mag = 0
        x.append(len(vE))
        y.append(mag)
        print("\n")
        print(n, len(vE), mag)
        print(MIndx + 1, cs)
    #else:
    #    y.append(y[-1])
    vEs.append(len(vE))
for i in range(len(tally)):
    if tally[i] > 0:
        print(str(i + 1) + ":", tally[i])
plt.plot(x, y)
plt.savefig(imgPath + str(math.floor(time.time())) + "innerprodmag" + str(egnNum) + ".png")