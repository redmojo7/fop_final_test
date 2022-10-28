import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 3:
    print("Syntax: python3 heatcmd.py heatsource.csv 20 100")

print(sys.argv)
filename = sys.argv[1]


def calcheat(b, r, c):
    result = (b[r - 1, c - 1] * 0.1 + b[r - 1, c] * 0.1 + b[r - 1, c + 1] * 0.1
              + b[r, c - 1] * 0.1 + b[r, c] * 0.2 + b[r, c + 1] * 0.1
              + b[r + 1, c - 1] * 0.1 + b[r + 1, c] * 0.1 + b[r + 1, c + 1] * 0.1)
    return result


size = 10
# read in heat source
hlist = []
fileobj = open(filename, 'r')
for line in fileobj:
    line_s = line.strip()
    ints = [float(x) for x in line_s.split(',')]
    hlist.append(ints)
fileobj.close()
heat = np.array(hlist, dtype=int)
curr = heat.copy()
nextt = np.zeros((size, size))
for timestep in range(5):
    for r in range(1, size - 1):
        for c in range(1, size - 1):
            nextt[r, c] = calcheat(curr, r, c)
            nextt = np.where(heat > nextt, heat, nextt)  # 2(e)
            curr = nextt.copy()  # 2(f)
plt.imshow(nextt, cmap=plt.cm.hot)
plt.show()
