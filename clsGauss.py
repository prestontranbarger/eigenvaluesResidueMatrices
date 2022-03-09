from baseCubic import *
from tqdm import tqdm
import matplotlib.pyplot as plt

imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\3\\square\\image\\"

x = []
y = []
a = []
vEs = []
for norm in tqdm(range(2, 100)):
    #print(norm)
    sum = 0 + 0 * omega
    vE = computeViableElementsCubicLargeSieve(norm)
    x.append(norm)
    a.append((2 * (2 * math.pi) ** (2 / 3) * norm ** (5 / 6)) / (5 * 1.354117939426 * math.log(norm)))
    if len(vE) not in vEs:
        vEs.append(len(vE))
        c = 0
        for element in vE:
            sum = sum + normalizedGaussSum(element)
        y.append(simplifyComplex(sum).real())
    else:
        y.append(y[-1])
print(x)
print(y)
print(a)
plt.plot(x, y, color = 'b')
plt.plot(x, a, color = 'r')
plt.savefig(imgPath + str(math.floor(time.time())) + "clsGauss.png")