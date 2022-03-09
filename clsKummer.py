from baseCubic import *
from tqdm import tqdm
import matplotlib.pyplot as plt

imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\221\\491\\output\\3\\square\\image\\"

xS = []
yS = []
aS = []
for x in tqdm(range(2, 100)):
    sum = 0 + 0 * I
    for p in range(1, x + 1):
        if p % 3 == 1 and isPrime(factor(p)):
            #print(p)
            sum += cexps(p) / (2 * math.sqrt(p))
    xS.append(x)
    yS.append(sum.real())
    aS.append((2 * (2 * math.pi) ** (2 / 3) * x ** (5 / 6)) / (5 * 1.354117939426 * math.log(x)))
print(xS)
print(yS)
print(aS)
plt.plot(xS, yS, color = 'b')
plt.plot(xS, aS, color = 'r')
plt.savefig(imgPath + str(math.floor(time.time())) + "clsKummer.png")