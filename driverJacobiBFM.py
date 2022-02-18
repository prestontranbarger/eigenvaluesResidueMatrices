from baseJacobi import *
from readWriteBFM import *

bfmPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\2\\square\\BFQM9000.txt"
RWBFM = rwBFM(bfmPath)

maxNorm = 100000

print("Computing viable elements...")
vE = computeViableElementsJacobi(maxNorm)

m = []

print("Creating BFM...")
for a in tqdm(vE):
    m.append([jacobiSymbol(a, b)[0] for b in vE])

print("Writing BFM...")
RWBFM.writeBFM(m, vE, vE)