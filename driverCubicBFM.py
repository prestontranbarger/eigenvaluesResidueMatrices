from baseCubic import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\F21\\MATH 491.201\\output\\3\\square\\BFCM9000.txt"
RWBFM = rwBFM(bfmPath)

maxNorm = 7500

print("Computing viable elements...")
vE = computeViableElementsCubic(maxNorm)
vEGuide = [toStringEisenstein(alpha) for alpha in vE]

m = []

print("Creating BFM...")
for a in tqdm(vE):
    m.append([toStringEisenstein(extendedCubicResidueSymbol(a, b)[0]) for b in vE])

print("Writing BFM...")
RWBFM.writeBFM(m, vEGuide, vEGuide)