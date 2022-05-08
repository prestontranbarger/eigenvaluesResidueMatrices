from baseCubic import *

maxNorm = 35
primaryOnly = False

def primeTest(alpha):
    n = normEisenstein(alpha)
    if isPrime(factor(n)):
        return True
    if math.sqrt(n) == int(math.sqrt(n)):
        if isPrime(factor(int(math.sqrt(n)))):
            return True
    return False

indexOffset = math.floor(math.sqrt(4 * maxNorm / 3))
for y in tqdm(range(-indexOffset, indexOffset + 1)):
    for x in range(math.ceil((y - math.sqrt(4 * maxNorm - 3 * y ** 2)) / 2), \
                   math.floor((y + math.sqrt(4 * maxNorm - 3 * y ** 2)) / 2) + 1):
        if x != 0 or y != 0:
            alpha = x + y * omega
            if not (primaryOnly and not isPrimary(alpha)) and primeTest(alpha):
                print(toStringEisenstein(alpha), normEisenstein(alpha))