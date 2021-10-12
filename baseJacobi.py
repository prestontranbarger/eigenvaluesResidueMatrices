from base import *

def conditionsJacobi(x):
    return (1 <= x) and\
           (x % 2 == 1) and\
           (isNthPowerFree(factor(x), 2))

def computeViableElementsJacobi(maxNorm, timer = False):
    bT = time.time()
    viableCandidates = []
    for i in range(maxNorm + 1):
        if conditionsJacobi(i):
            viableCandidates.append(i)
    if timer:
        print("time to find valid a, n:", str(time.time() - bT) + "s")
    return viableCandidates

def constructMatrixJacobi(viableElements, timer = False):
    bT = time.time()
    m = matrix(RDF, len(viableElements), len(viableElements), lambda x, y: jacobiSymbol(viableElements[x],\
                                                                                        viableElements[y])[0])
    if timer:
        print("time to construct matrix:", str(time.time() - bT) + "s")
    return m