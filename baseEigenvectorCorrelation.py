from baseCubic import *
from readWriteEVectors import *
from tqdm import tqdm

def tradEgnvecFunction(element):
    return conjugate(simplifyComplex(normalizedGaussSum(element)))

def muEgnvecFuction(params, element):
    return conjugate(simplifyComplex(normalizedGaussMuSum(params[0], element)))

def twistedEgnvecFunction(params, element):
    return simplifyComplex(eisensteinToComplex(extendedCubicResidueSymbol(0 * omega + params[0], element)) * conjugate(normalizedGaussMuSum(1, element)))

def twistedMuEgnvecFunction(params, element):
    return simplifyComplex(eisensteinToComplex(extendedCubicResidueSymbol(0 * omega + params[0], element)) * conjugate(normalizedGaussMuSum(egnNum, element)))

def egnCorrelModule(evsPath, min, max, func, params = []):
    csms = []
    vEs = [0]
    RWEVectors = rwEVectors()
    for n in range(min, max):
        v = []
        l = 0
        vE = computeViableElementsCubic(n)
        if len(vE) not in vEs:
            for element in tqdm(vE):
                ngs = func(params, element)
                v.append(ngs)
                l += ngs.real() ** 2 + ngs.imag() ** 2
            l = math.sqrt(l)
            for i in range(len(v)):
                v[i] /= l
            RWEVectors.setReadPath(evsPath)
            rowDict = RWEVectors.guideToDict(RWEVectors.readEVectorsGuide())
            egnVec = [[parseComplex(z) for z in eV] for eV in RWEVectors.readEVectors([rowDict[str(len(vE))]])]
            csms.append([((vector(v).hermitian_inner_product(vector(comp))) / (vector(comp).hermitian_inner_product(vector(comp)))).abs() for comp in egnVec])
        vEs.append(len(vE))
    vEs = list(set(vEs[1:]))
    vEs.sort()
    return vEs, csms

#mu = 1 + 0 * omega
#vEs, csms = egnCorrelModule(4, 10, muEgnvecFuction, [mu])
#correlationPlotPColorMesh(vEs, csms, imgPath, toStringEisenstein(mu))