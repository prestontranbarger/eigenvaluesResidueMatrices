from sage.all import *
import math
import time
import matplotlib.pyplot as plt

eisenstienIntegers = EisensteinIntegers(names=('omega',)); (omega,) = eisenstienIntegers._first_ngens(1)

def normEisenstien(alpha):
    #computes magnitude squared of an eisenstien integer
    return Integer(alpha[0]) ** 2 - Integer(alpha[0]) * Integer(alpha[1]) + Integer(alpha[1]) ** 2

def factorEisenstein(alpha):
    #computes the factorization of an eisenstien integer over the eisenstien integers
    #input can be list or eisenstien integer
    return factor(Integer(alpha[0]) + Integer(alpha[1]) * omega)

def isPrime(f):
    #uses a given factorization to determine if a number is prime in a specific field
    if len(f) == 1 and f[0][1] == 1:
        return True
    return False

def isPrimary(alpha):
    if alpha[0] % 3 == 2 and alpha[1] % 3 == 0:
        return True
    return False

def isNthPowerFree(f, n):
    #pass n=2 to find squarefree, n=3 to find cubefree, etc
    for factor in f:
        if factor[1] >= n:
            return False
    return True

def legendreSymbol(a, p):
    if p == 2:
        return [0, False]
    else:
        out = power_mod(a, (p - 1) // 2, p)
        if out == p - 1:
            out = -1
        return [out, True]

def jacobiSymbol(a, n):
    if n == 1:
        return [1, True]
    if n % 2 == 0:
        return [0, False]
    if math.gcd(a, n) != 1:
        return [0, True]
    else:
        prod = 1
        if a < 0:
            a = -1 * a
            if(n % 4 == 3):
                prod *= -1
        while a > 1:
            if a > n:
                a = a % n
            m = (-1 if (n % 8 == 3 or n % 8 == 5) else 1)
            while(not (a % 2)):
                a = a // 2
                prod *= m
            if(a > 2):
                if(((a - 1) * (n - 1) / 4) % 2):
                    prod *= -1
                t = a
                a = n
                n = t
        return [prod, True]

def jacobiSymbolSlow(a, n):
    f = factor(n)
    product = 1
    for i in range(len(f)):
        p = legendreSymbol(a, f[i][0])
        if p[1]:
            product *= p[0] ** f[i][1]
        else:
            return [0, False]
    return [product, True]

def cubicResidueSymbol(alpha, pi):
    if normEisenstien(pi) == 3:
        return [0, False]
    else:
        quotientModulusPi = eisenstienIntegers.quotient(eisenstienIntegers.ideal(pi), 'p')
        inModulus = quotientModulusPi(alpha ** Integer((normEisenstien(pi) - 1) / 3))
        if inModulus == 0:
            return [0, True]
        out = [omega ** bsgs(quotientModulusPi(omega), inModulus, (0, 2)), True]
        return out

def extendedCubicResidueSymbol(alpha, n):
    f = factor(n)
    product = 1
    for i in range(len(f)):
        p = cubicResidueSymbol(alpha, (f.unit() * f[i][0]) if i == 0 else (f[i][0]))
        if p[1]:
            product *= p[0] ** f[i][1]
        else:
            return [0, False]
    return [product, True]

def svd(m, timer = False):
    bT = time.time()
    svdDecomp = m.SVD()
    if timer:
        print("time to evaluate SVD decomposition:", str(time.time() - bT) + "s")
    return svdDecomp

def extractEigenvals(svdDecomp, dim, timer = False):
    bT = time.time()
    maxEv = svdDecomp[1][0][0] ** 2
    evs = [(svdDecomp[1][i][i] ** 2) for i in range(dim)]
    normEvs = [(svdDecomp[1][i][i] ** 2 / maxEv) for i in range(dim)]
    if timer:
        print("time to extract eigenvalues:", str(time.time() - bT) + "s")
    return [evs, normEvs]

def createPlot(evs, normEvs, useNormValsX = True, numYTicks = 0, path = "output/", timer = False, colorscheme = "jet"):
    bT = time.time()
    oneDimEvs = []
    oneDimNormEvs = []
    y = []
    yTicks = []
    yTicksLabels = []
    for i in range(len(evs)):
        yTicks.append(i)
        yTicksLabels.append(len(evs[i]))
        for j in range(len(evs[i])):
            oneDimEvs.append(evs[i][j])
            oneDimNormEvs.append(normEvs[i][j])
            y.append(i)
    if useNormValsX:
        plt.scatter(oneDimNormEvs, y, c = oneDimNormEvs, cmap = colorscheme, vmin = 0)
        plt.xlabel("Normalized Eigenvalues")
    else:
        plt.scatter(oneDimEvs, y, c = oneDimNormEvs, cmap = colorscheme, vmin=0)
        plt.xlabel("Eigenvalues")
    plt.ylabel("Number of Eigenvalues")
    if numYTicks > len(yTicks):
        return -1
    elif numYTicks == -1:
        plt.yticks([yTicks[0]], [yTicksLabels[0]])
    elif numYTicks == 0:
        plt.yticks(yTicks, yTicksLabels)
    elif numYTicks == 1:
        plt.yticks([yTicks[-1]], [yTicksLabels[-1]])
    else:
        plt.yticks([yTicks[int(round(i * (len(yTicks) - 1) / (numYTicks - 1)))] for i in range(numYTicks)],\
                   [yTicksLabels[int(round(i * (len(yTicksLabels) - 1) / (numYTicks - 1)))] for i in range(numYTicks)])
    plt.savefig(path + str(math.floor(time.time())) + "ev.png")
    if timer:
        print("time to create plot:", str(time.time() - bT) + "s")
    return 0
