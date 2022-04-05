from base import *
import random
import matplotlib.pyplot as plt

imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\image\\"

def genRandComplexUnitVec(dim):
    v = []
    D = RealDistribution('uniform', [-1, 1])
    m = 0
    for i in range(dim):
        a = D.get_random_element()
        b = D.get_random_element()
        v.append(a + b * I)
        m += a ** 2 + b ** 2
    for i in range(len(v)):
        v[i] = v[i] / m
    return v

x = []
y = []
c = []
trials = 2500
for dim in range(1, 10):
    print(dim)
    s = 0
    for i in tqdm(range(trials)):
        s += vector(genRandComplexUnitVec(dim)).hermitian_inner_product(vector(genRandComplexUnitVec(dim))).abs()
    print(s / trials)
    x.append(dim)
    y.append(s / trials)
    c.append((s / trials) / (1 / sqrt(dim)))
plt.plot(x, y)
plt.plot(x, c)
plt.savefig(imgPath + str(math.floor(time.time())) + "control.png")