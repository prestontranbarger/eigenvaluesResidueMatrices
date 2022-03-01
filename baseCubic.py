from base import *
from tqdm import tqdm

rollingT = 0
beginT = 0

def conditionsCubicLargeSieve(alpha):
    alpha = Integer(alpha[0]) + Integer(alpha[1]) * omega
    norm = normEisenstein(alpha)
    return alpha[1] != 0 and\
           isPrimary(alpha) and\
           isPrime(factorEisenstein(alpha))

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

def computeViableElementsCubicLargeSieve(maxNorm):
    viableElements = []
    indexOffset = math.floor(math.sqrt(4 * maxNorm / 3))
    for y in tqdm(range(-indexOffset, indexOffset + 1)):
        for x in range(math.ceil((y - math.sqrt(4 * maxNorm - 3 * y ** 2)) / 2),\
                       math.floor((y + math.sqrt(4 * maxNorm - 3 * y ** 2)) / 2) + 1):
            if conditionsCubicLargeSieve((x, y)):
                viableElements.append(Integer(x) + Integer(y) * omega)
    return viableElements

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
        for x in range(math.ceil((y - math.sqrt(4 * maxNorm - 3 * y ** 2)) / 2),\
                       math.floor((y + math.sqrt(4 * maxNorm - 3 * y ** 2)) / 2) + 1):
            if conditionsPrimeCubic((x, y)):
                viableElements.append(Integer(x) + Integer(y) * omega)
    return viableElements

def ecrsCounter(alpha, beta, symbol, x, y, veLen):
    global rollingT, beginT
    if y == 0:
        print(str(x) + "/" + str(veLen))
        currentT = time.time()
        if rollingT != 0:
            print(str(currentT - rollingT) + "s")
            print(str(currentT - beginT) + "s")
        else:
            beginT = time.time()
        rollingT = currentT
    return symbol(alpha, beta)

def constructMatrixCubic(viableElements, symbol, timer = False):
    bT = time.time()
    m = matrix(CDF, len(viableElements), len(viableElements), lambda x, y: ecrsCounter(viableElements[x], viableElements[y], symbol, x, y, len(viableElements))[0])
    if timer:
        print("time to construct matrix:", str(time.time() - bT) + "s")
    return m

def constructMatrixCubicFromBFM(m, numRows, numCols, timer = True):
    bT = time.time()
    out = matrix(CDF, numRows, numCols, lambda x, y: toEisensteinString(m[x][y]))
    if timer:
        print("time to construct matrix:", str(time.time() - bT) + "s")
    return out