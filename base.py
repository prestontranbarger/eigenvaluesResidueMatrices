from sage.all import *
import math
import time
import matplotlib.pyplot as plt

eisenstienIntegers = EisensteinIntegers(names=('omega',)); (omega,) = eisenstienIntegers._first_ngens(1)

def toStringEisenstein(alpha):
    return "(" + str(Integer(alpha[0])) + ";" + str(Integer(alpha[1])) + ")"

def toEisensteinString(string):
    oP = string[1:-1].split(";")
    return Integer(oP[0]) + Integer(oP[1]) * omega

def conjugateEisenstein(alpha):
    return Integer(alpha[0] - alpha[1]) - Integer(alpha[1]) * omega

def normEisenstein(alpha):
    #computes magnitude squared of an eisenstien integer
    return Integer(alpha[0]) ** 2 - Integer(alpha[0]) * Integer(alpha[1]) + Integer(alpha[1]) ** 2

def factorEisenstein(alpha):
    #computes the factorization of an eisenstien integer over the eisenstien integers
    #input can be list or eisenstien integer
    return factor(Integer(alpha[0]) + Integer(alpha[1]) * omega)

def modEisenstein(alpha, beta):
    z = alpha / beta
    kappa = round(z[0]) + round(z[1]) * omega
    rho = alpha - kappa * beta
    return rho

def gcdEisenstein(alpha, beta):
    [p, q, gamma] = makePrimary(alpha)
    [r, s, delta] = makePrimary(beta)
    g = (1 - omega) ** min([q, s])
    alpha, beta = gamma, delta
    while alpha != beta:
        [p, q, gamma] = makePrimary(alpha - beta)
        if normEisenstein(alpha) > normEisenstein(beta):
            alpha = gamma
        else:
            beta = gamma
    return g * alpha

def isPrime(f):
    #uses a given factorization to determine if a number is prime in a specific field
    if len(f) == 1 and f[0][1] == 1:
        return True
    return False

def isPrimary(alpha):
    if alpha[0] % 3 == 1 and alpha[1] % 3 == 0:
        return True
    return False

def makePrimary(alpha):
    i, j = 0, 0
    alphaCopy = alpha
    while not (alphaCopy[0] % 3 == 1 and alphaCopy[1] % 3 == 0):
        a, b = Integer(alphaCopy[0]), Integer(alphaCopy[1])
        am, bm = 1 * (a % 3), 1 * (b % 3)
        if (am + bm) % 3:
            i += (4 * bm + (am + bm == 2) * (4 * bm + 3)) % 6
        else:
            if am:
                i += (3 + am + 4 * am * (a // 3 + b // 3)) % 6
                j += 1
            else:
                i += 5
                j += 2
        i %= 6
        alphaCopy = alpha / ((-1 * omega) ** i * (1 - omega) ** j)
    return [i, j, alphaCopy]

def isNthPowerFree(f, n):
    #pass n=2 to find squarefree, n=3 to find cubefree, etc
    for factor in f:
        if factor[1] >= n:
            return False
    return True

def legendreSymbolSlow(a, p):
    if p == 2:
        return [0, False]
    else:
        out = power_mod(a, (p - 1) // 2, p)
        if out == p - 1:
            out = -1
        return [out, True]

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

def jacobiSymbol(a, n):
    if n == 1:
        return [1, True]
    if n % 2 == 0 or n < 0:
        return [0, False]
    if math.gcd(a, n) != 1:
        return [0, True]
    else:
        prod = 1
        if a < 0:
            a *= -1
            if n % 4 == 3:
                prod *= -1
        while a > 1:
            a %= n
            m = (-1 if (n % 8 == 3 or n % 8 == 5) else 1)
            while not a % 2:
                a = a // 2
                prod *= m
            if a > 2:
                if (a - 1) * (n - 1) / 4 % 2:
                    prod *= -1
                a, n = n, a
        return [prod, True]

def cubicResidueSymbolSlow(alpha, pi):
    if normEisenstein(pi) == 3:
        return [Integer(0) + Integer(0) * omega, False]
    else:
        quotientModulusPi = eisenstienIntegers.quotient(eisenstienIntegers.ideal(pi), 'p')
        inModulus = quotientModulusPi(alpha ** Integer((normEisenstein(pi) - 1) / 3))
        if inModulus == 0:
            return [Integer(0) + Integer(0) * omega, True]
        out = [omega ** bsgs(quotientModulusPi(omega), inModulus, (0, 2)), True]
        return out

def extendedCubicResidueSymbolSlow(alpha, beta):
    f = factor(beta)
    product = 1
    for i in range(len(f)):
        p = cubicResidueSymbolSlow(alpha, (f.unit() * f[i][0]) if i == 0 else (f[i][0]))
        if p[1]:
            product *= p[0] ** f[i][1]
        else:
            return [Integer(0) + Integer(0) * omega, False]
    return [product, True]

def extendedCubicResidueSymbolSlowish(alpha, beta):
    [i1, j1, gamma] = makePrimary(alpha)
    [i2, j2, delta] = makePrimary(beta)
    if j2:
        return [Integer(0) + Integer(0) * omega, False]
    m, n = (delta[0] - 1) // 3, delta[1] // 3
    t = (m * j1 - (m + n) * i1) % 3
    alpha = gamma
    beta = delta
    if normEisenstein(alpha) < normEisenstein(beta):
        alpha, beta = beta, alpha
    while alpha != beta:
        [i1, j1, gamma] = makePrimary(alpha - beta)
        m, n = (beta[0] - 1) // 3, beta[1] // 3
        t += (m * j1 - (m + n) * i1) % 3
        alpha = gamma
        if normEisenstein(alpha) < normEisenstein(beta):
            alpha, beta = beta, alpha
    if alpha != 1:
        return [Integer(0) + Integer(0) * omega, True]
    return [omega ** (t % 3), True]

def extendedCubicResidueSymbol(alpha, beta):
    units = [-1, 1, omega, -1 * omega, -1 * omega ** 2, omega ** 2]
    exp = 0
    while alpha != -1 and not (beta in units):
        if not alpha:
            return [Integer(0) + Integer(0) * omega, True]
        [p, q, gamma] = makePrimary(alpha)
        [r, s, delta] = makePrimary(beta)
        if s:
            return [Integer(0) + Integer(0) * omega, False]
        exp += ((p - q) * (1 - delta[0]) - p * delta[1]) // 3
        alpha, beta = gamma, delta
        if normEisenstein(alpha) < normEisenstein(beta):
            alpha, beta = beta, alpha
        alpha, beta = modEisenstein(alpha, beta), beta
    return [omega ** (exp % 3), True]

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

def extractEigen(m):
    eValuesVectors = sorted(m.eigenvectors_right(), key = lambda x: x[0], reverse = True)
    eValues = [element[0].real() for element in eValuesVectors]
    normEValues = [(element / eValues[0]) for element in eValues]
    eVectors = [list(element[1][0]) for element in eValuesVectors]
    return [eValues, normEValues], eVectors

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
