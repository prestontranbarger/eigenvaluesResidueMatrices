from base import *
from tqdm import tqdm

def conditionsCubic(alpha):
    alpha = Integer(alpha[0]) + Integer(alpha[1]) * omega
    norm = normEisenstein(alpha)
    return (1 <= norm) and\
           (norm != 3) and\
           (isPrimary(alpha)) and\
           (isNthPowerFree(factorEisenstein(alpha), 2))

def conditionsPrimeCubic(alpha):
    alpha = Integer(alpha[0]) + Integer(alpha[1]) * omega
    norm = normEisenstein(alpha)
    return (1 <= norm) and\
           (norm != 3) and\
           (isPrimary(alpha)) and\
           (isPrime(factorEisenstein(alpha)))

def computeViableElementsCubic(maxNorm):
    viableElements = []
    indexOffset = math.floor(math.sqrt(4 * maxNorm / 3))
    for y in tqdm(range(-indexOffset, indexOffset + 1)):
        for x in range(math.ceil((y - math.sqrt(4 * maxNorm - 3 * y ** 2)) / 2),\
                       math.floor((y + math.sqrt(4 * maxNorm - 3 * y ** 2)) / 2) + 1):
            if conditionsCubic((x, y)):
                viableElements.append(Integer(x) + Integer(y) * omega)
    return viableElements

def computeViablePrimeElementsCubic(maxNorm):
    viableElements = []
    indexOffset = math.floor(math.sqrt(4 * maxNorm / 3))
    for y in tqdm(range(-indexOffset, indexOffset + 1)):
        for x in range(math.ceil((y - math.sqrt(4 * maxNorm - 3 * y ** 2)) / 2), \
                       math.floor((y + math.sqrt(4 * maxNorm - 3 * y ** 2)) / 2) + 1):
            if conditionsPrimeCubic((x, y)):
                viableElements.append(Integer(x) + Integer(y) * omega)
    return viableElements

def constructMatrixCubic(viableElements, timer = False):
    bT = time.time()
    m = matrix(CDF, len(viableElements), len(viableElements), lambda x, y: extendedCubicResidueSymbol(viableElements[x],\
                                                                                                      viableElements[y])[0])
    if timer:
        print("time to construct matrix:", str(time.time() - bT) + "s")
    return m

def constructMatrixCubicFromBFM(m, numRows, numCols):
    return matrix(CDF, numRows, numCols, lambda x, y: toEisensteinString(m[x][y]))
