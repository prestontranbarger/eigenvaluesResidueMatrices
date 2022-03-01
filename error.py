from baseCubic import *
from tqdm import tqdm

import matplotlib.pyplot as plt

imgPath = "C:\\Users\\Preston\\Documents\\TAMU\\Courses\\213\\491\\output\\3\\square\\image\\"

x = []
y = []
a = []
e = []
for n in tqdm(range(2, 10000)):
    x.append(n)
    Sp = SPatterson(n)
    Sa = (2 * math.pi) ** (2 / 3) * n ** (4/3) / (8 * 1.354117939426 * math.log(n))
    y.append(Sp)
    a.append(Sa)
    e.append(Sp - Sa)
print(x)
print(y)
print(a)
print(e)
plt.plot(x, y, color = 'b')
plt.plot(x, a, color = 'r')
plt.plot(x, e, color = 'g')
plt.savefig(imgPath + str(math.floor(time.time())) + "error.png")