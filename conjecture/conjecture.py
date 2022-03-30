import sys
import matplotlib.pyplot as plt
import numpy as np

def K2p1(num):
    return num*3+1

def K2(num):
    return num / 2

n = int(sys.argv[1])

idk = []

while True:
    idk.append(n)
    if n == 1:
        break
    else:
        if n%2 == 0:
            n = K2(n) 
        else:
            n = K2p1(n)

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
print(idk)
ypoints = np.array(idk)
plt.margins(x=0, y=0)
plt.plot(ypoints, color = 'r')
plt.yticks(ypoints)
plt.xticks([um for um in range(len(idk) + 1)])
plt.show()
