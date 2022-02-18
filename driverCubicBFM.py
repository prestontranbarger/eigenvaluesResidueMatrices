from baseCubic import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\square\\BFCM9001.txt"
RWBFM = rwBFM(bfmPath)

maxNorm = 100

print("Computing viable elements...")
vE = computeViableElementsCubic(maxNorm)
vEGuide = [toStringEisenstein(alpha) for alpha in vE]

m = []

print("Creating BFM...")
for a in tqdm(vE):
    m.append([toStringEisenstein(extendedCubicResidueSymbol(a, b)[0]) for b in vE])

print("Writing BFM...")
RWBFM.writeBFM(m, vEGuide, vEGuide)