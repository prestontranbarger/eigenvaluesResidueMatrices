from baseCubic import *

max = 10
mpT, mpd1T = 0, 0
for a in range(max):
    for b in range(max):
        if not (a == 0 and b == 0):
            alpha = a + b * omega
            bT = time.time()
            makePrimaryOld(alpha)
            mpT += (time.time() - bT)
            bT = time.time()
            makePrimary(alpha)
            mpd1T += (time.time() - bT)
            if makePrimary(alpha) != makePrimaryOld(alpha):
                print(makePrimary(alpha))
                print(makePrimaryOld(alpha))
print(mpT / (max ** 2 - 1))
print(mpd1T / (max ** 2 - 1))