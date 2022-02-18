from baseChirality import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\chiralityTest\\BFCM9000.txt"
RWBFM = rwBFM(bfmPath)

maxNorm = 500

print("Computing viable elements...")
vE = computeViableElementsMultiplicative(maxNorm)
vEGuide = [toStringEisensteinPair(pair) for pair in vE]

m = []

print("Creating BFM...")
for ab in tqdm(vE):
    m.append([toStringEisenstein(nonChiralExtendedCubicResidue(ab[0], ab[1], cd[0], cd[1])) for cd in vE])

print("Writing BFM...")
RWBFM.writeBFM(m, vEGuide, vEGuide)