from base import *
import random
import matplotlib.pyplot as plt

imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\eigenvaluesResidueMatrices\\output\\3\\square\\image\\"

def genRandComplexUnitVec(dim):
    v = []
    s = 1
    for i in range(dim - 1):
        D = RealDistribution('uniform', [-math.sqrt(s), math.sqrt(s)])
        a = D.get_random_element()
        s -= a ** 2
        D = RealDistribution('uniform', [-math.sqrt(s), math.sqrt(s)])
        b = D.get_random_element()
        s -= b ** 2
        v.append(a + b * I)
    D = RealDistribution('uniform', [-math.sqrt(s), math.sqrt(s)])
    a = D.get_random_element()
    b = math.copysign(1, random.random() - 0.5) * sqrt(s - a ** 2)
    v.append(a + b * I)
    return v

x = []
y = []
trials = 2500
for dim in range(100, 101):
    s = 0
    for i in tqdm(range(trials)):
        s += vector(genRandComplexUnitVec(dim)).hermitian_inner_product(vector(genRandComplexUnitVec(dim))).abs()
    print(s / trials)
    x.append(dim)
    y.append(s / trials)
plt.plot(x, y)
plt.savefig(imgPath + str(math.floor(time.time())) + "control.png")