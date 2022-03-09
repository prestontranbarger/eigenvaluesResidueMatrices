from baseCubic import *
from readWriteEVectors import *
from tqdm import tqdm
import matplotlib.pyplot as plt

imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\image\\"
eVectorsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\eVectors.txt"

RWEVectors = rwEVectors()

x = []
y = []
vEs = []
for n in range(4, 450):
    print(n)
    v = []
    l = 0
    vE = computeViableElementsCubic(n)
    x.append(n)
    if len(vE) not in vEs:
        for element in tqdm(vE):
            ngs = conjugate(simplifyComplex(normalizedGaussSum(element)))
            v.append(ngs)
            l += ngs.real() ** 2 + ngs.imag() ** 2
        l = math.sqrt(l)
        for i in range(len(v)):
            v[i] /= l
        #print(v)

        RWEVectors.setReadPath(eVectorsPath)
        rowDict = RWEVectors.guideToDict(RWEVectors.readEVectorsGuide())
        row = [parseComplex(element) for element in RWEVectors.readEVectors([rowDict[str(len(vE))]])[0]]
        #print(row)
        mag = vector(v).hermitian_inner_product(vector(row))
        print(mag)
        y.append(mag.abs())
    else:
        y.append(y[-1])
    vEs.append(len(vE))
plt.plot(x, y)
plt.savefig(imgPath + str(math.floor(time.time())) + "innerprodmag.png")