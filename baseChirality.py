from baseCubic import *

def nonChiralExtendedCubicResidue(a, b, c, d):
    return extendedCubicResidueSymbol(c, a)[0] *\
           conjugateEisenstein(extendedCubicResidueSymbol(c, b)[0]) *\
           conjugateEisenstein(extendedCubicResidueSymbol(d, a)[0]) *\
           extendedCubicResidueSymbol(d, b)[0]

def computeViableElementsMultiplicative(maxNorm):
    viablePairs = set()
    for maxNormA in range(1, maxNorm):
        for vEA in computeViableElementsCubic(maxNormA):
            for maxNormB in range(1, maxNorm // maxNormA):
                for vEB in computeViableElementsCubic(maxNormB):
                    if gcdEisenstein(vEA, vEB):
                        viablePairs.add((vEA, vEB))
    return list(viablePairs)

def constructMatrixNonChiral(vE):
    return matrix(CDF, len(vE), len(vE), lambda x, y: nonChiralExtendedCubicResidue(vE[x][0],\
                                                                                    vE[x][1],\
                                                                                    vE[y][0],\
                                                                                    vE[y][1]))

def toStringEisensteinPair(pair):
    return str(toStringEisenstein(pair[0]) + "/" + toStringEisenstein(pair[1]))