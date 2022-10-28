import numpy as np
import matplotlib.pyplot as plt


def calcheat(b, r, c):  # 2(d)
    '''
    result = (b[r - 1, c - 1] * 0.1 + b[r - 1, c] * 0.1 + b[r - 1, c + 1] * 0.1
              + b[r, c - 1] * 0.1 + b[r, c] * 0.2 + b[r, c + 1] * 0.1
              + b[r + 1, c - 1] * 0.1 + b[r + 1, c] * 0.1 + b[r + 1, c + 1] * 0.1)
    '''

    result = curr[r-1:r+2, c-1:c+2].sum() * 0.1 + b[r, c] * 0.1
    return result


size = 10
# read in heat source
hlist = []
fileobj = open('heatsource.csv', 'r')
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
