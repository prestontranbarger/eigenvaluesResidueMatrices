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

evTarget = 0
eVs = RWEValues.readEValues(rows)
eValues = []
for i in range(evTarget, len(eVs)):
    eValues.append(float(eVs[i][evTarget]))

x = []
y = []
for i in range(1, len(eValues)):
    x.append(i)
    y.append(math.log(eValues[i]) / math.log(sizes[i]))

print(statistics.mean(y))
print(statistics.median(y))
histOrGrowth = 'g'
if histOrGrowth == 'h':
    plt.hist(y, 50)
else:
    plt.plot(x, y)
plt.savefig(imgPath + str(math.floor(time.time())) + histOrGrowth + "e" + str(evTarget + 1) + ".png")