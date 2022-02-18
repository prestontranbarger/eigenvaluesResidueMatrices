from baseCubic import *
from cubicGaussSum import *

p = 19
split = - 5 - 3 * omega

print(cexps(p) / (2 * math.sqrt(p)))
print(normalizedGaussSum(split))
print(normalizedGaussSum(1 + 0 * omega))