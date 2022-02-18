import math

from baseCubic import *
from readWriteEValues import *
import matplotlib.pyplot as plt
import statistics

evsPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\square\\eValuesLarge.txt"
imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\square\\image\\"

RWEValues = rwEValues()

RWEValues.setReadPath(evsPath)
eValuesGuide = RWEValues.readEValuesGuide()
eValuesDict = RWEValues.guideToDict(eValuesGuide)

sizes = [int(size) for size in eValuesGuide]
rows = [eValuesDict[size] for size in eValuesGuide]

evTarget = 4
eVs = RWEValues.readEValues(rows)
eValues = []
for i in range(evTarget, len(eVs)):
    eValues.append(float(eVs[i][evTarget]))

x = []
y = []
c = []
for i in range(1, len(eValues)):
    x.append(sizes[i])
    exp = math.log(eValues[i]) / math.log(sizes[i])
    y.append(exp)
    c.append(eValues[i] / (sizes[i] ** (4/3)))

plt.axhline(y = 1.333333333, color = 'r', linestyle = '-')
plt.plot(x, y)
plt.annotate("(" + str(x[-1]) + ", " + str(round(y[-1], 5)) + ")",\
             (x[-1], y[-1]),\
             textcoords="offset points",\
             xytext=(0, -10),\
             ha='right')
plt.savefig(imgPath + str(math.floor(time.time())) + "exp" + str(evTarget + 1) + ".png")

plt.clf()

plt.plot(x, c)
plt.annotate("(" + str(x[-1]) + ", " + str(round(c[-1], 5)) + ")",\
             (x[-1], c[-1]),\
             textcoords="offset points",\
             xytext=(0, -10),\
             ha='right')
plt.savefig(imgPath + str(math.floor(time.time()) + 1) + "const" + str(evTarget + 1) + ".png")

print(eValues)
print(x)
print(y)
print(c)